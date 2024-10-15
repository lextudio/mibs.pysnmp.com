# SNMP MIB module (MRV-IN-REACH-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRV-IN-REACH-PPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:45 2024
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

(mrvInReachProductDivision,) = mibBuilder.importSymbols(
    "MRV-IN-REACH-PRODUCT-DIVISION-MIB",
    "mrvInReachProductDivision")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XPpp_ObjectIdentity = ObjectIdentity
xPpp = _XPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 22)
)
_XPppBasic_ObjectIdentity = ObjectIdentity
xPppBasic = _XPppBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 22, 1)
)
_XPppConfigTable_Object = MibTable
xPppConfigTable = _XPppConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 1)
)
if mibBuilder.loadTexts:
    xPppConfigTable.setStatus("mandatory")
_XPppConfigEntry_Object = MibTableRow
xPppConfigEntry = _XPppConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 1, 1)
)
xPppConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xPppConfigEntry.setStatus("mandatory")


class _XPppConfigOpen_Type(Integer32):
    """Custom type xPppConfigOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_XPppConfigOpen_Type.__name__ = "Integer32"
_XPppConfigOpen_Object = MibTableColumn
xPppConfigOpen = _XPppConfigOpen_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 1, 1, 1),
    _XPppConfigOpen_Type()
)
xPppConfigOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppConfigOpen.setStatus("mandatory")


class _XPppConfigActive_Type(Integer32):
    """Custom type xPppConfigActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_XPppConfigActive_Type.__name__ = "Integer32"
_XPppConfigActive_Object = MibTableColumn
xPppConfigActive = _XPppConfigActive_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 1, 1, 2),
    _XPppConfigActive_Type()
)
xPppConfigActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppConfigActive.setStatus("mandatory")


class _XPppConfigDefaults_Type(Integer32):
    """Custom type xPppConfigDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_XPppConfigDefaults_Type.__name__ = "Integer32"
_XPppConfigDefaults_Object = MibTableColumn
xPppConfigDefaults = _XPppConfigDefaults_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 1, 1, 3),
    _XPppConfigDefaults_Type()
)
xPppConfigDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppConfigDefaults.setStatus("mandatory")


class _XPppConfigRestartTimer_Type(Integer32):
    """Custom type xPppConfigRestartTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_XPppConfigRestartTimer_Type.__name__ = "Integer32"
_XPppConfigRestartTimer_Object = MibTableColumn
xPppConfigRestartTimer = _XPppConfigRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 1, 1, 4),
    _XPppConfigRestartTimer_Type()
)
xPppConfigRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppConfigRestartTimer.setStatus("mandatory")


class _XPppConfigConfLimit_Type(Integer32):
    """Custom type xPppConfigConfLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_XPppConfigConfLimit_Type.__name__ = "Integer32"
_XPppConfigConfLimit_Object = MibTableColumn
xPppConfigConfLimit = _XPppConfigConfLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 1, 1, 5),
    _XPppConfigConfLimit_Type()
)
xPppConfigConfLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppConfigConfLimit.setStatus("mandatory")


class _XPppConfigFailLimit_Type(Integer32):
    """Custom type xPppConfigFailLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_XPppConfigFailLimit_Type.__name__ = "Integer32"
_XPppConfigFailLimit_Object = MibTableColumn
xPppConfigFailLimit = _XPppConfigFailLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 1, 1, 6),
    _XPppConfigFailLimit_Type()
)
xPppConfigFailLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppConfigFailLimit.setStatus("mandatory")


class _XPppConfigPacketLogging_Type(Integer32):
    """Custom type xPppConfigPacketLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interpreted", 3),
          ("none", 1),
          ("raw", 2))
    )


_XPppConfigPacketLogging_Type.__name__ = "Integer32"
_XPppConfigPacketLogging_Object = MibTableColumn
xPppConfigPacketLogging = _XPppConfigPacketLogging_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 1, 1, 7),
    _XPppConfigPacketLogging_Type()
)
xPppConfigPacketLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppConfigPacketLogging.setStatus("mandatory")


class _XPppConfigKATimer_Type(Integer32):
    """Custom type xPppConfigKATimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_XPppConfigKATimer_Type.__name__ = "Integer32"
_XPppConfigKATimer_Object = MibTableColumn
xPppConfigKATimer = _XPppConfigKATimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 1, 1, 8),
    _XPppConfigKATimer_Type()
)
xPppConfigKATimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppConfigKATimer.setStatus("mandatory")
_XPppConfigKATimeout_Type = Integer32
_XPppConfigKATimeout_Object = MibTableColumn
xPppConfigKATimeout = _XPppConfigKATimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 1, 1, 9),
    _XPppConfigKATimeout_Type()
)
xPppConfigKATimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppConfigKATimeout.setStatus("mandatory")
_XPppStatusTable_Object = MibTable
xPppStatusTable = _XPppStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 2)
)
if mibBuilder.loadTexts:
    xPppStatusTable.setStatus("mandatory")
_XPppStatusEntry_Object = MibTableRow
xPppStatusEntry = _XPppStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 2, 1)
)
xPppStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xPppStatusEntry.setStatus("mandatory")


class _XPppStatusState_Type(Integer32):
    """Custom type xPppStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_XPppStatusState_Type.__name__ = "Integer32"
_XPppStatusState_Object = MibTableColumn
xPppStatusState = _XPppStatusState_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 2, 1, 1),
    _XPppStatusState_Type()
)
xPppStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppStatusState.setStatus("mandatory")


class _XPppLinkOpen_Type(Integer32):
    """Custom type xPppLinkOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOpen", 1),
          ("open", 2))
    )


