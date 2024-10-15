# SNMP MIB module (Wellfleet-IPEX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-IPEX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:27 2024
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

(wfIpexGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIpexGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIpex_ObjectIdentity = ObjectIdentity
wfIpex = _WfIpex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1)
)


class _WfIpexDelete_Type(Integer32):
    """Custom type wfIpexDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpexDelete_Type.__name__ = "Integer32"
_WfIpexDelete_Object = MibScalar
wfIpexDelete = _WfIpexDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 1),
    _WfIpexDelete_Type()
)
wfIpexDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexDelete.setStatus("mandatory")


class _WfIpexDisable_Type(Integer32):
    """Custom type wfIpexDisable based on Integer32"""
    defaultValue = 1

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


_WfIpexDisable_Type.__name__ = "Integer32"
_WfIpexDisable_Object = MibScalar
wfIpexDisable = _WfIpexDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 2),
    _WfIpexDisable_Type()
)
wfIpexDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexDisable.setStatus("mandatory")


class _WfIpexState_Type(Integer32):
    """Custom type wfIpexState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfIpexState_Type.__name__ = "Integer32"
_WfIpexState_Object = MibScalar
wfIpexState = _WfIpexState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 3),
    _WfIpexState_Type()
)
wfIpexState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexState.setStatus("mandatory")


class _WfIpexMaxMessageSize_Type(Integer32):
    """Custom type wfIpexMaxMessageSize based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4096),
    )


_WfIpexMaxMessageSize_Type.__name__ = "Integer32"
_WfIpexMaxMessageSize_Object = MibScalar
wfIpexMaxMessageSize = _WfIpexMaxMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 4),
    _WfIpexMaxMessageSize_Type()
)
wfIpexMaxMessageSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMaxMessageSize.setStatus("mandatory")


class _WfIpexInsCalledDte_Type(Integer32):
    """Custom type wfIpexInsCalledDte based on Integer32"""
    defaultValue = 2

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


_WfIpexInsCalledDte_Type.__name__ = "Integer32"
_WfIpexInsCalledDte_Object = MibScalar
wfIpexInsCalledDte = _WfIpexInsCalledDte_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 5),
    _WfIpexInsCalledDte_Type()
)
wfIpexInsCalledDte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexInsCalledDte.setStatus("mandatory")


class _WfIpexInsCallingDte_Type(Integer32):
    """Custom type wfIpexInsCallingDte based on Integer32"""
    defaultValue = 2

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


_WfIpexInsCallingDte_Type.__name__ = "Integer32"
_WfIpexInsCallingDte_Object = MibScalar
wfIpexInsCallingDte = _WfIpexInsCallingDte_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 6),
    _WfIpexInsCallingDte_Type()
)
wfIpexInsCallingDte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexInsCallingDte.setStatus("mandatory")


class _WfIpexTcpRequestLimit_Type(Integer32):
    """Custom type wfIpexTcpRequestLimit based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WfIpexTcpRequestLimit_Type.__name__ = "Integer32"
_WfIpexTcpRequestLimit_Object = MibScalar
wfIpexTcpRequestLimit = _WfIpexTcpRequestLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 7),
    _WfIpexTcpRequestLimit_Type()
)
wfIpexTcpRequestLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexTcpRequestLimit.setStatus("mandatory")


