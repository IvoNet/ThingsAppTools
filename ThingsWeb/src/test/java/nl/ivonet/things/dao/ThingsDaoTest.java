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

import nl.ivonet.ResourceProvider;
import nl.ivonet.things.Things;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertNull;

/**
 *
 * @author Ivo Woltring
 */
public final class ThingsDaoTest {
    private ThingsDao dao;

    @Before
    public void setUp() throws Exception {
        dao = new ThingsDao();

    }

    @Test
    public void testRetrieveThings() throws Exception {
        final Things things = dao.retrieveThings(ResourceProvider.getFileResource("ThingsToday.xml"));
        assertNotNull(things);
        assertNotNull(things.getToday());
        assertNull(things.getInbox());
        assertNull(things.getTags());
        assertNull(things.getAreas());
        assertNull(things.getProjects());
        assertNull(things.getNext());
        assertNull(things.getScheduled());
        assertNull(things.getSomeday());
        assertEquals("159C3AF1-1193-43D2-8027-2FE5913AE2C6", things.getToday().getTodos().getTodos().get(0).getId());

    }
}
