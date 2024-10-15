# SNMP MIB module (ECPPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ECPPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:28 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class PortRef(Integer32):
    """Custom type PortRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )





class PppState(Integer32):
    """Custom type PppState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("closing", 5),
          ("negotiating", 3),
          ("opened", 4),
          ("opening", 2),
          ("other", 6))
    )





class NcpState(Integer32):
    """Custom type NcpState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("other", 11),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Eicon_ObjectIdentity = ObjectIdentity
eicon = _Eicon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434)
)
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2)
)
_Mibv2_ObjectIdentity = ObjectIdentity
mibv2 = _Mibv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2)
)
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4)
)
_Ecppp_ObjectIdentity = ObjectIdentity
ecppp = _Ecppp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23)
)
_EcpppStatusTable_Object = MibTable
ecpppStatusTable = _EcpppStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1)
)
if mibBuilder.loadTexts:
    ecpppStatusTable.setStatus("mandatory")
_EcpppStatusEntry_Object = MibTableRow
ecpppStatusEntry = _EcpppStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1, 1)
)
ecpppStatusEntry.setIndexNames(
    (0, "ECPPP-MIB", "ecpppStatusPortRef"),
)
if mibBuilder.loadTexts:
    ecpppStatusEntry.setStatus("mandatory")
_EcpppStatusPortRef_Type = PortRef
_EcpppStatusPortRef_Object = MibTableColumn
ecpppStatusPortRef = _EcpppStatusPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1, 1, 1),
    _EcpppStatusPortRef_Type()
)
ecpppStatusPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatusPortRef.setStatus("mandatory")
_EcpppStatusState_Type = PppState
_EcpppStatusState_Object = MibTableColumn
ecpppStatusState = _EcpppStatusState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1, 1, 2),
    _EcpppStatusState_Type()
)
ecpppStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatusState.setStatus("mandatory")


class _EcpppStatusAuthentProtocol_Type(Integer32):
    """Custom type ecpppStatusAuthentProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 2),
          ("other", 3),
          ("pap", 1))
    )


_EcpppStatusAuthentProtocol_Type.__name__ = "Integer32"
_EcpppStatusAuthentProtocol_Object = MibTableColumn
ecpppStatusAuthentProtocol = _EcpppStatusAuthentProtocol_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1, 1, 3),
    _EcpppStatusAuthentProtocol_Type()
)
ecpppStatusAuthentProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatusAuthentProtocol.setStatus("mandatory")


class _EcpppStatusQualityProtocol_Type(Integer32):
    """Custom type ecpppStatusQualityProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lqr", 1),
          ("other", 2))
    )


_EcpppStatusQualityProtocol_Type.__name__ = "Integer32"
_EcpppStatusQualityProtocol_Object = MibTableColumn
ecpppStatusQualityProtocol = _EcpppStatusQualityProtocol_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1, 1, 4),
    _EcpppStatusQualityProtocol_Type()
)
ecpppStatusQualityProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatusQualityProtocol.setStatus("mandatory")
_EcpppStatusNegotiatedPktSize_Type = Integer32
_EcpppStatusNegotiatedPktSize_Object = MibTableColumn
ecpppStatusNegotiatedPktSize = _EcpppStatusNegotiatedPktSize_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1, 1, 5),
    _EcpppStatusNegotiatedPktSize_Type()
)
ecpppStatusNegotiatedPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatusNegotiatedPktSize.setStatus("mandatory")
_EcpppStatusWindowSize_Type = Integer32
_EcpppStatusWindowSize_Object = MibTableColumn
ecpppStatusWindowSize = _EcpppStatusWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1, 1, 6),
    _EcpppStatusWindowSize_Type()
)
ecpppStatusWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatusWindowSize.setStatus("mandatory")


class _EcpppStatusProtocolCompr_Type(Integer32):
    """Custom type ecpppStatusProtocolCompr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EcpppStatusProtocolCompr_Type.__name__ = "Integer32"
_EcpppStatusProtocolCompr_Object = MibTableColumn
ecpppStatusProtocolCompr = _EcpppStatusProtocolCompr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1, 1, 7),
    _EcpppStatusProtocolCompr_Type()
)
ecpppStatusProtocolCompr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatusProtocolCompr.setStatus("mandatory")


