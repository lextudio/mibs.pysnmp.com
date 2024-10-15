# SNMP MIB module (HM2-TRACKING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-TRACKING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:33 2024
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

(HmEnabledStatus,
 HmTimeSeconds1970,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "HmTimeSeconds1970",
    "hm2ConfigurationMibs")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(inetCidrRouteEntry,) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "inetCidrRouteEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hm2TrackingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 115)
)
hm2TrackingMib.setRevisions(
        ("2013-09-03 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2TrackingMibNotifications_ObjectIdentity = ObjectIdentity
hm2TrackingMibNotifications = _Hm2TrackingMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 0)
)
_Hm2TrackingMibObjects_ObjectIdentity = ObjectIdentity
hm2TrackingMibObjects = _Hm2TrackingMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1)
)
_Hm2TrackingConfigGroup_ObjectIdentity = ObjectIdentity
hm2TrackingConfigGroup = _Hm2TrackingConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1)
)
_Hm2TrackingConfigTable_Object = MibTable
hm2TrackingConfigTable = _Hm2TrackingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hm2TrackingConfigTable.setStatus("current")
_Hm2TrackingConfigEntry_Object = MibTableRow
hm2TrackingConfigEntry = _Hm2TrackingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1)
)
hm2TrackingConfigEntry.setIndexNames(
    (0, "HM2-TRACKING-MIB", "hm2TrackType"),
    (0, "HM2-TRACKING-MIB", "hm2TrackId"),
)
if mibBuilder.loadTexts:
    hm2TrackingConfigEntry.setStatus("current")


class _Hm2TrackType_Type(Integer32):
    """Custom type hm2TrackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("logical", 3),
          ("ping", 2))
    )


_Hm2TrackType_Type.__name__ = "Integer32"
_Hm2TrackType_Object = MibTableColumn
hm2TrackType = _Hm2TrackType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 1),
    _Hm2TrackType_Type()
)
hm2TrackType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2TrackType.setStatus("current")


class _Hm2TrackId_Type(Integer32):
    """Custom type hm2TrackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Hm2TrackId_Type.__name__ = "Integer32"
_Hm2TrackId_Object = MibTableColumn
hm2TrackId = _Hm2TrackId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 2),
    _Hm2TrackId_Type()
)
hm2TrackId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2TrackId.setStatus("current")
_Hm2TrackName_Type = SnmpAdminString
_Hm2TrackName_Object = MibTableColumn
hm2TrackName = _Hm2TrackName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 3),
    _Hm2TrackName_Type()
)
hm2TrackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TrackName.setStatus("current")
_Hm2TrackDescription_Type = SnmpAdminString
_Hm2TrackDescription_Object = MibTableColumn
hm2TrackDescription = _Hm2TrackDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 4),
    _Hm2TrackDescription_Type()
)
hm2TrackDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2TrackDescription.setStatus("current")


