# SNMP MIB module (JUNIPER-L2ALD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-L2ALD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:24 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(jnxl2aldMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxl2aldMibRoot")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxl2aldMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1)
)
jnxl2aldMib.setRevisions(
        ("2015-01-22 10:00",
         "2015-01-14 10:00",
         "2012-08-08 10:00",
         "2007-02-15 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Jnxl2aldNotification_ObjectIdentity = ObjectIdentity
jnxl2aldNotification = _Jnxl2aldNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 0)
)
_Jnxl2aldObjects_ObjectIdentity = ObjectIdentity
jnxl2aldObjects = _Jnxl2aldObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1)
)
_Jnxl2aldInterfaceTable_Object = MibTable
jnxl2aldInterfaceTable = _Jnxl2aldInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxl2aldInterfaceTable.setStatus("current")
_Jnxl2aldEntry_Object = MibTableRow
jnxl2aldEntry = _Jnxl2aldEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 1, 1)
)
jnxl2aldEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxl2aldEntry.setStatus("current")
_Jnxl2aldIntfLogicalRouter_Type = DisplayString
_Jnxl2aldIntfLogicalRouter_Object = MibTableColumn
jnxl2aldIntfLogicalRouter = _Jnxl2aldIntfLogicalRouter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 1, 1, 1),
    _Jnxl2aldIntfLogicalRouter_Type()
)
jnxl2aldIntfLogicalRouter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxl2aldIntfLogicalRouter.setStatus("current")
_Jnxl2aldIntfRoutingInst_Type = DisplayString
_Jnxl2aldIntfRoutingInst_Object = MibTableColumn
jnxl2aldIntfRoutingInst = _Jnxl2aldIntfRoutingInst_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 1, 1, 2),
    _Jnxl2aldIntfRoutingInst_Type()
)
jnxl2aldIntfRoutingInst.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxl2aldIntfRoutingInst.setStatus("current")
_Jnxl2aldIntfBridgeDomain_Type = DisplayString
_Jnxl2aldIntfBridgeDomain_Object = MibTableColumn
jnxl2aldIntfBridgeDomain = _Jnxl2aldIntfBridgeDomain_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 1, 1, 3),
    _Jnxl2aldIntfBridgeDomain_Type()
)
jnxl2aldIntfBridgeDomain.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxl2aldIntfBridgeDomain.setStatus("current")
_Jnxl2aldIntfMacLimit_Type = Unsigned32
_Jnxl2aldIntfMacLimit_Object = MibTableColumn
jnxl2aldIntfMacLimit = _Jnxl2aldIntfMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 1, 1, 4),
    _Jnxl2aldIntfMacLimit_Type()
)
jnxl2aldIntfMacLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxl2aldIntfMacLimit.setStatus("current")
_Jnxl2aldRoutingInst_Type = DisplayString
_Jnxl2aldRoutingInst_Object = MibScalar
jnxl2aldRoutingInst = _Jnxl2aldRoutingInst_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 2),
    _Jnxl2aldRoutingInst_Type()
)
jnxl2aldRoutingInst.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxl2aldRoutingInst.setStatus("current")
_Jnxl2aldBridgeDomain_Type = DisplayString
_Jnxl2aldBridgeDomain_Object = MibScalar
jnxl2aldBridgeDomain = _Jnxl2aldBridgeDomain_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 3),
    _Jnxl2aldBridgeDomain_Type()
)
jnxl2aldBridgeDomain.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxl2aldBridgeDomain.setStatus("current")
_Jnxl2aldLogicalRouter_Type = DisplayString
_Jnxl2aldLogicalRouter_Object = MibScalar
jnxl2aldLogicalRouter = _Jnxl2aldLogicalRouter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 4),
    _Jnxl2aldLogicalRouter_Type()
)
jnxl2aldLogicalRouter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxl2aldLogicalRouter.setStatus("current")
_Jnxl2aldMacLimit_Type = Unsigned32
_Jnxl2aldMacLimit_Object = MibScalar
jnxl2aldMacLimit = _Jnxl2aldMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 5),
    _Jnxl2aldMacLimit_Type()
)
jnxl2aldMacLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxl2aldMacLimit.setStatus("current")
_Jnxl2aldGbMacLimit_Type = Unsigned32
_Jnxl2aldGbMacLimit_Object = MibScalar
jnxl2aldGbMacLimit = _Jnxl2aldGbMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 6),
    _Jnxl2aldGbMacLimit_Type()
)
jnxl2aldGbMacLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxl2aldGbMacLimit.setStatus("current")
_Jnxl2aldMacAdress_Type = DisplayString
_Jnxl2aldMacAdress_Object = MibScalar
jnxl2aldMacAdress = _Jnxl2aldMacAdress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 7),
    _Jnxl2aldMacAdress_Type()
)
jnxl2aldMacAdress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxl2aldMacAdress.setStatus("current")
_JnxL2aldMacNotificationMIBObjects_ObjectIdentity = ObjectIdentity
jnxL2aldMacNotificationMIBObjects = _JnxL2aldMacNotificationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2)
)
_JnxL2aldMacNotificationMIBGlobalObjects_ObjectIdentity = ObjectIdentity
jnxL2aldMacNotificationMIBGlobalObjects = _JnxL2aldMacNotificationMIBGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1)
)
_JnxL2aldMacGlobalFeatureEnabled_Type = TruthValue
_JnxL2aldMacGlobalFeatureEnabled_Object = MibScalar
jnxL2aldMacGlobalFeatureEnabled = _JnxL2aldMacGlobalFeatureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 1),
    _JnxL2aldMacGlobalFeatureEnabled_Type()
)
jnxL2aldMacGlobalFeatureEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2aldMacGlobalFeatureEnabled.setStatus("current")


