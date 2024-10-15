# SNMP MIB module (ACC-L2TP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-L2TP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:29 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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
 NotificationType,
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
    "NotificationType",
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

_AccL2tp_ObjectIdentity = ObjectIdentity
accL2tp = _AccL2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71)
)
_AccL2tpGeneral_ObjectIdentity = ObjectIdentity
accL2tpGeneral = _AccL2tpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1)
)
_AccL2tpGeneralScalars_ObjectIdentity = ObjectIdentity
accL2tpGeneralScalars = _AccL2tpGeneralScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1)
)
_AccL2tpVendorName_Type = DisplayString
_AccL2tpVendorName_Object = MibScalar
accL2tpVendorName = _AccL2tpVendorName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 1),
    _AccL2tpVendorName_Type()
)
accL2tpVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpVendorName.setStatus("mandatory")
_AccL2tpFirmwareRev_Type = DisplayString
_AccL2tpFirmwareRev_Object = MibScalar
accL2tpFirmwareRev = _AccL2tpFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 2),
    _AccL2tpFirmwareRev_Type()
)
accL2tpFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpFirmwareRev.setStatus("mandatory")


class _AccL2pAdminState_Type(Integer32):
    """Custom type accL2pAdminState based on Integer32"""
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


_AccL2pAdminState_Type.__name__ = "Integer32"
_AccL2pAdminState_Object = MibScalar
accL2pAdminState = _AccL2pAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 3),
    _AccL2pAdminState_Type()
)
accL2pAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2pAdminState.setStatus("mandatory")
_AccL2tpProtocolVersion_Type = DisplayString
_AccL2tpProtocolVersion_Object = MibScalar
accL2tpProtocolVersion = _AccL2tpProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 4),
    _AccL2tpProtocolVersion_Type()
)
accL2tpProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpProtocolVersion.setStatus("mandatory")


class _AccL2tpControlRWS_Type(Integer32):
    """Custom type accL2tpControlRWS based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AccL2tpControlRWS_Type.__name__ = "Integer32"
_AccL2tpControlRWS_Object = MibScalar
accL2tpControlRWS = _AccL2tpControlRWS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 5),
    _AccL2tpControlRWS_Type()
)
accL2tpControlRWS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpControlRWS.setStatus("mandatory")


class _AccL2tpPayloadSeq_Type(Integer32):
    """Custom type accL2tpPayloadSeq based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccL2tpPayloadSeq_Type.__name__ = "Integer32"
_AccL2tpPayloadSeq_Object = MibScalar
accL2tpPayloadSeq = _AccL2tpPayloadSeq_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 6),
    _AccL2tpPayloadSeq_Type()
)
accL2tpPayloadSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpPayloadSeq.setStatus("mandatory")


class _AccL2tpPayloadRWS_Type(Integer32):
    """Custom type accL2tpPayloadRWS based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AccL2tpPayloadRWS_Type.__name__ = "Integer32"
_AccL2tpPayloadRWS_Object = MibScalar
accL2tpPayloadRWS = _AccL2tpPayloadRWS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 7),
    _AccL2tpPayloadRWS_Type()
)
accL2tpPayloadRWS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpPayloadRWS.setStatus("mandatory")


class _AccL2tpKeepAlive_Type(Integer32):
    """Custom type accL2tpKeepAlive based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AccL2tpKeepAlive_Type.__name__ = "Integer32"
_AccL2tpKeepAlive_Object = MibScalar
accL2tpKeepAlive = _AccL2tpKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 8),
    _AccL2tpKeepAlive_Type()
)
accL2tpKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpKeepAlive.setStatus("mandatory")


class _AccL2tpMaxAckTimeout_Type(Integer32):
    """Custom type accL2tpMaxAckTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_AccL2tpMaxAckTimeout_Type.__name__ = "Integer32"
_AccL2tpMaxAckTimeout_Object = MibScalar
accL2tpMaxAckTimeout = _AccL2tpMaxAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 9),
    _AccL2tpMaxAckTimeout_Type()
)
accL2tpMaxAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpMaxAckTimeout.setStatus("mandatory")


class _AccL2tpMaxRetrans_Type(Integer32):
    """Custom type accL2tpMaxRetrans based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AccL2tpMaxRetrans_Type.__name__ = "Integer32"
_AccL2tpMaxRetrans_Object = MibScalar
accL2tpMaxRetrans = _AccL2tpMaxRetrans_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 10),
    _AccL2tpMaxRetrans_Type()
)
accL2tpMaxRetrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpMaxRetrans.setStatus("mandatory")


class _AccL2tpIdleDisconnect_Type(Integer32):
    """Custom type accL2tpIdleDisconnect based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AccL2tpIdleDisconnect_Type.__name__ = "Integer32"
_AccL2tpIdleDisconnect_Object = MibScalar
accL2tpIdleDisconnect = _AccL2tpIdleDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 11),
    _AccL2tpIdleDisconnect_Type()
)
accL2tpIdleDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpIdleDisconnect.setStatus("mandatory")


class _AccL2tpTunnelAuthentication_Type(Integer32):
    """Custom type accL2tpTunnelAuthentication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endpointauth", 2),
          ("none", 1))
    )


_AccL2tpTunnelAuthentication_Type.__name__ = "Integer32"
_AccL2tpTunnelAuthentication_Object = MibScalar
accL2tpTunnelAuthentication = _AccL2tpTunnelAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 12),
    _AccL2tpTunnelAuthentication_Type()
)
accL2tpTunnelAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelAuthentication.setStatus("mandatory")


class _AccL2tpKeyDistribution_Type(Integer32):
    """Custom type accL2tpKeyDistribution based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 2),
          ("static", 1))
    )


_AccL2tpKeyDistribution_Type.__name__ = "Integer32"
_AccL2tpKeyDistribution_Object = MibScalar
accL2tpKeyDistribution = _AccL2tpKeyDistribution_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 13),
    _AccL2tpKeyDistribution_Type()
)
accL2tpKeyDistribution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpKeyDistribution.setStatus("mandatory")


class _AccL2tpProxyAuthentication_Type(Integer32):
    """Custom type accL2tpProxyAuthentication based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("ignore", 1))
    )


_AccL2tpProxyAuthentication_Type.__name__ = "Integer32"
_AccL2tpProxyAuthentication_Object = MibScalar
accL2tpProxyAuthentication = _AccL2tpProxyAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 14),
    _AccL2tpProxyAuthentication_Type()
)
accL2tpProxyAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpProxyAuthentication.setStatus("mandatory")


class _AccL2tpServerState_Type(Integer32):
    """Custom type accL2tpServerState based on Integer32"""
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


_AccL2tpServerState_Type.__name__ = "Integer32"
_AccL2tpServerState_Object = MibScalar
accL2tpServerState = _AccL2tpServerState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 15),
    _AccL2tpServerState_Type()
)
accL2tpServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpServerState.setStatus("mandatory")


class _AccL2tpMessageLevel_Type(Integer32):
    """Custom type accL2tpMessageLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccL2tpMessageLevel_Type.__name__ = "Integer32"
_AccL2tpMessageLevel_Object = MibScalar
accL2tpMessageLevel = _AccL2tpMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 16),
    _AccL2tpMessageLevel_Type()
)
accL2tpMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpMessageLevel.setStatus("mandatory")


class _AccL2tpDebugMask_Type(Integer32):
    """Custom type accL2tpDebugMask based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccL2tpDebugMask_Type.__name__ = "Integer32"
_AccL2tpDebugMask_Object = MibScalar
accL2tpDebugMask = _AccL2tpDebugMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 17),
    _AccL2tpDebugMask_Type()
)
accL2tpDebugMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpDebugMask.setStatus("mandatory")


class _AccL2tpPayLoadLength_Type(Integer32):
    """Custom type accL2tpPayLoadLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )


_AccL2tpPayLoadLength_Type.__name__ = "Integer32"
_AccL2tpPayLoadLength_Object = MibScalar
accL2tpPayLoadLength = _AccL2tpPayLoadLength_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 18),
    _AccL2tpPayLoadLength_Type()
)
accL2tpPayLoadLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpPayLoadLength.setStatus("mandatory")


class _AccL2tpAttributeHiding_Type(Integer32):
    """Custom type accL2tpAttributeHiding based on Integer32"""
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


_AccL2tpAttributeHiding_Type.__name__ = "Integer32"
_AccL2tpAttributeHiding_Object = MibScalar
accL2tpAttributeHiding = _AccL2tpAttributeHiding_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 19),
    _AccL2tpAttributeHiding_Type()
)
accL2tpAttributeHiding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpAttributeHiding.setStatus("mandatory")


class _AccL2tpCallConfirm_Type(Integer32):
    """Custom type accL2tpCallConfirm based on Integer32"""
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


_AccL2tpCallConfirm_Type.__name__ = "Integer32"
_AccL2tpCallConfirm_Object = MibScalar
accL2tpCallConfirm = _AccL2tpCallConfirm_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 1, 20),
    _AccL2tpCallConfirm_Type()
)
accL2tpCallConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpCallConfirm.setStatus("mandatory")
_AccL2tpTunnelConfigTable_Object = MibTable
accL2tpTunnelConfigTable = _AccL2tpTunnelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2)
)
if mibBuilder.loadTexts:
    accL2tpTunnelConfigTable.setStatus("mandatory")
_AccL2tpTunnelConfigEntry_Object = MibTableRow
accL2tpTunnelConfigEntry = _AccL2tpTunnelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1)
)
accL2tpTunnelConfigEntry.setIndexNames(
    (0, "ACC-L2TP", "accL2tpTunnelConfigTunnelIfIndex"),
)
if mibBuilder.loadTexts:
    accL2tpTunnelConfigEntry.setStatus("mandatory")


class _AccL2tpTunnelConfigTunnelIfIndex_Type(Integer32):
    """Custom type accL2tpTunnelConfigTunnelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AccL2tpTunnelConfigTunnelIfIndex_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigTunnelIfIndex_Object = MibTableColumn
accL2tpTunnelConfigTunnelIfIndex = _AccL2tpTunnelConfigTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 1),
    _AccL2tpTunnelConfigTunnelIfIndex_Type()
)
accL2tpTunnelConfigTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigTunnelIfIndex.setStatus("mandatory")


class _AccL2tpTunnelConfigControlRWS_Type(Integer32):
    """Custom type accL2tpTunnelConfigControlRWS based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AccL2tpTunnelConfigControlRWS_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigControlRWS_Object = MibTableColumn
accL2tpTunnelConfigControlRWS = _AccL2tpTunnelConfigControlRWS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 2),
    _AccL2tpTunnelConfigControlRWS_Type()
)
accL2tpTunnelConfigControlRWS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigControlRWS.setStatus("mandatory")


class _AccL2tpTunnelConfigPayloadSeq_Type(Integer32):
    """Custom type accL2tpTunnelConfigPayloadSeq based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccL2tpTunnelConfigPayloadSeq_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigPayloadSeq_Object = MibTableColumn