class _Hm2TrackOperState_Type(Integer32):
    """Custom type hm2TrackOperState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("notReady", 3),
          ("up", 1))
    )


_Hm2TrackOperState_Type.__name__ = "Integer32"
_Hm2TrackOperState_Object = MibTableColumn
hm2TrackOperState = _Hm2TrackOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 5),
    _Hm2TrackOperState_Type()
)
hm2TrackOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TrackOperState.setStatus("current")
_Hm2TrackNumberOfChanges_Type = Integer32
_Hm2TrackNumberOfChanges_Object = MibTableColumn
hm2TrackNumberOfChanges = _Hm2TrackNumberOfChanges_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 6),
    _Hm2TrackNumberOfChanges_Type()
)
hm2TrackNumberOfChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TrackNumberOfChanges.setStatus("current")
_Hm2TrackTimeLastChange_Type = HmTimeSeconds1970
_Hm2TrackTimeLastChange_Object = MibTableColumn
hm2TrackTimeLastChange = _Hm2TrackTimeLastChange_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 7),
    _Hm2TrackTimeLastChange_Type()
)
hm2TrackTimeLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TrackTimeLastChange.setStatus("current")


class _Hm2TrackSendStateChangeTrap_Type(HmEnabledStatus):
    """Custom type hm2TrackSendStateChangeTrap based on HmEnabledStatus"""


_Hm2TrackSendStateChangeTrap_Object = MibTableColumn
hm2TrackSendStateChangeTrap = _Hm2TrackSendStateChangeTrap_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 8),
    _Hm2TrackSendStateChangeTrap_Type()
)
hm2TrackSendStateChangeTrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2TrackSendStateChangeTrap.setStatus("current")
_Hm2TrackStatus_Type = RowStatus
_Hm2TrackStatus_Object = MibTableColumn
hm2TrackStatus = _Hm2TrackStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 1, 1, 1, 9),
    _Hm2TrackStatus_Type()
)
hm2TrackStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2TrackStatus.setStatus("current")
_Hm2TrackingInterfaceGroup_ObjectIdentity = ObjectIdentity
hm2TrackingInterfaceGroup = _Hm2TrackingInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 2)
)
_Hm2TrackingInterfaceTable_Object = MibTable
hm2TrackingInterfaceTable = _Hm2TrackingInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hm2TrackingInterfaceTable.setStatus("current")
_Hm2TrackingInterfaceEntry_Object = MibTableRow
hm2TrackingInterfaceEntry = _Hm2TrackingInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 2, 1, 1)
)
hm2TrackingInterfaceEntry.setIndexNames(
    (0, "HM2-TRACKING-MIB", "hm2TrackInterfaceId"),
)
if mibBuilder.loadTexts:
    hm2TrackingInterfaceEntry.setStatus("current")
_Hm2TrackInterfaceId_Type = Integer32
_Hm2TrackInterfaceId_Object = MibTableColumn
hm2TrackInterfaceId = _Hm2TrackInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 2, 1, 1, 1),
    _Hm2TrackInterfaceId_Type()
)
hm2TrackInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2TrackInterfaceId.setStatus("current")


class _Hm2TrackIfNumber_Type(InterfaceIndexOrZero):
    """Custom type hm2TrackIfNumber based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2TrackIfNumber_Object = MibTableColumn
hm2TrackIfNumber = _Hm2TrackIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 2, 1, 1, 2),
    _Hm2TrackIfNumber_Type()
)
hm2TrackIfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrackIfNumber.setStatus("current")


class _Hm2TrackIfLinkUpDelay_Type(Integer32):
    """Custom type hm2TrackIfLinkUpDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hm2TrackIfLinkUpDelay_Type.__name__ = "Integer32"
_Hm2TrackIfLinkUpDelay_Object = MibTableColumn
hm2TrackIfLinkUpDelay = _Hm2TrackIfLinkUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 2, 1, 1, 3),
    _Hm2TrackIfLinkUpDelay_Type()
)
hm2TrackIfLinkUpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrackIfLinkUpDelay.setStatus("current")
if mibBuilder.loadTexts:
    hm2TrackIfLinkUpDelay.setUnits("seconds")


class _Hm2TrackIfLinkDownDelay_Type(Integer32):
    """Custom type hm2TrackIfLinkDownDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hm2TrackIfLinkDownDelay_Type.__name__ = "Integer32"
_Hm2TrackIfLinkDownDelay_Object = MibTableColumn
hm2TrackIfLinkDownDelay = _Hm2TrackIfLinkDownDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 2, 1, 1, 4),
    _Hm2TrackIfLinkDownDelay_Type()
)
hm2TrackIfLinkDownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrackIfLinkDownDelay.setStatus("current")
if mibBuilder.loadTexts:
    hm2TrackIfLinkDownDelay.setUnits("seconds")
