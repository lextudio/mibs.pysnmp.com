# SNMP MIB module (TPLINK-ETHERNETOAMPDUSTAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-ETHERNETOAMPDUSTAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:04 2024
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

(ethernetOamStatistics,) = mibBuilder.importSymbols(
    "TPLINK-ETHERNETOAM-MIB",
    "ethernetOamStatistics")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EthernetOamPduStatTable_Object = MibTable
ethernetOamPduStatTable = _EthernetOamPduStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ethernetOamPduStatTable.setStatus("current")
_EthernetOamPduStatEntry_Object = MibTableRow
ethernetOamPduStatEntry = _EthernetOamPduStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1)
)
ethernetOamPduStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ethernetOamPduStatEntry.setStatus("current")
_EthernetOamPduStatPort_Type = DisplayString
_EthernetOamPduStatPort_Object = MibTableColumn
ethernetOamPduStatPort = _EthernetOamPduStatPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 1),
    _EthernetOamPduStatPort_Type()
)
ethernetOamPduStatPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatPort.setStatus("current")


class _EthernetOamPduStatClear_Type(Integer32):
    """Custom type ethernetOamPduStatClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("unchanged", 0))
    )


_EthernetOamPduStatClear_Type.__name__ = "Integer32"
_EthernetOamPduStatClear_Object = MibTableColumn
ethernetOamPduStatClear = _EthernetOamPduStatClear_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 2),
    _EthernetOamPduStatClear_Type()
)
ethernetOamPduStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOamPduStatClear.setStatus("current")
_EthernetOamPduStatInfoTx_Type = Counter32
_EthernetOamPduStatInfoTx_Object = MibTableColumn
ethernetOamPduStatInfoTx = _EthernetOamPduStatInfoTx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 3),
    _EthernetOamPduStatInfoTx_Type()
)
ethernetOamPduStatInfoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatInfoTx.setStatus("current")
_EthernetOamPduStatInfoRx_Type = Counter32
_EthernetOamPduStatInfoRx_Object = MibTableColumn
ethernetOamPduStatInfoRx = _EthernetOamPduStatInfoRx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 4),
    _EthernetOamPduStatInfoRx_Type()
)
ethernetOamPduStatInfoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatInfoRx.setStatus("current")
_EthernetOamPduStatUniEventTx_Type = Counter32
_EthernetOamPduStatUniEventTx_Object = MibTableColumn
ethernetOamPduStatUniEventTx = _EthernetOamPduStatUniEventTx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 5),
    _EthernetOamPduStatUniEventTx_Type()
)
ethernetOamPduStatUniEventTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatUniEventTx.setStatus("current")
_EthernetOamPduStatUniEventRx_Type = Counter32
_EthernetOamPduStatUniEventRx_Object = MibTableColumn
ethernetOamPduStatUniEventRx = _EthernetOamPduStatUniEventRx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 6),
    _EthernetOamPduStatUniEventRx_Type()
)
ethernetOamPduStatUniEventRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatUniEventRx.setStatus("current")
_EthernetOamPduStatDupEventTx_Type = Counter32
_EthernetOamPduStatDupEventTx_Object = MibTableColumn
ethernetOamPduStatDupEventTx = _EthernetOamPduStatDupEventTx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 7),
    _EthernetOamPduStatDupEventTx_Type()
)
ethernetOamPduStatDupEventTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatDupEventTx.setStatus("current")
_EthernetOamPduStatDupEventRx_Type = Counter32
_EthernetOamPduStatDupEventRx_Object = MibTableColumn
ethernetOamPduStatDupEventRx = _EthernetOamPduStatDupEventRx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 8),
    _EthernetOamPduStatDupEventRx_Type()
)
ethernetOamPduStatDupEventRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatDupEventRx.setStatus("current")
_EthernetOamPduStatVarReqTx_Type = Counter32
_EthernetOamPduStatVarReqTx_Object = MibTableColumn
ethernetOamPduStatVarReqTx = _EthernetOamPduStatVarReqTx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 9),
    _EthernetOamPduStatVarReqTx_Type()
)
ethernetOamPduStatVarReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatVarReqTx.setStatus("current")
_EthernetOamPduStatVarReqRx_Type = Counter32
_EthernetOamPduStatVarReqRx_Object = MibTableColumn
ethernetOamPduStatVarReqRx = _EthernetOamPduStatVarReqRx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 10),
    _EthernetOamPduStatVarReqRx_Type()
)
ethernetOamPduStatVarReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatVarReqRx.setStatus("current")
_EthernetOamPduStatVarRespTx_Type = Counter32
_EthernetOamPduStatVarRespTx_Object = MibTableColumn
ethernetOamPduStatVarRespTx = _EthernetOamPduStatVarRespTx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 11),
    _EthernetOamPduStatVarRespTx_Type()
)
ethernetOamPduStatVarRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatVarRespTx.setStatus("current")
_EthernetOamPduStatVarRespRx_Type = Counter32
_EthernetOamPduStatVarRespRx_Object = MibTableColumn
ethernetOamPduStatVarRespRx = _EthernetOamPduStatVarRespRx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 12),
    _EthernetOamPduStatVarRespRx_Type()
)
ethernetOamPduStatVarRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatVarRespRx.setStatus("current")
_EthernetOamPduStatLoopbackCtrlTx_Type = Counter32
_EthernetOamPduStatLoopbackCtrlTx_Object = MibTableColumn
ethernetOamPduStatLoopbackCtrlTx = _EthernetOamPduStatLoopbackCtrlTx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 13),
    _EthernetOamPduStatLoopbackCtrlTx_Type()
)
ethernetOamPduStatLoopbackCtrlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatLoopbackCtrlTx.setStatus("current")
_EthernetOamPduStatLoopbackCtrlRx_Type = Counter32
_EthernetOamPduStatLoopbackCtrlRx_Object = MibTableColumn
ethernetOamPduStatLoopbackCtrlRx = _EthernetOamPduStatLoopbackCtrlRx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 14),
    _EthernetOamPduStatLoopbackCtrlRx_Type()
)
ethernetOamPduStatLoopbackCtrlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatLoopbackCtrlRx.setStatus("current")
_EthernetOamPduStatOrgSpecTx_Type = Counter32
_EthernetOamPduStatOrgSpecTx_Object = MibTableColumn
ethernetOamPduStatOrgSpecTx = _EthernetOamPduStatOrgSpecTx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 15),
    _EthernetOamPduStatOrgSpecTx_Type()
)
ethernetOamPduStatOrgSpecTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatOrgSpecTx.setStatus("current")
_EthernetOamPduStatOrgSpecRx_Type = Counter32
_EthernetOamPduStatOrgSpecRx_Object = MibTableColumn
ethernetOamPduStatOrgSpecRx = _EthernetOamPduStatOrgSpecRx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 16),
    _EthernetOamPduStatOrgSpecRx_Type()
)
ethernetOamPduStatOrgSpecRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatOrgSpecRx.setStatus("current")
_EthernetOamPduStatUnsupportedTx_Type = Counter32
_EthernetOamPduStatUnsupportedTx_Object = MibTableColumn
ethernetOamPduStatUnsupportedTx = _EthernetOamPduStatUnsupportedTx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 17),
    _EthernetOamPduStatUnsupportedTx_Type()
)
ethernetOamPduStatUnsupportedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatUnsupportedTx.setStatus("current")
_EthernetOamPduStatUnsupportedRx_Type = Counter32
_EthernetOamPduStatUnsupportedRx_Object = MibTableColumn
ethernetOamPduStatUnsupportedRx = _EthernetOamPduStatUnsupportedRx_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 18),
    _EthernetOamPduStatUnsupportedRx_Type()
)
ethernetOamPduStatUnsupportedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatUnsupportedRx.setStatus("current")
_EthernetOamPduStatFrmLostDueToOam_Type = Counter32
_EthernetOamPduStatFrmLostDueToOam_Object = MibTableColumn
ethernetOamPduStatFrmLostDueToOam = _EthernetOamPduStatFrmLostDueToOam_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6, 1, 1, 19),
    _EthernetOamPduStatFrmLostDueToOam_Type()
)
ethernetOamPduStatFrmLostDueToOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamPduStatFrmLostDueToOam.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-ETHERNETOAMPDUSTAT-MIB",
    **{"ethernetOamPduStatTable": ethernetOamPduStatTable,
       "ethernetOamPduStatEntry": ethernetOamPduStatEntry,
       "ethernetOamPduStatPort": ethernetOamPduStatPort,
       "ethernetOamPduStatClear": ethernetOamPduStatClear,
       "ethernetOamPduStatInfoTx": ethernetOamPduStatInfoTx,
       "ethernetOamPduStatInfoRx": ethernetOamPduStatInfoRx,
       "ethernetOamPduStatUniEventTx": ethernetOamPduStatUniEventTx,
       "ethernetOamPduStatUniEventRx": ethernetOamPduStatUniEventRx,
       "ethernetOamPduStatDupEventTx": ethernetOamPduStatDupEventTx,
       "ethernetOamPduStatDupEventRx": ethernetOamPduStatDupEventRx,
       "ethernetOamPduStatVarReqTx": ethernetOamPduStatVarReqTx,
       "ethernetOamPduStatVarReqRx": ethernetOamPduStatVarReqRx,
       "ethernetOamPduStatVarRespTx": ethernetOamPduStatVarRespTx,
       "ethernetOamPduStatVarRespRx": ethernetOamPduStatVarRespRx,
       "ethernetOamPduStatLoopbackCtrlTx": ethernetOamPduStatLoopbackCtrlTx,
       "ethernetOamPduStatLoopbackCtrlRx": ethernetOamPduStatLoopbackCtrlRx,
       "ethernetOamPduStatOrgSpecTx": ethernetOamPduStatOrgSpecTx,
       "ethernetOamPduStatOrgSpecRx": ethernetOamPduStatOrgSpecRx,
       "ethernetOamPduStatUnsupportedTx": ethernetOamPduStatUnsupportedTx,
       "ethernetOamPduStatUnsupportedRx": ethernetOamPduStatUnsupportedRx,
       "ethernetOamPduStatFrmLostDueToOam": ethernetOamPduStatFrmLostDueToOam}
)