class _EcpppStatusAddrCtrlCompr_Type(Integer32):
    """Custom type ecpppStatusAddrCtrlCompr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EcpppStatusAddrCtrlCompr_Type.__name__ = "Integer32"
_EcpppStatusAddrCtrlCompr_Object = MibTableColumn
ecpppStatusAddrCtrlCompr = _EcpppStatusAddrCtrlCompr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1, 1, 8),
    _EcpppStatusAddrCtrlCompr_Type()
)
ecpppStatusAddrCtrlCompr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatusAddrCtrlCompr.setStatus("mandatory")
_EcpppStatusRestartTimer_Type = Integer32
_EcpppStatusRestartTimer_Object = MibTableColumn
ecpppStatusRestartTimer = _EcpppStatusRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1, 1, 9),
    _EcpppStatusRestartTimer_Type()
)
ecpppStatusRestartTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatusRestartTimer.setStatus("mandatory")
_EcpppStatusMaxPacketSize_Type = Integer32
_EcpppStatusMaxPacketSize_Object = MibTableColumn
ecpppStatusMaxPacketSize = _EcpppStatusMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1, 1, 10),
    _EcpppStatusMaxPacketSize_Type()
)
ecpppStatusMaxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatusMaxPacketSize.setStatus("mandatory")
_EcpppStatusMaxTerminate_Type = Integer32
_EcpppStatusMaxTerminate_Object = MibTableColumn
ecpppStatusMaxTerminate = _EcpppStatusMaxTerminate_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1, 1, 11),
    _EcpppStatusMaxTerminate_Type()
)
ecpppStatusMaxTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatusMaxTerminate.setStatus("mandatory")
_EcpppStatusMaxConfig_Type = Integer32
_EcpppStatusMaxConfig_Object = MibTableColumn
ecpppStatusMaxConfig = _EcpppStatusMaxConfig_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1, 1, 12),
    _EcpppStatusMaxConfig_Type()
)
ecpppStatusMaxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatusMaxConfig.setStatus("mandatory")
_EcpppStatusMaxFailure_Type = Integer32
_EcpppStatusMaxFailure_Object = MibTableColumn
ecpppStatusMaxFailure = _EcpppStatusMaxFailure_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1, 1, 13),
    _EcpppStatusMaxFailure_Type()
)
ecpppStatusMaxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatusMaxFailure.setStatus("mandatory")
_EcpppStatusNcpMask_Type = Integer32
_EcpppStatusNcpMask_Object = MibTableColumn
ecpppStatusNcpMask = _EcpppStatusNcpMask_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 1, 1, 14),
    _EcpppStatusNcpMask_Type()
)
ecpppStatusNcpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatusNcpMask.setStatus("mandatory")
_EcpppStatsTable_Object = MibTable
ecpppStatsTable = _EcpppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2)
)
if mibBuilder.loadTexts:
    ecpppStatsTable.setStatus("mandatory")
_EcpppStatsEntry_Object = MibTableRow
ecpppStatsEntry = _EcpppStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1)
)
ecpppStatsEntry.setIndexNames(
    (0, "ECPPP-MIB", "ecpppStatsPortRef"),
)
if mibBuilder.loadTexts:
    ecpppStatsEntry.setStatus("mandatory")
_EcpppStatsPortRef_Type = PortRef
_EcpppStatsPortRef_Object = MibTableColumn
ecpppStatsPortRef = _EcpppStatsPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 1),
    _EcpppStatsPortRef_Type()
)
ecpppStatsPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsPortRef.setStatus("mandatory")
_EcpppStatsLcpReqTx_Type = Counter32
_EcpppStatsLcpReqTx_Object = MibTableColumn
ecpppStatsLcpReqTx = _EcpppStatsLcpReqTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 2),
    _EcpppStatsLcpReqTx_Type()
)
ecpppStatsLcpReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpReqTx.setStatus("mandatory")
_EcpppStatsLcpReqRx_Type = Counter32
_EcpppStatsLcpReqRx_Object = MibTableColumn
ecpppStatsLcpReqRx = _EcpppStatsLcpReqRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 3),
    _EcpppStatsLcpReqRx_Type()
)
ecpppStatsLcpReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpReqRx.setStatus("mandatory")
_EcpppStatsLcpAckTx_Type = Counter32
_EcpppStatsLcpAckTx_Object = MibTableColumn
ecpppStatsLcpAckTx = _EcpppStatsLcpAckTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 4),
    _EcpppStatsLcpAckTx_Type()
)
ecpppStatsLcpAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpAckTx.setStatus("mandatory")
_EcpppStatsLcpAckRx_Type = Counter32
_EcpppStatsLcpAckRx_Object = MibTableColumn
ecpppStatsLcpAckRx = _EcpppStatsLcpAckRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 5),
    _EcpppStatsLcpAckRx_Type()
)
ecpppStatsLcpAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpAckRx.setStatus("mandatory")
_EcpppStatsLcpNakTx_Type = Counter32
_EcpppStatsLcpNakTx_Object = MibTableColumn
ecpppStatsLcpNakTx = _EcpppStatsLcpNakTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 6),
    _EcpppStatsLcpNakTx_Type()
)
ecpppStatsLcpNakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpNakTx.setStatus("mandatory")
_EcpppStatsLcpNakRx_Type = Counter32
_EcpppStatsLcpNakRx_Object = MibTableColumn
ecpppStatsLcpNakRx = _EcpppStatsLcpNakRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 7),
    _EcpppStatsLcpNakRx_Type()
)
ecpppStatsLcpNakRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpNakRx.setStatus("mandatory")
_EcpppStatsLcpRejTx_Type = Counter32
_EcpppStatsLcpRejTx_Object = MibTableColumn
ecpppStatsLcpRejTx = _EcpppStatsLcpRejTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 8),
    _EcpppStatsLcpRejTx_Type()
)
ecpppStatsLcpRejTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpRejTx.setStatus("mandatory")
_EcpppStatsLcpRejRx_Type = Counter32
_EcpppStatsLcpRejRx_Object = MibTableColumn
ecpppStatsLcpRejRx = _EcpppStatsLcpRejRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 9),
    _EcpppStatsLcpRejRx_Type()
)
ecpppStatsLcpRejRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpRejRx.setStatus("mandatory")
_EcpppStatsLcpCodeRejTx_Type = Counter32
_EcpppStatsLcpCodeRejTx_Object = MibTableColumn
ecpppStatsLcpCodeRejTx = _EcpppStatsLcpCodeRejTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 10),
    _EcpppStatsLcpCodeRejTx_Type()
)
ecpppStatsLcpCodeRejTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpCodeRejTx.setStatus("mandatory")
_EcpppStatsLcpCodeRejRx_Type = Counter32
_EcpppStatsLcpCodeRejRx_Object = MibTableColumn
ecpppStatsLcpCodeRejRx = _EcpppStatsLcpCodeRejRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 11),
    _EcpppStatsLcpCodeRejRx_Type()
)
ecpppStatsLcpCodeRejRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpCodeRejRx.setStatus("mandatory")
_EcpppStatsLcpProRejTx_Type = Counter32
_EcpppStatsLcpProRejTx_Object = MibTableColumn
ecpppStatsLcpProRejTx = _EcpppStatsLcpProRejTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 12),
    _EcpppStatsLcpProRejTx_Type()
)
ecpppStatsLcpProRejTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpProRejTx.setStatus("mandatory")
_EcpppStatsLcpProRejRx_Type = Counter32
_EcpppStatsLcpProRejRx_Object = MibTableColumn
ecpppStatsLcpProRejRx = _EcpppStatsLcpProRejRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 13),
    _EcpppStatsLcpProRejRx_Type()
)
ecpppStatsLcpProRejRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpProRejRx.setStatus("mandatory")
_EcpppStatsLcpEchoReqTx_Type = Counter32
_EcpppStatsLcpEchoReqTx_Object = MibTableColumn
ecpppStatsLcpEchoReqTx = _EcpppStatsLcpEchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 14),
    _EcpppStatsLcpEchoReqTx_Type()
)
ecpppStatsLcpEchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpEchoReqTx.setStatus("mandatory")
_EcpppStatsLcpEchoReqRx_Type = Counter32
_EcpppStatsLcpEchoReqRx_Object = MibTableColumn
ecpppStatsLcpEchoReqRx = _EcpppStatsLcpEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 15),
    _EcpppStatsLcpEchoReqRx_Type()
)
ecpppStatsLcpEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpEchoReqRx.setStatus("mandatory")
_EcpppStatsLcpEchoReplyTx_Type = Counter32
_EcpppStatsLcpEchoReplyTx_Object = MibTableColumn
ecpppStatsLcpEchoReplyTx = _EcpppStatsLcpEchoReplyTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 16),
    _EcpppStatsLcpEchoReplyTx_Type()
)
ecpppStatsLcpEchoReplyTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpEchoReplyTx.setStatus("mandatory")
_EcpppStatsLcpEchoReplyRx_Type = Counter32
_EcpppStatsLcpEchoReplyRx_Object = MibTableColumn
ecpppStatsLcpEchoReplyRx = _EcpppStatsLcpEchoReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 17),
    _EcpppStatsLcpEchoReplyRx_Type()
)
ecpppStatsLcpEchoReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpEchoReplyRx.setStatus("mandatory")
_EcpppStatsLcpRestartTimeout_Type = Counter32
_EcpppStatsLcpRestartTimeout_Object = MibTableColumn
ecpppStatsLcpRestartTimeout = _EcpppStatsLcpRestartTimeout_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 18),
    _EcpppStatsLcpRestartTimeout_Type()
)
ecpppStatsLcpRestartTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpRestartTimeout.setStatus("mandatory")
_EcpppStatsLcpTermRetrans_Type = Counter32
_EcpppStatsLcpTermRetrans_Object = MibTableColumn
ecpppStatsLcpTermRetrans = _EcpppStatsLcpTermRetrans_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 19),
    _EcpppStatsLcpTermRetrans_Type()
)
ecpppStatsLcpTermRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpTermRetrans.setStatus("mandatory")
_EcpppStatsLcpConfRetrans_Type = Counter32
_EcpppStatsLcpConfRetrans_Object = MibTableColumn
ecpppStatsLcpConfRetrans = _EcpppStatsLcpConfRetrans_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 20),
    _EcpppStatsLcpConfRetrans_Type()
)
ecpppStatsLcpConfRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsLcpConfRetrans.setStatus("mandatory")
_EcpppStatsFrameTx_Type = Counter32
_EcpppStatsFrameTx_Object = MibTableColumn
ecpppStatsFrameTx = _EcpppStatsFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 21),
    _EcpppStatsFrameTx_Type()
)
ecpppStatsFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsFrameTx.setStatus("mandatory")
_EcpppStatsFrameRx_Type = Counter32
_EcpppStatsFrameRx_Object = MibTableColumn
ecpppStatsFrameRx = _EcpppStatsFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 22),
    _EcpppStatsFrameRx_Type()
)
ecpppStatsFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsFrameRx.setStatus("mandatory")
_EcpppStatsCharTx_Type = Counter32
_EcpppStatsCharTx_Object = MibTableColumn
ecpppStatsCharTx = _EcpppStatsCharTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 23),
    _EcpppStatsCharTx_Type()
)
ecpppStatsCharTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsCharTx.setStatus("mandatory")
_EcpppStatsCharRx_Type = Counter32
_EcpppStatsCharRx_Object = MibTableColumn
ecpppStatsCharRx = _EcpppStatsCharRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 2, 1, 24),
    _EcpppStatsCharRx_Type()
)
ecpppStatsCharRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppStatsCharRx.setStatus("mandatory")
_EcpppIPInfoTable_Object = MibTable
ecpppIPInfoTable = _EcpppIPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 3)
)
if mibBuilder.loadTexts:
    ecpppIPInfoTable.setStatus("mandatory")
_EcpppIPInfoEntry_Object = MibTableRow
ecpppIPInfoEntry = _EcpppIPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 3, 1)
)
ecpppIPInfoEntry.setIndexNames(
    (0, "ECPPP-MIB", "ecpppIPInfoPortRef"),
)
if mibBuilder.loadTexts:
    ecpppIPInfoEntry.setStatus("mandatory")
_EcpppIPInfoPortRef_Type = PortRef
_EcpppIPInfoPortRef_Object = MibTableColumn
ecpppIPInfoPortRef = _EcpppIPInfoPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 3, 1, 1),
    _EcpppIPInfoPortRef_Type()
)
ecpppIPInfoPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPInfoPortRef.setStatus("mandatory")
_EcpppIPInfoNcpState_Type = NcpState
_EcpppIPInfoNcpState_Object = MibTableColumn
ecpppIPInfoNcpState = _EcpppIPInfoNcpState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 3, 1, 2),
    _EcpppIPInfoNcpState_Type()
)
ecpppIPInfoNcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPInfoNcpState.setStatus("mandatory")


class _EcpppIPInfoIPComprProtocol_Type(Integer32):
    """Custom type ecpppIPInfoIPComprProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vj-tcp", 2))
    )