_Hm2TrackingPingGroup_ObjectIdentity = ObjectIdentity
hm2TrackingPingGroup = _Hm2TrackingPingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3)
)
_Hm2TrackingPingTable_Object = MibTable
hm2TrackingPingTable = _Hm2TrackingPingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hm2TrackingPingTable.setStatus("current")
_Hm2TrackingPingEntry_Object = MibTableRow
hm2TrackingPingEntry = _Hm2TrackingPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1)
)
hm2TrackingPingEntry.setIndexNames(
    (0, "HM2-TRACKING-MIB", "hm2TrackPingId"),
)
if mibBuilder.loadTexts:
    hm2TrackingPingEntry.setStatus("current")
_Hm2TrackPingId_Type = Integer32
_Hm2TrackPingId_Object = MibTableColumn
hm2TrackPingId = _Hm2TrackPingId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 1),
    _Hm2TrackPingId_Type()
)
hm2TrackPingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2TrackPingId.setStatus("current")


class _Hm2TrackPingIfNumber_Type(InterfaceIndexOrZero):
    """Custom type hm2TrackPingIfNumber based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2TrackPingIfNumber_Object = MibTableColumn
hm2TrackPingIfNumber = _Hm2TrackPingIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 2),
    _Hm2TrackPingIfNumber_Type()
)
hm2TrackPingIfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrackPingIfNumber.setStatus("current")
_Hm2TrackPingInetAddrType_Type = InetAddressType
_Hm2TrackPingInetAddrType_Object = MibTableColumn
hm2TrackPingInetAddrType = _Hm2TrackPingInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 3),
    _Hm2TrackPingInetAddrType_Type()
)
hm2TrackPingInetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrackPingInetAddrType.setStatus("current")
_Hm2TrackPingInetAddr_Type = InetAddress
_Hm2TrackPingInetAddr_Object = MibTableColumn
hm2TrackPingInetAddr = _Hm2TrackPingInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 4),
    _Hm2TrackPingInetAddr_Type()
)
hm2TrackPingInetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrackPingInetAddr.setStatus("current")


class _Hm2TrackPingInterval_Type(Integer32):
    """Custom type hm2TrackPingInterval based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 20000),
    )


_Hm2TrackPingInterval_Type.__name__ = "Integer32"
_Hm2TrackPingInterval_Object = MibTableColumn
hm2TrackPingInterval = _Hm2TrackPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 5),
    _Hm2TrackPingInterval_Type()
)
hm2TrackPingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrackPingInterval.setStatus("current")
if mibBuilder.loadTexts:
    hm2TrackPingInterval.setUnits("milliseconds")


class _Hm2TrackPingMiss_Type(Integer32):
    """Custom type hm2TrackPingMiss based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hm2TrackPingMiss_Type.__name__ = "Integer32"
_Hm2TrackPingMiss_Object = MibTableColumn
hm2TrackPingMiss = _Hm2TrackPingMiss_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 6),
    _Hm2TrackPingMiss_Type()
)
hm2TrackPingMiss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrackPingMiss.setStatus("current")


class _Hm2TrackPingSuccess_Type(Integer32):
    """Custom type hm2TrackPingSuccess based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hm2TrackPingSuccess_Type.__name__ = "Integer32"
_Hm2TrackPingSuccess_Object = MibTableColumn
hm2TrackPingSuccess = _Hm2TrackPingSuccess_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 7),
    _Hm2TrackPingSuccess_Type()
)
hm2TrackPingSuccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrackPingSuccess.setStatus("current")


class _Hm2TrackPingTimeout_Type(Integer32):
    """Custom type hm2TrackPingTimeout based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_Hm2TrackPingTimeout_Type.__name__ = "Integer32"
_Hm2TrackPingTimeout_Object = MibTableColumn
hm2TrackPingTimeout = _Hm2TrackPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 8),
    _Hm2TrackPingTimeout_Type()
)
hm2TrackPingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrackPingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hm2TrackPingTimeout.setUnits("milliseconds")


class _Hm2TrackPingTTL_Type(Integer32):
    """Custom type hm2TrackPingTTL based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hm2TrackPingTTL_Type.__name__ = "Integer32"
