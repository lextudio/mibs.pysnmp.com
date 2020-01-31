#
# PySNMP MIB module USERGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/USERGROUP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:28:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
hmConfiguration, = mibBuilder.importSymbols("HMPRIV-MGMT-SNMP-MIB", "hmConfiguration")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter32, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TextualConvention, MibIdentifier, Unsigned32, IpAddress, Counter64, NotificationType, Bits, Integer32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TextualConvention", "MibIdentifier", "Unsigned32", "IpAddress", "Counter64", "NotificationType", "Bits", "Integer32", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hmUserGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 14, 3))
hmUserGroup.setRevisions(('2007-09-13 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hmUserGroup.setRevisionsDescriptions(('First release in SMIv2',))
if mibBuilder.loadTexts: hmUserGroup.setLastUpdated('200709131200Z')
if mibBuilder.loadTexts: hmUserGroup.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hmUserGroup.setContactInfo('Customer Support Postal: Hirschmann Automation and Control GmbH Stuttgarter Str. 45-51 72654 Neckartenzlingen Germany Tel: +49 7127 14 1981 Web: http://www.hicomcenter.com/ E-Mail: hicomcenter@hirschmann.com')
if mibBuilder.loadTexts: hmUserGroup.setDescription('The Hirschmann Private Usergroup MIB definitions for Platform devices.')
class MemberID(TextualConvention, OctetString):
    description = 'mac address in canonical byte order.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

hmUserGroupTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 3, 1), )
if mibBuilder.loadTexts: hmUserGroupTable.setStatus('current')
if mibBuilder.loadTexts: hmUserGroupTable.setDescription('A list of user group definitions.')
hmUserGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 3, 1, 1), ).setIndexNames((0, "USERGROUP-MIB", "hmUserGroupID"))
if mibBuilder.loadTexts: hmUserGroupEntry.setStatus('current')
if mibBuilder.loadTexts: hmUserGroupEntry.setDescription('user group definition')
hmUserGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmUserGroupID.setStatus('current')
if mibBuilder.loadTexts: hmUserGroupID.setDescription('The user group number identifying this instance.')
hmUserGroupDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmUserGroupDescription.setStatus('current')
if mibBuilder.loadTexts: hmUserGroupDescription.setDescription('A textual description of the user group instance.')
hmUserGroupRestricted = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmUserGroupRestricted.setStatus('current')
if mibBuilder.loadTexts: hmUserGroupRestricted.setDescription('If set to true(1) any member of this group is restricted to ports - which have hmPortSecPermission set to group(2) and - the group is in hmPortSecAllowedGroupIDs. If set to false(2) the user may also connect to a port if permitted by other hmPortSecPermission settings, e.g. known(3) or world(4). The following access restrictions apply: UserRestr. UserGroupRestr. PortSecPermission access allowed -------------------------------------------------------------------- false false user hmPortSecAllowedUserID false false group hmPortSecAllowedGroupIDs false false known any user group member false false world yes true false/true user hmPortSecAllowedUserID true false/true group no true false/true known no true false/true world no false true user hmPortSecAllowedUserID false true group hmPortSecAllowedGroupIDs false true known no false true world no ')
hmUserGroupSecAction = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("trapOnly", 2), ("portDisable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmUserGroupSecAction.setStatus('current')
if mibBuilder.loadTexts: hmUserGroupSecAction.setDescription('This variable specifies the action which is taken if a user tries to connect to the given port when he is not allowed to do so. Setting the variable to none(1) disables any action. A value of trapOnly(2) generates a trap. Setting the value to portDisable(3) will send a trap, and additionally disable the port until it is re-enabled by management.')
hmUserGroupMemberTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 3, 2), )
if mibBuilder.loadTexts: hmUserGroupMemberTable.setStatus('current')
if mibBuilder.loadTexts: hmUserGroupMemberTable.setDescription('A list of users which are members of a given user group.')
hmUserGroupMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 3, 2, 1), ).setIndexNames((0, "USERGROUP-MIB", "hmUserGroupMemberGroupID"), (0, "USERGROUP-MIB", "hmUserGroupMemberUserID"))
if mibBuilder.loadTexts: hmUserGroupMemberEntry.setStatus('current')
if mibBuilder.loadTexts: hmUserGroupMemberEntry.setDescription('An user group member entry.')
hmUserGroupMemberGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmUserGroupMemberGroupID.setStatus('current')
if mibBuilder.loadTexts: hmUserGroupMemberGroupID.setDescription('user group id of this member.')
hmUserGroupMemberUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 2, 1, 2), MemberID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmUserGroupMemberUserID.setStatus('current')
if mibBuilder.loadTexts: hmUserGroupMemberUserID.setDescription('user ID of this member.')
hmUserTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 3, 3), )
if mibBuilder.loadTexts: hmUserTable.setStatus('current')
if mibBuilder.loadTexts: hmUserTable.setDescription('List of all user group members.')
hmUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 3, 3, 1), ).setIndexNames((0, "USERGROUP-MIB", "hmUserID"))
if mibBuilder.loadTexts: hmUserEntry.setStatus('current')
if mibBuilder.loadTexts: hmUserEntry.setDescription('An user entry.')
hmUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 3, 1, 1), MemberID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmUserID.setStatus('current')
if mibBuilder.loadTexts: hmUserID.setDescription('User ID.')
hmUserRestricted = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmUserRestricted.setStatus('current')
if mibBuilder.loadTexts: hmUserRestricted.setDescription('If set to true(1) the user may only connect to ports which have hmPortSecPermission set to user(1) and hmPortSecAllowedUserID set to hmUserID. If set to false(2) the user may also connect to a port if permitted by other hmPortSecPermission settings, e.g. group(2), known(3) or world(4). The following access restrictions apply: UserRestr. UserGroupRestr. PortSecPermission access allowed --------------------------------------------------------------------- false false user hmPortSecAllowedUserID false false group hmPortSecAllowedGroupIDs false false known any user group member false false world yes true false/true user hmPortSecAllowedUserID true false/true group no true false/true known no true false/true world no false true user hmPortSecAllowedUserID false true group hmPortSecAllowedGroupIDs false true known no false true world no ')
hmPortSecurityTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 3, 4), )
if mibBuilder.loadTexts: hmPortSecurityTable.setStatus('current')
if mibBuilder.loadTexts: hmPortSecurityTable.setDescription('List of port security entries.')
hmPortSecurityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1), ).setIndexNames((0, "USERGROUP-MIB", "hmPortSecSlotID"), (0, "USERGROUP-MIB", "hmPortSecPortID"))
if mibBuilder.loadTexts: hmPortSecurityEntry.setStatus('current')
if mibBuilder.loadTexts: hmPortSecurityEntry.setDescription('A single port security entry.')
hmPortSecSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPortSecSlotID.setStatus('current')
if mibBuilder.loadTexts: hmPortSecSlotID.setDescription('Slot number the switch unit is plugged in.')
hmPortSecPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPortSecPortID.setStatus('current')
if mibBuilder.loadTexts: hmPortSecPortID.setDescription('Port number within the group.')
hmPortSecPermission = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("user", 1), ("group", 2), ("known", 3), ("world", 4), ("uplink", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecPermission.setStatus('current')
if mibBuilder.loadTexts: hmPortSecPermission.setDescription('This variable specifies the security level of the port. If set to user(1) only the user defined by hmPortSecAllowedUserID may connect to this port. In group(2) mode only members of the user group specified by hmPortSecAllowedGroupIDs are allowed. known(3) means that all users belonging to any user group (all known users) are accepted. Setting the value to world(4) disables the security features, i.e. any user is permitted. For backbone ports the value uplink(5) should be used. If a user does not match the allowed permission he is not able to connect to the network over this port, additionally the actions configured through hmPortSecAction are taken.')
hmPortSecAllowedUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 4), MemberID()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecAllowedUserID.setStatus('current')
if mibBuilder.loadTexts: hmPortSecAllowedUserID.setDescription('This variable specifies the allowed user ID if hmPortSecPermission has been set to user(1).')
hmPortSecAllowedGroupIDs = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(128, 128)).setFixedLength(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecAllowedGroupIDs.setStatus('current')
if mibBuilder.loadTexts: hmPortSecAllowedGroupIDs.setDescription('This variable specifies the allowed user groups if hmPortSecPermission has been set to group(2). Each group is represented by a single bit. If a group does not exist the value of the bit is ignored.')
hmPortSecConnectedUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 6), MemberID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPortSecConnectedUserID.setStatus('current')
if mibBuilder.loadTexts: hmPortSecConnectedUserID.setDescription('This variable reflects the user ID of a connected user actually seen on this port. If there is no user connected the value will be 0x00:00:00:00:00:00.')
hmPortSecAction = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("trapOnly", 2), ("portDisable", 3), ("autoDisable", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecAction.setStatus('current')
if mibBuilder.loadTexts: hmPortSecAction.setDescription('This variable specifies the action which is taken if a user tries to connect to the given port when he is not allowed to do so. Setting the variable to none(1) disables any action. A value of trapOnly(2) generates a trap. Setting the value to portDisable(3) will send a trap, and additionally disable the port until it is re-enabled by management. Setting the value to autoDisable(3) will send a trap, and additionally auto-disable the port for the amount of time specified per port.')
hmPortSecAutoReconfigure = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecAutoReconfigure.setStatus('current')
if mibBuilder.loadTexts: hmPortSecAutoReconfigure.setDescription('This variable controls whether the agent should re-configure the port when another user with an incompatible user group setting has been detected. The default setting, true(1), should be used if a single user is connected to the port. The value false(2) might be useful if more than one user is connected to the port (workgroup mode).')
hmPortSecPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("enabledWithWrongAddr", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPortSecPortStatus.setStatus('current')
if mibBuilder.loadTexts: hmPortSecPortStatus.setDescription('This variable shows the current status of the port with respect to port security. If the address seen on the port is allowed, the status is enabled(1), if it is not allowed, the status is disabled(2) if hmUserGroupSecurityAction is portDisable(3), or enabledWithWrongAddr(3) if hmUserGroupSecurityAction is none(1) or trapOnly(2).')
hmPortSecAllowedUserIPID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecAllowedUserIPID.setStatus('current')
if mibBuilder.loadTexts: hmPortSecAllowedUserIPID.setDescription('This variable specifies the allowed user IP ID if hmPortSecPermission has been set to user(1).')
hmPortSecDynamicLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecDynamicLimit.setStatus('current')
if mibBuilder.loadTexts: hmPortSecDynamicLimit.setDescription('This variable signifies the limit of dynamically learned allowed MAC addresses for a specific port.')
hmPortSecDynamicCount = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPortSecDynamicCount.setStatus('current')
if mibBuilder.loadTexts: hmPortSecDynamicCount.setDescription('The current number of dynamically learned allowed MAC addresses on this port.')
hmUserGroupSecurityAction = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("trapOnly", 2), ("portDisable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmUserGroupSecurityAction.setStatus('current')
if mibBuilder.loadTexts: hmUserGroupSecurityAction.setDescription('This variable specifies the action which is taken if a user tries to connect to the given port when he is not allowed to do so. Setting the variable to none(1) disables any action. A value of trapOnly(2) generates a trap. Setting the value to portDisable(3) will send a trap, and additionally disable the port until it is re-enabled by management.')
hmUserGroupPortSecurityMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("macAddressBased", 1), ("ipAddressBased", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmUserGroupPortSecurityMode.setStatus('current')
if mibBuilder.loadTexts: hmUserGroupPortSecurityMode.setDescription('This variable specifies the mode of the hmPortSecurityTable.')
hmPortSecExtendedGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 3, 10))
hmPortSecExtendedTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 1), )
if mibBuilder.loadTexts: hmPortSecExtendedTable.setStatus('current')
if mibBuilder.loadTexts: hmPortSecExtendedTable.setDescription('List of extended port security entries.')
hmPortSecExtendedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 1, 1), ).setIndexNames((0, "USERGROUP-MIB", "hmPortSecExtSlotID"), (0, "USERGROUP-MIB", "hmPortSecExtPortID"))
if mibBuilder.loadTexts: hmPortSecExtendedEntry.setStatus('current')
if mibBuilder.loadTexts: hmPortSecExtendedEntry.setDescription('A single extended port security entry.')
hmPortSecExtSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: hmPortSecExtSlotID.setStatus('current')
if mibBuilder.loadTexts: hmPortSecExtSlotID.setDescription('Slot number the switch unit is plugged in.')
hmPortSecExtPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: hmPortSecExtPortID.setStatus('current')
if mibBuilder.loadTexts: hmPortSecExtPortID.setDescription('Port number within the group.')
hmPortSecExtAction = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("trapOnly", 2), ("portDisable", 3))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecExtAction.setStatus('current')
if mibBuilder.loadTexts: hmPortSecExtAction.setDescription('This variable specifies the action which is taken if a user tries to connect to the given port when he is not allowed to do so. Setting the variable to none(1) disables any action. A value of trapOnly(2) generates a trap. Setting the value to portDisable(3) will send a trap, and additionally disable the port until it is re-enabled by management.')
hmPortSecExtPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("enabledWithWrongAddr", 3))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPortSecExtPortStatus.setStatus('current')
if mibBuilder.loadTexts: hmPortSecExtPortStatus.setDescription('This variable shows the current status of the port with respect to port security. If the address seen on the port is allowed, the status is enabled(1), if it is not allowed, the status is disabled(2) if hmUserGroupSecurityAction is portDisable(3), or enabledWithWrongAddr(3) if hmUserGroupSecurityAction is none(1) or trapOnly(2).')
hmPortSecMultipleAdressesTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2), )
if mibBuilder.loadTexts: hmPortSecMultipleAdressesTable.setStatus('current')
if mibBuilder.loadTexts: hmPortSecMultipleAdressesTable.setDescription('List of port security entries with multiple allowed addresses.')
hmPortSecMultipleAdressesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2, 1), ).setIndexNames((0, "USERGROUP-MIB", "hmPortSecMASlotID"), (0, "USERGROUP-MIB", "hmPortSecMAPortID"), (0, "USERGROUP-MIB", "hmPortSecMAExtendedIndex"))
if mibBuilder.loadTexts: hmPortSecMultipleAdressesEntry.setStatus('current')
if mibBuilder.loadTexts: hmPortSecMultipleAdressesEntry.setDescription('A single port security entry with multiple allowed addresses.')
hmPortSecMASlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: hmPortSecMASlotID.setStatus('current')
if mibBuilder.loadTexts: hmPortSecMASlotID.setDescription('Slot number the switch unit is plugged in.')
hmPortSecMAPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: hmPortSecMAPortID.setStatus('current')
if mibBuilder.loadTexts: hmPortSecMAPortID.setDescription('Port number within the group.')
hmPortSecMAExtendedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)))
if mibBuilder.loadTexts: hmPortSecMAExtendedIndex.setStatus('current')
if mibBuilder.loadTexts: hmPortSecMAExtendedIndex.setDescription('Number of adresses.')
hmPortSecMAAllowedUserIDs = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2, 1, 4), MemberID()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecMAAllowedUserIDs.setStatus('current')
if mibBuilder.loadTexts: hmPortSecMAAllowedUserIDs.setDescription('This variable specifies the allowed user ID if hmPortSecPermission has been set to user(1).')
hmPortSecMAAllowedUserIPIDs = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecMAAllowedUserIPIDs.setStatus('current')
if mibBuilder.loadTexts: hmPortSecMAAllowedUserIPIDs.setDescription('This variable specifies the allowed user IP ID if hmPortSecPermission has been set to user(1).')
hmPortSecMAAllowedUserIDMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 48)).clone(48)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecMAAllowedUserIDMask.setStatus('current')
if mibBuilder.loadTexts: hmPortSecMAAllowedUserIDMask.setDescription('The number of bits from left ro right, that are used from the MAC address.')
hmUserGroupEvent = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 14, 3, 0))
if mibBuilder.loadTexts: hmUserGroupEvent.setStatus('current')
if mibBuilder.loadTexts: hmUserGroupEvent.setDescription('The events of hmUserGroup.')
hmNewUserTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 14, 3, 0, 1)).setObjects(("USERGROUP-MIB", "hmPortSecConnectedUserID"))
if mibBuilder.loadTexts: hmNewUserTrap.setStatus('current')
if mibBuilder.loadTexts: hmNewUserTrap.setDescription('This trap is sent if an unknown MAC address is detected on a port.')
hmPortSecurityTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 14, 3, 0, 2)).setObjects(("USERGROUP-MIB", "hmPortSecPermission"), ("USERGROUP-MIB", "hmPortSecAction"), ("USERGROUP-MIB", "hmPortSecConnectedUserID"), ("USERGROUP-MIB", "hmPortSecAllowedUserID"), ("USERGROUP-MIB", "hmPortSecAllowedUserIPID"), ("USERGROUP-MIB", "hmPortSecAllowedGroupIDs"))
if mibBuilder.loadTexts: hmPortSecurityTrap.setStatus('current')
if mibBuilder.loadTexts: hmPortSecurityTrap.setDescription('This trap is sent if a MAC address / IP address is detected on a port which is not acceptable for the current setting of hmPortSecPermission AND ...SecAction is either set to trapOnly(2) or portDisable(3).')
hmPortSecConfigErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 14, 3, 0, 3)).setObjects(("USERGROUP-MIB", "hmPortSecConnectedUserID"))
if mibBuilder.loadTexts: hmPortSecConfigErrorTrap.setStatus('current')
if mibBuilder.loadTexts: hmPortSecConfigErrorTrap.setDescription('This trap is sent when two or more users with incompatible user group settings have been detected at the port.')
mibBuilder.exportSymbols("USERGROUP-MIB", hmUserGroupTable=hmUserGroupTable, hmPortSecDynamicLimit=hmPortSecDynamicLimit, hmPortSecConfigErrorTrap=hmPortSecConfigErrorTrap, hmPortSecMultipleAdressesTable=hmPortSecMultipleAdressesTable, hmUserRestricted=hmUserRestricted, hmPortSecExtAction=hmPortSecExtAction, hmUserGroupSecAction=hmUserGroupSecAction, hmUserEntry=hmUserEntry, hmUserGroupID=hmUserGroupID, hmUserTable=hmUserTable, hmPortSecPermission=hmPortSecPermission, hmPortSecAutoReconfigure=hmPortSecAutoReconfigure, hmPortSecDynamicCount=hmPortSecDynamicCount, hmPortSecMultipleAdressesEntry=hmPortSecMultipleAdressesEntry, hmPortSecExtendedEntry=hmPortSecExtendedEntry, hmPortSecMAAllowedUserIDs=hmPortSecMAAllowedUserIDs, hmPortSecSlotID=hmPortSecSlotID, hmPortSecMASlotID=hmPortSecMASlotID, hmUserGroupMemberEntry=hmUserGroupMemberEntry, hmPortSecExtPortID=hmPortSecExtPortID, hmPortSecurityEntry=hmPortSecurityEntry, MemberID=MemberID, hmUserGroupEvent=hmUserGroupEvent, hmPortSecMAExtendedIndex=hmPortSecMAExtendedIndex, hmPortSecAction=hmPortSecAction, hmPortSecPortID=hmPortSecPortID, hmUserGroupSecurityAction=hmUserGroupSecurityAction, hmPortSecurityTrap=hmPortSecurityTrap, hmUserGroupMemberTable=hmUserGroupMemberTable, hmPortSecExtendedTable=hmPortSecExtendedTable, hmPortSecAllowedGroupIDs=hmPortSecAllowedGroupIDs, hmUserGroupEntry=hmUserGroupEntry, hmUserID=hmUserID, hmPortSecAllowedUserID=hmPortSecAllowedUserID, hmUserGroupMemberUserID=hmUserGroupMemberUserID, hmPortSecExtendedGroup=hmPortSecExtendedGroup, hmUserGroupDescription=hmUserGroupDescription, PYSNMP_MODULE_ID=hmUserGroup, hmPortSecPortStatus=hmPortSecPortStatus, hmPortSecAllowedUserIPID=hmPortSecAllowedUserIPID, hmPortSecMAPortID=hmPortSecMAPortID, hmUserGroupPortSecurityMode=hmUserGroupPortSecurityMode, hmPortSecConnectedUserID=hmPortSecConnectedUserID, hmPortSecMAAllowedUserIDMask=hmPortSecMAAllowedUserIDMask, hmUserGroup=hmUserGroup, hmPortSecurityTable=hmPortSecurityTable, hmPortSecMAAllowedUserIPIDs=hmPortSecMAAllowedUserIPIDs, hmPortSecExtSlotID=hmPortSecExtSlotID, hmPortSecExtPortStatus=hmPortSecExtPortStatus, hmUserGroupMemberGroupID=hmUserGroupMemberGroupID, hmNewUserTrap=hmNewUserTrap, hmUserGroupRestricted=hmUserGroupRestricted)