class _WfIpexTcpRequestCheck_Type(Integer32):
    """Custom type wfIpexTcpRequestCheck based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_WfIpexTcpRequestCheck_Type.__name__ = "Integer32"
_WfIpexTcpRequestCheck_Object = MibScalar
wfIpexTcpRequestCheck = _WfIpexTcpRequestCheck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 8),
    _WfIpexTcpRequestCheck_Type()
)
wfIpexTcpRequestCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexTcpRequestCheck.setStatus("mandatory")


class _WfIpexSendResetRequestOnTCPUp_Type(Integer32):
    """Custom type wfIpexSendResetRequestOnTCPUp based on Integer32"""
    defaultValue = 9


_WfIpexSendResetRequestOnTCPUp_Object = MibScalar
wfIpexSendResetRequestOnTCPUp = _WfIpexSendResetRequestOnTCPUp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 9),
    _WfIpexSendResetRequestOnTCPUp_Type()
)
wfIpexSendResetRequestOnTCPUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexSendResetRequestOnTCPUp.setStatus("mandatory")


class _WfIpexTranslateNetworkOutOfOrder_Type(Integer32):
    """Custom type wfIpexTranslateNetworkOutOfOrder based on Integer32"""
    defaultValue = 29


_WfIpexTranslateNetworkOutOfOrder_Object = MibScalar
wfIpexTranslateNetworkOutOfOrder = _WfIpexTranslateNetworkOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 10),
    _WfIpexTranslateNetworkOutOfOrder_Type()
)
wfIpexTranslateNetworkOutOfOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexTranslateNetworkOutOfOrder.setStatus("mandatory")


class _WfIpexTcpUseIpAddress_Type(Integer32):
    """Custom type wfIpexTcpUseIpAddress based on Integer32"""
    defaultValue = 2

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


_WfIpexTcpUseIpAddress_Type.__name__ = "Integer32"
_WfIpexTcpUseIpAddress_Object = MibScalar
wfIpexTcpUseIpAddress = _WfIpexTcpUseIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 11),
    _WfIpexTcpUseIpAddress_Type()
)
wfIpexTcpUseIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexTcpUseIpAddress.setStatus("mandatory")


class _WfIpexBobEnabled_Type(Integer32):
    """Custom type wfIpexBobEnabled based on Integer32"""
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


_WfIpexBobEnabled_Type.__name__ = "Integer32"
_WfIpexBobEnabled_Object = MibScalar
wfIpexBobEnabled = _WfIpexBobEnabled_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 12),
    _WfIpexBobEnabled_Type()
)
wfIpexBobEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexBobEnabled.setStatus("mandatory")


class _WfIpexBobTimeout_Type(Integer32):
    """Custom type wfIpexBobTimeout based on Integer32"""
    defaultValue = 15000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_WfIpexBobTimeout_Type.__name__ = "Integer32"
_WfIpexBobTimeout_Object = MibScalar
wfIpexBobTimeout = _WfIpexBobTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 13),
    _WfIpexBobTimeout_Type()
)
wfIpexBobTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexBobTimeout.setStatus("mandatory")


class _WfIpexMaxAuditIp_Type(Integer32):
    """Custom type wfIpexMaxAuditIp based on Integer32"""
    defaultValue = 25


_WfIpexMaxAuditIp_Object = MibScalar
wfIpexMaxAuditIp = _WfIpexMaxAuditIp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 14),
    _WfIpexMaxAuditIp_Type()
)
wfIpexMaxAuditIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMaxAuditIp.setStatus("mandatory")


class _WfIpexSessionInstanceIdOffsetForSvc_Type(Integer32):
    """Custom type wfIpexSessionInstanceIdOffsetForSvc based on Integer32"""
    defaultValue = 0


_WfIpexSessionInstanceIdOffsetForSvc_Object = MibScalar
wfIpexSessionInstanceIdOffsetForSvc = _WfIpexSessionInstanceIdOffsetForSvc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 1, 15),
    _WfIpexSessionInstanceIdOffsetForSvc_Type()
)
wfIpexSessionInstanceIdOffsetForSvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexSessionInstanceIdOffsetForSvc.setStatus("mandatory")
_WfIpexMappingTable_Object = MibTable
wfIpexMappingTable = _WfIpexMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2)
)
if mibBuilder.loadTexts:
    wfIpexMappingTable.setStatus("mandatory")
_WfIpexMappingEntry_Object = MibTableRow
wfIpexMappingEntry = _WfIpexMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1)
)
wfIpexMappingEntry.setIndexNames(
    (0, "Wellfleet-IPEX-MIB", "wfIpexMappingSrcConnCct"),
    (0, "Wellfleet-IPEX-MIB", "wfIpexMappingSrcConnType"),
    (0, "Wellfleet-IPEX-MIB", "wfIpexMappingID1"),
    (0, "Wellfleet-IPEX-MIB", "wfIpexMappingID2"),
)
if mibBuilder.loadTexts:
    wfIpexMappingEntry.setStatus("mandatory")


class _WfIpexMappingDelete_Type(Integer32):
    """Custom type wfIpexMappingDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpexMappingDelete_Type.__name__ = "Integer32"
