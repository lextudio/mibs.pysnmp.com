# SNMP MIB module (HPN-ICF-FC-TRACE-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-FC-TRACE-ROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:19 2024
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

(HpnicfFcAddress,
 HpnicfFcAddressType,
 HpnicfFcNameId,
 HpnicfFcStartOper,
 HpnicfFcVsanIndex) = mibBuilder.importSymbols(
    "HPN-ICF-FC-TC-MIB",
    "HpnicfFcAddress",
    "HpnicfFcAddressType",
    "HpnicfFcNameId",
    "HpnicfFcStartOper",
    "HpnicfFcVsanIndex")

(hpnicfSan,) = mibBuilder.importSymbols(
    "HPN-ICF-VSAN-MIB",
    "hpnicfSan")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfFcTraceRoute = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4)
)
hpnicfFcTraceRoute.setRevisions(
        ("2013-02-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfFcTraceRouteObjects_ObjectIdentity = ObjectIdentity
hpnicfFcTraceRouteObjects = _HpnicfFcTraceRouteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1)
)
_HpnicfFcTraceRouteConfigurations_ObjectIdentity = ObjectIdentity
hpnicfFcTraceRouteConfigurations = _HpnicfFcTraceRouteConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 1)
)
_HpnicfFcTraceRouteTable_Object = MibTable
hpnicfFcTraceRouteTable = _HpnicfFcTraceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteTable.setStatus("current")
_HpnicfFcTraceRouteEntry_Object = MibTableRow
hpnicfFcTraceRouteEntry = _HpnicfFcTraceRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 1, 1, 1)
)
hpnicfFcTraceRouteEntry.setIndexNames(
    (0, "HPN-ICF-FC-TRACE-ROUTE-MIB", "hpnicfFcTraceRouteIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteEntry.setStatus("current")


class _HpnicfFcTraceRouteIndex_Type(Unsigned32):
    """Custom type hpnicfFcTraceRouteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfFcTraceRouteIndex_Type.__name__ = "Unsigned32"
_HpnicfFcTraceRouteIndex_Object = MibTableColumn
hpnicfFcTraceRouteIndex = _HpnicfFcTraceRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 1, 1, 1, 1),
    _HpnicfFcTraceRouteIndex_Type()
)
hpnicfFcTraceRouteIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteIndex.setStatus("current")
_HpnicfFcTraceRouteVsan_Type = HpnicfFcVsanIndex
_HpnicfFcTraceRouteVsan_Object = MibTableColumn
hpnicfFcTraceRouteVsan = _HpnicfFcTraceRouteVsan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 1, 1, 1, 2),
    _HpnicfFcTraceRouteVsan_Type()
)
hpnicfFcTraceRouteVsan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteVsan.setStatus("current")


class _HpnicfFcTraceRouteAddressType_Type(HpnicfFcAddressType):
    """Custom type hpnicfFcTraceRouteAddressType based on HpnicfFcAddressType"""


_HpnicfFcTraceRouteAddressType_Object = MibTableColumn
hpnicfFcTraceRouteAddressType = _HpnicfFcTraceRouteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 1, 1, 1, 3),
    _HpnicfFcTraceRouteAddressType_Type()
)
hpnicfFcTraceRouteAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteAddressType.setStatus("current")
_HpnicfFcTraceRouteAddress_Type = HpnicfFcAddress
_HpnicfFcTraceRouteAddress_Object = MibTableColumn
hpnicfFcTraceRouteAddress = _HpnicfFcTraceRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 1, 1, 1, 4),
    _HpnicfFcTraceRouteAddress_Type()
)
hpnicfFcTraceRouteAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteAddress.setStatus("current")


class _HpnicfFcTraceRouteTimeout_Type(Unsigned32):
    """Custom type hpnicfFcTraceRouteTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpnicfFcTraceRouteTimeout_Type.__name__ = "Unsigned32"
_HpnicfFcTraceRouteTimeout_Object = MibTableColumn
hpnicfFcTraceRouteTimeout = _HpnicfFcTraceRouteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 1, 1, 1, 5),
    _HpnicfFcTraceRouteTimeout_Type()
)
hpnicfFcTraceRouteTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteTimeout.setUnits("seconds")