accL2tpTunnelConfigPayloadSeq = _AccL2tpTunnelConfigPayloadSeq_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 3),
    _AccL2tpTunnelConfigPayloadSeq_Type()
)
accL2tpTunnelConfigPayloadSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigPayloadSeq.setStatus("mandatory")


class _AccL2tpTunnelConfigPayloadRWS_Type(Integer32):
    """Custom type accL2tpTunnelConfigPayloadRWS based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AccL2tpTunnelConfigPayloadRWS_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigPayloadRWS_Object = MibTableColumn
accL2tpTunnelConfigPayloadRWS = _AccL2tpTunnelConfigPayloadRWS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 4),
    _AccL2tpTunnelConfigPayloadRWS_Type()
)
accL2tpTunnelConfigPayloadRWS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigPayloadRWS.setStatus("mandatory")


class _AccL2tpTunnelConfigKeepAlive_Type(Integer32):
    """Custom type accL2tpTunnelConfigKeepAlive based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AccL2tpTunnelConfigKeepAlive_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigKeepAlive_Object = MibTableColumn
accL2tpTunnelConfigKeepAlive = _AccL2tpTunnelConfigKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 5),
    _AccL2tpTunnelConfigKeepAlive_Type()
)
accL2tpTunnelConfigKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigKeepAlive.setStatus("mandatory")


class _AccL2tpTunnelConfigMaxAckTimeout_Type(Integer32):
    """Custom type accL2tpTunnelConfigMaxAckTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_AccL2tpTunnelConfigMaxAckTimeout_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigMaxAckTimeout_Object = MibTableColumn
accL2tpTunnelConfigMaxAckTimeout = _AccL2tpTunnelConfigMaxAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 6),
    _AccL2tpTunnelConfigMaxAckTimeout_Type()
)
accL2tpTunnelConfigMaxAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigMaxAckTimeout.setStatus("mandatory")


class _AccL2tpTunnelConfigMaxRetrans_Type(Integer32):
    """Custom type accL2tpTunnelConfigMaxRetrans based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AccL2tpTunnelConfigMaxRetrans_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigMaxRetrans_Object = MibTableColumn
accL2tpTunnelConfigMaxRetrans = _AccL2tpTunnelConfigMaxRetrans_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 7),
    _AccL2tpTunnelConfigMaxRetrans_Type()
)
accL2tpTunnelConfigMaxRetrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigMaxRetrans.setStatus("mandatory")


class _AccL2tpTunnelConfigIdleDisconnect_Type(Integer32):
    """Custom type accL2tpTunnelConfigIdleDisconnect based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AccL2tpTunnelConfigIdleDisconnect_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigIdleDisconnect_Object = MibTableColumn
accL2tpTunnelConfigIdleDisconnect = _AccL2tpTunnelConfigIdleDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 8),
    _AccL2tpTunnelConfigIdleDisconnect_Type()
)
accL2tpTunnelConfigIdleDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigIdleDisconnect.setStatus("mandatory")


class _AccL2tpTunnelConfigTransportMech_Type(Integer32):
    """Custom type accL2tpTunnelConfigTransportMech based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("framerelay", 2),
          ("udp", 1))
    )


_AccL2tpTunnelConfigTransportMech_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigTransportMech_Object = MibTableColumn
accL2tpTunnelConfigTransportMech = _AccL2tpTunnelConfigTransportMech_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 9),
    _AccL2tpTunnelConfigTransportMech_Type()
)
accL2tpTunnelConfigTransportMech.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigTransportMech.setStatus("mandatory")


class _AccL2tpTunnelConfigTunnelAuthentication_Type(Integer32):
    """Custom type accL2tpTunnelConfigTunnelAuthentication based on Integer32"""
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
          ("enable", 1))
    )


_AccL2tpTunnelConfigTunnelAuthentication_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigTunnelAuthentication_Object = MibTableColumn
accL2tpTunnelConfigTunnelAuthentication = _AccL2tpTunnelConfigTunnelAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 10),
    _AccL2tpTunnelConfigTunnelAuthentication_Type()
)
accL2tpTunnelConfigTunnelAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigTunnelAuthentication.setStatus("mandatory")


class _AccL2tpTunnelConfigProxyAuthentication_Type(Integer32):
    """Custom type accL2tpTunnelConfigProxyAuthentication based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("ignore", 1))
    )


_AccL2tpTunnelConfigProxyAuthentication_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigProxyAuthentication_Object = MibTableColumn
accL2tpTunnelConfigProxyAuthentication = _AccL2tpTunnelConfigProxyAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 11),
    _AccL2tpTunnelConfigProxyAuthentication_Type()
)
accL2tpTunnelConfigProxyAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigProxyAuthentication.setStatus("mandatory")


class _AccL2tpTunnelConfigMessageLevel_Type(Integer32):
    """Custom type accL2tpTunnelConfigMessageLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccL2tpTunnelConfigMessageLevel_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigMessageLevel_Object = MibTableColumn
accL2tpTunnelConfigMessageLevel = _AccL2tpTunnelConfigMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 12),
    _AccL2tpTunnelConfigMessageLevel_Type()
)
accL2tpTunnelConfigMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigMessageLevel.setStatus("mandatory")


class _AccL2tpTunnelConfigDebugMask_Type(Integer32):
    """Custom type accL2tpTunnelConfigDebugMask based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccL2tpTunnelConfigDebugMask_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigDebugMask_Object = MibTableColumn
accL2tpTunnelConfigDebugMask = _AccL2tpTunnelConfigDebugMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 13),
    _AccL2tpTunnelConfigDebugMask_Type()
)
accL2tpTunnelConfigDebugMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigDebugMask.setStatus("mandatory")


class _AccL2tpTunnelConfigPayLoadLength_Type(Integer32):
    """Custom type accL2tpTunnelConfigPayLoadLength based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )


_AccL2tpTunnelConfigPayLoadLength_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigPayLoadLength_Object = MibTableColumn
accL2tpTunnelConfigPayLoadLength = _AccL2tpTunnelConfigPayLoadLength_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 14),
    _AccL2tpTunnelConfigPayLoadLength_Type()
)
accL2tpTunnelConfigPayLoadLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigPayLoadLength.setStatus("mandatory")


class _AccL2tpTunnelConfigAttributeHiding_Type(Integer32):
    """Custom type accL2tpTunnelConfigAttributeHiding based on Integer32"""
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


_AccL2tpTunnelConfigAttributeHiding_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigAttributeHiding_Object = MibTableColumn
accL2tpTunnelConfigAttributeHiding = _AccL2tpTunnelConfigAttributeHiding_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 15),
    _AccL2tpTunnelConfigAttributeHiding_Type()
)
accL2tpTunnelConfigAttributeHiding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigAttributeHiding.setStatus("mandatory")


class _AccL2tpTunnelConfigCallConfirm_Type(Integer32):
    """Custom type accL2tpTunnelConfigCallConfirm based on Integer32"""
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


_AccL2tpTunnelConfigCallConfirm_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigCallConfirm_Object = MibTableColumn
accL2tpTunnelConfigCallConfirm = _AccL2tpTunnelConfigCallConfirm_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 16),
    _AccL2tpTunnelConfigCallConfirm_Type()
)
accL2tpTunnelConfigCallConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigCallConfirm.setStatus("mandatory")


class _AccL2tpTunnelConfigEvents_Type(Integer32):
    """Custom type accL2tpTunnelConfigEvents based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_AccL2tpTunnelConfigEvents_Type.__name__ = "Integer32"
_AccL2tpTunnelConfigEvents_Object = MibTableColumn
accL2tpTunnelConfigEvents = _AccL2tpTunnelConfigEvents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 17),
    _AccL2tpTunnelConfigEvents_Type()
)
accL2tpTunnelConfigEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigEvents.setStatus("mandatory")
_AccL2tpTunnelConfigCreate_Type = RowStatus
_AccL2tpTunnelConfigCreate_Object = MibTableColumn
accL2tpTunnelConfigCreate = _AccL2tpTunnelConfigCreate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 18),
    _AccL2tpTunnelConfigCreate_Type()
)
accL2tpTunnelConfigCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigCreate.setStatus("mandatory")
_AccL2tpTunnelConfigStatus_Type = RowStatus
_AccL2tpTunnelConfigStatus_Object = MibTableColumn
accL2tpTunnelConfigStatus = _AccL2tpTunnelConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 2, 1, 19),
    _AccL2tpTunnelConfigStatus_Type()
)
accL2tpTunnelConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelConfigStatus.setStatus("mandatory")
_AccL2tpTunnelStatusTable_Object = MibTable
accL2tpTunnelStatusTable = _AccL2tpTunnelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3)
)
if mibBuilder.loadTexts:
    accL2tpTunnelStatusTable.setStatus("mandatory")
_AccL2tpTunnelStatusEntry_Object = MibTableRow
accL2tpTunnelStatusEntry = _AccL2tpTunnelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1)
)
accL2tpTunnelStatusEntry.setIndexNames(
    (0, "ACC-L2TP", "accL2tpTunnelStatusTunnelIfIndex"),
)
if mibBuilder.loadTexts:
    accL2tpTunnelStatusEntry.setStatus("mandatory")


class _AccL2tpTunnelStatusTunnelIfIndex_Type(Integer32):
    """Custom type accL2tpTunnelStatusTunnelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AccL2tpTunnelStatusTunnelIfIndex_Type.__name__ = "Integer32"
_AccL2tpTunnelStatusTunnelIfIndex_Object = MibTableColumn
accL2tpTunnelStatusTunnelIfIndex = _AccL2tpTunnelStatusTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 1),
    _AccL2tpTunnelStatusTunnelIfIndex_Type()
)
accL2tpTunnelStatusTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusTunnelIfIndex.setStatus("mandatory")


class _AccL2tpTunnelStatusLocalTunnelId_Type(Integer32):
    """Custom type accL2tpTunnelStatusLocalTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccL2tpTunnelStatusLocalTunnelId_Type.__name__ = "Integer32"
_AccL2tpTunnelStatusLocalTunnelId_Object = MibTableColumn
accL2tpTunnelStatusLocalTunnelId = _AccL2tpTunnelStatusLocalTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 2),
    _AccL2tpTunnelStatusLocalTunnelId_Type()
)
accL2tpTunnelStatusLocalTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusLocalTunnelId.setStatus("mandatory")


class _AccL2tpTunnelStatusRemTunnelId_Type(Integer32):
    """Custom type accL2tpTunnelStatusRemTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccL2tpTunnelStatusRemTunnelId_Type.__name__ = "Integer32"