_XPppLinkOpen_Type.__name__ = "Integer32"
_XPppLinkOpen_Object = MibTableColumn
xPppLinkOpen = _XPppLinkOpen_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 2, 1, 2),
    _XPppLinkOpen_Type()
)
xPppLinkOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLinkOpen.setStatus("mandatory")
_XPppHdlcRxTotalPkts_Type = Counter32
_XPppHdlcRxTotalPkts_Object = MibTableColumn
xPppHdlcRxTotalPkts = _XPppHdlcRxTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 2, 1, 3),
    _XPppHdlcRxTotalPkts_Type()
)
xPppHdlcRxTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppHdlcRxTotalPkts.setStatus("mandatory")
_XPppHdlcTxTotalPkts_Type = Counter32
_XPppHdlcTxTotalPkts_Object = MibTableColumn
xPppHdlcTxTotalPkts = _XPppHdlcTxTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 2, 1, 4),
    _XPppHdlcTxTotalPkts_Type()
)
xPppHdlcTxTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppHdlcTxTotalPkts.setStatus("mandatory")
_XPppHdlcRxFrameErrs_Type = Counter32
_XPppHdlcRxFrameErrs_Object = MibTableColumn
xPppHdlcRxFrameErrs = _XPppHdlcRxFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 2, 1, 5),
    _XPppHdlcRxFrameErrs_Type()
)
xPppHdlcRxFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppHdlcRxFrameErrs.setStatus("mandatory")
_XPppHdlcRxNoBuffer_Type = Counter32
_XPppHdlcRxNoBuffer_Object = MibTableColumn
xPppHdlcRxNoBuffer = _XPppHdlcRxNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 2, 1, 6),
    _XPppHdlcRxNoBuffer_Type()
)
xPppHdlcRxNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppHdlcRxNoBuffer.setStatus("mandatory")
_XPppHdlcTxNoBuffer_Type = Counter32
_XPppHdlcTxNoBuffer_Object = MibTableColumn
xPppHdlcTxNoBuffer = _XPppHdlcTxNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 2, 1, 7),
    _XPppHdlcTxNoBuffer_Type()
)
xPppHdlcTxNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppHdlcTxNoBuffer.setStatus("mandatory")
_XPppHdlcRxBadFcs_Type = Counter32
_XPppHdlcRxBadFcs_Object = MibTableColumn
xPppHdlcRxBadFcs = _XPppHdlcRxBadFcs_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 2, 1, 8),
    _XPppHdlcRxBadFcs_Type()
)
xPppHdlcRxBadFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppHdlcRxBadFcs.setStatus("mandatory")
_XPppHdlcVJDiscards_Type = Counter32
_XPppHdlcVJDiscards_Object = MibTableColumn
xPppHdlcVJDiscards = _XPppHdlcVJDiscards_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 1, 2, 1, 9),
    _XPppHdlcVJDiscards_Type()
)
xPppHdlcVJDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppHdlcVJDiscards.setStatus("mandatory")
_XPppLcp_ObjectIdentity = ObjectIdentity
xPppLcp = _XPppLcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 22, 2)
)
_XPppLcpConfigTable_Object = MibTable
xPppLcpConfigTable = _XPppLcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 1)
)
if mibBuilder.loadTexts:
    xPppLcpConfigTable.setStatus("mandatory")
_XPppLcpConfigEntry_Object = MibTableRow
xPppLcpConfigEntry = _XPppLcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 1, 1)
)
xPppLcpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xPppLcpConfigEntry.setStatus("mandatory")


class _XPppLcpConfigAuth_Type(Integer32):
    """Custom type xPppLcpConfigAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pap", 2))
    )


_XPppLcpConfigAuth_Type.__name__ = "Integer32"
_XPppLcpConfigAuth_Object = MibTableColumn
xPppLcpConfigAuth = _XPppLcpConfigAuth_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 1, 1, 1),
    _XPppLcpConfigAuth_Type()
)
xPppLcpConfigAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppLcpConfigAuth.setStatus("mandatory")


class _XPppLcpConfigChapAuth_Type(Integer32):
    """Custom type xPppLcpConfigChapAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 2),
          ("none", 1))
    )


_XPppLcpConfigChapAuth_Type.__name__ = "Integer32"
_XPppLcpConfigChapAuth_Object = MibTableColumn
xPppLcpConfigChapAuth = _XPppLcpConfigChapAuth_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 1, 1, 2),
    _XPppLcpConfigChapAuth_Type()
)
xPppLcpConfigChapAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppLcpConfigChapAuth.setStatus("mandatory")
_XPppLcpStatusTable_Object = MibTable
xPppLcpStatusTable = _XPppLcpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2)
)
if mibBuilder.loadTexts:
    xPppLcpStatusTable.setStatus("mandatory")
_XPppLcpStatusEntry_Object = MibTableRow
xPppLcpStatusEntry = _XPppLcpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1)
)
xPppLcpStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xPppLcpStatusEntry.setStatus("mandatory")


class _XPppLcpStatusState_Type(Integer32):
    """Custom type xPppLcpStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ackReceived", 4),
          ("ackSent", 5),
          ("closed", 1),
          ("closing", 7),
          ("listen", 2),
          ("open", 6),
          ("requestSent", 3))
    )


_XPppLcpStatusState_Type.__name__ = "Integer32"
_XPppLcpStatusState_Object = MibTableColumn
xPppLcpStatusState = _XPppLcpStatusState_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 1),
    _XPppLcpStatusState_Type()
)
xPppLcpStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusState.setStatus("deprecated")


class _XPppLcpStatusRxAuth_Type(Integer32):
    """Custom type xPppLcpStatusRxAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pap", 2))
    )


_XPppLcpStatusRxAuth_Type.__name__ = "Integer32"
_XPppLcpStatusRxAuth_Object = MibTableColumn
xPppLcpStatusRxAuth = _XPppLcpStatusRxAuth_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 2),
    _XPppLcpStatusRxAuth_Type()
)
xPppLcpStatusRxAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusRxAuth.setStatus("mandatory")


