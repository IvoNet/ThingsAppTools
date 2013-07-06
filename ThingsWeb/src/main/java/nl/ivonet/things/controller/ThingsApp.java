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

package nl.ivonet.things.controller;

import nl.ivonet.things.Things;
import nl.ivonet.things.dao.ThingsDao;

import javax.inject.Inject;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

/**
 *
 * @author Ivo Woltring
 */
@Path("/things")
public class ThingsApp {
    @Inject private ThingsDao dao;

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Things getClichedMessage() {
        //FIXME Adjust the path below to the folder you have this file in!
        return dao.retrieveThings("/Users/ivonet/dev/github/ThingsExporter/tmp/ThingsExport.xml");
    }


}