_WfIpexMappingDelete_Object = MibTableColumn
wfIpexMappingDelete = _WfIpexMappingDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 1),
    _WfIpexMappingDelete_Type()
)
wfIpexMappingDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingDelete.setStatus("mandatory")


class _WfIpexMappingDisable_Type(Integer32):
    """Custom type wfIpexMappingDisable based on Integer32"""
    defaultValue = 1

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


_WfIpexMappingDisable_Type.__name__ = "Integer32"
_WfIpexMappingDisable_Object = MibTableColumn
wfIpexMappingDisable = _WfIpexMappingDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 2),
    _WfIpexMappingDisable_Type()
)
wfIpexMappingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingDisable.setStatus("mandatory")
_WfIpexMappingSrcConnCct_Type = Integer32
_WfIpexMappingSrcConnCct_Object = MibTableColumn
wfIpexMappingSrcConnCct = _WfIpexMappingSrcConnCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 3),
    _WfIpexMappingSrcConnCct_Type()
)
wfIpexMappingSrcConnCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexMappingSrcConnCct.setStatus("mandatory")


class _WfIpexMappingSrcConnType_Type(Integer32):
    """Custom type wfIpexMappingSrcConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dcesvc", 4),
          ("lapb", 8),
          ("pvc", 1),
          ("svc", 2),
          ("tcp", 16))
    )


_WfIpexMappingSrcConnType_Type.__name__ = "Integer32"
_WfIpexMappingSrcConnType_Object = MibTableColumn
wfIpexMappingSrcConnType = _WfIpexMappingSrcConnType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 4),
    _WfIpexMappingSrcConnType_Type()
)
wfIpexMappingSrcConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexMappingSrcConnType.setStatus("mandatory")
_WfIpexMappingID1_Type = Integer32
_WfIpexMappingID1_Object = MibTableColumn
wfIpexMappingID1 = _WfIpexMappingID1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 5),
    _WfIpexMappingID1_Type()
)
wfIpexMappingID1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexMappingID1.setStatus("mandatory")
_WfIpexMappingID2_Type = OctetString
_WfIpexMappingID2_Object = MibTableColumn
wfIpexMappingID2 = _WfIpexMappingID2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 6),
    _WfIpexMappingID2_Type()
)
wfIpexMappingID2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexMappingID2.setStatus("mandatory")
_WfIpexMappingDstConnCct_Type = Integer32
_WfIpexMappingDstConnCct_Object = MibTableColumn
wfIpexMappingDstConnCct = _WfIpexMappingDstConnCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 7),
    _WfIpexMappingDstConnCct_Type()
)
wfIpexMappingDstConnCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingDstConnCct.setStatus("mandatory")


class _WfIpexMappingDstConnType_Type(Integer32):
    """Custom type wfIpexMappingDstConnType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dcesvc", 4),
          ("lapb", 8),
          ("pvc", 1),
          ("svc", 2),
          ("tcp", 16))
    )


_WfIpexMappingDstConnType_Type.__name__ = "Integer32"
_WfIpexMappingDstConnType_Object = MibTableColumn
wfIpexMappingDstConnType = _WfIpexMappingDstConnType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 8),
    _WfIpexMappingDstConnType_Type()
)
wfIpexMappingDstConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingDstConnType.setStatus("mandatory")
_WfIpexMappingLocalDTEAddr_Type = DisplayString
_WfIpexMappingLocalDTEAddr_Object = MibTableColumn
wfIpexMappingLocalDTEAddr = _WfIpexMappingLocalDTEAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 9),
    _WfIpexMappingLocalDTEAddr_Type()
)
wfIpexMappingLocalDTEAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingLocalDTEAddr.setStatus("mandatory")
_WfIpexMappingRemoteDTEAddr_Type = DisplayString
_WfIpexMappingRemoteDTEAddr_Object = MibTableColumn
wfIpexMappingRemoteDTEAddr = _WfIpexMappingRemoteDTEAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 10),
    _WfIpexMappingRemoteDTEAddr_Type()
)
wfIpexMappingRemoteDTEAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingRemoteDTEAddr.setStatus("mandatory")