_AccL2tpTunnelStatusRemTunnelId_Object = MibTableColumn
accL2tpTunnelStatusRemTunnelId = _AccL2tpTunnelStatusRemTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 3),
    _AccL2tpTunnelStatusRemTunnelId_Type()
)
accL2tpTunnelStatusRemTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusRemTunnelId.setStatus("mandatory")


class _AccL2tpTunnelStatusRemFraming_Type(Integer32):
    """Custom type accL2tpTunnelStatusRemFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("async", 2),
          ("sync", 1),
          ("syncasync", 3))
    )


_AccL2tpTunnelStatusRemFraming_Type.__name__ = "Integer32"
_AccL2tpTunnelStatusRemFraming_Object = MibTableColumn
accL2tpTunnelStatusRemFraming = _AccL2tpTunnelStatusRemFraming_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 4),
    _AccL2tpTunnelStatusRemFraming_Type()
)
accL2tpTunnelStatusRemFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusRemFraming.setStatus("mandatory")


class _AccL2tpTunnelStatusRemBearerCap_Type(Integer32):
    """Custom type accL2tpTunnelStatusRemBearerCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog", 2),
          ("digital", 1),
          ("digitalanalog", 3))
    )


_AccL2tpTunnelStatusRemBearerCap_Type.__name__ = "Integer32"
_AccL2tpTunnelStatusRemBearerCap_Object = MibTableColumn
accL2tpTunnelStatusRemBearerCap = _AccL2tpTunnelStatusRemBearerCap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 5),
    _AccL2tpTunnelStatusRemBearerCap_Type()
)
accL2tpTunnelStatusRemBearerCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusRemBearerCap.setStatus("mandatory")


class _AccL2tpTunnelStatusRemControlRWS_Type(Integer32):
    """Custom type accL2tpTunnelStatusRemControlRWS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AccL2tpTunnelStatusRemControlRWS_Type.__name__ = "Integer32"
_AccL2tpTunnelStatusRemControlRWS_Object = MibTableColumn
accL2tpTunnelStatusRemControlRWS = _AccL2tpTunnelStatusRemControlRWS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 6),
    _AccL2tpTunnelStatusRemControlRWS_Type()
)
accL2tpTunnelStatusRemControlRWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusRemControlRWS.setStatus("mandatory")


class _AccL2tpTunnelStatusRemKeepAlive_Type(Integer32):
    """Custom type accL2tpTunnelStatusRemKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AccL2tpTunnelStatusRemKeepAlive_Type.__name__ = "Integer32"
_AccL2tpTunnelStatusRemKeepAlive_Object = MibTableColumn
accL2tpTunnelStatusRemKeepAlive = _AccL2tpTunnelStatusRemKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 7),
    _AccL2tpTunnelStatusRemKeepAlive_Type()
)
accL2tpTunnelStatusRemKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusRemKeepAlive.setStatus("mandatory")
_AccL2tpTunnelStatusRemVendorName_Type = DisplayString
_AccL2tpTunnelStatusRemVendorName_Object = MibTableColumn
accL2tpTunnelStatusRemVendorName = _AccL2tpTunnelStatusRemVendorName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 8),
    _AccL2tpTunnelStatusRemVendorName_Type()
)
accL2tpTunnelStatusRemVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusRemVendorName.setStatus("mandatory")
_AccL2tpTunnelStatusRemFirmRev_Type = DisplayString
_AccL2tpTunnelStatusRemFirmRev_Object = MibTableColumn
accL2tpTunnelStatusRemFirmRev = _AccL2tpTunnelStatusRemFirmRev_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 9),
    _AccL2tpTunnelStatusRemFirmRev_Type()
)
accL2tpTunnelStatusRemFirmRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusRemFirmRev.setStatus("mandatory")
_AccL2tpTunnelStatusRemHostName_Type = DisplayString
_AccL2tpTunnelStatusRemHostName_Object = MibTableColumn
accL2tpTunnelStatusRemHostName = _AccL2tpTunnelStatusRemHostName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 10),
    _AccL2tpTunnelStatusRemHostName_Type()
)
accL2tpTunnelStatusRemHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusRemHostName.setStatus("mandatory")
_AccL2tpTunnelStatusRemProtocolVer_Type = DisplayString
_AccL2tpTunnelStatusRemProtocolVer_Object = MibTableColumn
accL2tpTunnelStatusRemProtocolVer = _AccL2tpTunnelStatusRemProtocolVer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 11),
    _AccL2tpTunnelStatusRemProtocolVer_Type()
)
accL2tpTunnelStatusRemProtocolVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusRemProtocolVer.setStatus("mandatory")


class _AccL2tpTunnelStatusTunnelState_Type(Integer32):
    """Custom type accL2tpTunnelStatusTunnelState based on Integer32"""
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
        *(("established", 4),
          ("idle", 1),
          ("waitconn", 3),
          ("waitreply", 2),
          ("waitstop", 5))
    )


_AccL2tpTunnelStatusTunnelState_Type.__name__ = "Integer32"
_AccL2tpTunnelStatusTunnelState_Object = MibTableColumn
accL2tpTunnelStatusTunnelState = _AccL2tpTunnelStatusTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 12),
    _AccL2tpTunnelStatusTunnelState_Type()
)
accL2tpTunnelStatusTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusTunnelState.setStatus("mandatory")


class _AccL2tpTunnelStatusKeepAlive_Type(Integer32):
    """Custom type accL2tpTunnelStatusKeepAlive based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AccL2tpTunnelStatusKeepAlive_Type.__name__ = "Integer32"
_AccL2tpTunnelStatusKeepAlive_Object = MibTableColumn
accL2tpTunnelStatusKeepAlive = _AccL2tpTunnelStatusKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 13),
    _AccL2tpTunnelStatusKeepAlive_Type()
)
accL2tpTunnelStatusKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusKeepAlive.setStatus("mandatory")
_AccL2tpTunnelStatusCalcRemRWS_Type = Gauge32
_AccL2tpTunnelStatusCalcRemRWS_Object = MibTableColumn
accL2tpTunnelStatusCalcRemRWS = _AccL2tpTunnelStatusCalcRemRWS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 14),
    _AccL2tpTunnelStatusCalcRemRWS_Type()
)
accL2tpTunnelStatusCalcRemRWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusCalcRemRWS.setStatus("mandatory")
_AccL2tpTunnelStatusCalcRemRetransTimeout_Type = Gauge32
_AccL2tpTunnelStatusCalcRemRetransTimeout_Object = MibTableColumn
accL2tpTunnelStatusCalcRemRetransTimeout = _AccL2tpTunnelStatusCalcRemRetransTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 15),
    _AccL2tpTunnelStatusCalcRemRetransTimeout_Type()
)
accL2tpTunnelStatusCalcRemRetransTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusCalcRemRetransTimeout.setStatus("mandatory")
_AccL2tpTunnelStatusQueueLength_Type = Gauge32
_AccL2tpTunnelStatusQueueLength_Object = MibTableColumn
accL2tpTunnelStatusQueueLength = _AccL2tpTunnelStatusQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 16),
    _AccL2tpTunnelStatusQueueLength_Type()
)
accL2tpTunnelStatusQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusQueueLength.setStatus("mandatory")
_AccL2tpTunnelStatusTxOctets_Type = Counter32
_AccL2tpTunnelStatusTxOctets_Object = MibTableColumn
accL2tpTunnelStatusTxOctets = _AccL2tpTunnelStatusTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 17),
    _AccL2tpTunnelStatusTxOctets_Type()
)
accL2tpTunnelStatusTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusTxOctets.setStatus("mandatory")
_AccL2tpTunnelStatusTxPackets_Type = Counter32
_AccL2tpTunnelStatusTxPackets_Object = MibTableColumn
accL2tpTunnelStatusTxPackets = _AccL2tpTunnelStatusTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 18),
    _AccL2tpTunnelStatusTxPackets_Type()
)
accL2tpTunnelStatusTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusTxPackets.setStatus("mandatory")
_AccL2tpTunnelStatusRxOctets_Type = Counter32
_AccL2tpTunnelStatusRxOctets_Object = MibTableColumn
accL2tpTunnelStatusRxOctets = _AccL2tpTunnelStatusRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 19),
    _AccL2tpTunnelStatusRxOctets_Type()
)
accL2tpTunnelStatusRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusRxOctets.setStatus("mandatory")
_AccL2tpTunnelStatusRxPackets_Type = Counter32
_AccL2tpTunnelStatusRxPackets_Object = MibTableColumn
accL2tpTunnelStatusRxPackets = _AccL2tpTunnelStatusRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 20),
    _AccL2tpTunnelStatusRxPackets_Type()
)
accL2tpTunnelStatusRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusRxPackets.setStatus("mandatory")
_AccL2tpTunnelStatusTotalSessions_Type = Counter32
_AccL2tpTunnelStatusTotalSessions_Object = MibTableColumn
accL2tpTunnelStatusTotalSessions = _AccL2tpTunnelStatusTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 21),
    _AccL2tpTunnelStatusTotalSessions_Type()
)
accL2tpTunnelStatusTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusTotalSessions.setStatus("mandatory")
_AccL2tpTunnelStatusActiveSessions_Type = Gauge32
_AccL2tpTunnelStatusActiveSessions_Object = MibTableColumn
accL2tpTunnelStatusActiveSessions = _AccL2tpTunnelStatusActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 22),
    _AccL2tpTunnelStatusActiveSessions_Type()
)
accL2tpTunnelStatusActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusActiveSessions.setStatus("mandatory")
_AccL2tpTunnelStatusAttemptFails_Type = Counter32
_AccL2tpTunnelStatusAttemptFails_Object = MibTableColumn
accL2tpTunnelStatusAttemptFails = _AccL2tpTunnelStatusAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 23),
    _AccL2tpTunnelStatusAttemptFails_Type()
)
accL2tpTunnelStatusAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusAttemptFails.setStatus("mandatory")
_AccL2tpTunnelStatusRetransTimeouts_Type = Counter32
_AccL2tpTunnelStatusRetransTimeouts_Object = MibTableColumn
accL2tpTunnelStatusRetransTimeouts = _AccL2tpTunnelStatusRetransTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 24),
    _AccL2tpTunnelStatusRetransTimeouts_Type()
)
accL2tpTunnelStatusRetransTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusRetransTimeouts.setStatus("mandatory")
_AccL2tpTunnelStatusBackwardTransitions_Type = Counter32
_AccL2tpTunnelStatusBackwardTransitions_Object = MibTableColumn
accL2tpTunnelStatusBackwardTransitions = _AccL2tpTunnelStatusBackwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 25),
    _AccL2tpTunnelStatusBackwardTransitions_Type()
)
accL2tpTunnelStatusBackwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusBackwardTransitions.setStatus("mandatory")
_AccL2tpTunnelStatusLastTransitions_Type = TimeTicks
_AccL2tpTunnelStatusLastTransitions_Object = MibTableColumn
accL2tpTunnelStatusLastTransitions = _AccL2tpTunnelStatusLastTransitions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 26),
    _AccL2tpTunnelStatusLastTransitions_Type()
)
accL2tpTunnelStatusLastTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusLastTransitions.setStatus("mandatory")
_AccL2tpTunnelStatusLastCause_Type = DisplayString
_AccL2tpTunnelStatusLastCause_Object = MibTableColumn
accL2tpTunnelStatusLastCause = _AccL2tpTunnelStatusLastCause_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 27),
    _AccL2tpTunnelStatusLastCause_Type()
)
accL2tpTunnelStatusLastCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusLastCause.setStatus("mandatory")
_AccL2tpTunnelStatusNextSendSeq_Type = Integer32
_AccL2tpTunnelStatusNextSendSeq_Object = MibTableColumn
accL2tpTunnelStatusNextSendSeq = _AccL2tpTunnelStatusNextSendSeq_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 28),
    _AccL2tpTunnelStatusNextSendSeq_Type()
)
accL2tpTunnelStatusNextSendSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusNextSendSeq.setStatus("mandatory")
_AccL2tpTunnelStatusNextSendSeqAck_Type = Integer32
_AccL2tpTunnelStatusNextSendSeqAck_Object = MibTableColumn
accL2tpTunnelStatusNextSendSeqAck = _AccL2tpTunnelStatusNextSendSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 29),
    _AccL2tpTunnelStatusNextSendSeqAck_Type()
)
accL2tpTunnelStatusNextSendSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusNextSendSeqAck.setStatus("mandatory")
_AccL2tpTunnelStatusRecvSeq_Type = Integer32
_AccL2tpTunnelStatusRecvSeq_Object = MibTableColumn
accL2tpTunnelStatusRecvSeq = _AccL2tpTunnelStatusRecvSeq_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 30),
    _AccL2tpTunnelStatusRecvSeq_Type()
)
accL2tpTunnelStatusRecvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusRecvSeq.setStatus("mandatory")
_AccL2tpTunnelStatusRecvSeqAck_Type = Integer32
_AccL2tpTunnelStatusRecvSeqAck_Object = MibTableColumn
accL2tpTunnelStatusRecvSeqAck = _AccL2tpTunnelStatusRecvSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 31),
    _AccL2tpTunnelStatusRecvSeqAck_Type()
)
accL2tpTunnelStatusRecvSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusRecvSeqAck.setStatus("mandatory")
_AccL2tpTunnelStatusOutOfSeqs_Type = Counter32
_AccL2tpTunnelStatusOutOfSeqs_Object = MibTableColumn
accL2tpTunnelStatusOutOfSeqs = _AccL2tpTunnelStatusOutOfSeqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 32),
    _AccL2tpTunnelStatusOutOfSeqs_Type()
)
accL2tpTunnelStatusOutOfSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusOutOfSeqs.setStatus("mandatory")
_AccL2tpTunnelStatusOutOfSeqQLen_Type = Gauge32
_AccL2tpTunnelStatusOutOfSeqQLen_Object = MibTableColumn
accL2tpTunnelStatusOutOfSeqQLen = _AccL2tpTunnelStatusOutOfSeqQLen_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 33),
    _AccL2tpTunnelStatusOutOfSeqQLen_Type()
)
accL2tpTunnelStatusOutOfSeqQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusOutOfSeqQLen.setStatus("mandatory")
_AccL2tpTunnelStatusOutOfWindows_Type = Counter32
_AccL2tpTunnelStatusOutOfWindows_Object = MibTableColumn
accL2tpTunnelStatusOutOfWindows = _AccL2tpTunnelStatusOutOfWindows_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 34),
    _AccL2tpTunnelStatusOutOfWindows_Type()
)
accL2tpTunnelStatusOutOfWindows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusOutOfWindows.setStatus("mandatory")
_AccL2tpTunnelStatusInDiscards_Type = Counter32
_AccL2tpTunnelStatusInDiscards_Object = MibTableColumn
accL2tpTunnelStatusInDiscards = _AccL2tpTunnelStatusInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 35),
    _AccL2tpTunnelStatusInDiscards_Type()
)
accL2tpTunnelStatusInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusInDiscards.setStatus("mandatory")
_AccL2tpTunnelStatusOutDiscards_Type = Counter32
_AccL2tpTunnelStatusOutDiscards_Object = MibTableColumn
accL2tpTunnelStatusOutDiscards = _AccL2tpTunnelStatusOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 3, 1, 36),
    _AccL2tpTunnelStatusOutDiscards_Type()
)
accL2tpTunnelStatusOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTunnelStatusOutDiscards.setStatus("mandatory")
_AccL2tpSessionTable_Object = MibTable
accL2tpSessionTable = _AccL2tpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5)
)
if mibBuilder.loadTexts:
    accL2tpSessionTable.setStatus("mandatory")
_AccL2tpSessionEntry_Object = MibTableRow
accL2tpSessionEntry = _AccL2tpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1)
)
accL2tpSessionEntry.setIndexNames(
    (0, "ACC-L2TP", "accL2tpSessionTunnelIfIndex"),
    (0, "ACC-L2TP", "accL2tpSessionLocalCallId"),
)
if mibBuilder.loadTexts:
    accL2tpSessionEntry.setStatus("mandatory")


class _AccL2tpSessionTunnelIfIndex_Type(Integer32):
    """Custom type accL2tpSessionTunnelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AccL2tpSessionTunnelIfIndex_Type.__name__ = "Integer32"