class _HpnicfFcTraceRouteAdminStatus_Type(HpnicfFcStartOper):
    """Custom type hpnicfFcTraceRouteAdminStatus based on HpnicfFcStartOper"""


_HpnicfFcTraceRouteAdminStatus_Object = MibTableColumn
hpnicfFcTraceRouteAdminStatus = _HpnicfFcTraceRouteAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 1, 1, 1, 6),
    _HpnicfFcTraceRouteAdminStatus_Type()
)
hpnicfFcTraceRouteAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteAdminStatus.setStatus("current")


class _HpnicfFcTraceRouteOperStatus_Type(Integer32):
    """Custom type hpnicfFcTraceRouteOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 5),
          ("failure", 4),
          ("inProgress", 1),
          ("partialSuccess", 3),
          ("success", 2))
    )


_HpnicfFcTraceRouteOperStatus_Type.__name__ = "Integer32"
_HpnicfFcTraceRouteOperStatus_Object = MibTableColumn
hpnicfFcTraceRouteOperStatus = _HpnicfFcTraceRouteOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 1, 1, 1, 7),
    _HpnicfFcTraceRouteOperStatus_Type()
)
hpnicfFcTraceRouteOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteOperStatus.setStatus("current")


class _HpnicfFcTraceRouteAgeInterval_Type(Unsigned32):
    """Custom type hpnicfFcTraceRouteAgeInterval based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 900),
    )


_HpnicfFcTraceRouteAgeInterval_Type.__name__ = "Unsigned32"
_HpnicfFcTraceRouteAgeInterval_Object = MibTableColumn
hpnicfFcTraceRouteAgeInterval = _HpnicfFcTraceRouteAgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 1, 1, 1, 8),
    _HpnicfFcTraceRouteAgeInterval_Type()
)
hpnicfFcTraceRouteAgeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteAgeInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteAgeInterval.setUnits("seconds")


class _HpnicfFcTraceRouteTrapOnCompletion_Type(TruthValue):
    """Custom type hpnicfFcTraceRouteTrapOnCompletion based on TruthValue"""