class _XPppLcpStatusTxAuth_Type(Integer32):
    """Custom type xPppLcpStatusTxAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pap", 2))
    )


_XPppLcpStatusTxAuth_Type.__name__ = "Integer32"
_XPppLcpStatusTxAuth_Object = MibTableColumn
xPppLcpStatusTxAuth = _XPppLcpStatusTxAuth_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 3),
    _XPppLcpStatusTxAuth_Type()
)
xPppLcpStatusTxAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusTxAuth.setStatus("mandatory")
_XPppLcpStatusRxConReq_Type = Counter32
_XPppLcpStatusRxConReq_Object = MibTableColumn
xPppLcpStatusRxConReq = _XPppLcpStatusRxConReq_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 4),
    _XPppLcpStatusRxConReq_Type()
)
xPppLcpStatusRxConReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusRxConReq.setStatus("mandatory")
_XPppLcpStatusTxConReq_Type = Counter32
_XPppLcpStatusTxConReq_Object = MibTableColumn
xPppLcpStatusTxConReq = _XPppLcpStatusTxConReq_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 5),
    _XPppLcpStatusTxConReq_Type()
)
xPppLcpStatusTxConReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusTxConReq.setStatus("mandatory")
_XPppLcpStatusRxConNak_Type = Counter32
_XPppLcpStatusRxConNak_Object = MibTableColumn
xPppLcpStatusRxConNak = _XPppLcpStatusRxConNak_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 6),
    _XPppLcpStatusRxConNak_Type()
)
xPppLcpStatusRxConNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusRxConNak.setStatus("mandatory")
_XPppLcpStatusTxConNak_Type = Counter32
_XPppLcpStatusTxConNak_Object = MibTableColumn
xPppLcpStatusTxConNak = _XPppLcpStatusTxConNak_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 7),
    _XPppLcpStatusTxConNak_Type()
)
xPppLcpStatusTxConNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusTxConNak.setStatus("mandatory")
_XPppLcpStatusRxConAck_Type = Counter32
_XPppLcpStatusRxConAck_Object = MibTableColumn
xPppLcpStatusRxConAck = _XPppLcpStatusRxConAck_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 8),
    _XPppLcpStatusRxConAck_Type()
)
xPppLcpStatusRxConAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusRxConAck.setStatus("mandatory")
_XPppLcpStatusTxConAck_Type = Counter32
_XPppLcpStatusTxConAck_Object = MibTableColumn
xPppLcpStatusTxConAck = _XPppLcpStatusTxConAck_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 9),
    _XPppLcpStatusTxConAck_Type()
)
xPppLcpStatusTxConAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusTxConAck.setStatus("mandatory")
_XPppLcpStatusRxConRej_Type = Counter32
_XPppLcpStatusRxConRej_Object = MibTableColumn
xPppLcpStatusRxConRej = _XPppLcpStatusRxConRej_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 10),
    _XPppLcpStatusRxConRej_Type()
)
xPppLcpStatusRxConRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusRxConRej.setStatus("mandatory")
_XPppLcpStatusTxConRej_Type = Counter32
_XPppLcpStatusTxConRej_Object = MibTableColumn
xPppLcpStatusTxConRej = _XPppLcpStatusTxConRej_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 11),
    _XPppLcpStatusTxConRej_Type()
)
xPppLcpStatusTxConRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusTxConRej.setStatus("mandatory")
_XPppLcpStatusRxTrmReq_Type = Counter32
_XPppLcpStatusRxTrmReq_Object = MibTableColumn
xPppLcpStatusRxTrmReq = _XPppLcpStatusRxTrmReq_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 12),
    _XPppLcpStatusRxTrmReq_Type()
)
xPppLcpStatusRxTrmReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusRxTrmReq.setStatus("mandatory")
_XPppLcpStatusTxTrmReq_Type = Counter32
_XPppLcpStatusTxTrmReq_Object = MibTableColumn
xPppLcpStatusTxTrmReq = _XPppLcpStatusTxTrmReq_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 13),
    _XPppLcpStatusTxTrmReq_Type()
)
xPppLcpStatusTxTrmReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusTxTrmReq.setStatus("mandatory")
_XPppLcpStatusRxTrmAck_Type = Counter32
_XPppLcpStatusRxTrmAck_Object = MibTableColumn
xPppLcpStatusRxTrmAck = _XPppLcpStatusRxTrmAck_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 14),
    _XPppLcpStatusRxTrmAck_Type()
)
xPppLcpStatusRxTrmAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusRxTrmAck.setStatus("mandatory")
_XPppLcpStatusTxTrmAck_Type = Counter32
_XPppLcpStatusTxTrmAck_Object = MibTableColumn
xPppLcpStatusTxTrmAck = _XPppLcpStatusTxTrmAck_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 15),
    _XPppLcpStatusTxTrmAck_Type()
)
xPppLcpStatusTxTrmAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusTxTrmAck.setStatus("mandatory")
_XPppLcpStatusRxEcoReq_Type = Counter32
_XPppLcpStatusRxEcoReq_Object = MibTableColumn
xPppLcpStatusRxEcoReq = _XPppLcpStatusRxEcoReq_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 16),
    _XPppLcpStatusRxEcoReq_Type()
)
xPppLcpStatusRxEcoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusRxEcoReq.setStatus("mandatory")
_XPppLcpStatusTxEcoReq_Type = Counter32
_XPppLcpStatusTxEcoReq_Object = MibTableColumn
xPppLcpStatusTxEcoReq = _XPppLcpStatusTxEcoReq_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 17),
    _XPppLcpStatusTxEcoReq_Type()
)
xPppLcpStatusTxEcoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusTxEcoReq.setStatus("mandatory")
_XPppLcpStatusRxEcoRep_Type = Counter32
_XPppLcpStatusRxEcoRep_Object = MibTableColumn
xPppLcpStatusRxEcoRep = _XPppLcpStatusRxEcoRep_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 18),
    _XPppLcpStatusRxEcoRep_Type()
)
xPppLcpStatusRxEcoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusRxEcoRep.setStatus("mandatory")
_XPppLcpStatusTxEcoRep_Type = Counter32
_XPppLcpStatusTxEcoRep_Object = MibTableColumn
xPppLcpStatusTxEcoRep = _XPppLcpStatusTxEcoRep_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 19),
    _XPppLcpStatusTxEcoRep_Type()
)
xPppLcpStatusTxEcoRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusTxEcoRep.setStatus("mandatory")
_XPppLcpStatusRxCodRej_Type = Counter32
_XPppLcpStatusRxCodRej_Object = MibTableColumn
xPppLcpStatusRxCodRej = _XPppLcpStatusRxCodRej_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 20),
    _XPppLcpStatusRxCodRej_Type()
)
xPppLcpStatusRxCodRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusRxCodRej.setStatus("mandatory")
_XPppLcpStatusTxCodRej_Type = Counter32
_XPppLcpStatusTxCodRej_Object = MibTableColumn
xPppLcpStatusTxCodRej = _XPppLcpStatusTxCodRej_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 21),
    _XPppLcpStatusTxCodRej_Type()
)
xPppLcpStatusTxCodRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusTxCodRej.setStatus("mandatory")
_XPppLcpStatusRxProRej_Type = Counter32
_XPppLcpStatusRxProRej_Object = MibTableColumn
xPppLcpStatusRxProRej = _XPppLcpStatusRxProRej_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 22),
    _XPppLcpStatusRxProRej_Type()
)
xPppLcpStatusRxProRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusRxProRej.setStatus("mandatory")
_XPppLcpStatusTxProRej_Type = Counter32
_XPppLcpStatusTxProRej_Object = MibTableColumn
xPppLcpStatusTxProRej = _XPppLcpStatusTxProRej_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 23),
    _XPppLcpStatusTxProRej_Type()
)
xPppLcpStatusTxProRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusTxProRej.setStatus("mandatory")


class _XPppLcpStatusState2_Type(Integer32):
    """Custom type xPppLcpStatusState2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("ackRcvd", 8),
          ("ackSent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("reqSent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_XPppLcpStatusState2_Type.__name__ = "Integer32"
_XPppLcpStatusState2_Object = MibTableColumn
xPppLcpStatusState2 = _XPppLcpStatusState2_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 2, 2, 1, 24),
    _XPppLcpStatusState2_Type()
)
xPppLcpStatusState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppLcpStatusState2.setStatus("mandatory")
_XPppIpcp_ObjectIdentity = ObjectIdentity
xPppIpcp = _XPppIpcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 22, 3)
)
_XPppIpcpConfigTable_Object = MibTable
xPppIpcpConfigTable = _XPppIpcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 1)
)
if mibBuilder.loadTexts:
    xPppIpcpConfigTable.setStatus("mandatory")
_XPppIpcpConfigEntry_Object = MibTableRow
xPppIpcpConfigEntry = _XPppIpcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 1, 1)
)
xPppIpcpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xPppIpcpConfigEntry.setStatus("mandatory")
_XPppIpcpConfigLocalAddress_Type = IpAddress
_XPppIpcpConfigLocalAddress_Object = MibTableColumn
xPppIpcpConfigLocalAddress = _XPppIpcpConfigLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 1, 1, 1),
    _XPppIpcpConfigLocalAddress_Type()
)
xPppIpcpConfigLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppIpcpConfigLocalAddress.setStatus("mandatory")
_XPppIpcpConfigRemoteAddress_Type = IpAddress
_XPppIpcpConfigRemoteAddress_Object = MibTableColumn
xPppIpcpConfigRemoteAddress = _XPppIpcpConfigRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 1, 1, 2),
    _XPppIpcpConfigRemoteAddress_Type()
)
xPppIpcpConfigRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppIpcpConfigRemoteAddress.setStatus("mandatory")