_EcpppIPInfoIPComprProtocol_Type.__name__ = "Integer32"
_EcpppIPInfoIPComprProtocol_Object = MibTableColumn
ecpppIPInfoIPComprProtocol = _EcpppIPInfoIPComprProtocol_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 3, 1, 3),
    _EcpppIPInfoIPComprProtocol_Type()
)
ecpppIPInfoIPComprProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPInfoIPComprProtocol.setStatus("mandatory")
_EcpppIPInfoIPAddr_Type = IpAddress
_EcpppIPInfoIPAddr_Object = MibTableColumn
ecpppIPInfoIPAddr = _EcpppIPInfoIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 3, 1, 4),
    _EcpppIPInfoIPAddr_Type()
)
ecpppIPInfoIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPInfoIPAddr.setStatus("mandatory")
_EcpppIPInfoIPcpMaxTerm_Type = Integer32
_EcpppIPInfoIPcpMaxTerm_Object = MibTableColumn
ecpppIPInfoIPcpMaxTerm = _EcpppIPInfoIPcpMaxTerm_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 3, 1, 5),
    _EcpppIPInfoIPcpMaxTerm_Type()
)
ecpppIPInfoIPcpMaxTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPInfoIPcpMaxTerm.setStatus("mandatory")
_EcpppIPInfoIPcpMaxConfig_Type = Integer32
_EcpppIPInfoIPcpMaxConfig_Object = MibTableColumn
ecpppIPInfoIPcpMaxConfig = _EcpppIPInfoIPcpMaxConfig_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 3, 1, 6),
    _EcpppIPInfoIPcpMaxConfig_Type()
)
ecpppIPInfoIPcpMaxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPInfoIPcpMaxConfig.setStatus("mandatory")
_EcpppIPInfoIPcpMaxFailure_Type = Integer32
_EcpppIPInfoIPcpMaxFailure_Object = MibTableColumn
ecpppIPInfoIPcpMaxFailure = _EcpppIPInfoIPcpMaxFailure_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 3, 1, 7),
    _EcpppIPInfoIPcpMaxFailure_Type()
)
ecpppIPInfoIPcpMaxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPInfoIPcpMaxFailure.setStatus("mandatory")
_EcpppIPStatsTable_Object = MibTable
ecpppIPStatsTable = _EcpppIPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 4)
)
if mibBuilder.loadTexts:
    ecpppIPStatsTable.setStatus("mandatory")