_AccL2tpSessionTunnelIfIndex_Object = MibTableColumn
accL2tpSessionTunnelIfIndex = _AccL2tpSessionTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 1),
    _AccL2tpSessionTunnelIfIndex_Type()
)
accL2tpSessionTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionTunnelIfIndex.setStatus("mandatory")


class _AccL2tpSessionCallType_Type(Integer32):
    """Custom type accL2tpSessionCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_AccL2tpSessionCallType_Type.__name__ = "Integer32"
_AccL2tpSessionCallType_Object = MibTableColumn
accL2tpSessionCallType = _AccL2tpSessionCallType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 2),
    _AccL2tpSessionCallType_Type()
)
accL2tpSessionCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionCallType.setStatus("mandatory")


class _AccL2tpSessionLocalCallId_Type(Integer32):
    """Custom type accL2tpSessionLocalCallId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccL2tpSessionLocalCallId_Type.__name__ = "Integer32"
_AccL2tpSessionLocalCallId_Object = MibTableColumn
accL2tpSessionLocalCallId = _AccL2tpSessionLocalCallId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 3),
    _AccL2tpSessionLocalCallId_Type()
)
accL2tpSessionLocalCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionLocalCallId.setStatus("mandatory")


class _AccL2tpSessionRemoteCallId_Type(Integer32):
    """Custom type accL2tpSessionRemoteCallId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccL2tpSessionRemoteCallId_Type.__name__ = "Integer32"
_AccL2tpSessionRemoteCallId_Object = MibTableColumn
accL2tpSessionRemoteCallId = _AccL2tpSessionRemoteCallId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 4),
    _AccL2tpSessionRemoteCallId_Type()
)
accL2tpSessionRemoteCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionRemoteCallId.setStatus("mandatory")
_AccL2tpSessionCallSerialId_Type = DisplayString
_AccL2tpSessionCallSerialId_Object = MibTableColumn
accL2tpSessionCallSerialId = _AccL2tpSessionCallSerialId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 5),
    _AccL2tpSessionCallSerialId_Type()
)
accL2tpSessionCallSerialId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionCallSerialId.setStatus("mandatory")
_AccL2tpSessionRemoteHostName_Type = DisplayString
_AccL2tpSessionRemoteHostName_Object = MibTableColumn
accL2tpSessionRemoteHostName = _AccL2tpSessionRemoteHostName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 6),
    _AccL2tpSessionRemoteHostName_Type()
)
accL2tpSessionRemoteHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionRemoteHostName.setStatus("mandatory")


class _AccL2tpSessionPhysChanId_Type(Integer32):
    """Custom type accL2tpSessionPhysChanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccL2tpSessionPhysChanId_Type.__name__ = "Integer32"
_AccL2tpSessionPhysChanId_Object = MibTableColumn
accL2tpSessionPhysChanId = _AccL2tpSessionPhysChanId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 7),
    _AccL2tpSessionPhysChanId_Type()
)
accL2tpSessionPhysChanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionPhysChanId.setStatus("mandatory")


class _AccL2tpSessionBearerCap_Type(Integer32):
    """Custom type accL2tpSessionBearerCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog", 2),
          ("digital", 1))
    )


_AccL2tpSessionBearerCap_Type.__name__ = "Integer32"
_AccL2tpSessionBearerCap_Object = MibTableColumn
accL2tpSessionBearerCap = _AccL2tpSessionBearerCap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 8),
    _AccL2tpSessionBearerCap_Type()
)
accL2tpSessionBearerCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionBearerCap.setStatus("mandatory")


class _AccL2tpSessionFramingCap_Type(Integer32):
    """Custom type accL2tpSessionFramingCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("async", 2),
          ("sync", 1))
    )


_AccL2tpSessionFramingCap_Type.__name__ = "Integer32"
_AccL2tpSessionFramingCap_Object = MibTableColumn
accL2tpSessionFramingCap = _AccL2tpSessionFramingCap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 9),
    _AccL2tpSessionFramingCap_Type()
)
accL2tpSessionFramingCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionFramingCap.setStatus("mandatory")


class _AccL2tpSessionConnectSpeed_Type(Integer32):
    """Custom type accL2tpSessionConnectSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AccL2tpSessionConnectSpeed_Type.__name__ = "Integer32"
_AccL2tpSessionConnectSpeed_Object = MibTableColumn
accL2tpSessionConnectSpeed = _AccL2tpSessionConnectSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 10),
    _AccL2tpSessionConnectSpeed_Type()
)
accL2tpSessionConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionConnectSpeed.setStatus("mandatory")


class _AccL2tpSessionDNIS_Type(DisplayString):
    """Custom type accL2tpSessionDNIS based on DisplayString"""
    defaultValue = OctetString("N/A")


_AccL2tpSessionDNIS_Object = MibTableColumn
accL2tpSessionDNIS = _AccL2tpSessionDNIS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 11),
    _AccL2tpSessionDNIS_Type()
)
accL2tpSessionDNIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionDNIS.setStatus("mandatory")


class _AccL2tpSessionCLID_Type(DisplayString):
    """Custom type accL2tpSessionCLID based on DisplayString"""
    defaultValue = OctetString("N/A")


_AccL2tpSessionCLID_Object = MibTableColumn
accL2tpSessionCLID = _AccL2tpSessionCLID_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 12),
    _AccL2tpSessionCLID_Type()
)
accL2tpSessionCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionCLID.setStatus("mandatory")
_AccL2tpSessionSubAddress_Type = DisplayString
_AccL2tpSessionSubAddress_Object = MibTableColumn
accL2tpSessionSubAddress = _AccL2tpSessionSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 13),
    _AccL2tpSessionSubAddress_Type()
)
accL2tpSessionSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionSubAddress.setStatus("mandatory")


class _AccL2tpSessionRemoteRWS_Type(Integer32):
    """Custom type accL2tpSessionRemoteRWS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccL2tpSessionRemoteRWS_Type.__name__ = "Integer32"
