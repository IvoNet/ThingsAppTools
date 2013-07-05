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

/**
 * The Things Controller for angular.
 *
 * @param $scope the scope for the application
 * @param $http for doing http requests
 */
function CtrlThings($scope, $http) {
    $scope.debug = false;

    $http.get('rest/things').success(function (data) {
        $scope.things = data;
        $scope.todos = data.today.todos.todo;
    });


    $scope.showToDos = function (category) {
        if (!category.todos) {
            $scope.todos = []
        } else {
            $scope.todos = category.todos.todo;
        }
    };

    $scope.toggleDebug = function () {
        $scope.debug = !$scope.debug;
    };

//    $scope.tagById = function (ids) {
//        tags = $scope.things.tags.tag;
//        mytags = "";
//        for (x = 0; x < ids.length; x++) {
//            id = ids[x];
//            for (i = 0; i < tags.length; i++) {
//                tag = tags[i];
//                alert(tag.id + " " + id);
//                if (tag.id == id) {
//                    mytags = mytags + " " + tag.name;
//                }
//            }
//        }
//        return mytags;
//    }

}