_EcpppIPStatsEntry_Object = MibTableRow
ecpppIPStatsEntry = _EcpppIPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 4, 1)
)
ecpppIPStatsEntry.setIndexNames(
    (0, "ECPPP-MIB", "ecpppIPStatsPortRef"),
)
if mibBuilder.loadTexts:
    ecpppIPStatsEntry.setStatus("mandatory")
_EcpppIPStatsPortRef_Type = PortRef
_EcpppIPStatsPortRef_Object = MibTableColumn
ecpppIPStatsPortRef = _EcpppIPStatsPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 4, 1, 1),
    _EcpppIPStatsPortRef_Type()
)
ecpppIPStatsPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPStatsPortRef.setStatus("mandatory")
_EcpppIPStatsDatagramsTx_Type = Counter32
_EcpppIPStatsDatagramsTx_Object = MibTableColumn
ecpppIPStatsDatagramsTx = _EcpppIPStatsDatagramsTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 4, 1, 2),
    _EcpppIPStatsDatagramsTx_Type()
)
ecpppIPStatsDatagramsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPStatsDatagramsTx.setStatus("mandatory")
_EcpppIPStatsDatagramsRx_Type = Counter32
_EcpppIPStatsDatagramsRx_Object = MibTableColumn
ecpppIPStatsDatagramsRx = _EcpppIPStatsDatagramsRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 4, 1, 3),
    _EcpppIPStatsDatagramsRx_Type()
)
ecpppIPStatsDatagramsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPStatsDatagramsRx.setStatus("mandatory")
_EcpppIPStatsCharTx_Type = Counter32
_EcpppIPStatsCharTx_Object = MibTableColumn
ecpppIPStatsCharTx = _EcpppIPStatsCharTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 4, 1, 4),
    _EcpppIPStatsCharTx_Type()
)
ecpppIPStatsCharTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPStatsCharTx.setStatus("mandatory")
_EcpppIPStatsCharRx_Type = Counter32
_EcpppIPStatsCharRx_Object = MibTableColumn
ecpppIPStatsCharRx = _EcpppIPStatsCharRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 4, 1, 5),
    _EcpppIPStatsCharRx_Type()
)
ecpppIPStatsCharRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPStatsCharRx.setStatus("mandatory")
_EcpppIPStatsNcpRestartTimeout_Type = Counter32
_EcpppIPStatsNcpRestartTimeout_Object = MibTableColumn
ecpppIPStatsNcpRestartTimeout = _EcpppIPStatsNcpRestartTimeout_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 4, 1, 6),
    _EcpppIPStatsNcpRestartTimeout_Type()
)
ecpppIPStatsNcpRestartTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPStatsNcpRestartTimeout.setStatus("mandatory")
_EcpppIPStatsNcpTermRetrans_Type = Counter32
_EcpppIPStatsNcpTermRetrans_Object = MibTableColumn
ecpppIPStatsNcpTermRetrans = _EcpppIPStatsNcpTermRetrans_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 4, 1, 7),
    _EcpppIPStatsNcpTermRetrans_Type()
)
ecpppIPStatsNcpTermRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPStatsNcpTermRetrans.setStatus("mandatory")
_EcpppIPStatsNcpReqRetrans_Type = Counter32
_EcpppIPStatsNcpReqRetrans_Object = MibTableColumn
ecpppIPStatsNcpReqRetrans = _EcpppIPStatsNcpReqRetrans_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 4, 1, 8),
    _EcpppIPStatsNcpReqRetrans_Type()
)
ecpppIPStatsNcpReqRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPStatsNcpReqRetrans.setStatus("mandatory")
_EcpppIPXInfoTable_Object = MibTable
ecpppIPXInfoTable = _EcpppIPXInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 5)
)
if mibBuilder.loadTexts:
    ecpppIPXInfoTable.setStatus("mandatory")
_EcpppIPXInfoEntry_Object = MibTableRow
ecpppIPXInfoEntry = _EcpppIPXInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 5, 1)
)
ecpppIPXInfoEntry.setIndexNames(
    (0, "ECPPP-MIB", "ecpppIPXInfoPortRef"),
)
if mibBuilder.loadTexts:
    ecpppIPXInfoEntry.setStatus("mandatory")
