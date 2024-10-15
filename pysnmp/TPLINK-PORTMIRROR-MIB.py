# SNMP MIB module (TPLINK-PORTMIRROR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-PORTMIRROR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:30 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkPortMirrorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 11)
)
tplinkPortMirrorMIB.setRevisions(
        ("2012-12-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkPortMirrorMIBObjects_ObjectIdentity = ObjectIdentity
tplinkPortMirrorMIBObjects = _TplinkPortMirrorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 11, 1)
)
_TpPortMirrorTable_Object = MibTable
tpPortMirrorTable = _TpPortMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 11, 1, 1)
)
if mibBuilder.loadTexts:
    tpPortMirrorTable.setStatus("current")
_TpPortMirrorEntry_Object = MibTableRow
tpPortMirrorEntry = _TpPortMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 11, 1, 1, 1)
)
tpPortMirrorEntry.setIndexNames(
    (0, "TPLINK-PORTMIRROR-MIB", "tpPortMirrorSession"),
)
if mibBuilder.loadTexts:
    tpPortMirrorEntry.setStatus("current")
_TpPortMirrorSession_Type = Integer32
_TpPortMirrorSession_Object = MibTableColumn
tpPortMirrorSession = _TpPortMirrorSession_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 11, 1, 1, 1, 1),
    _TpPortMirrorSession_Type()
)
tpPortMirrorSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortMirrorSession.setStatus("current")
_TpPortMirrorDestination_Type = OctetString
_TpPortMirrorDestination_Object = MibTableColumn
tpPortMirrorDestination = _TpPortMirrorDestination_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 11, 1, 1, 1, 2),
    _TpPortMirrorDestination_Type()
)
tpPortMirrorDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortMirrorDestination.setStatus("current")
_TpPortMirrorIngressSource_Type = OctetString
_TpPortMirrorIngressSource_Object = MibTableColumn
tpPortMirrorIngressSource = _TpPortMirrorIngressSource_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 11, 1, 1, 1, 3),
    _TpPortMirrorIngressSource_Type()
)
tpPortMirrorIngressSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortMirrorIngressSource.setStatus("current")
_TpPortMirrorEgressSource_Type = OctetString
_TpPortMirrorEgressSource_Object = MibTableColumn
tpPortMirrorEgressSource = _TpPortMirrorEgressSource_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 11, 1, 1, 1, 4),
    _TpPortMirrorEgressSource_Type()
)
tpPortMirrorEgressSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortMirrorEgressSource.setStatus("current")
_TpPortMirrorBothSource_Type = OctetString
_TpPortMirrorBothSource_Object = MibTableColumn
tpPortMirrorBothSource = _TpPortMirrorBothSource_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 11, 1, 1, 1, 5),
    _TpPortMirrorBothSource_Type()
)
tpPortMirrorBothSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortMirrorBothSource.setStatus("current")


class _TpPortMirrorSessionState_Type(Integer32):
    """Custom type tpPortMirrorSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("clear", 3),
          ("negative", 1))
    )


_TpPortMirrorSessionState_Type.__name__ = "Integer32"
_TpPortMirrorSessionState_Object = MibTableColumn
tpPortMirrorSessionState = _TpPortMirrorSessionState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 11, 1, 1, 1, 6),
    _TpPortMirrorSessionState_Type()
)
tpPortMirrorSessionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortMirrorSessionState.setStatus("current")
_TplinkPortMirrorMIBNotifications_ObjectIdentity = ObjectIdentity
tplinkPortMirrorMIBNotifications = _TplinkPortMirrorMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 11, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-PORTMIRROR-MIB",
    **{"tplinkPortMirrorMIB": tplinkPortMirrorMIB,
       "tplinkPortMirrorMIBObjects": tplinkPortMirrorMIBObjects,
       "tpPortMirrorTable": tpPortMirrorTable,
       "tpPortMirrorEntry": tpPortMirrorEntry,
       "tpPortMirrorSession": tpPortMirrorSession,
       "tpPortMirrorDestination": tpPortMirrorDestination,
       "tpPortMirrorIngressSource": tpPortMirrorIngressSource,
       "tpPortMirrorEgressSource": tpPortMirrorEgressSource,
       "tpPortMirrorBothSource": tpPortMirrorBothSource,
       "tpPortMirrorSessionState": tpPortMirrorSessionState,
       "tplinkPortMirrorMIBNotifications": tplinkPortMirrorMIBNotifications}
)