_AccL2tpSessionRemoteRWS_Object = MibTableColumn
accL2tpSessionRemoteRWS = _AccL2tpSessionRemoteRWS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 14),
    _AccL2tpSessionRemoteRWS_Type()
)
accL2tpSessionRemoteRWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionRemoteRWS.setStatus("mandatory")


class _AccL2tpSessionRemotePPD_Type(Integer32):
    """Custom type accL2tpSessionRemotePPD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccL2tpSessionRemotePPD_Type.__name__ = "Integer32"
_AccL2tpSessionRemotePPD_Object = MibTableColumn
accL2tpSessionRemotePPD = _AccL2tpSessionRemotePPD_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 15),
    _AccL2tpSessionRemotePPD_Type()
)
accL2tpSessionRemotePPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionRemotePPD.setStatus("mandatory")


class _AccL2tpSessionProxyPpp_Type(Integer32):
    """Custom type accL2tpSessionProxyPpp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccL2tpSessionProxyPpp_Type.__name__ = "Integer32"
_AccL2tpSessionProxyPpp_Object = MibTableColumn
accL2tpSessionProxyPpp = _AccL2tpSessionProxyPpp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 16),
    _AccL2tpSessionProxyPpp_Type()
)
accL2tpSessionProxyPpp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionProxyPpp.setStatus("mandatory")


class _AccL2tpSessionAuthMethod_Type(Integer32):
    """Custom type accL2tpSessionAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 3),
          ("none", 1),
          ("pap", 2))
    )


_AccL2tpSessionAuthMethod_Type.__name__ = "Integer32"
_AccL2tpSessionAuthMethod_Object = MibTableColumn
accL2tpSessionAuthMethod = _AccL2tpSessionAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 17),
    _AccL2tpSessionAuthMethod_Type()
)
accL2tpSessionAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionAuthMethod.setStatus("mandatory")


class _AccL2tpSessionState_Type(Integer32):
    """Custom type accL2tpSessionState based on Integer32"""
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
        *(("established", 5),
          ("idle", 1),
          ("waitconn", 4),
          ("waitnotify", 6),
          ("waitreply", 3),
          ("waittunnel", 2))
    )


_AccL2tpSessionState_Type.__name__ = "Integer32"
_AccL2tpSessionState_Object = MibTableColumn
accL2tpSessionState = _AccL2tpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 18),
    _AccL2tpSessionState_Type()
)
accL2tpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionState.setStatus("mandatory")


class _AccL2tpSessionLocalPort_Type(Integer32):
    """Custom type accL2tpSessionLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccL2tpSessionLocalPort_Type.__name__ = "Integer32"
_AccL2tpSessionLocalPort_Object = MibTableColumn
accL2tpSessionLocalPort = _AccL2tpSessionLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 5, 1, 19),
    _AccL2tpSessionLocalPort_Type()
)
accL2tpSessionLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionLocalPort.setStatus("mandatory")
_AccL2tpSessionStatusTable_Object = MibTable
accL2tpSessionStatusTable = _AccL2tpSessionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6)
)
if mibBuilder.loadTexts:
    accL2tpSessionStatusTable.setStatus("mandatory")
_AccL2tpSessionStatusEntry_Object = MibTableRow
accL2tpSessionStatusEntry = _AccL2tpSessionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1)
)
accL2tpSessionStatusEntry.setIndexNames(
    (0, "ACC-L2TP", "accL2tpSessionStatusTunnelIfIndex"),
    (0, "ACC-L2TP", "accL2tpSessionStatusLocalCallId"),
)
if mibBuilder.loadTexts:
    accL2tpSessionStatusEntry.setStatus("mandatory")


class _AccL2tpSessionStatusTunnelIfIndex_Type(Integer32):
    """Custom type accL2tpSessionStatusTunnelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AccL2tpSessionStatusTunnelIfIndex_Type.__name__ = "Integer32"
_AccL2tpSessionStatusTunnelIfIndex_Object = MibTableColumn
accL2tpSessionStatusTunnelIfIndex = _AccL2tpSessionStatusTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 1),
    _AccL2tpSessionStatusTunnelIfIndex_Type()
)
accL2tpSessionStatusTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusTunnelIfIndex.setStatus("mandatory")


class _AccL2tpSessionStatusLocalCallId_Type(Integer32):
    """Custom type accL2tpSessionStatusLocalCallId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccL2tpSessionStatusLocalCallId_Type.__name__ = "Integer32"
_AccL2tpSessionStatusLocalCallId_Object = MibTableColumn
accL2tpSessionStatusLocalCallId = _AccL2tpSessionStatusLocalCallId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 2),
    _AccL2tpSessionStatusLocalCallId_Type()
)
accL2tpSessionStatusLocalCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusLocalCallId.setStatus("mandatory")
_AccL2tpSessionStatusInDiscards_Type = Counter32
_AccL2tpSessionStatusInDiscards_Object = MibTableColumn
accL2tpSessionStatusInDiscards = _AccL2tpSessionStatusInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 3),
    _AccL2tpSessionStatusInDiscards_Type()
)
accL2tpSessionStatusInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusInDiscards.setStatus("mandatory")
_AccL2tpSessionStatusTxSequenceResets_Type = Counter32
_AccL2tpSessionStatusTxSequenceResets_Object = MibTableColumn
accL2tpSessionStatusTxSequenceResets = _AccL2tpSessionStatusTxSequenceResets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 4),
    _AccL2tpSessionStatusTxSequenceResets_Type()
)
accL2tpSessionStatusTxSequenceResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusTxSequenceResets.setStatus("mandatory")
_AccL2tpSessionStatusCalcRWS_Type = Gauge32
_AccL2tpSessionStatusCalcRWS_Object = MibTableColumn
accL2tpSessionStatusCalcRWS = _AccL2tpSessionStatusCalcRWS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 5),
    _AccL2tpSessionStatusCalcRWS_Type()
)
accL2tpSessionStatusCalcRWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusCalcRWS.setStatus("mandatory")
_AccL2tpSessionStatusTxQueueLength_Type = Gauge32
_AccL2tpSessionStatusTxQueueLength_Object = MibTableColumn
accL2tpSessionStatusTxQueueLength = _AccL2tpSessionStatusTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 6),
    _AccL2tpSessionStatusTxQueueLength_Type()
)
accL2tpSessionStatusTxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusTxQueueLength.setStatus("mandatory")
_AccL2tpSessionStatusNextSendSeq_Type = Integer32
_AccL2tpSessionStatusNextSendSeq_Object = MibTableColumn
accL2tpSessionStatusNextSendSeq = _AccL2tpSessionStatusNextSendSeq_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 7),
    _AccL2tpSessionStatusNextSendSeq_Type()
)
accL2tpSessionStatusNextSendSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusNextSendSeq.setStatus("mandatory")
_AccL2tpSessionStatusNextSendSeqAck_Type = Integer32
_AccL2tpSessionStatusNextSendSeqAck_Object = MibTableColumn
accL2tpSessionStatusNextSendSeqAck = _AccL2tpSessionStatusNextSendSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 8),
    _AccL2tpSessionStatusNextSendSeqAck_Type()
)
accL2tpSessionStatusNextSendSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusNextSendSeqAck.setStatus("mandatory")
_AccL2tpSessionStatusNextRecvSeq_Type = Integer32
_AccL2tpSessionStatusNextRecvSeq_Object = MibTableColumn
accL2tpSessionStatusNextRecvSeq = _AccL2tpSessionStatusNextRecvSeq_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 9),
    _AccL2tpSessionStatusNextRecvSeq_Type()
)
accL2tpSessionStatusNextRecvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusNextRecvSeq.setStatus("mandatory")
_AccL2tpSessionStatusNextRecvSeqAck_Type = Integer32
_AccL2tpSessionStatusNextRecvSeqAck_Object = MibTableColumn
accL2tpSessionStatusNextRecvSeqAck = _AccL2tpSessionStatusNextRecvSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 10),
    _AccL2tpSessionStatusNextRecvSeqAck_Type()
)
accL2tpSessionStatusNextRecvSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusNextRecvSeqAck.setStatus("mandatory")
_AccL2tpSessionStatusOutOfSeqs_Type = Counter32
_AccL2tpSessionStatusOutOfSeqs_Object = MibTableColumn
accL2tpSessionStatusOutOfSeqs = _AccL2tpSessionStatusOutOfSeqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 11),
    _AccL2tpSessionStatusOutOfSeqs_Type()
)
accL2tpSessionStatusOutOfSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusOutOfSeqs.setStatus("mandatory")
_AccL2tpSessionStatusOutOfSeqQLen_Type = Gauge32
_AccL2tpSessionStatusOutOfSeqQLen_Object = MibTableColumn
accL2tpSessionStatusOutOfSeqQLen = _AccL2tpSessionStatusOutOfSeqQLen_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 12),
    _AccL2tpSessionStatusOutOfSeqQLen_Type()
)
accL2tpSessionStatusOutOfSeqQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusOutOfSeqQLen.setStatus("mandatory")
_AccL2tpSessionStatusTxOctets_Type = Counter32
_AccL2tpSessionStatusTxOctets_Object = MibTableColumn
accL2tpSessionStatusTxOctets = _AccL2tpSessionStatusTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 13),
    _AccL2tpSessionStatusTxOctets_Type()
)
accL2tpSessionStatusTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusTxOctets.setStatus("mandatory")
_AccL2tpSessionStatusTxPackets_Type = Counter32
_AccL2tpSessionStatusTxPackets_Object = MibTableColumn
accL2tpSessionStatusTxPackets = _AccL2tpSessionStatusTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 14),
    _AccL2tpSessionStatusTxPackets_Type()
)
accL2tpSessionStatusTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusTxPackets.setStatus("mandatory")
_AccL2tpSessionStatusRxOctets_Type = Counter32
_AccL2tpSessionStatusRxOctets_Object = MibTableColumn
accL2tpSessionStatusRxOctets = _AccL2tpSessionStatusRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 15),
    _AccL2tpSessionStatusRxOctets_Type()
)
accL2tpSessionStatusRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusRxOctets.setStatus("mandatory")
_AccL2tpSessionStatusRxPackets_Type = Counter32
_AccL2tpSessionStatusRxPackets_Object = MibTableColumn
accL2tpSessionStatusRxPackets = _AccL2tpSessionStatusRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 16),
    _AccL2tpSessionStatusRxPackets_Type()
)
accL2tpSessionStatusRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusRxPackets.setStatus("mandatory")
_AccL2tpSessionStatusOutDiscards_Type = Counter32
_AccL2tpSessionStatusOutDiscards_Object = MibTableColumn
accL2tpSessionStatusOutDiscards = _AccL2tpSessionStatusOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 17),
    _AccL2tpSessionStatusOutDiscards_Type()
)
accL2tpSessionStatusOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusOutDiscards.setStatus("mandatory")
_AccL2tpSessionStatusOutOfWindows_Type = Counter32
_AccL2tpSessionStatusOutOfWindows_Object = MibTableColumn
accL2tpSessionStatusOutOfWindows = _AccL2tpSessionStatusOutOfWindows_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 18),
    _AccL2tpSessionStatusOutOfWindows_Type()
)
accL2tpSessionStatusOutOfWindows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusOutOfWindows.setStatus("mandatory")
_AccL2tpSessionStatusRxSequenceResets_Type = Integer32
_AccL2tpSessionStatusRxSequenceResets_Object = MibTableColumn
accL2tpSessionStatusRxSequenceResets = _AccL2tpSessionStatusRxSequenceResets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 6, 1, 19),
    _AccL2tpSessionStatusRxSequenceResets_Type()
)
accL2tpSessionStatusRxSequenceResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpSessionStatusRxSequenceResets.setStatus("mandatory")
_AccL2tpEndpointDomainTable_Object = MibTable
accL2tpEndpointDomainTable = _AccL2tpEndpointDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 7)
)
if mibBuilder.loadTexts:
    accL2tpEndpointDomainTable.setStatus("mandatory")