class _XPppIpcpConfigVJCompSlots_Type(Integer32):
    """Custom type xPppIpcpConfigVJCompSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 15),
    )


_XPppIpcpConfigVJCompSlots_Type.__name__ = "Integer32"
_XPppIpcpConfigVJCompSlots_Object = MibTableColumn
xPppIpcpConfigVJCompSlots = _XPppIpcpConfigVJCompSlots_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 1, 1, 3),
    _XPppIpcpConfigVJCompSlots_Type()
)
xPppIpcpConfigVJCompSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppIpcpConfigVJCompSlots.setStatus("mandatory")
_XPppIpcpConfigRangeStart_Type = IpAddress
_XPppIpcpConfigRangeStart_Object = MibTableColumn
xPppIpcpConfigRangeStart = _XPppIpcpConfigRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 1, 1, 4),
    _XPppIpcpConfigRangeStart_Type()
)
xPppIpcpConfigRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppIpcpConfigRangeStart.setStatus("mandatory")
_XPppIpcpConfigRangeEnd_Type = IpAddress
_XPppIpcpConfigRangeEnd_Object = MibTableColumn
xPppIpcpConfigRangeEnd = _XPppIpcpConfigRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 1, 1, 5),
    _XPppIpcpConfigRangeEnd_Type()
)
xPppIpcpConfigRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppIpcpConfigRangeEnd.setStatus("mandatory")


class _XPppIpcpConfigState_Type(Integer32):
    """Custom type xPppIpcpConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_XPppIpcpConfigState_Type.__name__ = "Integer32"
_XPppIpcpConfigState_Object = MibTableColumn
xPppIpcpConfigState = _XPppIpcpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 1, 1, 6),
    _XPppIpcpConfigState_Type()
)
xPppIpcpConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppIpcpConfigState.setStatus("mandatory")
_XPppIpcpConfigLocalRangeStart_Type = IpAddress
_XPppIpcpConfigLocalRangeStart_Object = MibTableColumn
xPppIpcpConfigLocalRangeStart = _XPppIpcpConfigLocalRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 1, 1, 7),
    _XPppIpcpConfigLocalRangeStart_Type()
)
xPppIpcpConfigLocalRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppIpcpConfigLocalRangeStart.setStatus("mandatory")
_XPppIpcpConfigLocalRangeEnd_Type = IpAddress
_XPppIpcpConfigLocalRangeEnd_Object = MibTableColumn
xPppIpcpConfigLocalRangeEnd = _XPppIpcpConfigLocalRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 1, 1, 8),
    _XPppIpcpConfigLocalRangeEnd_Type()
)
xPppIpcpConfigLocalRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppIpcpConfigLocalRangeEnd.setStatus("mandatory")


class _XPppIpcpConfigPppIpMask_Type(IpAddress):
    """Custom type xPppIpcpConfigPppIpMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_XPppIpcpConfigPppIpMask_Object = MibTableColumn
xPppIpcpConfigPppIpMask = _XPppIpcpConfigPppIpMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 1, 1, 9),
    _XPppIpcpConfigPppIpMask_Type()
)
xPppIpcpConfigPppIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppIpcpConfigPppIpMask.setStatus("mandatory")
_XPppIpcpAsyncConfigTable_Object = MibTable
xPppIpcpAsyncConfigTable = _XPppIpcpAsyncConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 2)
)
if mibBuilder.loadTexts:
    xPppIpcpAsyncConfigTable.setStatus("mandatory")
_XPppIpcpAsyncConfigEntry_Object = MibTableRow
xPppIpcpAsyncConfigEntry = _XPppIpcpAsyncConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 2, 1)
)
xPppIpcpAsyncConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xPppIpcpAsyncConfigEntry.setStatus("mandatory")


class _XPppIpcpAsyncConfigBrdcast_Type(Integer32):
    """Custom type xPppIpcpAsyncConfigBrdcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_XPppIpcpAsyncConfigBrdcast_Type.__name__ = "Integer32"
_XPppIpcpAsyncConfigBrdcast_Object = MibTableColumn
xPppIpcpAsyncConfigBrdcast = _XPppIpcpAsyncConfigBrdcast_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 2, 1, 1),
    _XPppIpcpAsyncConfigBrdcast_Type()
)
xPppIpcpAsyncConfigBrdcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppIpcpAsyncConfigBrdcast.setStatus("mandatory")
_XPppIpcpStatusTable_Object = MibTable
xPppIpcpStatusTable = _XPppIpcpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3)
)
if mibBuilder.loadTexts:
    xPppIpcpStatusTable.setStatus("mandatory")
_XPppIpcpStatusEntry_Object = MibTableRow
xPppIpcpStatusEntry = _XPppIpcpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1)
)
xPppIpcpStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xPppIpcpStatusEntry.setStatus("mandatory")