class _JnxL2aldMacNotificationInterval_Type(Unsigned32):
    """Custom type jnxL2aldMacNotificationInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxL2aldMacNotificationInterval_Type.__name__ = "Unsigned32"
_JnxL2aldMacNotificationInterval_Object = MibScalar
jnxL2aldMacNotificationInterval = _JnxL2aldMacNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 2),
    _JnxL2aldMacNotificationInterval_Type()
)
jnxL2aldMacNotificationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2aldMacNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    jnxL2aldMacNotificationInterval.setUnits("seconds")
_JnxL2aldMacAddressesLearnt_Type = Counter64
_JnxL2aldMacAddressesLearnt_Object = MibScalar
jnxL2aldMacAddressesLearnt = _JnxL2aldMacAddressesLearnt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 3),
    _JnxL2aldMacAddressesLearnt_Type()
)
jnxL2aldMacAddressesLearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2aldMacAddressesLearnt.setStatus("current")
_JnxL2aldMacAddressesRemoved_Type = Counter64
_JnxL2aldMacAddressesRemoved_Object = MibScalar
jnxL2aldMacAddressesRemoved = _JnxL2aldMacAddressesRemoved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 4),
    _JnxL2aldMacAddressesRemoved_Type()
)
jnxL2aldMacAddressesRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2aldMacAddressesRemoved.setStatus("current")


class _JnxL2aldMacNotificationsEnabled_Type(TruthValue):
    """Custom type jnxL2aldMacNotificationsEnabled based on TruthValue"""


_JnxL2aldMacNotificationsEnabled_Object = MibScalar
jnxL2aldMacNotificationsEnabled = _JnxL2aldMacNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 5),
    _JnxL2aldMacNotificationsEnabled_Type()
)
jnxL2aldMacNotificationsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2aldMacNotificationsEnabled.setStatus("current")
_JnxL2aldMacNotificationsSent_Type = Counter64
_JnxL2aldMacNotificationsSent_Object = MibScalar
jnxL2aldMacNotificationsSent = _JnxL2aldMacNotificationsSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 6),
    _JnxL2aldMacNotificationsSent_Type()
)
jnxL2aldMacNotificationsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2aldMacNotificationsSent.setStatus("current")


class _JnxL2aldMacHistTableMaxLength_Type(Unsigned32):
    """Custom type jnxL2aldMacHistTableMaxLength based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_JnxL2aldMacHistTableMaxLength_Type.__name__ = "Unsigned32"