_AccL2tpEndpointDomainEntry_Object = MibTableRow
accL2tpEndpointDomainEntry = _AccL2tpEndpointDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 7, 1)
)
accL2tpEndpointDomainEntry.setIndexNames(
    (0, "ACC-L2TP", "accL2tpEndpointDomain"),
)
if mibBuilder.loadTexts:
    accL2tpEndpointDomainEntry.setStatus("mandatory")
_AccL2tpEndpointDomain_Type = DisplayString
_AccL2tpEndpointDomain_Object = MibTableColumn
accL2tpEndpointDomain = _AccL2tpEndpointDomain_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 7, 1, 1),
    _AccL2tpEndpointDomain_Type()
)
accL2tpEndpointDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpEndpointDomain.setStatus("mandatory")
_AccL2tpEndpointDomainSecret_Type = DisplayString
_AccL2tpEndpointDomainSecret_Object = MibTableColumn
accL2tpEndpointDomainSecret = _AccL2tpEndpointDomainSecret_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 7, 1, 2),
    _AccL2tpEndpointDomainSecret_Type()
)
accL2tpEndpointDomainSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpEndpointDomainSecret.setStatus("mandatory")
_AccL2tpEndpointDomainNumberGroup_Type = Integer32
_AccL2tpEndpointDomainNumberGroup_Object = MibTableColumn
accL2tpEndpointDomainNumberGroup = _AccL2tpEndpointDomainNumberGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 7, 1, 3),
    _AccL2tpEndpointDomainNumberGroup_Type()
)
accL2tpEndpointDomainNumberGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpEndpointDomainNumberGroup.setStatus("mandatory")
_AccL2tpEndpointDomainStatus_Type = RowStatus
_AccL2tpEndpointDomainStatus_Object = MibTableColumn
accL2tpEndpointDomainStatus = _AccL2tpEndpointDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 1, 7, 1, 4),
    _AccL2tpEndpointDomainStatus_Type()
)
accL2tpEndpointDomainStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpEndpointDomainStatus.setStatus("mandatory")
_AccL2tpTransport_ObjectIdentity = ObjectIdentity
accL2tpTransport = _AccL2tpTransport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2)
)
_AccL2tpTransportUdp_ObjectIdentity = ObjectIdentity
accL2tpTransportUdp = _AccL2tpTransportUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1)
)
_AccL2tpTransportUdpScalars_ObjectIdentity = ObjectIdentity
accL2tpTransportUdpScalars = _AccL2tpTransportUdpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 1)
)


class _AccL2tpUdpServerPort_Type(Integer32):
    """Custom type accL2tpUdpServerPort based on Integer32"""
    defaultValue = 1701

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccL2tpUdpServerPort_Type.__name__ = "Integer32"
_AccL2tpUdpServerPort_Object = MibScalar
accL2tpUdpServerPort = _AccL2tpUdpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 1, 1),
    _AccL2tpUdpServerPort_Type()
)
accL2tpUdpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpUdpServerPort.setStatus("mandatory")


class _AccL2tpUdpPayloadCksums_Type(Integer32):
    """Custom type accL2tpUdpPayloadCksums based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccL2tpUdpPayloadCksums_Type.__name__ = "Integer32"
_AccL2tpUdpPayloadCksums_Object = MibScalar
accL2tpUdpPayloadCksums = _AccL2tpUdpPayloadCksums_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 1, 2),
    _AccL2tpUdpPayloadCksums_Type()
)
accL2tpUdpPayloadCksums.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpUdpPayloadCksums.setStatus("mandatory")


class _AccL2tpUdpFixedAddress_Type(Integer32):
    """Custom type accL2tpUdpFixedAddress based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccL2tpUdpFixedAddress_Type.__name__ = "Integer32"
_AccL2tpUdpFixedAddress_Object = MibScalar
accL2tpUdpFixedAddress = _AccL2tpUdpFixedAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 1, 3),
    _AccL2tpUdpFixedAddress_Type()
)
accL2tpUdpFixedAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpUdpFixedAddress.setStatus("mandatory")
_AccL2tpUdpSrcIpAddress_Type = IpAddress
_AccL2tpUdpSrcIpAddress_Object = MibScalar
accL2tpUdpSrcIpAddress = _AccL2tpUdpSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 1, 4),
    _AccL2tpUdpSrcIpAddress_Type()
)
accL2tpUdpSrcIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpUdpSrcIpAddress.setStatus("mandatory")
_AccL2tpUdpStatsRsrcFails_Type = Counter32
_AccL2tpUdpStatsRsrcFails_Object = MibScalar
accL2tpUdpStatsRsrcFails = _AccL2tpUdpStatsRsrcFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 1, 5),
    _AccL2tpUdpStatsRsrcFails_Type()
)
accL2tpUdpStatsRsrcFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpUdpStatsRsrcFails.setStatus("mandatory")
_AccL2tpUdpStatsInDiscards_Type = Counter32
_AccL2tpUdpStatsInDiscards_Object = MibScalar
accL2tpUdpStatsInDiscards = _AccL2tpUdpStatsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 1, 6),
    _AccL2tpUdpStatsInDiscards_Type()
)
accL2tpUdpStatsInDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpUdpStatsInDiscards.setStatus("mandatory")
_AccL2tpUdpStatsUnknownTIDs_Type = Counter32
_AccL2tpUdpStatsUnknownTIDs_Object = MibScalar
accL2tpUdpStatsUnknownTIDs = _AccL2tpUdpStatsUnknownTIDs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 1, 7),
    _AccL2tpUdpStatsUnknownTIDs_Type()
)
accL2tpUdpStatsUnknownTIDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpUdpStatsUnknownTIDs.setStatus("mandatory")
_AccL2tpUdpTransportTable_Object = MibTable
accL2tpUdpTransportTable = _AccL2tpUdpTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 2)
)
if mibBuilder.loadTexts:
    accL2tpUdpTransportTable.setStatus("mandatory")
_AccL2tpUdpTransportEntry_Object = MibTableRow
accL2tpUdpTransportEntry = _AccL2tpUdpTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 2, 1)
)
accL2tpUdpTransportEntry.setIndexNames(
    (0, "ACC-L2TP", "accL2tpUdpTransportTunnelIfIndex"),
)
if mibBuilder.loadTexts:
    accL2tpUdpTransportEntry.setStatus("mandatory")


class _AccL2tpUdpTransportTunnelIfIndex_Type(Integer32):
    """Custom type accL2tpUdpTransportTunnelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AccL2tpUdpTransportTunnelIfIndex_Type.__name__ = "Integer32"
_AccL2tpUdpTransportTunnelIfIndex_Object = MibTableColumn
accL2tpUdpTransportTunnelIfIndex = _AccL2tpUdpTransportTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 2, 1, 1),
    _AccL2tpUdpTransportTunnelIfIndex_Type()
)
accL2tpUdpTransportTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpUdpTransportTunnelIfIndex.setStatus("mandatory")
_AccL2tpUdpTransportEndpointIpAddress_Type = IpAddress
_AccL2tpUdpTransportEndpointIpAddress_Object = MibTableColumn
accL2tpUdpTransportEndpointIpAddress = _AccL2tpUdpTransportEndpointIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 2, 1, 2),
    _AccL2tpUdpTransportEndpointIpAddress_Type()
)
accL2tpUdpTransportEndpointIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpUdpTransportEndpointIpAddress.setStatus("mandatory")


class _AccL2tpUdpTransportPort_Type(Integer32):
    """Custom type accL2tpUdpTransportPort based on Integer32"""
    defaultValue = 1701

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccL2tpUdpTransportPort_Type.__name__ = "Integer32"
_AccL2tpUdpTransportPort_Object = MibTableColumn
accL2tpUdpTransportPort = _AccL2tpUdpTransportPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 2, 1, 3),
    _AccL2tpUdpTransportPort_Type()
)
accL2tpUdpTransportPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpUdpTransportPort.setStatus("mandatory")


class _AccL2tpUdpTransportPayloadCksum_Type(Integer32):
    """Custom type accL2tpUdpTransportPayloadCksum based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccL2tpUdpTransportPayloadCksum_Type.__name__ = "Integer32"
_AccL2tpUdpTransportPayloadCksum_Object = MibTableColumn
accL2tpUdpTransportPayloadCksum = _AccL2tpUdpTransportPayloadCksum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 2, 1, 4),
    _AccL2tpUdpTransportPayloadCksum_Type()
)
accL2tpUdpTransportPayloadCksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpUdpTransportPayloadCksum.setStatus("mandatory")


