# SNMP MIB module (HH3C-FC-TRACE-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-FC-TRACE-ROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:19 2024
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

(Hh3cFcAddress,
 Hh3cFcAddressType,
 Hh3cFcNameId,
 Hh3cFcStartOper,
 Hh3cFcVsanIndex) = mibBuilder.importSymbols(
    "HH3C-FC-TC-MIB",
    "Hh3cFcAddress",
    "Hh3cFcAddressType",
    "Hh3cFcNameId",
    "Hh3cFcStartOper",
    "Hh3cFcVsanIndex")

(hh3cSan,) = mibBuilder.importSymbols(
    "HH3C-VSAN-MIB",
    "hh3cSan")

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

hh3cFcTraceRoute = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4)
)
hh3cFcTraceRoute.setRevisions(
        ("2013-02-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cFcTraceRouteObjects_ObjectIdentity = ObjectIdentity
hh3cFcTraceRouteObjects = _Hh3cFcTraceRouteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1)
)
_Hh3cFcTraceRouteConfigurations_ObjectIdentity = ObjectIdentity
hh3cFcTraceRouteConfigurations = _Hh3cFcTraceRouteConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 1)
)
_Hh3cFcTraceRouteTable_Object = MibTable
hh3cFcTraceRouteTable = _Hh3cFcTraceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cFcTraceRouteTable.setStatus("current")
_Hh3cFcTraceRouteEntry_Object = MibTableRow
hh3cFcTraceRouteEntry = _Hh3cFcTraceRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 1, 1, 1)
)
hh3cFcTraceRouteEntry.setIndexNames(
    (0, "HH3C-FC-TRACE-ROUTE-MIB", "hh3cFcTraceRouteIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcTraceRouteEntry.setStatus("current")


class _Hh3cFcTraceRouteIndex_Type(Unsigned32):
    """Custom type hh3cFcTraceRouteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cFcTraceRouteIndex_Type.__name__ = "Unsigned32"
_Hh3cFcTraceRouteIndex_Object = MibTableColumn
hh3cFcTraceRouteIndex = _Hh3cFcTraceRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 1, 1, 1, 1),
    _Hh3cFcTraceRouteIndex_Type()
)
hh3cFcTraceRouteIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cFcTraceRouteIndex.setStatus("current")
_Hh3cFcTraceRouteVsan_Type = Hh3cFcVsanIndex
_Hh3cFcTraceRouteVsan_Object = MibTableColumn
hh3cFcTraceRouteVsan = _Hh3cFcTraceRouteVsan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 1, 1, 1, 2),
    _Hh3cFcTraceRouteVsan_Type()
)
hh3cFcTraceRouteVsan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcTraceRouteVsan.setStatus("current")


class _Hh3cFcTraceRouteAddressType_Type(Hh3cFcAddressType):
    """Custom type hh3cFcTraceRouteAddressType based on Hh3cFcAddressType"""


_Hh3cFcTraceRouteAddressType_Object = MibTableColumn
hh3cFcTraceRouteAddressType = _Hh3cFcTraceRouteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 1, 1, 1, 3),
    _Hh3cFcTraceRouteAddressType_Type()
)
hh3cFcTraceRouteAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcTraceRouteAddressType.setStatus("current")
_Hh3cFcTraceRouteAddress_Type = Hh3cFcAddress
_Hh3cFcTraceRouteAddress_Object = MibTableColumn
hh3cFcTraceRouteAddress = _Hh3cFcTraceRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 1, 1, 1, 4),
    _Hh3cFcTraceRouteAddress_Type()
)
hh3cFcTraceRouteAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcTraceRouteAddress.setStatus("current")


class _Hh3cFcTraceRouteTimeout_Type(Unsigned32):
    """Custom type hh3cFcTraceRouteTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hh3cFcTraceRouteTimeout_Type.__name__ = "Unsigned32"
_Hh3cFcTraceRouteTimeout_Object = MibTableColumn
hh3cFcTraceRouteTimeout = _Hh3cFcTraceRouteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 1, 1, 1, 5),
    _Hh3cFcTraceRouteTimeout_Type()
)
hh3cFcTraceRouteTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcTraceRouteTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFcTraceRouteTimeout.setUnits("seconds")


