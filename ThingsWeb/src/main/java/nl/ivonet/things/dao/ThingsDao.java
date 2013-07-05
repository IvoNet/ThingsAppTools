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

package nl.ivonet.things.dao;

import nl.ivonet.things.Things;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import java.io.File;

/**
 *
 * @author Ivo Woltring
 */
public class ThingsDao {

    public Things retrieveThings(final String location) {
        try {
            final JAXBContext jaxbContext = JAXBContext.newInstance("nl.ivonet.things");
            final Unmarshaller unmarshaller = jaxbContext.createUnmarshaller();
            return (Things) unmarshaller.unmarshal(new File(location));
        } catch (JAXBException e) {
            e.printStackTrace();
        }
        throw new IllegalStateException("should not be here");
    }
}