class _WfIpexMappingPvcLcn_Type(Integer32):
    """Custom type wfIpexMappingPvcLcn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WfIpexMappingPvcLcn_Type.__name__ = "Integer32"
_WfIpexMappingPvcLcn_Object = MibTableColumn
wfIpexMappingPvcLcn = _WfIpexMappingPvcLcn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 11),
    _WfIpexMappingPvcLcn_Type()
)
wfIpexMappingPvcLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingPvcLcn.setStatus("mandatory")
_WfIpexMappingRemoteIpAddr_Type = IpAddress
_WfIpexMappingRemoteIpAddr_Object = MibTableColumn
wfIpexMappingRemoteIpAddr = _WfIpexMappingRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 12),
    _WfIpexMappingRemoteIpAddr_Type()
)
wfIpexMappingRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingRemoteIpAddr.setStatus("mandatory")
_WfIpexMappingRemoteTcpPort_Type = Integer32
_WfIpexMappingRemoteTcpPort_Object = MibTableColumn
wfIpexMappingRemoteTcpPort = _WfIpexMappingRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 13),
    _WfIpexMappingRemoteTcpPort_Type()
)
wfIpexMappingRemoteTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingRemoteTcpPort.setStatus("mandatory")


class _WfIpexMappingQueueSize_Type(Integer32):
    """Custom type wfIpexMappingQueueSize based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 8192),
    )


_WfIpexMappingQueueSize_Type.__name__ = "Integer32"
_WfIpexMappingQueueSize_Object = MibTableColumn
wfIpexMappingQueueSize = _WfIpexMappingQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 14),
    _WfIpexMappingQueueSize_Type()
)
wfIpexMappingQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingQueueSize.setStatus("mandatory")


class _WfIpexMappingSlotNumber_Type(Integer32):
    """Custom type wfIpexMappingSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_WfIpexMappingSlotNumber_Type.__name__ = "Integer32"
_WfIpexMappingSlotNumber_Object = MibTableColumn
wfIpexMappingSlotNumber = _WfIpexMappingSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 15),
    _WfIpexMappingSlotNumber_Type()
)
wfIpexMappingSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingSlotNumber.setStatus("mandatory")


class _WfIpexMappingCtrlMode_Type(Integer32):
    """Custom type wfIpexMappingCtrlMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("end2end", 2),
          ("gateway", 3),
          ("local", 1))
    )


_WfIpexMappingCtrlMode_Type.__name__ = "Integer32"
_WfIpexMappingCtrlMode_Object = MibTableColumn
wfIpexMappingCtrlMode = _WfIpexMappingCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 16),
    _WfIpexMappingCtrlMode_Type()
)
wfIpexMappingCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingCtrlMode.setStatus("mandatory")
_WfIpexMappingX25CUDF_Type = OctetString
_WfIpexMappingX25CUDF_Object = MibTableColumn
wfIpexMappingX25CUDF = _WfIpexMappingX25CUDF_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 17),
    _WfIpexMappingX25CUDF_Type()
)
wfIpexMappingX25CUDF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingX25CUDF.setStatus("mandatory")


class _WfIpexMappingIdleTimer_Type(Integer32):
    """Custom type wfIpexMappingIdleTimer based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_WfIpexMappingIdleTimer_Type.__name__ = "Integer32"
_WfIpexMappingIdleTimer_Object = MibTableColumn
wfIpexMappingIdleTimer = _WfIpexMappingIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 18),
    _WfIpexMappingIdleTimer_Type()
)
wfIpexMappingIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingIdleTimer.setStatus("mandatory")


class _WfIpexMappingKeepaliveTimer_Type(Integer32):
    """Custom type wfIpexMappingKeepaliveTimer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_WfIpexMappingKeepaliveTimer_Type.__name__ = "Integer32"
