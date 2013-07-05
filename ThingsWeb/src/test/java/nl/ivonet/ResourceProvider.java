/*
 * Copyright (c) 2013 by Ivo Wolring (http://ivonet.nl)
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *        http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package nl.ivonet;

import org.apache.commons.io.FileUtils;

import java.io.File;
import java.io.IOException;

/**
 *
 * @author Ivo Woltring
 */
public class ResourceProvider {

    /**
     * Get a filname from the recourse folder.
     *
     * @param fileName the filename to get in src/test/resources
     * @return the absolute path to the filename
     */
    public static String getFileResource(final String fileName) {
        String abspath = new File(".").getAbsolutePath();
        abspath = abspath.substring(0, abspath.length() - 1);
        return new File(String.format("%sThingsWeb/src/test/resources/%s", abspath, fileName)).getAbsolutePath();
    }

    /**
     * Get and read the filename.
     *
     * @param fileName the file in src/test/resources to read
     * @return the contents of the file as a string
     * @throws java.io.IOException when io went wrong on resource
     */
    public static String getResourceAsString(final String fileName) throws IOException {
        final String abspath = getFileResource(fileName);
        return FileUtils.readFileToString(new File(abspath));
    }

}
