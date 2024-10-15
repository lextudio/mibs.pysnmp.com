# SNMP MIB module (TPLINK-DLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-DLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:57 2024
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

tplinkDldpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 58)
)
tplinkDldpMIB.setRevisions(
        ("2013-07-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkDldpMIBObjects_ObjectIdentity = ObjectIdentity
tplinkDldpMIBObjects = _TplinkDldpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 58, 1)
)


class _TpDldpEnable_Type(Integer32):
    """Custom type tpDldpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpDldpEnable_Type.__name__ = "Integer32"
_TpDldpEnable_Object = MibScalar
tpDldpEnable = _TpDldpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 58, 1, 1),
    _TpDldpEnable_Type()
)
tpDldpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpDldpEnable.setStatus("current")


class _TpDldpInterval_Type(Integer32):
    """Custom type tpDldpInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TpDldpInterval_Type.__name__ = "Integer32"
_TpDldpInterval_Object = MibScalar
tpDldpInterval = _TpDldpInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 58, 1, 2),
    _TpDldpInterval_Type()
)
tpDldpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpDldpInterval.setStatus("current")


class _TpDldpShutmode_Type(Integer32):
    """Custom type tpDldpShutmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("manual", 1))
    )


_TpDldpShutmode_Type.__name__ = "Integer32"
_TpDldpShutmode_Object = MibScalar
tpDldpShutmode = _TpDldpShutmode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 58, 1, 3),
    _TpDldpShutmode_Type()
)
tpDldpShutmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpDldpShutmode.setStatus("current")
_TpDldpCtrlTable_Object = MibTable
tpDldpCtrlTable = _TpDldpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 58, 1, 4)
)
if mibBuilder.loadTexts:
    tpDldpCtrlTable.setStatus("current")
_TpDldpCtrlEntry_Object = MibTableRow
tpDldpCtrlEntry = _TpDldpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 58, 1, 4, 1)
)
tpDldpCtrlEntry.setIndexNames(
    (0, "TPLINK-DLDP-MIB", "tpDldpPortId"),
)
if mibBuilder.loadTexts:
    tpDldpCtrlEntry.setStatus("current")
_TpDldpPortId_Type = Integer32
_TpDldpPortId_Object = MibTableColumn
tpDldpPortId = _TpDldpPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 58, 1, 4, 1, 1),
    _TpDldpPortId_Type()
)
tpDldpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDldpPortId.setStatus("current")


class _TpDldpState_Type(Integer32):
    """Custom type tpDldpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpDldpState_Type.__name__ = "Integer32"
_TpDldpState_Object = MibTableColumn
tpDldpState = _TpDldpState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 58, 1, 4, 1, 2),
    _TpDldpState_Type()
)
tpDldpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpDldpState.setStatus("current")


class _TpDldpProtocolState_Type(Integer32):
    """Custom type tpDldpProtocolState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("adver", 4),
          ("disable", 5),
          ("inactive", 1),
          ("initial", 0),
          ("probe", 3))
    )


_TpDldpProtocolState_Type.__name__ = "Integer32"
_TpDldpProtocolState_Object = MibTableColumn
tpDldpProtocolState = _TpDldpProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 58, 1, 4, 1, 3),
    _TpDldpProtocolState_Type()
)
tpDldpProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDldpProtocolState.setStatus("current")


class _TpDldpLinkState_Type(Integer32):
    """Custom type tpDldpLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 0),
          ("link-up", 1))
    )


_TpDldpLinkState_Type.__name__ = "Integer32"
_TpDldpLinkState_Object = MibTableColumn
tpDldpLinkState = _TpDldpLinkState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 58, 1, 4, 1, 4),
    _TpDldpLinkState_Type()
)
tpDldpLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDldpLinkState.setStatus("current")


class _TpDldpNeighborState_Type(Integer32):
    """Custom type tpDldpNeighborState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aging", 3),
          ("bidirectional", 2),
          ("notAccess", 4),
          ("unidirectional", 1),
          ("unknown", 0))
    )


_TpDldpNeighborState_Type.__name__ = "Integer32"
_TpDldpNeighborState_Object = MibTableColumn
tpDldpNeighborState = _TpDldpNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 58, 1, 4, 1, 5),
    _TpDldpNeighborState_Type()
)
tpDldpNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDldpNeighborState.setStatus("current")
_TplinkDldpNotifications_ObjectIdentity = ObjectIdentity
tplinkDldpNotifications = _TplinkDldpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 58, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DLDP-MIB",
    **{"tplinkDldpMIB": tplinkDldpMIB,
       "tplinkDldpMIBObjects": tplinkDldpMIBObjects,
       "tpDldpEnable": tpDldpEnable,
       "tpDldpInterval": tpDldpInterval,
       "tpDldpShutmode": tpDldpShutmode,
       "tpDldpCtrlTable": tpDldpCtrlTable,
       "tpDldpCtrlEntry": tpDldpCtrlEntry,
       "tpDldpPortId": tpDldpPortId,
       "tpDldpState": tpDldpState,
       "tpDldpProtocolState": tpDldpProtocolState,
       "tpDldpLinkState": tpDldpLinkState,
       "tpDldpNeighborState": tpDldpNeighborState,
       "tplinkDldpNotifications": tplinkDldpNotifications}
)