_WfIpexMappingKeepaliveTimer_Object = MibTableColumn
wfIpexMappingKeepaliveTimer = _WfIpexMappingKeepaliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 19),
    _WfIpexMappingKeepaliveTimer_Type()
)
wfIpexMappingKeepaliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingKeepaliveTimer.setStatus("mandatory")


class _WfIpexMappingKeepaliveRetries_Type(Integer32):
    """Custom type wfIpexMappingKeepaliveRetries based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_WfIpexMappingKeepaliveRetries_Type.__name__ = "Integer32"
_WfIpexMappingKeepaliveRetries_Object = MibTableColumn
wfIpexMappingKeepaliveRetries = _WfIpexMappingKeepaliveRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 20),
    _WfIpexMappingKeepaliveRetries_Type()
)
wfIpexMappingKeepaliveRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingKeepaliveRetries.setStatus("mandatory")


class _WfIpexMappingTrace_Type(Integer32):
    """Custom type wfIpexMappingTrace based on Integer32"""
    defaultValue = 0


_WfIpexMappingTrace_Object = MibTableColumn
wfIpexMappingTrace = _WfIpexMappingTrace_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 21),
    _WfIpexMappingTrace_Type()
)
wfIpexMappingTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingTrace.setStatus("mandatory")


class _WfIpexMappingMsgHdrType_Type(Integer32):
    """Custom type wfIpexMappingMsgHdrType based on Integer32"""
    defaultValue = 4

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
        *(("full", 4),
          ("long", 3),
          ("none", 1),
          ("short", 2))
    )


_WfIpexMappingMsgHdrType_Type.__name__ = "Integer32"
_WfIpexMappingMsgHdrType_Object = MibTableColumn
wfIpexMappingMsgHdrType = _WfIpexMappingMsgHdrType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 22),
    _WfIpexMappingMsgHdrType_Type()
)
wfIpexMappingMsgHdrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingMsgHdrType.setStatus("mandatory")
_WfIpexMappingRemoteBackupIp_Type = IpAddress
_WfIpexMappingRemoteBackupIp_Object = MibTableColumn
wfIpexMappingRemoteBackupIp = _WfIpexMappingRemoteBackupIp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 23),
    _WfIpexMappingRemoteBackupIp_Type()
)
wfIpexMappingRemoteBackupIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingRemoteBackupIp.setStatus("mandatory")
_WfIpexMappingXlateCallingX121_Type = DisplayString
_WfIpexMappingXlateCallingX121_Object = MibTableColumn
wfIpexMappingXlateCallingX121 = _WfIpexMappingXlateCallingX121_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 24),
    _WfIpexMappingXlateCallingX121_Type()
)
wfIpexMappingXlateCallingX121.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingXlateCallingX121.setStatus("mandatory")


class _WfIpexMappingTcpMaxRetry_Type(Integer32):
    """Custom type wfIpexMappingTcpMaxRetry based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_WfIpexMappingTcpMaxRetry_Type.__name__ = "Integer32"
_WfIpexMappingTcpMaxRetry_Object = MibTableColumn
wfIpexMappingTcpMaxRetry = _WfIpexMappingTcpMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 25),
    _WfIpexMappingTcpMaxRetry_Type()
)
wfIpexMappingTcpMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingTcpMaxRetry.setStatus("mandatory")
_WfIpexMappingCfgLocalIpAddr_Type = IpAddress
_WfIpexMappingCfgLocalIpAddr_Object = MibTableColumn
wfIpexMappingCfgLocalIpAddr = _WfIpexMappingCfgLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 26),
    _WfIpexMappingCfgLocalIpAddr_Type()
)
wfIpexMappingCfgLocalIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingCfgLocalIpAddr.setStatus("mandatory")
_WfIpexMappingRemoteBackupTcpPort_Type = Integer32
_WfIpexMappingRemoteBackupTcpPort_Object = MibTableColumn
wfIpexMappingRemoteBackupTcpPort = _WfIpexMappingRemoteBackupTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 2, 1, 27),
    _WfIpexMappingRemoteBackupTcpPort_Type()
)
wfIpexMappingRemoteBackupTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpexMappingRemoteBackupTcpPort.setStatus("mandatory")
_WfIpexSessionTable_Object = MibTable
wfIpexSessionTable = _WfIpexSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3)
)
if mibBuilder.loadTexts:
    wfIpexSessionTable.setStatus("mandatory")