_JnxL2aldMacHistTableMaxLength_Object = MibScalar
jnxL2aldMacHistTableMaxLength = _JnxL2aldMacHistTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 7),
    _JnxL2aldMacHistTableMaxLength_Type()
)
jnxL2aldMacHistTableMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2aldMacHistTableMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    jnxL2aldMacHistTableMaxLength.setUnits("entries")
_JnxL2aldMacHistoryTable_Object = MibTable
jnxL2aldMacHistoryTable = _JnxL2aldMacHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    jnxL2aldMacHistoryTable.setStatus("current")
_JnxL2aldMacHistoryEntry_Object = MibTableRow
jnxL2aldMacHistoryEntry = _JnxL2aldMacHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 8, 1)
)
jnxL2aldMacHistoryEntry.setIndexNames(
    (0, "JUNIPER-L2ALD-MIB", "jnxL2aldHistIndex"),
)
if mibBuilder.loadTexts:
    jnxL2aldMacHistoryEntry.setStatus("current")


class _JnxL2aldHistIndex_Type(Unsigned32):
    """Custom type jnxL2aldHistIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxL2aldHistIndex_Type.__name__ = "Unsigned32"
_JnxL2aldHistIndex_Object = MibTableColumn
jnxL2aldHistIndex = _JnxL2aldHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 8, 1, 1),
    _JnxL2aldHistIndex_Type()
)
jnxL2aldHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxL2aldHistIndex.setStatus("current")


class _JnxL2aldHistMacChangedMsg_Type(OctetString):
    """Custom type jnxL2aldHistMacChangedMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_JnxL2aldHistMacChangedMsg_Type.__name__ = "OctetString"
_JnxL2aldHistMacChangedMsg_Object = MibTableColumn
jnxL2aldHistMacChangedMsg = _JnxL2aldHistMacChangedMsg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 8, 1, 2),
    _JnxL2aldHistMacChangedMsg_Type()
)
jnxL2aldHistMacChangedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2aldHistMacChangedMsg.setStatus("current")
_JnxL2aldHistTimestamp_Type = TimeTicks
_JnxL2aldHistTimestamp_Object = MibTableColumn
jnxL2aldHistTimestamp = _JnxL2aldHistTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 8, 1, 3),
    _JnxL2aldHistTimestamp_Type()
)
jnxL2aldHistTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2aldHistTimestamp.setStatus("current")
_JnxL2aldMacAddressesUpdated_Type = Counter64
_JnxL2aldMacAddressesUpdated_Object = MibScalar
jnxL2aldMacAddressesUpdated = _JnxL2aldMacAddressesUpdated_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 9),
    _JnxL2aldMacAddressesUpdated_Type()
)
jnxL2aldMacAddressesUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2aldMacAddressesUpdated.setStatus("current")
_JnxL2aldVlanMIBObjects_ObjectIdentity = ObjectIdentity
jnxL2aldVlanMIBObjects = _JnxL2aldVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3)
)
_JnxL2aldVlanTable_Object = MibTable
jnxL2aldVlanTable = _JnxL2aldVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxL2aldVlanTable.setStatus("current")
_JnxL2aldVlanEntry_Object = MibTableRow
jnxL2aldVlanEntry = _JnxL2aldVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3, 1, 1)
)
jnxL2aldVlanEntry.setIndexNames(
    (0, "JUNIPER-L2ALD-MIB", "jnxL2aldVlanID"),
)
if mibBuilder.loadTexts:
    jnxL2aldVlanEntry.setStatus("current")


class _JnxL2aldVlanID_Type(Integer32):
    """Custom type jnxL2aldVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_JnxL2aldVlanID_Type.__name__ = "Integer32"
_JnxL2aldVlanID_Object = MibTableColumn
jnxL2aldVlanID = _JnxL2aldVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3, 1, 1, 1),
    _JnxL2aldVlanID_Type()
)
jnxL2aldVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxL2aldVlanID.setStatus("current")


class _JnxL2aldVlanName_Type(DisplayString):
    """Custom type jnxL2aldVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxL2aldVlanName_Type.__name__ = "DisplayString"