_EcpppIPXInfoPortRef_Type = PortRef
_EcpppIPXInfoPortRef_Object = MibTableColumn
ecpppIPXInfoPortRef = _EcpppIPXInfoPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 5, 1, 1),
    _EcpppIPXInfoPortRef_Type()
)
ecpppIPXInfoPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPXInfoPortRef.setStatus("mandatory")
_EcpppIPXInfoNcpState_Type = NcpState
_EcpppIPXInfoNcpState_Object = MibTableColumn
ecpppIPXInfoNcpState = _EcpppIPXInfoNcpState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 5, 1, 2),
    _EcpppIPXInfoNcpState_Type()
)
ecpppIPXInfoNcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPXInfoNcpState.setStatus("mandatory")
_EcpppIPXInfoIPXcpMaxTerm_Type = Integer32
_EcpppIPXInfoIPXcpMaxTerm_Object = MibTableColumn
ecpppIPXInfoIPXcpMaxTerm = _EcpppIPXInfoIPXcpMaxTerm_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 5, 1, 3),
    _EcpppIPXInfoIPXcpMaxTerm_Type()
)
ecpppIPXInfoIPXcpMaxTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPXInfoIPXcpMaxTerm.setStatus("mandatory")
_EcpppIPXInfoIPXcpMaxConfig_Type = Integer32
_EcpppIPXInfoIPXcpMaxConfig_Object = MibTableColumn
ecpppIPXInfoIPXcpMaxConfig = _EcpppIPXInfoIPXcpMaxConfig_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 5, 1, 4),
    _EcpppIPXInfoIPXcpMaxConfig_Type()
)
ecpppIPXInfoIPXcpMaxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPXInfoIPXcpMaxConfig.setStatus("mandatory")
_EcpppIPXInfoIPXcpMaxFailure_Type = Integer32
_EcpppIPXInfoIPXcpMaxFailure_Object = MibTableColumn
ecpppIPXInfoIPXcpMaxFailure = _EcpppIPXInfoIPXcpMaxFailure_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 5, 1, 5),
    _EcpppIPXInfoIPXcpMaxFailure_Type()
)
ecpppIPXInfoIPXcpMaxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPXInfoIPXcpMaxFailure.setStatus("mandatory")
_EcpppIPXStatsTable_Object = MibTable
ecpppIPXStatsTable = _EcpppIPXStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 6)
)
if mibBuilder.loadTexts:
    ecpppIPXStatsTable.setStatus("mandatory")
_EcpppIPXStatsEntry_Object = MibTableRow
ecpppIPXStatsEntry = _EcpppIPXStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 6, 1)
)
ecpppIPXStatsEntry.setIndexNames(
    (0, "ECPPP-MIB", "ecpppIPXStatsPortRef"),
)
if mibBuilder.loadTexts:
    ecpppIPXStatsEntry.setStatus("mandatory")
_EcpppIPXStatsPortRef_Type = PortRef
_EcpppIPXStatsPortRef_Object = MibTableColumn
ecpppIPXStatsPortRef = _EcpppIPXStatsPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 6, 1, 1),
    _EcpppIPXStatsPortRef_Type()
)
ecpppIPXStatsPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPXStatsPortRef.setStatus("mandatory")
_EcpppIPXStatsDatagramsTx_Type = Counter32
_EcpppIPXStatsDatagramsTx_Object = MibTableColumn
ecpppIPXStatsDatagramsTx = _EcpppIPXStatsDatagramsTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 6, 1, 2),
    _EcpppIPXStatsDatagramsTx_Type()
)
ecpppIPXStatsDatagramsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPXStatsDatagramsTx.setStatus("mandatory")
_EcpppIPXStatsDatagramsRx_Type = Counter32
_EcpppIPXStatsDatagramsRx_Object = MibTableColumn
ecpppIPXStatsDatagramsRx = _EcpppIPXStatsDatagramsRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 6, 1, 3),
    _EcpppIPXStatsDatagramsRx_Type()
)
ecpppIPXStatsDatagramsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPXStatsDatagramsRx.setStatus("mandatory")
_EcpppIPXStatsCharTx_Type = Counter32
_EcpppIPXStatsCharTx_Object = MibTableColumn
ecpppIPXStatsCharTx = _EcpppIPXStatsCharTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 6, 1, 4),
    _EcpppIPXStatsCharTx_Type()
)
ecpppIPXStatsCharTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPXStatsCharTx.setStatus("mandatory")
_EcpppIPXStatsCharRx_Type = Counter32
_EcpppIPXStatsCharRx_Object = MibTableColumn
ecpppIPXStatsCharRx = _EcpppIPXStatsCharRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 6, 1, 5),
    _EcpppIPXStatsCharRx_Type()
)
ecpppIPXStatsCharRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPXStatsCharRx.setStatus("mandatory")
_EcpppIPXStatsNcpRestartTimeout_Type = Counter32
_EcpppIPXStatsNcpRestartTimeout_Object = MibTableColumn
ecpppIPXStatsNcpRestartTimeout = _EcpppIPXStatsNcpRestartTimeout_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 6, 1, 6),
    _EcpppIPXStatsNcpRestartTimeout_Type()
)
ecpppIPXStatsNcpRestartTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPXStatsNcpRestartTimeout.setStatus("mandatory")
_EcpppIPXStatsNcpTermRetrans_Type = Counter32
_EcpppIPXStatsNcpTermRetrans_Object = MibTableColumn
ecpppIPXStatsNcpTermRetrans = _EcpppIPXStatsNcpTermRetrans_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 6, 1, 7),
    _EcpppIPXStatsNcpTermRetrans_Type()
)
ecpppIPXStatsNcpTermRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPXStatsNcpTermRetrans.setStatus("mandatory")
_EcpppIPXStatsNcpReqRetrans_Type = Counter32
_EcpppIPXStatsNcpReqRetrans_Object = MibTableColumn
ecpppIPXStatsNcpReqRetrans = _EcpppIPXStatsNcpReqRetrans_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 6, 1, 8),
    _EcpppIPXStatsNcpReqRetrans_Type()
)
ecpppIPXStatsNcpReqRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppIPXStatsNcpReqRetrans.setStatus("mandatory")
_EcpppATInfoTable_Object = MibTable
ecpppATInfoTable = _EcpppATInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 7)
)
if mibBuilder.loadTexts:
    ecpppATInfoTable.setStatus("mandatory")