_Hm2TrackPingTTL_Object = MibTableColumn
hm2TrackPingTTL = _Hm2TrackPingTTL_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 9),
    _Hm2TrackPingTTL_Type()
)
hm2TrackPingTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrackPingTTL.setStatus("current")
_Hm2TrackPingBestRouteIfNumber_Type = InterfaceIndexOrZero
_Hm2TrackPingBestRouteIfNumber_Object = MibTableColumn
hm2TrackPingBestRouteIfNumber = _Hm2TrackPingBestRouteIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 3, 1, 1, 10),
    _Hm2TrackPingBestRouteIfNumber_Type()
)
hm2TrackPingBestRouteIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TrackPingBestRouteIfNumber.setStatus("current")
_Hm2TrackingLogicalGroup_ObjectIdentity = ObjectIdentity
hm2TrackingLogicalGroup = _Hm2TrackingLogicalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 4)
)
_Hm2TrackLogicalInstanceTable_Object = MibTable
hm2TrackLogicalInstanceTable = _Hm2TrackLogicalInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hm2TrackLogicalInstanceTable.setStatus("current")
_Hm2TrackLogicalInstanceEntry_Object = MibTableRow
hm2TrackLogicalInstanceEntry = _Hm2TrackLogicalInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 4, 1, 1)
)
hm2TrackLogicalInstanceEntry.setIndexNames(
    (0, "HM2-TRACKING-MIB", "hm2TrackLogicalId"),
)
if mibBuilder.loadTexts:
    hm2TrackLogicalInstanceEntry.setStatus("current")
_Hm2TrackLogicalId_Type = Integer32
_Hm2TrackLogicalId_Object = MibTableColumn
hm2TrackLogicalId = _Hm2TrackLogicalId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 4, 1, 1, 1),
    _Hm2TrackLogicalId_Type()
)
hm2TrackLogicalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2TrackLogicalId.setStatus("current")
_Hm2TrackLogicalOperandNameA_Type = SnmpAdminString
_Hm2TrackLogicalOperandNameA_Object = MibTableColumn
hm2TrackLogicalOperandNameA = _Hm2TrackLogicalOperandNameA_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 4, 1, 1, 2),
    _Hm2TrackLogicalOperandNameA_Type()
)
hm2TrackLogicalOperandNameA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrackLogicalOperandNameA.setStatus("current")
_Hm2TrackLogicalOperandNameB_Type = SnmpAdminString
_Hm2TrackLogicalOperandNameB_Object = MibTableColumn
hm2TrackLogicalOperandNameB = _Hm2TrackLogicalOperandNameB_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 4, 1, 1, 3),
    _Hm2TrackLogicalOperandNameB_Type()
)
hm2TrackLogicalOperandNameB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrackLogicalOperandNameB.setStatus("current")