_JnxL2aldVlanName_Object = MibTableColumn
jnxL2aldVlanName = _JnxL2aldVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3, 1, 1, 2),
    _JnxL2aldVlanName_Type()
)
jnxL2aldVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2aldVlanName.setStatus("current")


class _JnxL2aldVlanTag_Type(Integer32):
    """Custom type jnxL2aldVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_JnxL2aldVlanTag_Type.__name__ = "Integer32"
_JnxL2aldVlanTag_Object = MibTableColumn
jnxL2aldVlanTag = _JnxL2aldVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3, 1, 1, 3),
    _JnxL2aldVlanTag_Type()
)
jnxL2aldVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2aldVlanTag.setStatus("current")


class _JnxL2aldVlanType_Type(Integer32):
    """Custom type jnxL2aldVlanType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_JnxL2aldVlanType_Type.__name__ = "Integer32"
_JnxL2aldVlanType_Object = MibTableColumn
jnxL2aldVlanType = _JnxL2aldVlanType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3, 1, 1, 4),
    _JnxL2aldVlanType_Type()
)
jnxL2aldVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2aldVlanType.setStatus("current")


class _JnxL2aldVlanFdbId_Type(Unsigned32):
    """Custom type jnxL2aldVlanFdbId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxL2aldVlanFdbId_Type.__name__ = "Unsigned32"
_JnxL2aldVlanFdbId_Object = MibTableColumn
jnxL2aldVlanFdbId = _JnxL2aldVlanFdbId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3, 1, 1, 5),
    _JnxL2aldVlanFdbId_Type()
)
jnxL2aldVlanFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2aldVlanFdbId.setStatus("current")

# Managed Objects groups


# Notification objects

jnxl2aldRoutingInstMacLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 0, 1)
)
jnxl2aldRoutingInstMacLimit.setObjects(
      *(("JUNIPER-L2ALD-MIB", "jnxl2aldLogicalRouter"),
        ("JUNIPER-L2ALD-MIB", "jnxl2aldRoutingInst"),
        ("JUNIPER-L2ALD-MIB", "jnxl2aldBridgeDomain"),
        ("JUNIPER-L2ALD-MIB", "jnxl2aldMacLimit"))
)
if mibBuilder.loadTexts:
    jnxl2aldRoutingInstMacLimit.setStatus(
        "current"
    )

jnxl2aldInterfaceMacLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 0, 2)
)
jnxl2aldInterfaceMacLimit.setObjects(
      *(("JUNIPER-L2ALD-MIB", "jnxl2aldIntfLogicalRouter"),
        ("JUNIPER-L2ALD-MIB", "jnxl2aldIntfRoutingInst"),
        ("JUNIPER-L2ALD-MIB", "jnxl2aldIntfBridgeDomain"),
        ("IF-MIB", "ifDescr"),
        ("JUNIPER-L2ALD-MIB", "jnxl2aldIntfMacLimit"))
)
if mibBuilder.loadTexts:
    jnxl2aldInterfaceMacLimit.setStatus(
        "current"
    )

jnxl2aldGlobalMacLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 0, 3)
)
jnxl2aldGlobalMacLimit.setObjects(
    ("JUNIPER-L2ALD-MIB", "jnxl2aldGbMacLimit")
)
if mibBuilder.loadTexts:
    jnxl2aldGlobalMacLimit.setStatus(
        "current"
    )

jnxl2aldMacMoveThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 0, 4)
)
jnxl2aldMacMoveThreshold.setObjects(
      *(("JUNIPER-L2ALD-MIB", "jnxl2aldIntfLogicalRouter"),
        ("JUNIPER-L2ALD-MIB", "jnxl2aldIntfRoutingInst"),
        ("JUNIPER-L2ALD-MIB", "jnxl2aldIntfBridgeDomain"),
        ("IF-MIB", "ifDescr"),
        ("JUNIPER-L2ALD-MIB", "jnxl2aldMacAdress"))
)
if mibBuilder.loadTexts:
    jnxl2aldMacMoveThreshold.setStatus(
        "current"
    )

jnxL2aldMacChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 0, 5)
)
jnxL2aldMacChangedNotification.setObjects(
      *(("JUNIPER-L2ALD-MIB", "jnxL2aldHistMacChangedMsg"),
        ("JUNIPER-L2ALD-MIB", "jnxL2aldHistTimestamp"))
)
if mibBuilder.loadTexts:
    jnxL2aldMacChangedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-L2ALD-MIB",
    **{"jnxl2aldMib": jnxl2aldMib,
       "jnxl2aldNotification": jnxl2aldNotification,
       "jnxl2aldRoutingInstMacLimit": jnxl2aldRoutingInstMacLimit,
       "jnxl2aldInterfaceMacLimit": jnxl2aldInterfaceMacLimit,
       "jnxl2aldGlobalMacLimit": jnxl2aldGlobalMacLimit,
       "jnxl2aldMacMoveThreshold": jnxl2aldMacMoveThreshold,
       "jnxL2aldMacChangedNotification": jnxL2aldMacChangedNotification,
       "jnxl2aldObjects": jnxl2aldObjects,
       "jnxl2aldInterfaceTable": jnxl2aldInterfaceTable,
       "jnxl2aldEntry": jnxl2aldEntry,
       "jnxl2aldIntfLogicalRouter": jnxl2aldIntfLogicalRouter,
       "jnxl2aldIntfRoutingInst": jnxl2aldIntfRoutingInst,
       "jnxl2aldIntfBridgeDomain": jnxl2aldIntfBridgeDomain,
       "jnxl2aldIntfMacLimit": jnxl2aldIntfMacLimit,
       "jnxl2aldRoutingInst": jnxl2aldRoutingInst,
       "jnxl2aldBridgeDomain": jnxl2aldBridgeDomain,
       "jnxl2aldLogicalRouter": jnxl2aldLogicalRouter,
       "jnxl2aldMacLimit": jnxl2aldMacLimit,
       "jnxl2aldGbMacLimit": jnxl2aldGbMacLimit,
       "jnxl2aldMacAdress": jnxl2aldMacAdress,
       "jnxL2aldMacNotificationMIBObjects": jnxL2aldMacNotificationMIBObjects,
       "jnxL2aldMacNotificationMIBGlobalObjects": jnxL2aldMacNotificationMIBGlobalObjects,
       "jnxL2aldMacGlobalFeatureEnabled": jnxL2aldMacGlobalFeatureEnabled,
       "jnxL2aldMacNotificationInterval": jnxL2aldMacNotificationInterval,
       "jnxL2aldMacAddressesLearnt": jnxL2aldMacAddressesLearnt,
       "jnxL2aldMacAddressesRemoved": jnxL2aldMacAddressesRemoved,
       "jnxL2aldMacNotificationsEnabled": jnxL2aldMacNotificationsEnabled,
       "jnxL2aldMacNotificationsSent": jnxL2aldMacNotificationsSent,
       "jnxL2aldMacHistTableMaxLength": jnxL2aldMacHistTableMaxLength,
       "jnxL2aldMacHistoryTable": jnxL2aldMacHistoryTable,
       "jnxL2aldMacHistoryEntry": jnxL2aldMacHistoryEntry,
       "jnxL2aldHistIndex": jnxL2aldHistIndex,
       "jnxL2aldHistMacChangedMsg": jnxL2aldHistMacChangedMsg,
       "jnxL2aldHistTimestamp": jnxL2aldHistTimestamp,
       "jnxL2aldMacAddressesUpdated": jnxL2aldMacAddressesUpdated,
       "jnxL2aldVlanMIBObjects": jnxL2aldVlanMIBObjects,
       "jnxL2aldVlanTable": jnxL2aldVlanTable,
       "jnxL2aldVlanEntry": jnxL2aldVlanEntry,
       "jnxL2aldVlanID": jnxL2aldVlanID,
       "jnxL2aldVlanName": jnxL2aldVlanName,
       "jnxL2aldVlanTag": jnxL2aldVlanTag,
       "jnxL2aldVlanType": jnxL2aldVlanType,
       "jnxL2aldVlanFdbId": jnxL2aldVlanFdbId}
)