_HpnicfFcTraceRouteTrapOnCompletion_Object = MibTableColumn
hpnicfFcTraceRouteTrapOnCompletion = _HpnicfFcTraceRouteTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 1, 1, 1, 9),
    _HpnicfFcTraceRouteTrapOnCompletion_Type()
)
hpnicfFcTraceRouteTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteTrapOnCompletion.setStatus("current")
_HpnicfFcTraceRouteRowStatus_Type = RowStatus
_HpnicfFcTraceRouteRowStatus_Object = MibTableColumn
hpnicfFcTraceRouteRowStatus = _HpnicfFcTraceRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 1, 1, 1, 10),
    _HpnicfFcTraceRouteRowStatus_Type()
)
hpnicfFcTraceRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteRowStatus.setStatus("current")
_HpnicfFcTraceRouteResults_ObjectIdentity = ObjectIdentity
hpnicfFcTraceRouteResults = _HpnicfFcTraceRouteResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 2)
)
_HpnicfFcTraceRouteHopsTable_Object = MibTable
hpnicfFcTraceRouteHopsTable = _HpnicfFcTraceRouteHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteHopsTable.setStatus("current")
_HpnicfFcTraceRouteHopsEntry_Object = MibTableRow
hpnicfFcTraceRouteHopsEntry = _HpnicfFcTraceRouteHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 2, 1, 1)
)
hpnicfFcTraceRouteHopsEntry.setIndexNames(
    (0, "HPN-ICF-FC-TRACE-ROUTE-MIB", "hpnicfFcTraceRouteIndex"),
    (0, "HPN-ICF-FC-TRACE-ROUTE-MIB", "hpnicfFcTraceRouteHopsIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteHopsEntry.setStatus("current")


class _HpnicfFcTraceRouteHopsIndex_Type(Unsigned32):
    """Custom type hpnicfFcTraceRouteHopsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfFcTraceRouteHopsIndex_Type.__name__ = "Unsigned32"
_HpnicfFcTraceRouteHopsIndex_Object = MibTableColumn
hpnicfFcTraceRouteHopsIndex = _HpnicfFcTraceRouteHopsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 2, 1, 1, 1),
    _HpnicfFcTraceRouteHopsIndex_Type()
)
hpnicfFcTraceRouteHopsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteHopsIndex.setStatus("current")
_HpnicfFcTraceRouteHopsAddr_Type = HpnicfFcNameId
_HpnicfFcTraceRouteHopsAddr_Object = MibTableColumn
hpnicfFcTraceRouteHopsAddr = _HpnicfFcTraceRouteHopsAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 2, 1, 1, 2),
    _HpnicfFcTraceRouteHopsAddr_Type()
)
hpnicfFcTraceRouteHopsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteHopsAddr.setStatus("current")
_HpnicfFcTraceRouteNotifications_ObjectIdentity = ObjectIdentity
hpnicfFcTraceRouteNotifications = _HpnicfFcTraceRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 3)
)
_HpnicfFcTraceRouteNotifyPrefix_ObjectIdentity = ObjectIdentity
hpnicfFcTraceRouteNotifyPrefix = _HpnicfFcTraceRouteNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 3, 0)
)

# Managed Objects groups


# Notification objects

hpnicfFcTraceRouteCompletionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 4, 1, 3, 0, 1)
)
hpnicfFcTraceRouteCompletionNotify.setObjects(
      *(("HPN-ICF-FC-TRACE-ROUTE-MIB", "hpnicfFcTraceRouteIndex"),
        ("HPN-ICF-FC-TRACE-ROUTE-MIB", "hpnicfFcTraceRouteVsan"),
        ("HPN-ICF-FC-TRACE-ROUTE-MIB", "hpnicfFcTraceRouteAddressType"),
        ("HPN-ICF-FC-TRACE-ROUTE-MIB", "hpnicfFcTraceRouteAddress"),
        ("HPN-ICF-FC-TRACE-ROUTE-MIB", "hpnicfFcTraceRouteOperStatus"))
)
if mibBuilder.loadTexts:
    hpnicfFcTraceRouteCompletionNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-FC-TRACE-ROUTE-MIB",
    **{"hpnicfFcTraceRoute": hpnicfFcTraceRoute,
       "hpnicfFcTraceRouteObjects": hpnicfFcTraceRouteObjects,
       "hpnicfFcTraceRouteConfigurations": hpnicfFcTraceRouteConfigurations,
       "hpnicfFcTraceRouteTable": hpnicfFcTraceRouteTable,
       "hpnicfFcTraceRouteEntry": hpnicfFcTraceRouteEntry,
       "hpnicfFcTraceRouteIndex": hpnicfFcTraceRouteIndex,
       "hpnicfFcTraceRouteVsan": hpnicfFcTraceRouteVsan,
       "hpnicfFcTraceRouteAddressType": hpnicfFcTraceRouteAddressType,
       "hpnicfFcTraceRouteAddress": hpnicfFcTraceRouteAddress,
       "hpnicfFcTraceRouteTimeout": hpnicfFcTraceRouteTimeout,
       "hpnicfFcTraceRouteAdminStatus": hpnicfFcTraceRouteAdminStatus,
       "hpnicfFcTraceRouteOperStatus": hpnicfFcTraceRouteOperStatus,
       "hpnicfFcTraceRouteAgeInterval": hpnicfFcTraceRouteAgeInterval,
       "hpnicfFcTraceRouteTrapOnCompletion": hpnicfFcTraceRouteTrapOnCompletion,
       "hpnicfFcTraceRouteRowStatus": hpnicfFcTraceRouteRowStatus,
       "hpnicfFcTraceRouteResults": hpnicfFcTraceRouteResults,
       "hpnicfFcTraceRouteHopsTable": hpnicfFcTraceRouteHopsTable,
       "hpnicfFcTraceRouteHopsEntry": hpnicfFcTraceRouteHopsEntry,
       "hpnicfFcTraceRouteHopsIndex": hpnicfFcTraceRouteHopsIndex,
       "hpnicfFcTraceRouteHopsAddr": hpnicfFcTraceRouteHopsAddr,
       "hpnicfFcTraceRouteNotifications": hpnicfFcTraceRouteNotifications,
       "hpnicfFcTraceRouteNotifyPrefix": hpnicfFcTraceRouteNotifyPrefix,
       "hpnicfFcTraceRouteCompletionNotify": hpnicfFcTraceRouteCompletionNotify}
)