class _XPppIpcpStatusState_Type(Integer32):
    """Custom type xPppIpcpStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ackReceived", 4),
          ("ackSent", 5),
          ("closed", 1),
          ("closing", 7),
          ("listen", 2),
          ("open", 6),
          ("requestSent", 3))
    )


_XPppIpcpStatusState_Type.__name__ = "Integer32"
_XPppIpcpStatusState_Object = MibTableColumn
xPppIpcpStatusState = _XPppIpcpStatusState_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 1),
    _XPppIpcpStatusState_Type()
)
xPppIpcpStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpStatusState.setStatus("deprecated")
_XPppIpcpStatusLocalAddress_Type = IpAddress
_XPppIpcpStatusLocalAddress_Object = MibTableColumn
xPppIpcpStatusLocalAddress = _XPppIpcpStatusLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 2),
    _XPppIpcpStatusLocalAddress_Type()
)
xPppIpcpStatusLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpStatusLocalAddress.setStatus("mandatory")
_XPppIpcpStatusRemoteAddress_Type = IpAddress
_XPppIpcpStatusRemoteAddress_Object = MibTableColumn
xPppIpcpStatusRemoteAddress = _XPppIpcpStatusRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 3),
    _XPppIpcpStatusRemoteAddress_Type()
)
xPppIpcpStatusRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpStatusRemoteAddress.setStatus("mandatory")
_XPppIpcpRxPkts_Type = Counter32
_XPppIpcpRxPkts_Object = MibTableColumn
xPppIpcpRxPkts = _XPppIpcpRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 4),
    _XPppIpcpRxPkts_Type()
)
xPppIpcpRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpRxPkts.setStatus("mandatory")
_XPppIpcpTxPkts_Type = Counter32
_XPppIpcpTxPkts_Object = MibTableColumn
xPppIpcpTxPkts = _XPppIpcpTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 5),
    _XPppIpcpTxPkts_Type()
)
xPppIpcpTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpTxPkts.setStatus("mandatory")
_XPppIpcpRxConReq_Type = Counter32
_XPppIpcpRxConReq_Object = MibTableColumn
xPppIpcpRxConReq = _XPppIpcpRxConReq_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 6),
    _XPppIpcpRxConReq_Type()
)
xPppIpcpRxConReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpRxConReq.setStatus("mandatory")
_XPppIpcpTxConReq_Type = Counter32
_XPppIpcpTxConReq_Object = MibTableColumn
xPppIpcpTxConReq = _XPppIpcpTxConReq_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 7),
    _XPppIpcpTxConReq_Type()
)
xPppIpcpTxConReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpTxConReq.setStatus("mandatory")
_XPppIpcpRxConNak_Type = Counter32
_XPppIpcpRxConNak_Object = MibTableColumn
xPppIpcpRxConNak = _XPppIpcpRxConNak_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 8),
    _XPppIpcpRxConNak_Type()
)
xPppIpcpRxConNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpRxConNak.setStatus("mandatory")
_XPppIpcpTxConNak_Type = Counter32
_XPppIpcpTxConNak_Object = MibTableColumn
xPppIpcpTxConNak = _XPppIpcpTxConNak_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 9),
    _XPppIpcpTxConNak_Type()
)
xPppIpcpTxConNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpTxConNak.setStatus("mandatory")
_XPppIpcpRxConAck_Type = Counter32
_XPppIpcpRxConAck_Object = MibTableColumn
xPppIpcpRxConAck = _XPppIpcpRxConAck_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 10),
    _XPppIpcpRxConAck_Type()
)
xPppIpcpRxConAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpRxConAck.setStatus("mandatory")
_XPppIpcpTxConAck_Type = Counter32
_XPppIpcpTxConAck_Object = MibTableColumn
xPppIpcpTxConAck = _XPppIpcpTxConAck_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 11),
    _XPppIpcpTxConAck_Type()
)
xPppIpcpTxConAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpTxConAck.setStatus("mandatory")
_XPppIpcpRxConRej_Type = Counter32
_XPppIpcpRxConRej_Object = MibTableColumn
xPppIpcpRxConRej = _XPppIpcpRxConRej_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 12),
    _XPppIpcpRxConRej_Type()
)
xPppIpcpRxConRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpRxConRej.setStatus("mandatory")
_XPppIpcpTxConRej_Type = Counter32
_XPppIpcpTxConRej_Object = MibTableColumn
xPppIpcpTxConRej = _XPppIpcpTxConRej_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 13),
    _XPppIpcpTxConRej_Type()
)
xPppIpcpTxConRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpTxConRej.setStatus("mandatory")
_XPppIpcpRxTrmReq_Type = Counter32
_XPppIpcpRxTrmReq_Object = MibTableColumn
xPppIpcpRxTrmReq = _XPppIpcpRxTrmReq_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 14),
    _XPppIpcpRxTrmReq_Type()
)
xPppIpcpRxTrmReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpRxTrmReq.setStatus("mandatory")
_XPppIpcpTxTrmReq_Type = Counter32
_XPppIpcpTxTrmReq_Object = MibTableColumn
xPppIpcpTxTrmReq = _XPppIpcpTxTrmReq_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 15),
    _XPppIpcpTxTrmReq_Type()
)
xPppIpcpTxTrmReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpTxTrmReq.setStatus("mandatory")
_XPppIpcpRxTrmAck_Type = Counter32
_XPppIpcpRxTrmAck_Object = MibTableColumn
xPppIpcpRxTrmAck = _XPppIpcpRxTrmAck_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 16),
    _XPppIpcpRxTrmAck_Type()
)
xPppIpcpRxTrmAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpRxTrmAck.setStatus("mandatory")
_XPppIpcpTxTrmAck_Type = Counter32
_XPppIpcpTxTrmAck_Object = MibTableColumn
xPppIpcpTxTrmAck = _XPppIpcpTxTrmAck_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 17),
    _XPppIpcpTxTrmAck_Type()
)
xPppIpcpTxTrmAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpTxTrmAck.setStatus("mandatory")


class _XPppIpcpStatusState2_Type(Integer32):
    """Custom type xPppIpcpStatusState2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("ackRcvd", 8),
          ("ackSent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("reqSent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_XPppIpcpStatusState2_Type.__name__ = "Integer32"
_XPppIpcpStatusState2_Object = MibTableColumn
xPppIpcpStatusState2 = _XPppIpcpStatusState2_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 3, 3, 1, 18),
    _XPppIpcpStatusState2_Type()
)
xPppIpcpStatusState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpcpStatusState2.setStatus("mandatory")
_XPppAuth_ObjectIdentity = ObjectIdentity
xPppAuth = _XPppAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 22, 4)
)


class _XPppPapPassword_Type(OctetString):
    """Custom type xPppPapPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_XPppPapPassword_Type.__name__ = "OctetString"
_XPppPapPassword_Object = MibScalar
xPppPapPassword = _XPppPapPassword_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 4, 1),
    _XPppPapPassword_Type()
)
xPppPapPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppPapPassword.setStatus("mandatory")
_XPppAuthConfigTable_Object = MibTable
xPppAuthConfigTable = _XPppAuthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 4, 2)
)
if mibBuilder.loadTexts:
    xPppAuthConfigTable.setStatus("mandatory")
_XPppAuthConfigEntry_Object = MibTableRow
xPppAuthConfigEntry = _XPppAuthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 4, 2, 1)
)
xPppAuthConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xPppAuthConfigEntry.setStatus("mandatory")


class _XPppAuthChapChallengeTimer_Type(Integer32):
    """Custom type xPppAuthChapChallengeTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_XPppAuthChapChallengeTimer_Type.__name__ = "Integer32"
_XPppAuthChapChallengeTimer_Object = MibTableColumn
xPppAuthChapChallengeTimer = _XPppAuthChapChallengeTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 4, 2, 1, 4),
    _XPppAuthChapChallengeTimer_Type()
)
xPppAuthChapChallengeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppAuthChapChallengeTimer.setStatus("mandatory")


class _XPppAuthPapConfigState_Type(Integer32):
    """Custom type xPppAuthPapConfigState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("kerberos", 3),
          ("radius", 4))
    )


_XPppAuthPapConfigState_Type.__name__ = "Integer32"
_XPppAuthPapConfigState_Object = MibTableColumn
xPppAuthPapConfigState = _XPppAuthPapConfigState_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 4, 2, 1, 5),
    _XPppAuthPapConfigState_Type()
)
xPppAuthPapConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppAuthPapConfigState.setStatus("mandatory")


class _XPppAuthChapConfigState_Type(Integer32):
    """Custom type xPppAuthChapConfigState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("radius", 4))
    )


_XPppAuthChapConfigState_Type.__name__ = "Integer32"
_XPppAuthChapConfigState_Object = MibTableColumn
xPppAuthChapConfigState = _XPppAuthChapConfigState_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 4, 2, 1, 6),
    _XPppAuthChapConfigState_Type()
)
xPppAuthChapConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppAuthChapConfigState.setStatus("mandatory")
_XPppAuthStatusTable_Object = MibTable
xPppAuthStatusTable = _XPppAuthStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 4, 3)
)
if mibBuilder.loadTexts:
    xPppAuthStatusTable.setStatus("mandatory")
_XPppAuthStatusEntry_Object = MibTableRow
xPppAuthStatusEntry = _XPppAuthStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 4, 3, 1)
)
xPppAuthStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xPppAuthStatusEntry.setStatus("mandatory")