_EcpppATInfoEntry_Object = MibTableRow
ecpppATInfoEntry = _EcpppATInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 7, 1)
)
ecpppATInfoEntry.setIndexNames(
    (0, "ECPPP-MIB", "ecpppATInfoPortRef"),
)
if mibBuilder.loadTexts:
    ecpppATInfoEntry.setStatus("mandatory")
_EcpppATInfoPortRef_Type = PortRef
_EcpppATInfoPortRef_Object = MibTableColumn
ecpppATInfoPortRef = _EcpppATInfoPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 7, 1, 1),
    _EcpppATInfoPortRef_Type()
)
ecpppATInfoPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATInfoPortRef.setStatus("mandatory")
_EcpppATInfoNcpState_Type = NcpState
_EcpppATInfoNcpState_Object = MibTableColumn
ecpppATInfoNcpState = _EcpppATInfoNcpState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 7, 1, 2),
    _EcpppATInfoNcpState_Type()
)
ecpppATInfoNcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATInfoNcpState.setStatus("mandatory")


class _EcpppATInfoRoutingProtocol_Type(Integer32):
    """Custom type ecpppATInfoRoutingProtocol based on Integer32"""
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
        *(("abgp", 4),
          ("aurp", 3),
          ("none", 1),
          ("rtmp", 2))
    )


_EcpppATInfoRoutingProtocol_Type.__name__ = "Integer32"
_EcpppATInfoRoutingProtocol_Object = MibTableColumn
ecpppATInfoRoutingProtocol = _EcpppATInfoRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 7, 1, 3),
    _EcpppATInfoRoutingProtocol_Type()
)
ecpppATInfoRoutingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATInfoRoutingProtocol.setStatus("mandatory")


class _EcpppATInfoComprConfig_Type(Integer32):
    """Custom type ecpppATInfoComprConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-compression", 1),
          ("prorietary", 3),
          ("standard", 2))
    )


_EcpppATInfoComprConfig_Type.__name__ = "Integer32"
_EcpppATInfoComprConfig_Object = MibTableColumn
ecpppATInfoComprConfig = _EcpppATInfoComprConfig_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 7, 1, 4),
    _EcpppATInfoComprConfig_Type()
)
ecpppATInfoComprConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATInfoComprConfig.setStatus("mandatory")
_EcpppATInfoServerClass_Type = Integer32
_EcpppATInfoServerClass_Object = MibTableColumn
ecpppATInfoServerClass = _EcpppATInfoServerClass_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 7, 1, 5),
    _EcpppATInfoServerClass_Type()
)
ecpppATInfoServerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATInfoServerClass.setStatus("mandatory")
_EcpppATInfoATAddr_Type = Integer32
_EcpppATInfoATAddr_Object = MibTableColumn
ecpppATInfoATAddr = _EcpppATInfoATAddr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 7, 1, 6),
    _EcpppATInfoATAddr_Type()
)
ecpppATInfoATAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATInfoATAddr.setStatus("mandatory")
_EcpppATInfoATNode_Type = Integer32
_EcpppATInfoATNode_Object = MibTableColumn
ecpppATInfoATNode = _EcpppATInfoATNode_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 7, 1, 7),
    _EcpppATInfoATNode_Type()
)
ecpppATInfoATNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATInfoATNode.setStatus("mandatory")
_EcpppATInfoATcpMaxTerm_Type = Integer32
_EcpppATInfoATcpMaxTerm_Object = MibTableColumn
ecpppATInfoATcpMaxTerm = _EcpppATInfoATcpMaxTerm_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 7, 1, 8),
    _EcpppATInfoATcpMaxTerm_Type()
)
ecpppATInfoATcpMaxTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATInfoATcpMaxTerm.setStatus("mandatory")
_EcpppATInfoATcpMaxConfig_Type = Integer32
_EcpppATInfoATcpMaxConfig_Object = MibTableColumn
ecpppATInfoATcpMaxConfig = _EcpppATInfoATcpMaxConfig_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 7, 1, 9),
    _EcpppATInfoATcpMaxConfig_Type()
)
ecpppATInfoATcpMaxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATInfoATcpMaxConfig.setStatus("mandatory")
_EcpppATInfoATcpMaxFailure_Type = Integer32
_EcpppATInfoATcpMaxFailure_Object = MibTableColumn
ecpppATInfoATcpMaxFailure = _EcpppATInfoATcpMaxFailure_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 7, 1, 10),
    _EcpppATInfoATcpMaxFailure_Type()
)
ecpppATInfoATcpMaxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATInfoATcpMaxFailure.setStatus("mandatory")


class _EcpppATInfoSrvName_Type(DisplayString):
    """Custom type ecpppATInfoSrvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EcpppATInfoSrvName_Type.__name__ = "DisplayString"
_EcpppATInfoSrvName_Object = MibTableColumn
ecpppATInfoSrvName = _EcpppATInfoSrvName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 7, 1, 11),
    _EcpppATInfoSrvName_Type()
)
ecpppATInfoSrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATInfoSrvName.setStatus("mandatory")