class _Hm2TrackLogicalOperator_Type(Integer32):
    """Custom type hm2TrackLogicalOperator based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("and", 1),
          ("or", 2))
    )


_Hm2TrackLogicalOperator_Type.__name__ = "Integer32"
_Hm2TrackLogicalOperator_Object = MibTableColumn
hm2TrackLogicalOperator = _Hm2TrackLogicalOperator_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 4, 1, 1, 4),
    _Hm2TrackLogicalOperator_Type()
)
hm2TrackLogicalOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TrackLogicalOperator.setStatus("current")
_Hm2TrackingApplicationGroup_ObjectIdentity = ObjectIdentity
hm2TrackingApplicationGroup = _Hm2TrackingApplicationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 5)
)
_Hm2TrackingApplicationTable_Object = MibTable
hm2TrackingApplicationTable = _Hm2TrackingApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hm2TrackingApplicationTable.setStatus("current")
_Hm2TrackingApplicationEntry_Object = MibTableRow
hm2TrackingApplicationEntry = _Hm2TrackingApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 5, 1, 1)
)
hm2TrackingApplicationEntry.setIndexNames(
    (0, "HM2-TRACKING-MIB", "hm2TrackAppId"),
    (0, "HM2-TRACKING-MIB", "hm2TrackType"),
    (0, "HM2-TRACKING-MIB", "hm2TrackId"),
)
if mibBuilder.loadTexts:
    hm2TrackingApplicationEntry.setStatus("current")
_Hm2TrackAppId_Type = Integer32
_Hm2TrackAppId_Object = MibTableColumn
hm2TrackAppId = _Hm2TrackAppId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 5, 1, 1, 1),
    _Hm2TrackAppId_Type()
)
hm2TrackAppId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2TrackAppId.setStatus("current")
_Hm2TrackAppName_Type = SnmpAdminString
_Hm2TrackAppName_Object = MibTableColumn
hm2TrackAppName = _Hm2TrackAppName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 5, 1, 1, 4),
    _Hm2TrackAppName_Type()
)
hm2TrackAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TrackAppName.setStatus("current")
_Hm2TrackAppObjectName_Type = SnmpAdminString
_Hm2TrackAppObjectName_Object = MibTableColumn
hm2TrackAppObjectName = _Hm2TrackAppObjectName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 5, 1, 1, 5),
    _Hm2TrackAppObjectName_Type()
)
hm2TrackAppObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TrackAppObjectName.setStatus("current")
_Hm2TrackingStaticRouteGroup_ObjectIdentity = ObjectIdentity
hm2TrackingStaticRouteGroup = _Hm2TrackingStaticRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 6)
)
_Hm2TrackStaticRouteTable_Object = MibTable
hm2TrackStaticRouteTable = _Hm2TrackStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hm2TrackStaticRouteTable.setStatus("current")
_Hm2TrackStaticRouteEntry_Object = MibTableRow
hm2TrackStaticRouteEntry = _Hm2TrackStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hm2TrackStaticRouteEntry.setStatus("current")
_Hm2TrackStaticRouteTrackId_Type = SnmpAdminString
_Hm2TrackStaticRouteTrackId_Object = MibTableColumn
hm2TrackStaticRouteTrackId = _Hm2TrackStaticRouteTrackId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 6, 1, 1, 1),
    _Hm2TrackStaticRouteTrackId_Type()
)
hm2TrackStaticRouteTrackId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2TrackStaticRouteTrackId.setStatus("current")


class _Hm2TrackStaticRouteTrackState_Type(Integer32):
    """Custom type hm2TrackStaticRouteTrackState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("notReady", 3),
          ("up", 1))
    )


_Hm2TrackStaticRouteTrackState_Type.__name__ = "Integer32"
_Hm2TrackStaticRouteTrackState_Object = MibTableColumn
hm2TrackStaticRouteTrackState = _Hm2TrackStaticRouteTrackState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 1, 6, 1, 1, 2),
    _Hm2TrackStaticRouteTrackState_Type()
)
hm2TrackStaticRouteTrackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TrackStaticRouteTrackState.setStatus("current")
inetCidrRouteEntry.registerAugmentions(
    ("HM2-TRACKING-MIB",
     "hm2TrackStaticRouteEntry")
)
hm2TrackStaticRouteEntry.setIndexNames(*inetCidrRouteEntry.getIndexNames())

# Managed Objects groups


# Notification objects