class _XPppPapStatusState_Type(Integer32):
    """Custom type xPppPapStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("ackRecv", 6),
          ("ackSent", 7),
          ("closed", 2),
          ("closing", 4),
          ("initial", 1),
          ("kerberosAckRecv", 11),
          ("kerberosAckSent", 12),
          ("kerberosReqSent", 9),
          ("kerberosStopped", 10),
          ("opened", 8),
          ("papKerberosOpened", 13),
          ("reqSent", 5),
          ("stopped", 3))
    )


_XPppPapStatusState_Type.__name__ = "Integer32"
_XPppPapStatusState_Object = MibTableColumn
xPppPapStatusState = _XPppPapStatusState_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 4, 3, 1, 4),
    _XPppPapStatusState_Type()
)
xPppPapStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppPapStatusState.setStatus("mandatory")


class _XPppChapStatusState_Type(Integer32):
    """Custom type xPppChapStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("challengeSent", 3),
          ("challengeSentAckRecv", 6),
          ("challengeSentResponseSent", 5),
          ("challengeWait", 2),
          ("idle", 1),
          ("open", 7),
          ("responseSent", 4))
    )


_XPppChapStatusState_Type.__name__ = "Integer32"
_XPppChapStatusState_Object = MibTableColumn
xPppChapStatusState = _XPppChapStatusState_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 4, 3, 1, 5),
    _XPppChapStatusState_Type()
)
xPppChapStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppChapStatusState.setStatus("mandatory")


class _XPppChapPassword_Type(OctetString):
    """Custom type xPppChapPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_XPppChapPassword_Type.__name__ = "OctetString"
_XPppChapPassword_Object = MibScalar
xPppChapPassword = _XPppChapPassword_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 4, 4),
    _XPppChapPassword_Type()
)
xPppChapPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppChapPassword.setStatus("mandatory")
_XPppIpxcp_ObjectIdentity = ObjectIdentity
xPppIpxcp = _XPppIpxcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 22, 5)
)
_XPppIpxcpConfigTable_Object = MibTable
xPppIpxcpConfigTable = _XPppIpxcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 1)
)
if mibBuilder.loadTexts:
    xPppIpxcpConfigTable.setStatus("mandatory")
_XPppIpxcpConfigEntry_Object = MibTableRow
xPppIpxcpConfigEntry = _XPppIpxcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 1, 1)
)
xPppIpxcpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xPppIpxcpConfigEntry.setStatus("mandatory")


class _XPppIpxcpCipxCompression_Type(Integer32):
    """Custom type xPppIpxcpCipxCompression based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_XPppIpxcpCipxCompression_Type.__name__ = "Integer32"
_XPppIpxcpCipxCompression_Object = MibTableColumn
xPppIpxcpCipxCompression = _XPppIpxcpCipxCompression_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 1, 1, 1),
    _XPppIpxcpCipxCompression_Type()
)
xPppIpxcpCipxCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppIpxcpCipxCompression.setStatus("mandatory")


class _XPppIpxcpConfigRemoteNode_Type(OctetString):
    """Custom type xPppIpxcpConfigRemoteNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_XPppIpxcpConfigRemoteNode_Type.__name__ = "OctetString"
_XPppIpxcpConfigRemoteNode_Object = MibTableColumn
xPppIpxcpConfigRemoteNode = _XPppIpxcpConfigRemoteNode_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 1, 1, 2),
    _XPppIpxcpConfigRemoteNode_Type()
)
xPppIpxcpConfigRemoteNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPppIpxcpConfigRemoteNode.setStatus("mandatory")
_XPppIpxcpStatusTable_Object = MibTable
xPppIpxcpStatusTable = _XPppIpxcpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 2)
)
if mibBuilder.loadTexts:
    xPppIpxcpStatusTable.setStatus("mandatory")
_XPppIpxcpStatusEntry_Object = MibTableRow
xPppIpxcpStatusEntry = _XPppIpxcpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 2, 1)
)
xPppIpxcpStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xPppIpxcpStatusEntry.setStatus("mandatory")


class _XPppIpxcpStatusState_Type(Integer32):
    """Custom type xPppIpxcpStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("ackRcvd", 8),
          ("ackSent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("reqSent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_XPppIpxcpStatusState_Type.__name__ = "Integer32"
_XPppIpxcpStatusState_Object = MibTableColumn
xPppIpxcpStatusState = _XPppIpxcpStatusState_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 2, 1, 1),
    _XPppIpxcpStatusState_Type()
)
xPppIpxcpStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpStatusState.setStatus("mandatory")


class _XPppIpxcpCipxInCompression_Type(Integer32):
    """Custom type xPppIpxcpCipxInCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_XPppIpxcpCipxInCompression_Type.__name__ = "Integer32"
_XPppIpxcpCipxInCompression_Object = MibTableColumn
xPppIpxcpCipxInCompression = _XPppIpxcpCipxInCompression_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 2, 1, 2),
    _XPppIpxcpCipxInCompression_Type()
)
xPppIpxcpCipxInCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpCipxInCompression.setStatus("mandatory")


class _XPppIpxcpCipxOutCompression_Type(Integer32):
    """Custom type xPppIpxcpCipxOutCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_XPppIpxcpCipxOutCompression_Type.__name__ = "Integer32"
_XPppIpxcpCipxOutCompression_Object = MibTableColumn
xPppIpxcpCipxOutCompression = _XPppIpxcpCipxOutCompression_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 2, 1, 3),
    _XPppIpxcpCipxOutCompression_Type()
)
xPppIpxcpCipxOutCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpCipxOutCompression.setStatus("mandatory")
_XPppIpxcpCipxInSlots_Type = Integer32
_XPppIpxcpCipxInSlots_Object = MibTableColumn
xPppIpxcpCipxInSlots = _XPppIpxcpCipxInSlots_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 2, 1, 4),
    _XPppIpxcpCipxInSlots_Type()
)
xPppIpxcpCipxInSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpCipxInSlots.setStatus("mandatory")
_XPppIpxcpCipxOutSlots_Type = Integer32
_XPppIpxcpCipxOutSlots_Object = MibTableColumn
xPppIpxcpCipxOutSlots = _XPppIpxcpCipxOutSlots_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 2, 1, 5),
    _XPppIpxcpCipxOutSlots_Type()
)
xPppIpxcpCipxOutSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpCipxOutSlots.setStatus("mandatory")