class _EcpppATInfoZoneName_Type(DisplayString):
    """Custom type ecpppATInfoZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EcpppATInfoZoneName_Type.__name__ = "DisplayString"
_EcpppATInfoZoneName_Object = MibTableColumn
ecpppATInfoZoneName = _EcpppATInfoZoneName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 7, 1, 12),
    _EcpppATInfoZoneName_Type()
)
ecpppATInfoZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATInfoZoneName.setStatus("mandatory")
_EcpppATStatsTable_Object = MibTable
ecpppATStatsTable = _EcpppATStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 8)
)
if mibBuilder.loadTexts:
    ecpppATStatsTable.setStatus("mandatory")
_EcpppATStatsEntry_Object = MibTableRow
ecpppATStatsEntry = _EcpppATStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 8, 1)
)
ecpppATStatsEntry.setIndexNames(
    (0, "ECPPP-MIB", "ecpppATStatsPortRef"),
)
if mibBuilder.loadTexts:
    ecpppATStatsEntry.setStatus("mandatory")
_EcpppATStatsPortRef_Type = PortRef
_EcpppATStatsPortRef_Object = MibTableColumn
ecpppATStatsPortRef = _EcpppATStatsPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 8, 1, 1),
    _EcpppATStatsPortRef_Type()
)
ecpppATStatsPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATStatsPortRef.setStatus("mandatory")
_EcpppATStatsDatagramsTx_Type = Counter32
_EcpppATStatsDatagramsTx_Object = MibTableColumn
ecpppATStatsDatagramsTx = _EcpppATStatsDatagramsTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 8, 1, 2),
    _EcpppATStatsDatagramsTx_Type()
)
ecpppATStatsDatagramsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATStatsDatagramsTx.setStatus("mandatory")
_EcpppATStatsDatagramsRx_Type = Counter32
_EcpppATStatsDatagramsRx_Object = MibTableColumn
ecpppATStatsDatagramsRx = _EcpppATStatsDatagramsRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 8, 1, 3),
    _EcpppATStatsDatagramsRx_Type()
)
ecpppATStatsDatagramsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATStatsDatagramsRx.setStatus("mandatory")
_EcpppATStatsCharTx_Type = Counter32
_EcpppATStatsCharTx_Object = MibTableColumn
ecpppATStatsCharTx = _EcpppATStatsCharTx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 8, 1, 4),
    _EcpppATStatsCharTx_Type()
)
ecpppATStatsCharTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATStatsCharTx.setStatus("mandatory")
_EcpppATStatsCharRx_Type = Counter32
_EcpppATStatsCharRx_Object = MibTableColumn
ecpppATStatsCharRx = _EcpppATStatsCharRx_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 8, 1, 5),
    _EcpppATStatsCharRx_Type()
)
ecpppATStatsCharRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATStatsCharRx.setStatus("mandatory")
_EcpppATStatsNcpRestartTimeout_Type = Counter32
_EcpppATStatsNcpRestartTimeout_Object = MibTableColumn
ecpppATStatsNcpRestartTimeout = _EcpppATStatsNcpRestartTimeout_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 8, 1, 6),
    _EcpppATStatsNcpRestartTimeout_Type()
)
ecpppATStatsNcpRestartTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATStatsNcpRestartTimeout.setStatus("mandatory")
_EcpppATStatsNcpTermRetrans_Type = Counter32
_EcpppATStatsNcpTermRetrans_Object = MibTableColumn
ecpppATStatsNcpTermRetrans = _EcpppATStatsNcpTermRetrans_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 8, 1, 7),
    _EcpppATStatsNcpTermRetrans_Type()
)
ecpppATStatsNcpTermRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATStatsNcpTermRetrans.setStatus("mandatory")
_EcpppATStatsNcpReqRetrans_Type = Counter32
_EcpppATStatsNcpReqRetrans_Object = MibTableColumn
ecpppATStatsNcpReqRetrans = _EcpppATStatsNcpReqRetrans_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 23, 8, 1, 8),
    _EcpppATStatsNcpReqRetrans_Type()
)
ecpppATStatsNcpReqRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpppATStatsNcpReqRetrans.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ECPPP-MIB",
    **{"PortRef": PortRef,
       "PppState": PppState,
       "NcpState": NcpState,
       "eicon": eicon,
       "management": management,
       "mibv2": mibv2,
       "module": module,
       "ecppp": ecppp,
       "ecpppStatusTable": ecpppStatusTable,
       "ecpppStatusEntry": ecpppStatusEntry,
       "ecpppStatusPortRef": ecpppStatusPortRef,
       "ecpppStatusState": ecpppStatusState,
       "ecpppStatusAuthentProtocol": ecpppStatusAuthentProtocol,
       "ecpppStatusQualityProtocol": ecpppStatusQualityProtocol,
       "ecpppStatusNegotiatedPktSize": ecpppStatusNegotiatedPktSize,
       "ecpppStatusWindowSize": ecpppStatusWindowSize,
       "ecpppStatusProtocolCompr": ecpppStatusProtocolCompr,
       "ecpppStatusAddrCtrlCompr": ecpppStatusAddrCtrlCompr,
       "ecpppStatusRestartTimer": ecpppStatusRestartTimer,
       "ecpppStatusMaxPacketSize": ecpppStatusMaxPacketSize,
       "ecpppStatusMaxTerminate": ecpppStatusMaxTerminate,
       "ecpppStatusMaxConfig": ecpppStatusMaxConfig,
       "ecpppStatusMaxFailure": ecpppStatusMaxFailure,
       "ecpppStatusNcpMask": ecpppStatusNcpMask,
       "ecpppStatsTable": ecpppStatsTable,
       "ecpppStatsEntry": ecpppStatsEntry,
       "ecpppStatsPortRef": ecpppStatsPortRef,
       "ecpppStatsLcpReqTx": ecpppStatsLcpReqTx,
       "ecpppStatsLcpReqRx": ecpppStatsLcpReqRx,
       "ecpppStatsLcpAckTx": ecpppStatsLcpAckTx,
       "ecpppStatsLcpAckRx": ecpppStatsLcpAckRx,
       "ecpppStatsLcpNakTx": ecpppStatsLcpNakTx,
       "ecpppStatsLcpNakRx": ecpppStatsLcpNakRx,
       "ecpppStatsLcpRejTx": ecpppStatsLcpRejTx,
       "ecpppStatsLcpRejRx": ecpppStatsLcpRejRx,
       "ecpppStatsLcpCodeRejTx": ecpppStatsLcpCodeRejTx,
       "ecpppStatsLcpCodeRejRx": ecpppStatsLcpCodeRejRx,
       "ecpppStatsLcpProRejTx": ecpppStatsLcpProRejTx,
       "ecpppStatsLcpProRejRx": ecpppStatsLcpProRejRx,
       "ecpppStatsLcpEchoReqTx": ecpppStatsLcpEchoReqTx,
       "ecpppStatsLcpEchoReqRx": ecpppStatsLcpEchoReqRx,
       "ecpppStatsLcpEchoReplyTx": ecpppStatsLcpEchoReplyTx,
       "ecpppStatsLcpEchoReplyRx": ecpppStatsLcpEchoReplyRx,
       "ecpppStatsLcpRestartTimeout": ecpppStatsLcpRestartTimeout,
       "ecpppStatsLcpTermRetrans": ecpppStatsLcpTermRetrans,
       "ecpppStatsLcpConfRetrans": ecpppStatsLcpConfRetrans,
       "ecpppStatsFrameTx": ecpppStatsFrameTx,
       "ecpppStatsFrameRx": ecpppStatsFrameRx,
       "ecpppStatsCharTx": ecpppStatsCharTx,
       "ecpppStatsCharRx": ecpppStatsCharRx,
       "ecpppIPInfoTable": ecpppIPInfoTable,
       "ecpppIPInfoEntry": ecpppIPInfoEntry,
       "ecpppIPInfoPortRef": ecpppIPInfoPortRef,
       "ecpppIPInfoNcpState": ecpppIPInfoNcpState,
       "ecpppIPInfoIPComprProtocol": ecpppIPInfoIPComprProtocol,
       "ecpppIPInfoIPAddr": ecpppIPInfoIPAddr,
       "ecpppIPInfoIPcpMaxTerm": ecpppIPInfoIPcpMaxTerm,
       "ecpppIPInfoIPcpMaxConfig": ecpppIPInfoIPcpMaxConfig,
       "ecpppIPInfoIPcpMaxFailure": ecpppIPInfoIPcpMaxFailure,
       "ecpppIPStatsTable": ecpppIPStatsTable,
       "ecpppIPStatsEntry": ecpppIPStatsEntry,
       "ecpppIPStatsPortRef": ecpppIPStatsPortRef,
       "ecpppIPStatsDatagramsTx": ecpppIPStatsDatagramsTx,
       "ecpppIPStatsDatagramsRx": ecpppIPStatsDatagramsRx,
       "ecpppIPStatsCharTx": ecpppIPStatsCharTx,
       "ecpppIPStatsCharRx": ecpppIPStatsCharRx,
       "ecpppIPStatsNcpRestartTimeout": ecpppIPStatsNcpRestartTimeout,
       "ecpppIPStatsNcpTermRetrans": ecpppIPStatsNcpTermRetrans,
       "ecpppIPStatsNcpReqRetrans": ecpppIPStatsNcpReqRetrans,
       "ecpppIPXInfoTable": ecpppIPXInfoTable,
       "ecpppIPXInfoEntry": ecpppIPXInfoEntry,
       "ecpppIPXInfoPortRef": ecpppIPXInfoPortRef,
       "ecpppIPXInfoNcpState": ecpppIPXInfoNcpState,
       "ecpppIPXInfoIPXcpMaxTerm": ecpppIPXInfoIPXcpMaxTerm,
       "ecpppIPXInfoIPXcpMaxConfig": ecpppIPXInfoIPXcpMaxConfig,
       "ecpppIPXInfoIPXcpMaxFailure": ecpppIPXInfoIPXcpMaxFailure,
       "ecpppIPXStatsTable": ecpppIPXStatsTable,
       "ecpppIPXStatsEntry": ecpppIPXStatsEntry,
       "ecpppIPXStatsPortRef": ecpppIPXStatsPortRef,
       "ecpppIPXStatsDatagramsTx": ecpppIPXStatsDatagramsTx,
       "ecpppIPXStatsDatagramsRx": ecpppIPXStatsDatagramsRx,
       "ecpppIPXStatsCharTx": ecpppIPXStatsCharTx,
       "ecpppIPXStatsCharRx": ecpppIPXStatsCharRx,
       "ecpppIPXStatsNcpRestartTimeout": ecpppIPXStatsNcpRestartTimeout,
       "ecpppIPXStatsNcpTermRetrans": ecpppIPXStatsNcpTermRetrans,
       "ecpppIPXStatsNcpReqRetrans": ecpppIPXStatsNcpReqRetrans,
       "ecpppATInfoTable": ecpppATInfoTable,
       "ecpppATInfoEntry": ecpppATInfoEntry,
       "ecpppATInfoPortRef": ecpppATInfoPortRef,
       "ecpppATInfoNcpState": ecpppATInfoNcpState,
       "ecpppATInfoRoutingProtocol": ecpppATInfoRoutingProtocol,
       "ecpppATInfoComprConfig": ecpppATInfoComprConfig,
       "ecpppATInfoServerClass": ecpppATInfoServerClass,
       "ecpppATInfoATAddr": ecpppATInfoATAddr,
       "ecpppATInfoATNode": ecpppATInfoATNode,
       "ecpppATInfoATcpMaxTerm": ecpppATInfoATcpMaxTerm,
       "ecpppATInfoATcpMaxConfig": ecpppATInfoATcpMaxConfig,
       "ecpppATInfoATcpMaxFailure": ecpppATInfoATcpMaxFailure,
       "ecpppATInfoSrvName": ecpppATInfoSrvName,
       "ecpppATInfoZoneName": ecpppATInfoZoneName,
       "ecpppATStatsTable": ecpppATStatsTable,
       "ecpppATStatsEntry": ecpppATStatsEntry,
       "ecpppATStatsPortRef": ecpppATStatsPortRef,
       "ecpppATStatsDatagramsTx": ecpppATStatsDatagramsTx,
       "ecpppATStatsDatagramsRx": ecpppATStatsDatagramsRx,
       "ecpppATStatsCharTx": ecpppATStatsCharTx,
       "ecpppATStatsCharRx": ecpppATStatsCharRx,
       "ecpppATStatsNcpRestartTimeout": ecpppATStatsNcpRestartTimeout,
       "ecpppATStatsNcpTermRetrans": ecpppATStatsNcpTermRetrans,
       "ecpppATStatsNcpReqRetrans": ecpppATStatsNcpReqRetrans}
)