class _AccL2tpUdpTransportFixedAddress_Type(Integer32):
    """Custom type accL2tpUdpTransportFixedAddress based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccL2tpUdpTransportFixedAddress_Type.__name__ = "Integer32"
_AccL2tpUdpTransportFixedAddress_Object = MibTableColumn
accL2tpUdpTransportFixedAddress = _AccL2tpUdpTransportFixedAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 2, 1, 5),
    _AccL2tpUdpTransportFixedAddress_Type()
)
accL2tpUdpTransportFixedAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpUdpTransportFixedAddress.setStatus("mandatory")
_AccL2tpUdpTransportStatus_Type = RowStatus
_AccL2tpUdpTransportStatus_Object = MibTableColumn
accL2tpUdpTransportStatus = _AccL2tpUdpTransportStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 2, 1, 6),
    _AccL2tpUdpTransportStatus_Type()
)
accL2tpUdpTransportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accL2tpUdpTransportStatus.setStatus("mandatory")
_AccL2tpUdpConnectionTable_Object = MibTable
accL2tpUdpConnectionTable = _AccL2tpUdpConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 3)
)
if mibBuilder.loadTexts:
    accL2tpUdpConnectionTable.setStatus("mandatory")
_AccL2tpUdpConnectionEntry_Object = MibTableRow
accL2tpUdpConnectionEntry = _AccL2tpUdpConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 3, 1)
)
accL2tpUdpConnectionEntry.setIndexNames(
    (0, "ACC-L2TP", "accL2tpUdpConnectionTunnelIfIndex"),
)
if mibBuilder.loadTexts:
    accL2tpUdpConnectionEntry.setStatus("mandatory")


class _AccL2tpUdpConnectionTunnelIfIndex_Type(Integer32):
    """Custom type accL2tpUdpConnectionTunnelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AccL2tpUdpConnectionTunnelIfIndex_Type.__name__ = "Integer32"
_AccL2tpUdpConnectionTunnelIfIndex_Object = MibTableColumn
accL2tpUdpConnectionTunnelIfIndex = _AccL2tpUdpConnectionTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 3, 1, 1),
    _AccL2tpUdpConnectionTunnelIfIndex_Type()
)
accL2tpUdpConnectionTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpUdpConnectionTunnelIfIndex.setStatus("mandatory")
_AccL2tpUdpConnectionEndpointIpAddress_Type = IpAddress
_AccL2tpUdpConnectionEndpointIpAddress_Object = MibTableColumn
accL2tpUdpConnectionEndpointIpAddress = _AccL2tpUdpConnectionEndpointIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 3, 1, 2),
    _AccL2tpUdpConnectionEndpointIpAddress_Type()
)
accL2tpUdpConnectionEndpointIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpUdpConnectionEndpointIpAddress.setStatus("mandatory")


class _AccL2tpUdpConnectionRxPort_Type(Integer32):
    """Custom type accL2tpUdpConnectionRxPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccL2tpUdpConnectionRxPort_Type.__name__ = "Integer32"
_AccL2tpUdpConnectionRxPort_Object = MibTableColumn
accL2tpUdpConnectionRxPort = _AccL2tpUdpConnectionRxPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 3, 1, 3),
    _AccL2tpUdpConnectionRxPort_Type()
)
accL2tpUdpConnectionRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpUdpConnectionRxPort.setStatus("mandatory")


class _AccL2tpUdpConnectionTxPort_Type(Integer32):
    """Custom type accL2tpUdpConnectionTxPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccL2tpUdpConnectionTxPort_Type.__name__ = "Integer32"