class _XPppIpxcpStatusRemoteNode_Type(OctetString):
    """Custom type xPppIpxcpStatusRemoteNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_XPppIpxcpStatusRemoteNode_Type.__name__ = "OctetString"
_XPppIpxcpStatusRemoteNode_Object = MibTableColumn
xPppIpxcpStatusRemoteNode = _XPppIpxcpStatusRemoteNode_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 2, 1, 6),
    _XPppIpxcpStatusRemoteNode_Type()
)
xPppIpxcpStatusRemoteNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpStatusRemoteNode.setStatus("mandatory")
_XPppIpxcpCountersTable_Object = MibTable
xPppIpxcpCountersTable = _XPppIpxcpCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 3)
)
if mibBuilder.loadTexts:
    xPppIpxcpCountersTable.setStatus("mandatory")
_XPppIpxcpCountersEntry_Object = MibTableRow
xPppIpxcpCountersEntry = _XPppIpxcpCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 3, 1)
)
xPppIpxcpCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xPppIpxcpCountersEntry.setStatus("mandatory")
_XPppIpxcpRxConReq_Type = Counter32
_XPppIpxcpRxConReq_Object = MibTableColumn
xPppIpxcpRxConReq = _XPppIpxcpRxConReq_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 3, 1, 1),
    _XPppIpxcpRxConReq_Type()
)
xPppIpxcpRxConReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpRxConReq.setStatus("mandatory")
_XPppIpxcpTxConReq_Type = Counter32
_XPppIpxcpTxConReq_Object = MibTableColumn
xPppIpxcpTxConReq = _XPppIpxcpTxConReq_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 3, 1, 2),
    _XPppIpxcpTxConReq_Type()
)
xPppIpxcpTxConReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpTxConReq.setStatus("mandatory")
_XPppIpxcpRxConNak_Type = Counter32
_XPppIpxcpRxConNak_Object = MibTableColumn
xPppIpxcpRxConNak = _XPppIpxcpRxConNak_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 3, 1, 3),
    _XPppIpxcpRxConNak_Type()
)
xPppIpxcpRxConNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpRxConNak.setStatus("mandatory")
_XPppIpxcpTxConNak_Type = Counter32
_XPppIpxcpTxConNak_Object = MibTableColumn
xPppIpxcpTxConNak = _XPppIpxcpTxConNak_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 3, 1, 4),
    _XPppIpxcpTxConNak_Type()
)
xPppIpxcpTxConNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpTxConNak.setStatus("mandatory")
_XPppIpxcpRxConAck_Type = Counter32
_XPppIpxcpRxConAck_Object = MibTableColumn
xPppIpxcpRxConAck = _XPppIpxcpRxConAck_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 3, 1, 5),
    _XPppIpxcpRxConAck_Type()
)
xPppIpxcpRxConAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpRxConAck.setStatus("mandatory")
_XPppIpxcpTxConAck_Type = Counter32
_XPppIpxcpTxConAck_Object = MibTableColumn
xPppIpxcpTxConAck = _XPppIpxcpTxConAck_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 3, 1, 6),
    _XPppIpxcpTxConAck_Type()
)
xPppIpxcpTxConAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpTxConAck.setStatus("mandatory")
_XPppIpxcpRxConRej_Type = Counter32
_XPppIpxcpRxConRej_Object = MibTableColumn
xPppIpxcpRxConRej = _XPppIpxcpRxConRej_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 3, 1, 7),
    _XPppIpxcpRxConRej_Type()
)
xPppIpxcpRxConRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpRxConRej.setStatus("mandatory")
_XPppIpxcpTxConRej_Type = Counter32
_XPppIpxcpTxConRej_Object = MibTableColumn
xPppIpxcpTxConRej = _XPppIpxcpTxConRej_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 3, 1, 8),
    _XPppIpxcpTxConRej_Type()
)
xPppIpxcpTxConRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpTxConRej.setStatus("mandatory")
_XPppIpxcpRxTrmReq_Type = Counter32
_XPppIpxcpRxTrmReq_Object = MibTableColumn
xPppIpxcpRxTrmReq = _XPppIpxcpRxTrmReq_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 3, 1, 9),
    _XPppIpxcpRxTrmReq_Type()
)
xPppIpxcpRxTrmReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpRxTrmReq.setStatus("mandatory")
_XPppIpxcpTxTrmReq_Type = Counter32
_XPppIpxcpTxTrmReq_Object = MibTableColumn
xPppIpxcpTxTrmReq = _XPppIpxcpTxTrmReq_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 3, 1, 10),
    _XPppIpxcpTxTrmReq_Type()
)
xPppIpxcpTxTrmReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpTxTrmReq.setStatus("mandatory")
_XPppIpxcpRxTrmAck_Type = Counter32
_XPppIpxcpRxTrmAck_Object = MibTableColumn
xPppIpxcpRxTrmAck = _XPppIpxcpRxTrmAck_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 3, 1, 11),
    _XPppIpxcpRxTrmAck_Type()
)
xPppIpxcpRxTrmAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpRxTrmAck.setStatus("mandatory")
_XPppIpxcpTxTrmAck_Type = Counter32
_XPppIpxcpTxTrmAck_Object = MibTableColumn
xPppIpxcpTxTrmAck = _XPppIpxcpTxTrmAck_Object(
    (1, 3, 6, 1, 4, 1, 33, 22, 5, 3, 1, 12),
    _XPppIpxcpTxTrmAck_Type()
)
xPppIpxcpTxTrmAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPppIpxcpTxTrmAck.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-IN-REACH-PPP-MIB",
    **{"xPpp": xPpp,
       "xPppBasic": xPppBasic,
       "xPppConfigTable": xPppConfigTable,
       "xPppConfigEntry": xPppConfigEntry,
       "xPppConfigOpen": xPppConfigOpen,
       "xPppConfigActive": xPppConfigActive,
       "xPppConfigDefaults": xPppConfigDefaults,
       "xPppConfigRestartTimer": xPppConfigRestartTimer,
       "xPppConfigConfLimit": xPppConfigConfLimit,
       "xPppConfigFailLimit": xPppConfigFailLimit,
       "xPppConfigPacketLogging": xPppConfigPacketLogging,
       "xPppConfigKATimer": xPppConfigKATimer,
       "xPppConfigKATimeout": xPppConfigKATimeout,
       "xPppStatusTable": xPppStatusTable,
       "xPppStatusEntry": xPppStatusEntry,
       "xPppStatusState": xPppStatusState,
       "xPppLinkOpen": xPppLinkOpen,
       "xPppHdlcRxTotalPkts": xPppHdlcRxTotalPkts,
       "xPppHdlcTxTotalPkts": xPppHdlcTxTotalPkts,
       "xPppHdlcRxFrameErrs": xPppHdlcRxFrameErrs,
       "xPppHdlcRxNoBuffer": xPppHdlcRxNoBuffer,
       "xPppHdlcTxNoBuffer": xPppHdlcTxNoBuffer,
       "xPppHdlcRxBadFcs": xPppHdlcRxBadFcs,
       "xPppHdlcVJDiscards": xPppHdlcVJDiscards,
       "xPppLcp": xPppLcp,
       "xPppLcpConfigTable": xPppLcpConfigTable,
       "xPppLcpConfigEntry": xPppLcpConfigEntry,
       "xPppLcpConfigAuth": xPppLcpConfigAuth,
       "xPppLcpConfigChapAuth": xPppLcpConfigChapAuth,
       "xPppLcpStatusTable": xPppLcpStatusTable,
       "xPppLcpStatusEntry": xPppLcpStatusEntry,
       "xPppLcpStatusState": xPppLcpStatusState,
       "xPppLcpStatusRxAuth": xPppLcpStatusRxAuth,
       "xPppLcpStatusTxAuth": xPppLcpStatusTxAuth,
       "xPppLcpStatusRxConReq": xPppLcpStatusRxConReq,
       "xPppLcpStatusTxConReq": xPppLcpStatusTxConReq,
       "xPppLcpStatusRxConNak": xPppLcpStatusRxConNak,
       "xPppLcpStatusTxConNak": xPppLcpStatusTxConNak,
       "xPppLcpStatusRxConAck": xPppLcpStatusRxConAck,
       "xPppLcpStatusTxConAck": xPppLcpStatusTxConAck,
       "xPppLcpStatusRxConRej": xPppLcpStatusRxConRej,
       "xPppLcpStatusTxConRej": xPppLcpStatusTxConRej,
       "xPppLcpStatusRxTrmReq": xPppLcpStatusRxTrmReq,
       "xPppLcpStatusTxTrmReq": xPppLcpStatusTxTrmReq,
       "xPppLcpStatusRxTrmAck": xPppLcpStatusRxTrmAck,
       "xPppLcpStatusTxTrmAck": xPppLcpStatusTxTrmAck,
       "xPppLcpStatusRxEcoReq": xPppLcpStatusRxEcoReq,
       "xPppLcpStatusTxEcoReq": xPppLcpStatusTxEcoReq,
       "xPppLcpStatusRxEcoRep": xPppLcpStatusRxEcoRep,
       "xPppLcpStatusTxEcoRep": xPppLcpStatusTxEcoRep,
       "xPppLcpStatusRxCodRej": xPppLcpStatusRxCodRej,
       "xPppLcpStatusTxCodRej": xPppLcpStatusTxCodRej,
       "xPppLcpStatusRxProRej": xPppLcpStatusRxProRej,
       "xPppLcpStatusTxProRej": xPppLcpStatusTxProRej,
       "xPppLcpStatusState2": xPppLcpStatusState2,
       "xPppIpcp": xPppIpcp,
       "xPppIpcpConfigTable": xPppIpcpConfigTable,
       "xPppIpcpConfigEntry": xPppIpcpConfigEntry,
       "xPppIpcpConfigLocalAddress": xPppIpcpConfigLocalAddress,
       "xPppIpcpConfigRemoteAddress": xPppIpcpConfigRemoteAddress,
       "xPppIpcpConfigVJCompSlots": xPppIpcpConfigVJCompSlots,
       "xPppIpcpConfigRangeStart": xPppIpcpConfigRangeStart,
       "xPppIpcpConfigRangeEnd": xPppIpcpConfigRangeEnd,
       "xPppIpcpConfigState": xPppIpcpConfigState,
       "xPppIpcpConfigLocalRangeStart": xPppIpcpConfigLocalRangeStart,
       "xPppIpcpConfigLocalRangeEnd": xPppIpcpConfigLocalRangeEnd,
       "xPppIpcpConfigPppIpMask": xPppIpcpConfigPppIpMask,
       "xPppIpcpAsyncConfigTable": xPppIpcpAsyncConfigTable,
       "xPppIpcpAsyncConfigEntry": xPppIpcpAsyncConfigEntry,
       "xPppIpcpAsyncConfigBrdcast": xPppIpcpAsyncConfigBrdcast,
       "xPppIpcpStatusTable": xPppIpcpStatusTable,
       "xPppIpcpStatusEntry": xPppIpcpStatusEntry,
       "xPppIpcpStatusState": xPppIpcpStatusState,
       "xPppIpcpStatusLocalAddress": xPppIpcpStatusLocalAddress,
       "xPppIpcpStatusRemoteAddress": xPppIpcpStatusRemoteAddress,
       "xPppIpcpRxPkts": xPppIpcpRxPkts,
       "xPppIpcpTxPkts": xPppIpcpTxPkts,
       "xPppIpcpRxConReq": xPppIpcpRxConReq,
       "xPppIpcpTxConReq": xPppIpcpTxConReq,
       "xPppIpcpRxConNak": xPppIpcpRxConNak,
       "xPppIpcpTxConNak": xPppIpcpTxConNak,
       "xPppIpcpRxConAck": xPppIpcpRxConAck,
       "xPppIpcpTxConAck": xPppIpcpTxConAck,
       "xPppIpcpRxConRej": xPppIpcpRxConRej,
       "xPppIpcpTxConRej": xPppIpcpTxConRej,
       "xPppIpcpRxTrmReq": xPppIpcpRxTrmReq,
       "xPppIpcpTxTrmReq": xPppIpcpTxTrmReq,
       "xPppIpcpRxTrmAck": xPppIpcpRxTrmAck,
       "xPppIpcpTxTrmAck": xPppIpcpTxTrmAck,
       "xPppIpcpStatusState2": xPppIpcpStatusState2,
       "xPppAuth": xPppAuth,
       "xPppPapPassword": xPppPapPassword,
       "xPppAuthConfigTable": xPppAuthConfigTable,
       "xPppAuthConfigEntry": xPppAuthConfigEntry,
       "xPppAuthChapChallengeTimer": xPppAuthChapChallengeTimer,
       "xPppAuthPapConfigState": xPppAuthPapConfigState,
       "xPppAuthChapConfigState": xPppAuthChapConfigState,
       "xPppAuthStatusTable": xPppAuthStatusTable,
       "xPppAuthStatusEntry": xPppAuthStatusEntry,
       "xPppPapStatusState": xPppPapStatusState,
       "xPppChapStatusState": xPppChapStatusState,
       "xPppChapPassword": xPppChapPassword,
       "xPppIpxcp": xPppIpxcp,
       "xPppIpxcpConfigTable": xPppIpxcpConfigTable,
       "xPppIpxcpConfigEntry": xPppIpxcpConfigEntry,
       "xPppIpxcpCipxCompression": xPppIpxcpCipxCompression,
       "xPppIpxcpConfigRemoteNode": xPppIpxcpConfigRemoteNode,
       "xPppIpxcpStatusTable": xPppIpxcpStatusTable,
       "xPppIpxcpStatusEntry": xPppIpxcpStatusEntry,
       "xPppIpxcpStatusState": xPppIpxcpStatusState,
       "xPppIpxcpCipxInCompression": xPppIpxcpCipxInCompression,
       "xPppIpxcpCipxOutCompression": xPppIpxcpCipxOutCompression,
       "xPppIpxcpCipxInSlots": xPppIpxcpCipxInSlots,
       "xPppIpxcpCipxOutSlots": xPppIpxcpCipxOutSlots,
       "xPppIpxcpStatusRemoteNode": xPppIpxcpStatusRemoteNode,
       "xPppIpxcpCountersTable": xPppIpxcpCountersTable,
       "xPppIpxcpCountersEntry": xPppIpxcpCountersEntry,
       "xPppIpxcpRxConReq": xPppIpxcpRxConReq,
       "xPppIpxcpTxConReq": xPppIpxcpTxConReq,
       "xPppIpxcpRxConNak": xPppIpxcpRxConNak,
       "xPppIpxcpTxConNak": xPppIpxcpTxConNak,
       "xPppIpxcpRxConAck": xPppIpxcpRxConAck,
       "xPppIpxcpTxConAck": xPppIpxcpTxConAck,
       "xPppIpxcpRxConRej": xPppIpxcpRxConRej,
       "xPppIpxcpTxConRej": xPppIpxcpTxConRej,
       "xPppIpxcpRxTrmReq": xPppIpxcpRxTrmReq,
       "xPppIpxcpTxTrmReq": xPppIpxcpTxTrmReq,
       "xPppIpxcpRxTrmAck": xPppIpxcpRxTrmAck,
       "xPppIpxcpTxTrmAck": xPppIpxcpTxTrmAck}
)