class _Hh3cFcTraceRouteAdminStatus_Type(Hh3cFcStartOper):
    """Custom type hh3cFcTraceRouteAdminStatus based on Hh3cFcStartOper"""


_Hh3cFcTraceRouteAdminStatus_Object = MibTableColumn
hh3cFcTraceRouteAdminStatus = _Hh3cFcTraceRouteAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 1, 1, 1, 6),
    _Hh3cFcTraceRouteAdminStatus_Type()
)
hh3cFcTraceRouteAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcTraceRouteAdminStatus.setStatus("current")


class _Hh3cFcTraceRouteOperStatus_Type(Integer32):
    """Custom type hh3cFcTraceRouteOperStatus based on Integer32"""
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


_Hh3cFcTraceRouteOperStatus_Type.__name__ = "Integer32"
_Hh3cFcTraceRouteOperStatus_Object = MibTableColumn
hh3cFcTraceRouteOperStatus = _Hh3cFcTraceRouteOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 1, 1, 1, 7),
    _Hh3cFcTraceRouteOperStatus_Type()
)
hh3cFcTraceRouteOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcTraceRouteOperStatus.setStatus("current")


class _Hh3cFcTraceRouteAgeInterval_Type(Unsigned32):
    """Custom type hh3cFcTraceRouteAgeInterval based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 900),
    )


_Hh3cFcTraceRouteAgeInterval_Type.__name__ = "Unsigned32"
_Hh3cFcTraceRouteAgeInterval_Object = MibTableColumn
hh3cFcTraceRouteAgeInterval = _Hh3cFcTraceRouteAgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 1, 1, 1, 8),
    _Hh3cFcTraceRouteAgeInterval_Type()
)
hh3cFcTraceRouteAgeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcTraceRouteAgeInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFcTraceRouteAgeInterval.setUnits("seconds")


class _Hh3cFcTraceRouteTrapOnCompletion_Type(TruthValue):
    """Custom type hh3cFcTraceRouteTrapOnCompletion based on TruthValue"""


_Hh3cFcTraceRouteTrapOnCompletion_Object = MibTableColumn
hh3cFcTraceRouteTrapOnCompletion = _Hh3cFcTraceRouteTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 1, 1, 1, 9),
    _Hh3cFcTraceRouteTrapOnCompletion_Type()
)
hh3cFcTraceRouteTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcTraceRouteTrapOnCompletion.setStatus("current")
_Hh3cFcTraceRouteRowStatus_Type = RowStatus
_Hh3cFcTraceRouteRowStatus_Object = MibTableColumn
hh3cFcTraceRouteRowStatus = _Hh3cFcTraceRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 1, 1, 1, 10),
    _Hh3cFcTraceRouteRowStatus_Type()
)
hh3cFcTraceRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcTraceRouteRowStatus.setStatus("current")
_Hh3cFcTraceRouteResults_ObjectIdentity = ObjectIdentity
hh3cFcTraceRouteResults = _Hh3cFcTraceRouteResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 2)
)
_Hh3cFcTraceRouteHopsTable_Object = MibTable
hh3cFcTraceRouteHopsTable = _Hh3cFcTraceRouteHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cFcTraceRouteHopsTable.setStatus("current")
_Hh3cFcTraceRouteHopsEntry_Object = MibTableRow
hh3cFcTraceRouteHopsEntry = _Hh3cFcTraceRouteHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 2, 1, 1)
)
hh3cFcTraceRouteHopsEntry.setIndexNames(
    (0, "HH3C-FC-TRACE-ROUTE-MIB", "hh3cFcTraceRouteIndex"),
    (0, "HH3C-FC-TRACE-ROUTE-MIB", "hh3cFcTraceRouteHopsIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcTraceRouteHopsEntry.setStatus("current")


class _Hh3cFcTraceRouteHopsIndex_Type(Unsigned32):
    """Custom type hh3cFcTraceRouteHopsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cFcTraceRouteHopsIndex_Type.__name__ = "Unsigned32"