_WfIpexSessionEntry_Object = MibTableRow
wfIpexSessionEntry = _WfIpexSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1)
)
wfIpexSessionEntry.setIndexNames(
    (0, "Wellfleet-IPEX-MIB", "wfIpexSessionSrcConnCct"),
    (0, "Wellfleet-IPEX-MIB", "wfIpexSessionIndex"),
)
if mibBuilder.loadTexts:
    wfIpexSessionEntry.setStatus("mandatory")


class _WfIpexSessionState_Type(Integer32):
    """Custom type wfIpexSessionState based on Integer32"""
    defaultValue = 4

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
        *(("ccestab", 3),
          ("lapbup", 5),
          ("notconn", 4),
          ("tcpup", 2),
          ("x25up", 1))
    )


_WfIpexSessionState_Type.__name__ = "Integer32"
_WfIpexSessionState_Object = MibTableColumn
wfIpexSessionState = _WfIpexSessionState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 1),
    _WfIpexSessionState_Type()
)
wfIpexSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexSessionState.setStatus("mandatory")
_WfIpexSessionSrcConnCct_Type = Integer32
_WfIpexSessionSrcConnCct_Object = MibTableColumn
wfIpexSessionSrcConnCct = _WfIpexSessionSrcConnCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 2),
    _WfIpexSessionSrcConnCct_Type()
)
wfIpexSessionSrcConnCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexSessionSrcConnCct.setStatus("mandatory")
_WfIpexSessionIndex_Type = Integer32
_WfIpexSessionIndex_Object = MibTableColumn
wfIpexSessionIndex = _WfIpexSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 3),
    _WfIpexSessionIndex_Type()
)
wfIpexSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexSessionIndex.setStatus("mandatory")


class _WfIpexSessionSrcConnType_Type(Integer32):
    """Custom type wfIpexSessionSrcConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dcesvc", 4),
          ("lapb", 8),
          ("pvc", 1),
          ("svc", 2),
          ("tcp", 16))
    )


_WfIpexSessionSrcConnType_Type.__name__ = "Integer32"
_WfIpexSessionSrcConnType_Object = MibTableColumn
wfIpexSessionSrcConnType = _WfIpexSessionSrcConnType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 4),
    _WfIpexSessionSrcConnType_Type()
)
wfIpexSessionSrcConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexSessionSrcConnType.setStatus("mandatory")
_WfIpexSessionDstConnCct_Type = Integer32
_WfIpexSessionDstConnCct_Object = MibTableColumn
wfIpexSessionDstConnCct = _WfIpexSessionDstConnCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 5),
    _WfIpexSessionDstConnCct_Type()
)
wfIpexSessionDstConnCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexSessionDstConnCct.setStatus("mandatory")


class _WfIpexSessionDstConnType_Type(Integer32):
    """Custom type wfIpexSessionDstConnType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dcesvc", 4),
          ("lapb", 8),
          ("pvc", 1),
          ("svc", 2),
          ("tcp", 16))
    )