_AccL2tpUdpConnectionTxPort_Object = MibTableColumn
accL2tpUdpConnectionTxPort = _AccL2tpUdpConnectionTxPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 3, 1, 4),
    _AccL2tpUdpConnectionTxPort_Type()
)
accL2tpUdpConnectionTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpUdpConnectionTxPort.setStatus("mandatory")
_AccL2tpUdpConnectionAddressChanges_Type = Counter32
_AccL2tpUdpConnectionAddressChanges_Object = MibTableColumn
accL2tpUdpConnectionAddressChanges = _AccL2tpUdpConnectionAddressChanges_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 3, 1, 5),
    _AccL2tpUdpConnectionAddressChanges_Type()
)
accL2tpUdpConnectionAddressChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpUdpConnectionAddressChanges.setStatus("mandatory")
_AccL2tpTraps_ObjectIdentity = ObjectIdentity
accL2tpTraps = _AccL2tpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 4)
)
_AccL2tpTrapMsg_Type = DisplayString
_AccL2tpTrapMsg_Object = MibScalar
accL2tpTrapMsg = _AccL2tpTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 4, 1),
    _AccL2tpTrapMsg_Type()
)
accL2tpTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accL2tpTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accL2tpTunnelDelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 4, 0, 1)
)
accL2tpTunnelDelTrap.setObjects(
      *(("ACC-L2TP", "accL2tpTrapMsg"),
        ("ACC-L2TP", "accL2tpSessionLocalCallId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accL2tpTunnelDelTrap.setStatus(
        ""
    )

accL2tpTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 4, 0, 2)
)
accL2tpTrap2.setObjects(
      *(("ACC-L2TP", "accL2tpTrapMsg"),
        ("ACC-L2TP", "accL2tpUdpTransportTunnelIfIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accL2tpTrap2.setStatus(
        ""
    )

accL2tpUdpEpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 4, 0, 3)
)
accL2tpUdpEpTrap.setObjects(
      *(("ACC-L2TP", "accL2tpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accL2tpUdpEpTrap.setStatus(
        ""
    )

accL2tpUdpEpCreateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 4, 0, 4)
)
accL2tpUdpEpCreateTrap.setObjects(
      *(("ACC-L2TP", "accL2tpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accL2tpUdpEpCreateTrap.setStatus(
        ""
    )

accL2tpTunnelCreateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 4, 0, 5)
)
accL2tpTunnelCreateTrap.setObjects(
      *(("ACC-L2TP", "accL2tpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accL2tpTunnelCreateTrap.setStatus(
        ""
    )

accL2tpInvIntfAddrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 4, 0, 6)
)
accL2tpInvIntfAddrTrap.setObjects(
      *(("ACC-L2TP", "accL2tpTrapMsg"),
        ("ACC-L2TP", "accL2tpUdpSrcIpAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accL2tpInvIntfAddrTrap.setStatus(
        ""
    )

accL2tpTunnelAbortCleanUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 4, 0, 7)
)
accL2tpTunnelAbortCleanUpTrap.setObjects(
      *(("ACC-L2TP", "accL2tpTrapMsg"),
        ("ACC-L2TP", "accL2tpTunnelStatusTunnelState"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accL2tpTunnelAbortCleanUpTrap.setStatus(
        ""
    )

accL2tpTrap8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 4, 0, 8)
)
accL2tpTrap8.setObjects(
      *(("ACC-L2TP", "accL2tpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accL2tpTrap8.setStatus(
        ""
    )

accL2tpUdpServTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 4, 0, 9)
)
accL2tpUdpServTrap.setObjects(
      *(("ACC-L2TP", "accL2tpTrapMsg"),
        ("ACC-L2TP", "accL2tpUdpTransportEndpointIpAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accL2tpUdpServTrap.setStatus(
        ""
    )

accL2tpTrap10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 71, 2, 1, 4, 0, 10)
)
accL2tpTrap10.setObjects(
      *(("ACC-L2TP", "accL2tpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accL2tpTrap10.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-L2TP",
    **{"accL2tp": accL2tp,
       "accL2tpGeneral": accL2tpGeneral,
       "accL2tpGeneralScalars": accL2tpGeneralScalars,
       "accL2tpVendorName": accL2tpVendorName,
       "accL2tpFirmwareRev": accL2tpFirmwareRev,
       "accL2pAdminState": accL2pAdminState,
       "accL2tpProtocolVersion": accL2tpProtocolVersion,
       "accL2tpControlRWS": accL2tpControlRWS,
       "accL2tpPayloadSeq": accL2tpPayloadSeq,
       "accL2tpPayloadRWS": accL2tpPayloadRWS,
       "accL2tpKeepAlive": accL2tpKeepAlive,
       "accL2tpMaxAckTimeout": accL2tpMaxAckTimeout,
       "accL2tpMaxRetrans": accL2tpMaxRetrans,
       "accL2tpIdleDisconnect": accL2tpIdleDisconnect,
       "accL2tpTunnelAuthentication": accL2tpTunnelAuthentication,
       "accL2tpKeyDistribution": accL2tpKeyDistribution,
       "accL2tpProxyAuthentication": accL2tpProxyAuthentication,
       "accL2tpServerState": accL2tpServerState,
       "accL2tpMessageLevel": accL2tpMessageLevel,
       "accL2tpDebugMask": accL2tpDebugMask,
       "accL2tpPayLoadLength": accL2tpPayLoadLength,
       "accL2tpAttributeHiding": accL2tpAttributeHiding,
       "accL2tpCallConfirm": accL2tpCallConfirm,
       "accL2tpTunnelConfigTable": accL2tpTunnelConfigTable,
       "accL2tpTunnelConfigEntry": accL2tpTunnelConfigEntry,
       "accL2tpTunnelConfigTunnelIfIndex": accL2tpTunnelConfigTunnelIfIndex,
       "accL2tpTunnelConfigControlRWS": accL2tpTunnelConfigControlRWS,
       "accL2tpTunnelConfigPayloadSeq": accL2tpTunnelConfigPayloadSeq,
       "accL2tpTunnelConfigPayloadRWS": accL2tpTunnelConfigPayloadRWS,
       "accL2tpTunnelConfigKeepAlive": accL2tpTunnelConfigKeepAlive,
       "accL2tpTunnelConfigMaxAckTimeout": accL2tpTunnelConfigMaxAckTimeout,
       "accL2tpTunnelConfigMaxRetrans": accL2tpTunnelConfigMaxRetrans,
       "accL2tpTunnelConfigIdleDisconnect": accL2tpTunnelConfigIdleDisconnect,
       "accL2tpTunnelConfigTransportMech": accL2tpTunnelConfigTransportMech,
       "accL2tpTunnelConfigTunnelAuthentication": accL2tpTunnelConfigTunnelAuthentication,
       "accL2tpTunnelConfigProxyAuthentication": accL2tpTunnelConfigProxyAuthentication,
       "accL2tpTunnelConfigMessageLevel": accL2tpTunnelConfigMessageLevel,
       "accL2tpTunnelConfigDebugMask": accL2tpTunnelConfigDebugMask,
       "accL2tpTunnelConfigPayLoadLength": accL2tpTunnelConfigPayLoadLength,
       "accL2tpTunnelConfigAttributeHiding": accL2tpTunnelConfigAttributeHiding,
       "accL2tpTunnelConfigCallConfirm": accL2tpTunnelConfigCallConfirm,
       "accL2tpTunnelConfigEvents": accL2tpTunnelConfigEvents,
       "accL2tpTunnelConfigCreate": accL2tpTunnelConfigCreate,
       "accL2tpTunnelConfigStatus": accL2tpTunnelConfigStatus,
       "accL2tpTunnelStatusTable": accL2tpTunnelStatusTable,
       "accL2tpTunnelStatusEntry": accL2tpTunnelStatusEntry,
       "accL2tpTunnelStatusTunnelIfIndex": accL2tpTunnelStatusTunnelIfIndex,
       "accL2tpTunnelStatusLocalTunnelId": accL2tpTunnelStatusLocalTunnelId,
       "accL2tpTunnelStatusRemTunnelId": accL2tpTunnelStatusRemTunnelId,
       "accL2tpTunnelStatusRemFraming": accL2tpTunnelStatusRemFraming,
       "accL2tpTunnelStatusRemBearerCap": accL2tpTunnelStatusRemBearerCap,
       "accL2tpTunnelStatusRemControlRWS": accL2tpTunnelStatusRemControlRWS,
       "accL2tpTunnelStatusRemKeepAlive": accL2tpTunnelStatusRemKeepAlive,
       "accL2tpTunnelStatusRemVendorName": accL2tpTunnelStatusRemVendorName,
       "accL2tpTunnelStatusRemFirmRev": accL2tpTunnelStatusRemFirmRev,
       "accL2tpTunnelStatusRemHostName": accL2tpTunnelStatusRemHostName,
       "accL2tpTunnelStatusRemProtocolVer": accL2tpTunnelStatusRemProtocolVer,
       "accL2tpTunnelStatusTunnelState": accL2tpTunnelStatusTunnelState,
       "accL2tpTunnelStatusKeepAlive": accL2tpTunnelStatusKeepAlive,
       "accL2tpTunnelStatusCalcRemRWS": accL2tpTunnelStatusCalcRemRWS,
       "accL2tpTunnelStatusCalcRemRetransTimeout": accL2tpTunnelStatusCalcRemRetransTimeout,
       "accL2tpTunnelStatusQueueLength": accL2tpTunnelStatusQueueLength,
       "accL2tpTunnelStatusTxOctets": accL2tpTunnelStatusTxOctets,
       "accL2tpTunnelStatusTxPackets": accL2tpTunnelStatusTxPackets,
       "accL2tpTunnelStatusRxOctets": accL2tpTunnelStatusRxOctets,
       "accL2tpTunnelStatusRxPackets": accL2tpTunnelStatusRxPackets,
       "accL2tpTunnelStatusTotalSessions": accL2tpTunnelStatusTotalSessions,
       "accL2tpTunnelStatusActiveSessions": accL2tpTunnelStatusActiveSessions,
       "accL2tpTunnelStatusAttemptFails": accL2tpTunnelStatusAttemptFails,
       "accL2tpTunnelStatusRetransTimeouts": accL2tpTunnelStatusRetransTimeouts,
       "accL2tpTunnelStatusBackwardTransitions": accL2tpTunnelStatusBackwardTransitions,
       "accL2tpTunnelStatusLastTransitions": accL2tpTunnelStatusLastTransitions,
       "accL2tpTunnelStatusLastCause": accL2tpTunnelStatusLastCause,
       "accL2tpTunnelStatusNextSendSeq": accL2tpTunnelStatusNextSendSeq,
       "accL2tpTunnelStatusNextSendSeqAck": accL2tpTunnelStatusNextSendSeqAck,
       "accL2tpTunnelStatusRecvSeq": accL2tpTunnelStatusRecvSeq,
       "accL2tpTunnelStatusRecvSeqAck": accL2tpTunnelStatusRecvSeqAck,
       "accL2tpTunnelStatusOutOfSeqs": accL2tpTunnelStatusOutOfSeqs,
       "accL2tpTunnelStatusOutOfSeqQLen": accL2tpTunnelStatusOutOfSeqQLen,
       "accL2tpTunnelStatusOutOfWindows": accL2tpTunnelStatusOutOfWindows,
       "accL2tpTunnelStatusInDiscards": accL2tpTunnelStatusInDiscards,
       "accL2tpTunnelStatusOutDiscards": accL2tpTunnelStatusOutDiscards,
       "accL2tpSessionTable": accL2tpSessionTable,
       "accL2tpSessionEntry": accL2tpSessionEntry,
       "accL2tpSessionTunnelIfIndex": accL2tpSessionTunnelIfIndex,
       "accL2tpSessionCallType": accL2tpSessionCallType,
       "accL2tpSessionLocalCallId": accL2tpSessionLocalCallId,
       "accL2tpSessionRemoteCallId": accL2tpSessionRemoteCallId,
       "accL2tpSessionCallSerialId": accL2tpSessionCallSerialId,
       "accL2tpSessionRemoteHostName": accL2tpSessionRemoteHostName,
       "accL2tpSessionPhysChanId": accL2tpSessionPhysChanId,
       "accL2tpSessionBearerCap": accL2tpSessionBearerCap,
       "accL2tpSessionFramingCap": accL2tpSessionFramingCap,
       "accL2tpSessionConnectSpeed": accL2tpSessionConnectSpeed,
       "accL2tpSessionDNIS": accL2tpSessionDNIS,
       "accL2tpSessionCLID": accL2tpSessionCLID,
       "accL2tpSessionSubAddress": accL2tpSessionSubAddress,
       "accL2tpSessionRemoteRWS": accL2tpSessionRemoteRWS,
       "accL2tpSessionRemotePPD": accL2tpSessionRemotePPD,
       "accL2tpSessionProxyPpp": accL2tpSessionProxyPpp,
       "accL2tpSessionAuthMethod": accL2tpSessionAuthMethod,
       "accL2tpSessionState": accL2tpSessionState,
       "accL2tpSessionLocalPort": accL2tpSessionLocalPort,
       "accL2tpSessionStatusTable": accL2tpSessionStatusTable,
       "accL2tpSessionStatusEntry": accL2tpSessionStatusEntry,
       "accL2tpSessionStatusTunnelIfIndex": accL2tpSessionStatusTunnelIfIndex,
       "accL2tpSessionStatusLocalCallId": accL2tpSessionStatusLocalCallId,
       "accL2tpSessionStatusInDiscards": accL2tpSessionStatusInDiscards,
       "accL2tpSessionStatusTxSequenceResets": accL2tpSessionStatusTxSequenceResets,
       "accL2tpSessionStatusCalcRWS": accL2tpSessionStatusCalcRWS,
       "accL2tpSessionStatusTxQueueLength": accL2tpSessionStatusTxQueueLength,
       "accL2tpSessionStatusNextSendSeq": accL2tpSessionStatusNextSendSeq,
       "accL2tpSessionStatusNextSendSeqAck": accL2tpSessionStatusNextSendSeqAck,
       "accL2tpSessionStatusNextRecvSeq": accL2tpSessionStatusNextRecvSeq,
       "accL2tpSessionStatusNextRecvSeqAck": accL2tpSessionStatusNextRecvSeqAck,
       "accL2tpSessionStatusOutOfSeqs": accL2tpSessionStatusOutOfSeqs,
       "accL2tpSessionStatusOutOfSeqQLen": accL2tpSessionStatusOutOfSeqQLen,
       "accL2tpSessionStatusTxOctets": accL2tpSessionStatusTxOctets,
       "accL2tpSessionStatusTxPackets": accL2tpSessionStatusTxPackets,
       "accL2tpSessionStatusRxOctets": accL2tpSessionStatusRxOctets,
       "accL2tpSessionStatusRxPackets": accL2tpSessionStatusRxPackets,
       "accL2tpSessionStatusOutDiscards": accL2tpSessionStatusOutDiscards,
       "accL2tpSessionStatusOutOfWindows": accL2tpSessionStatusOutOfWindows,
       "accL2tpSessionStatusRxSequenceResets": accL2tpSessionStatusRxSequenceResets,
       "accL2tpEndpointDomainTable": accL2tpEndpointDomainTable,
       "accL2tpEndpointDomainEntry": accL2tpEndpointDomainEntry,
       "accL2tpEndpointDomain": accL2tpEndpointDomain,
       "accL2tpEndpointDomainSecret": accL2tpEndpointDomainSecret,
       "accL2tpEndpointDomainNumberGroup": accL2tpEndpointDomainNumberGroup,
       "accL2tpEndpointDomainStatus": accL2tpEndpointDomainStatus,
       "accL2tpTransport": accL2tpTransport,
       "accL2tpTransportUdp": accL2tpTransportUdp,
       "accL2tpTransportUdpScalars": accL2tpTransportUdpScalars,
       "accL2tpUdpServerPort": accL2tpUdpServerPort,
       "accL2tpUdpPayloadCksums": accL2tpUdpPayloadCksums,
       "accL2tpUdpFixedAddress": accL2tpUdpFixedAddress,
       "accL2tpUdpSrcIpAddress": accL2tpUdpSrcIpAddress,
       "accL2tpUdpStatsRsrcFails": accL2tpUdpStatsRsrcFails,
       "accL2tpUdpStatsInDiscards": accL2tpUdpStatsInDiscards,
       "accL2tpUdpStatsUnknownTIDs": accL2tpUdpStatsUnknownTIDs,
       "accL2tpUdpTransportTable": accL2tpUdpTransportTable,
       "accL2tpUdpTransportEntry": accL2tpUdpTransportEntry,
       "accL2tpUdpTransportTunnelIfIndex": accL2tpUdpTransportTunnelIfIndex,
       "accL2tpUdpTransportEndpointIpAddress": accL2tpUdpTransportEndpointIpAddress,
       "accL2tpUdpTransportPort": accL2tpUdpTransportPort,
       "accL2tpUdpTransportPayloadCksum": accL2tpUdpTransportPayloadCksum,
       "accL2tpUdpTransportFixedAddress": accL2tpUdpTransportFixedAddress,
       "accL2tpUdpTransportStatus": accL2tpUdpTransportStatus,
       "accL2tpUdpConnectionTable": accL2tpUdpConnectionTable,
       "accL2tpUdpConnectionEntry": accL2tpUdpConnectionEntry,
       "accL2tpUdpConnectionTunnelIfIndex": accL2tpUdpConnectionTunnelIfIndex,
       "accL2tpUdpConnectionEndpointIpAddress": accL2tpUdpConnectionEndpointIpAddress,
       "accL2tpUdpConnectionRxPort": accL2tpUdpConnectionRxPort,
       "accL2tpUdpConnectionTxPort": accL2tpUdpConnectionTxPort,
       "accL2tpUdpConnectionAddressChanges": accL2tpUdpConnectionAddressChanges,
       "accL2tpTraps": accL2tpTraps,
       "accL2tpTunnelDelTrap": accL2tpTunnelDelTrap,
       "accL2tpTrap2": accL2tpTrap2,
       "accL2tpUdpEpTrap": accL2tpUdpEpTrap,
       "accL2tpUdpEpCreateTrap": accL2tpUdpEpCreateTrap,
       "accL2tpTunnelCreateTrap": accL2tpTunnelCreateTrap,
       "accL2tpInvIntfAddrTrap": accL2tpInvIntfAddrTrap,
       "accL2tpTunnelAbortCleanUpTrap": accL2tpTunnelAbortCleanUpTrap,
       "accL2tpTrap8": accL2tpTrap8,
       "accL2tpUdpServTrap": accL2tpUdpServTrap,
       "accL2tpTrap10": accL2tpTrap10,
       "accL2tpTrapMsg": accL2tpTrapMsg}
)