_Hh3cFcTraceRouteHopsIndex_Object = MibTableColumn
hh3cFcTraceRouteHopsIndex = _Hh3cFcTraceRouteHopsIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 2, 1, 1, 1),
    _Hh3cFcTraceRouteHopsIndex_Type()
)
hh3cFcTraceRouteHopsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFcTraceRouteHopsIndex.setStatus("current")
_Hh3cFcTraceRouteHopsAddr_Type = Hh3cFcNameId
_Hh3cFcTraceRouteHopsAddr_Object = MibTableColumn
hh3cFcTraceRouteHopsAddr = _Hh3cFcTraceRouteHopsAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 2, 1, 1, 2),
    _Hh3cFcTraceRouteHopsAddr_Type()
)
hh3cFcTraceRouteHopsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcTraceRouteHopsAddr.setStatus("current")
_Hh3cFcTraceRouteNotifications_ObjectIdentity = ObjectIdentity
hh3cFcTraceRouteNotifications = _Hh3cFcTraceRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 3)
)
_Hh3cFcTraceRouteNotifyPrefix_ObjectIdentity = ObjectIdentity
hh3cFcTraceRouteNotifyPrefix = _Hh3cFcTraceRouteNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cFcTraceRouteCompletionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 4, 1, 3, 0, 1)
)
hh3cFcTraceRouteCompletionNotify.setObjects(
      *(("HH3C-FC-TRACE-ROUTE-MIB", "hh3cFcTraceRouteIndex"),
        ("HH3C-FC-TRACE-ROUTE-MIB", "hh3cFcTraceRouteVsan"),
        ("HH3C-FC-TRACE-ROUTE-MIB", "hh3cFcTraceRouteAddressType"),
        ("HH3C-FC-TRACE-ROUTE-MIB", "hh3cFcTraceRouteAddress"),
        ("HH3C-FC-TRACE-ROUTE-MIB", "hh3cFcTraceRouteOperStatus"))
)
if mibBuilder.loadTexts:
    hh3cFcTraceRouteCompletionNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FC-TRACE-ROUTE-MIB",
    **{"hh3cFcTraceRoute": hh3cFcTraceRoute,
       "hh3cFcTraceRouteObjects": hh3cFcTraceRouteObjects,
       "hh3cFcTraceRouteConfigurations": hh3cFcTraceRouteConfigurations,
       "hh3cFcTraceRouteTable": hh3cFcTraceRouteTable,
       "hh3cFcTraceRouteEntry": hh3cFcTraceRouteEntry,
       "hh3cFcTraceRouteIndex": hh3cFcTraceRouteIndex,
       "hh3cFcTraceRouteVsan": hh3cFcTraceRouteVsan,
       "hh3cFcTraceRouteAddressType": hh3cFcTraceRouteAddressType,
       "hh3cFcTraceRouteAddress": hh3cFcTraceRouteAddress,
       "hh3cFcTraceRouteTimeout": hh3cFcTraceRouteTimeout,
       "hh3cFcTraceRouteAdminStatus": hh3cFcTraceRouteAdminStatus,
       "hh3cFcTraceRouteOperStatus": hh3cFcTraceRouteOperStatus,
       "hh3cFcTraceRouteAgeInterval": hh3cFcTraceRouteAgeInterval,
       "hh3cFcTraceRouteTrapOnCompletion": hh3cFcTraceRouteTrapOnCompletion,
       "hh3cFcTraceRouteRowStatus": hh3cFcTraceRouteRowStatus,
       "hh3cFcTraceRouteResults": hh3cFcTraceRouteResults,
       "hh3cFcTraceRouteHopsTable": hh3cFcTraceRouteHopsTable,
       "hh3cFcTraceRouteHopsEntry": hh3cFcTraceRouteHopsEntry,
       "hh3cFcTraceRouteHopsIndex": hh3cFcTraceRouteHopsIndex,
       "hh3cFcTraceRouteHopsAddr": hh3cFcTraceRouteHopsAddr,
       "hh3cFcTraceRouteNotifications": hh3cFcTraceRouteNotifications,
       "hh3cFcTraceRouteNotifyPrefix": hh3cFcTraceRouteNotifyPrefix,
       "hh3cFcTraceRouteCompletionNotify": hh3cFcTraceRouteCompletionNotify}
)