hm2TrackStatusChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 115, 0, 1)
)
hm2TrackStatusChangeEvent.setObjects(
      *(("HM2-TRACKING-MIB", "hm2TrackType"),
        ("HM2-TRACKING-MIB", "hm2TrackId"),
        ("HM2-TRACKING-MIB", "hm2TrackStatus"),
        ("HM2-TRACKING-MIB", "hm2TrackOperState"))
)
if mibBuilder.loadTexts:
    hm2TrackStatusChangeEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-TRACKING-MIB",
    **{"hm2TrackingMib": hm2TrackingMib,
       "hm2TrackingMibNotifications": hm2TrackingMibNotifications,
       "hm2TrackStatusChangeEvent": hm2TrackStatusChangeEvent,
       "hm2TrackingMibObjects": hm2TrackingMibObjects,
       "hm2TrackingConfigGroup": hm2TrackingConfigGroup,
       "hm2TrackingConfigTable": hm2TrackingConfigTable,
       "hm2TrackingConfigEntry": hm2TrackingConfigEntry,
       "hm2TrackType": hm2TrackType,
       "hm2TrackId": hm2TrackId,
       "hm2TrackName": hm2TrackName,
       "hm2TrackDescription": hm2TrackDescription,
       "hm2TrackOperState": hm2TrackOperState,
       "hm2TrackNumberOfChanges": hm2TrackNumberOfChanges,
       "hm2TrackTimeLastChange": hm2TrackTimeLastChange,
       "hm2TrackSendStateChangeTrap": hm2TrackSendStateChangeTrap,
       "hm2TrackStatus": hm2TrackStatus,
       "hm2TrackingInterfaceGroup": hm2TrackingInterfaceGroup,
       "hm2TrackingInterfaceTable": hm2TrackingInterfaceTable,
       "hm2TrackingInterfaceEntry": hm2TrackingInterfaceEntry,
       "hm2TrackInterfaceId": hm2TrackInterfaceId,
       "hm2TrackIfNumber": hm2TrackIfNumber,
       "hm2TrackIfLinkUpDelay": hm2TrackIfLinkUpDelay,
       "hm2TrackIfLinkDownDelay": hm2TrackIfLinkDownDelay,
       "hm2TrackingPingGroup": hm2TrackingPingGroup,
       "hm2TrackingPingTable": hm2TrackingPingTable,
       "hm2TrackingPingEntry": hm2TrackingPingEntry,
       "hm2TrackPingId": hm2TrackPingId,
       "hm2TrackPingIfNumber": hm2TrackPingIfNumber,
       "hm2TrackPingInetAddrType": hm2TrackPingInetAddrType,
       "hm2TrackPingInetAddr": hm2TrackPingInetAddr,
       "hm2TrackPingInterval": hm2TrackPingInterval,
       "hm2TrackPingMiss": hm2TrackPingMiss,
       "hm2TrackPingSuccess": hm2TrackPingSuccess,
       "hm2TrackPingTimeout": hm2TrackPingTimeout,
       "hm2TrackPingTTL": hm2TrackPingTTL,
       "hm2TrackPingBestRouteIfNumber": hm2TrackPingBestRouteIfNumber,
       "hm2TrackingLogicalGroup": hm2TrackingLogicalGroup,
       "hm2TrackLogicalInstanceTable": hm2TrackLogicalInstanceTable,
       "hm2TrackLogicalInstanceEntry": hm2TrackLogicalInstanceEntry,
       "hm2TrackLogicalId": hm2TrackLogicalId,
       "hm2TrackLogicalOperandNameA": hm2TrackLogicalOperandNameA,
       "hm2TrackLogicalOperandNameB": hm2TrackLogicalOperandNameB,
       "hm2TrackLogicalOperator": hm2TrackLogicalOperator,
       "hm2TrackingApplicationGroup": hm2TrackingApplicationGroup,
       "hm2TrackingApplicationTable": hm2TrackingApplicationTable,
       "hm2TrackingApplicationEntry": hm2TrackingApplicationEntry,
       "hm2TrackAppId": hm2TrackAppId,
       "hm2TrackAppName": hm2TrackAppName,
       "hm2TrackAppObjectName": hm2TrackAppObjectName,
       "hm2TrackingStaticRouteGroup": hm2TrackingStaticRouteGroup,
       "hm2TrackStaticRouteTable": hm2TrackStaticRouteTable,
       "hm2TrackStaticRouteEntry": hm2TrackStaticRouteEntry,
       "hm2TrackStaticRouteTrackId": hm2TrackStaticRouteTrackId,
       "hm2TrackStaticRouteTrackState": hm2TrackStaticRouteTrackState}
)
