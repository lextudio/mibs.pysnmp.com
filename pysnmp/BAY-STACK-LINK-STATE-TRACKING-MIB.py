# SNMP MIB module (BAY-STACK-LINK-STATE-TRACKING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-LINK-STATE-TRACKING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:06 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(IdList,) = mibBuilder.importSymbols(
    "RAPID-CITY",
    "IdList")

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

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackLinkStateTrackingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 43)
)
bayStackLinkStateTrackingMib.setRevisions(
        ("2013-10-11 00:00",
         "2013-02-13 00:00",
         "2012-11-15 00:00",
         "2012-10-17 00:00",
         "2012-09-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsLstNotifications_ObjectIdentity = ObjectIdentity
bsLstNotifications = _BsLstNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 0)
)
_BsLstObjects_ObjectIdentity = ObjectIdentity
bsLstObjects = _BsLstObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 1)
)
_BsLstScalars_ObjectIdentity = ObjectIdentity
bsLstScalars = _BsLstScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 1)
)
_BsLstGroupTable_Object = MibTable
bsLstGroupTable = _BsLstGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2)
)
if mibBuilder.loadTexts:
    bsLstGroupTable.setStatus("current")
_BsLstGroupEntry_Object = MibTableRow
bsLstGroupEntry = _BsLstGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1)
)
bsLstGroupEntry.setIndexNames(
    (0, "BAY-STACK-LINK-STATE-TRACKING-MIB", "bsLstGroupIndex"),
)
if mibBuilder.loadTexts:
    bsLstGroupEntry.setStatus("current")


class _BsLstGroupIndex_Type(Unsigned32):
    """Custom type bsLstGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BsLstGroupIndex_Type.__name__ = "Unsigned32"
_BsLstGroupIndex_Object = MibTableColumn
bsLstGroupIndex = _BsLstGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 1),
    _BsLstGroupIndex_Type()
)
bsLstGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLstGroupIndex.setStatus("current")


class _BsLstGroupEnabled_Type(TruthValue):
    """Custom type bsLstGroupEnabled based on TruthValue"""


_BsLstGroupEnabled_Object = MibTableColumn
bsLstGroupEnabled = _BsLstGroupEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 2),
    _BsLstGroupEnabled_Type()
)
bsLstGroupEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsLstGroupEnabled.setStatus("current")


class _BsLstGroupUpstreamPortList_Type(PortList):
    """Custom type bsLstGroupUpstreamPortList based on PortList"""
    defaultHexValue = ""


_BsLstGroupUpstreamPortList_Object = MibTableColumn
bsLstGroupUpstreamPortList = _BsLstGroupUpstreamPortList_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 3),
    _BsLstGroupUpstreamPortList_Type()
)
bsLstGroupUpstreamPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsLstGroupUpstreamPortList.setStatus("current")


class _BsLstGroupDownstreamPortList_Type(PortList):
    """Custom type bsLstGroupDownstreamPortList based on PortList"""
    defaultHexValue = ""


_BsLstGroupDownstreamPortList_Object = MibTableColumn
bsLstGroupDownstreamPortList = _BsLstGroupDownstreamPortList_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 4),
    _BsLstGroupDownstreamPortList_Type()
)
bsLstGroupDownstreamPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsLstGroupDownstreamPortList.setStatus("current")


class _BsLstGroupUpstreamMltList_Type(IdList):
    """Custom type bsLstGroupUpstreamMltList based on IdList"""
    defaultHexValue = ""


_BsLstGroupUpstreamMltList_Object = MibTableColumn
bsLstGroupUpstreamMltList = _BsLstGroupUpstreamMltList_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 5),
    _BsLstGroupUpstreamMltList_Type()
)
bsLstGroupUpstreamMltList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsLstGroupUpstreamMltList.setStatus("current")


class _BsLstGroupDownstreamMltList_Type(IdList):
    """Custom type bsLstGroupDownstreamMltList based on IdList"""
    defaultHexValue = ""


_BsLstGroupDownstreamMltList_Object = MibTableColumn
bsLstGroupDownstreamMltList = _BsLstGroupDownstreamMltList_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 6),
    _BsLstGroupDownstreamMltList_Type()
)
bsLstGroupDownstreamMltList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsLstGroupDownstreamMltList.setStatus("current")


class _BsLstGroupOperState_Type(Integer32):
    """Custom type bsLstGroupOperState based on Integer32"""
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
          ("notConfigured", 3),
          ("up", 1))
    )


_BsLstGroupOperState_Type.__name__ = "Integer32"
_BsLstGroupOperState_Object = MibTableColumn
bsLstGroupOperState = _BsLstGroupOperState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 7),
    _BsLstGroupOperState_Type()
)
bsLstGroupOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLstGroupOperState.setStatus("current")
_BsLstNotifObjects_ObjectIdentity = ObjectIdentity
bsLstNotifObjects = _BsLstNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 3)
)


class _BsLstInterfaceStatus_Type(Integer32):
    """Custom type bsLstInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_BsLstInterfaceStatus_Type.__name__ = "Integer32"
_BsLstInterfaceStatus_Object = MibScalar
bsLstInterfaceStatus = _BsLstInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 3, 1),
    _BsLstInterfaceStatus_Type()
)
bsLstInterfaceStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsLstInterfaceStatus.setStatus("current")

# Managed Objects groups


# Notification objects

bsLstInterfaceStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 0, 1)
)
bsLstInterfaceStatusChanged.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("BAY-STACK-LINK-STATE-TRACKING-MIB", "bsLstInterfaceStatus"),
        ("BAY-STACK-LINK-STATE-TRACKING-MIB", "bsLstGroupIndex"))
)
if mibBuilder.loadTexts:
    bsLstInterfaceStatusChanged.setStatus(
        "current"
    )

bsLstGroupOperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 43, 0, 2)
)
bsLstGroupOperStateChanged.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("BAY-STACK-LINK-STATE-TRACKING-MIB", "bsLstInterfaceStatus"),
        ("BAY-STACK-LINK-STATE-TRACKING-MIB", "bsLstGroupOperState"))
)
if mibBuilder.loadTexts:
    bsLstGroupOperStateChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-LINK-STATE-TRACKING-MIB",
    **{"bayStackLinkStateTrackingMib": bayStackLinkStateTrackingMib,
       "bsLstNotifications": bsLstNotifications,
       "bsLstInterfaceStatusChanged": bsLstInterfaceStatusChanged,
       "bsLstGroupOperStateChanged": bsLstGroupOperStateChanged,
       "bsLstObjects": bsLstObjects,
       "bsLstScalars": bsLstScalars,
       "bsLstGroupTable": bsLstGroupTable,
       "bsLstGroupEntry": bsLstGroupEntry,
       "bsLstGroupIndex": bsLstGroupIndex,
       "bsLstGroupEnabled": bsLstGroupEnabled,
       "bsLstGroupUpstreamPortList": bsLstGroupUpstreamPortList,
       "bsLstGroupDownstreamPortList": bsLstGroupDownstreamPortList,
       "bsLstGroupUpstreamMltList": bsLstGroupUpstreamMltList,
       "bsLstGroupDownstreamMltList": bsLstGroupDownstreamMltList,
       "bsLstGroupOperState": bsLstGroupOperState,
       "bsLstNotifObjects": bsLstNotifObjects,
       "bsLstInterfaceStatus": bsLstInterfaceStatus}
)