_WfIpexSessionDstConnType_Type.__name__ = "Integer32"
_WfIpexSessionDstConnType_Object = MibTableColumn
wfIpexSessionDstConnType = _WfIpexSessionDstConnType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 6),
    _WfIpexSessionDstConnType_Type()
)
wfIpexSessionDstConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexSessionDstConnType.setStatus("mandatory")
_WfIpexSessionLocalDTEAddr_Type = DisplayString
_WfIpexSessionLocalDTEAddr_Object = MibTableColumn
wfIpexSessionLocalDTEAddr = _WfIpexSessionLocalDTEAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 7),
    _WfIpexSessionLocalDTEAddr_Type()
)
wfIpexSessionLocalDTEAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexSessionLocalDTEAddr.setStatus("mandatory")
_WfIpexSessionRemoteDTEAddr_Type = DisplayString
_WfIpexSessionRemoteDTEAddr_Object = MibTableColumn
wfIpexSessionRemoteDTEAddr = _WfIpexSessionRemoteDTEAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 8),
    _WfIpexSessionRemoteDTEAddr_Type()
)
wfIpexSessionRemoteDTEAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexSessionRemoteDTEAddr.setStatus("mandatory")


class _WfIpexSessionLCN_Type(Integer32):
    """Custom type wfIpexSessionLCN based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfIpexSessionLCN_Type.__name__ = "Integer32"
_WfIpexSessionLCN_Object = MibTableColumn
wfIpexSessionLCN = _WfIpexSessionLCN_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 9),
    _WfIpexSessionLCN_Type()
)
wfIpexSessionLCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexSessionLCN.setStatus("mandatory")
_WfIpexSessionLocalIpAddr_Type = IpAddress
_WfIpexSessionLocalIpAddr_Object = MibTableColumn
wfIpexSessionLocalIpAddr = _WfIpexSessionLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 10),
    _WfIpexSessionLocalIpAddr_Type()
)
wfIpexSessionLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexSessionLocalIpAddr.setStatus("mandatory")
_WfIpexSessionLocalTcpPort_Type = Integer32
_WfIpexSessionLocalTcpPort_Object = MibTableColumn
wfIpexSessionLocalTcpPort = _WfIpexSessionLocalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 11),
    _WfIpexSessionLocalTcpPort_Type()
)
wfIpexSessionLocalTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexSessionLocalTcpPort.setStatus("mandatory")
_WfIpexSessionRemoteIpAddr_Type = IpAddress
_WfIpexSessionRemoteIpAddr_Object = MibTableColumn
wfIpexSessionRemoteIpAddr = _WfIpexSessionRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 12),
    _WfIpexSessionRemoteIpAddr_Type()
)
wfIpexSessionRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexSessionRemoteIpAddr.setStatus("mandatory")
_WfIpexSessionRemoteTcpPort_Type = Integer32
_WfIpexSessionRemoteTcpPort_Object = MibTableColumn
wfIpexSessionRemoteTcpPort = _WfIpexSessionRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 13),
    _WfIpexSessionRemoteTcpPort_Type()
)
wfIpexSessionRemoteTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexSessionRemoteTcpPort.setStatus("mandatory")
_WfIpexSessionQueueSize_Type = Integer32
_WfIpexSessionQueueSize_Object = MibTableColumn
wfIpexSessionQueueSize = _WfIpexSessionQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15, 3, 1, 14),
    _WfIpexSessionQueueSize_Type()
)
wfIpexSessionQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpexSessionQueueSize.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-IPEX-MIB",
    **{"wfIpex": wfIpex,
       "wfIpexDelete": wfIpexDelete,
       "wfIpexDisable": wfIpexDisable,
       "wfIpexState": wfIpexState,
       "wfIpexMaxMessageSize": wfIpexMaxMessageSize,
       "wfIpexInsCalledDte": wfIpexInsCalledDte,
       "wfIpexInsCallingDte": wfIpexInsCallingDte,
       "wfIpexTcpRequestLimit": wfIpexTcpRequestLimit,
       "wfIpexTcpRequestCheck": wfIpexTcpRequestCheck,
       "wfIpexSendResetRequestOnTCPUp": wfIpexSendResetRequestOnTCPUp,
       "wfIpexTranslateNetworkOutOfOrder": wfIpexTranslateNetworkOutOfOrder,
       "wfIpexTcpUseIpAddress": wfIpexTcpUseIpAddress,
       "wfIpexBobEnabled": wfIpexBobEnabled,
       "wfIpexBobTimeout": wfIpexBobTimeout,
       "wfIpexMaxAuditIp": wfIpexMaxAuditIp,
       "wfIpexSessionInstanceIdOffsetForSvc": wfIpexSessionInstanceIdOffsetForSvc,
       "wfIpexMappingTable": wfIpexMappingTable,
       "wfIpexMappingEntry": wfIpexMappingEntry,
       "wfIpexMappingDelete": wfIpexMappingDelete,
       "wfIpexMappingDisable": wfIpexMappingDisable,
       "wfIpexMappingSrcConnCct": wfIpexMappingSrcConnCct,
       "wfIpexMappingSrcConnType": wfIpexMappingSrcConnType,
       "wfIpexMappingID1": wfIpexMappingID1,
       "wfIpexMappingID2": wfIpexMappingID2,
       "wfIpexMappingDstConnCct": wfIpexMappingDstConnCct,
       "wfIpexMappingDstConnType": wfIpexMappingDstConnType,
       "wfIpexMappingLocalDTEAddr": wfIpexMappingLocalDTEAddr,
       "wfIpexMappingRemoteDTEAddr": wfIpexMappingRemoteDTEAddr,
       "wfIpexMappingPvcLcn": wfIpexMappingPvcLcn,
       "wfIpexMappingRemoteIpAddr": wfIpexMappingRemoteIpAddr,
       "wfIpexMappingRemoteTcpPort": wfIpexMappingRemoteTcpPort,
       "wfIpexMappingQueueSize": wfIpexMappingQueueSize,
       "wfIpexMappingSlotNumber": wfIpexMappingSlotNumber,
       "wfIpexMappingCtrlMode": wfIpexMappingCtrlMode,
       "wfIpexMappingX25CUDF": wfIpexMappingX25CUDF,
       "wfIpexMappingIdleTimer": wfIpexMappingIdleTimer,
       "wfIpexMappingKeepaliveTimer": wfIpexMappingKeepaliveTimer,
       "wfIpexMappingKeepaliveRetries": wfIpexMappingKeepaliveRetries,
       "wfIpexMappingTrace": wfIpexMappingTrace,
       "wfIpexMappingMsgHdrType": wfIpexMappingMsgHdrType,
       "wfIpexMappingRemoteBackupIp": wfIpexMappingRemoteBackupIp,
       "wfIpexMappingXlateCallingX121": wfIpexMappingXlateCallingX121,
       "wfIpexMappingTcpMaxRetry": wfIpexMappingTcpMaxRetry,
       "wfIpexMappingCfgLocalIpAddr": wfIpexMappingCfgLocalIpAddr,
       "wfIpexMappingRemoteBackupTcpPort": wfIpexMappingRemoteBackupTcpPort,
       "wfIpexSessionTable": wfIpexSessionTable,
       "wfIpexSessionEntry": wfIpexSessionEntry,
       "wfIpexSessionState": wfIpexSessionState,
       "wfIpexSessionSrcConnCct": wfIpexSessionSrcConnCct,
       "wfIpexSessionIndex": wfIpexSessionIndex,
       "wfIpexSessionSrcConnType": wfIpexSessionSrcConnType,
       "wfIpexSessionDstConnCct": wfIpexSessionDstConnCct,
       "wfIpexSessionDstConnType": wfIpexSessionDstConnType,
       "wfIpexSessionLocalDTEAddr": wfIpexSessionLocalDTEAddr,
       "wfIpexSessionRemoteDTEAddr": wfIpexSessionRemoteDTEAddr,
       "wfIpexSessionLCN": wfIpexSessionLCN,
       "wfIpexSessionLocalIpAddr": wfIpexSessionLocalIpAddr,
       "wfIpexSessionLocalTcpPort": wfIpexSessionLocalTcpPort,
       "wfIpexSessionRemoteIpAddr": wfIpexSessionRemoteIpAddr,
       "wfIpexSessionRemoteTcpPort": wfIpexSessionRemoteTcpPort,
       "wfIpexSessionQueueSize": wfIpexSessionQueueSize}
)
