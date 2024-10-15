# SNMP MIB module (Wellfleet-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-L2TP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:34 2024
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

(wfL2TPGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfL2TPGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfTunnelAuthTable_Object = MibTable
wfTunnelAuthTable = _WfTunnelAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 1)
)
if mibBuilder.loadTexts:
    wfTunnelAuthTable.setStatus("mandatory")
_WfTunnelAuthEntry_Object = MibTableRow
wfTunnelAuthEntry = _WfTunnelAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 1, 1)
)
wfTunnelAuthEntry.setIndexNames(
    (0, "Wellfleet-L2TP-MIB", "wfTunnelAuthSlot"),
    (0, "Wellfleet-L2TP-MIB", "wfTunnelAuthInstance"),
)
if mibBuilder.loadTexts:
    wfTunnelAuthEntry.setStatus("mandatory")


class _WfTunnelAuthDelete_Type(Integer32):
    """Custom type wfTunnelAuthDelete based on Integer32"""
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


_WfTunnelAuthDelete_Type.__name__ = "Integer32"
_WfTunnelAuthDelete_Object = MibTableColumn
wfTunnelAuthDelete = _WfTunnelAuthDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 1, 1, 1),
    _WfTunnelAuthDelete_Type()
)
wfTunnelAuthDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTunnelAuthDelete.setStatus("mandatory")


class _WfTunnelAuthDisable_Type(Integer32):
    """Custom type wfTunnelAuthDisable based on Integer32"""
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


_WfTunnelAuthDisable_Type.__name__ = "Integer32"
_WfTunnelAuthDisable_Object = MibTableColumn
wfTunnelAuthDisable = _WfTunnelAuthDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 1, 1, 2),
    _WfTunnelAuthDisable_Type()
)
wfTunnelAuthDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTunnelAuthDisable.setStatus("mandatory")
_WfTunnelAuthSlot_Type = Integer32
_WfTunnelAuthSlot_Object = MibTableColumn
wfTunnelAuthSlot = _WfTunnelAuthSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 1, 1, 3),
    _WfTunnelAuthSlot_Type()
)
wfTunnelAuthSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTunnelAuthSlot.setStatus("mandatory")
_WfTunnelAuthInstance_Type = Integer32
_WfTunnelAuthInstance_Object = MibTableColumn
wfTunnelAuthInstance = _WfTunnelAuthInstance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 1, 1, 4),
    _WfTunnelAuthInstance_Type()
)
wfTunnelAuthInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTunnelAuthInstance.setStatus("mandatory")
_WfTunnelAuthSecret_Type = DisplayString
_WfTunnelAuthSecret_Object = MibTableColumn
wfTunnelAuthSecret = _WfTunnelAuthSecret_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 1, 1, 5),
    _WfTunnelAuthSecret_Type()
)
wfTunnelAuthSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTunnelAuthSecret.setStatus("mandatory")
_WfL2TPTable_Object = MibTable
wfL2TPTable = _WfL2TPTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2)
)
if mibBuilder.loadTexts:
    wfL2TPTable.setStatus("mandatory")
_WfL2TPEntry_Object = MibTableRow
wfL2TPEntry = _WfL2TPEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1)
)
wfL2TPEntry.setIndexNames(
    (0, "Wellfleet-L2TP-MIB", "wfL2TPSlot"),
)
if mibBuilder.loadTexts:
    wfL2TPEntry.setStatus("mandatory")


class _WfL2TPDelete_Type(Integer32):
    """Custom type wfL2TPDelete based on Integer32"""
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


_WfL2TPDelete_Type.__name__ = "Integer32"
_WfL2TPDelete_Object = MibTableColumn
wfL2TPDelete = _WfL2TPDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 1),
    _WfL2TPDelete_Type()
)
wfL2TPDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPDelete.setStatus("mandatory")


class _WfL2TPDisable_Type(Integer32):
    """Custom type wfL2TPDisable based on Integer32"""
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


_WfL2TPDisable_Type.__name__ = "Integer32"
_WfL2TPDisable_Object = MibTableColumn
wfL2TPDisable = _WfL2TPDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 2),
    _WfL2TPDisable_Type()
)
wfL2TPDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPDisable.setStatus("mandatory")
_WfL2TPLnsAddr_Type = IpAddress
_WfL2TPLnsAddr_Object = MibTableColumn
wfL2TPLnsAddr = _WfL2TPLnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 3),
    _WfL2TPLnsAddr_Type()
)
wfL2TPLnsAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPLnsAddr.setStatus("mandatory")
_WfL2TPIPstate_Type = Integer32
_WfL2TPIPstate_Object = MibTableColumn
wfL2TPIPstate = _WfL2TPIPstate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 4),
    _WfL2TPIPstate_Type()
)
wfL2TPIPstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPIPstate.setStatus("mandatory")
_WfL2TPSlot_Type = Integer32
_WfL2TPSlot_Object = MibTableColumn
wfL2TPSlot = _WfL2TPSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 5),
    _WfL2TPSlot_Type()
)
wfL2TPSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSlot.setStatus("mandatory")


class _WfL2TPReceiveWindowSize_Type(Integer32):
    """Custom type wfL2TPReceiveWindowSize based on Integer32"""
    defaultValue = 4


_WfL2TPReceiveWindowSize_Object = MibTableColumn
wfL2TPReceiveWindowSize = _WfL2TPReceiveWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 6),
    _WfL2TPReceiveWindowSize_Type()
)
wfL2TPReceiveWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPReceiveWindowSize.setStatus("mandatory")


class _WfL2TPRetransmitTimer_Type(Integer32):
    """Custom type wfL2TPRetransmitTimer based on Integer32"""
    defaultValue = 1


_WfL2TPRetransmitTimer_Object = MibTableColumn
wfL2TPRetransmitTimer = _WfL2TPRetransmitTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 7),
    _WfL2TPRetransmitTimer_Type()
)
wfL2TPRetransmitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPRetransmitTimer.setStatus("mandatory")


class _WfL2TPMaxRetransmit_Type(Integer32):
    """Custom type wfL2TPMaxRetransmit based on Integer32"""
    defaultValue = 5


_WfL2TPMaxRetransmit_Object = MibTableColumn
wfL2TPMaxRetransmit = _WfL2TPMaxRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 8),
    _WfL2TPMaxRetransmit_Type()
)
wfL2TPMaxRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPMaxRetransmit.setStatus("mandatory")


class _WfL2TPHelloTimer_Type(Integer32):
    """Custom type wfL2TPHelloTimer based on Integer32"""
    defaultValue = 60


_WfL2TPHelloTimer_Object = MibTableColumn
wfL2TPHelloTimer = _WfL2TPHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 9),
    _WfL2TPHelloTimer_Type()
)
wfL2TPHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPHelloTimer.setStatus("mandatory")


class _WfL2TPAckTimer_Type(Integer32):
    """Custom type wfL2TPAckTimer based on Integer32"""
    defaultValue = 250


_WfL2TPAckTimer_Object = MibTableColumn
wfL2TPAckTimer = _WfL2TPAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 10),
    _WfL2TPAckTimer_Type()
)
wfL2TPAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPAckTimer.setStatus("mandatory")


class _WfL2TPAckLastNPkts_Type(Integer32):
    """Custom type wfL2TPAckLastNPkts based on Integer32"""
    defaultValue = 200


_WfL2TPAckLastNPkts_Object = MibTableColumn
wfL2TPAckLastNPkts = _WfL2TPAckLastNPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 11),
    _WfL2TPAckLastNPkts_Type()
)
wfL2TPAckLastNPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPAckLastNPkts.setStatus("mandatory")
_WfL2TPLnsHostName_Type = DisplayString
_WfL2TPLnsHostName_Object = MibTableColumn
wfL2TPLnsHostName = _WfL2TPLnsHostName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 12),
    _WfL2TPLnsHostName_Type()
)
wfL2TPLnsHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPLnsHostName.setStatus("mandatory")


class _WfL2TPTunnelInfo_Type(Integer32):
    """Custom type wfL2TPTunnelInfo based on Integer32"""
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


_WfL2TPTunnelInfo_Type.__name__ = "Integer32"
_WfL2TPTunnelInfo_Object = MibTableColumn
wfL2TPTunnelInfo = _WfL2TPTunnelInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 13),
    _WfL2TPTunnelInfo_Type()
)
wfL2TPTunnelInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPTunnelInfo.setStatus("mandatory")


class _WfL2TPSessionInfo_Type(Integer32):
    """Custom type wfL2TPSessionInfo based on Integer32"""
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


_WfL2TPSessionInfo_Type.__name__ = "Integer32"
_WfL2TPSessionInfo_Object = MibTableColumn
wfL2TPSessionInfo = _WfL2TPSessionInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 14),
    _WfL2TPSessionInfo_Type()
)
wfL2TPSessionInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPSessionInfo.setStatus("mandatory")


class _WfL2TPDebugFlag_Type(Integer32):
    """Custom type wfL2TPDebugFlag based on Integer32"""
    defaultValue = 0


_WfL2TPDebugFlag_Object = MibTableColumn
wfL2TPDebugFlag = _WfL2TPDebugFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 15),
    _WfL2TPDebugFlag_Type()
)
wfL2TPDebugFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPDebugFlag.setStatus("mandatory")


class _WfL2TPMaxSession_Type(Integer32):
    """Custom type wfL2TPMaxSession based on Integer32"""
    defaultValue = 100


_WfL2TPMaxSession_Object = MibTableColumn
wfL2TPMaxSession = _WfL2TPMaxSession_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 16),
    _WfL2TPMaxSession_Type()
)
wfL2TPMaxSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPMaxSession.setStatus("mandatory")


class _WfL2TPPortCfgMask_Type(Integer32):
    """Custom type wfL2TPPortCfgMask based on Integer32"""
    defaultValue = 0


_WfL2TPPortCfgMask_Object = MibTableColumn
wfL2TPPortCfgMask = _WfL2TPPortCfgMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 17),
    _WfL2TPPortCfgMask_Type()
)
wfL2TPPortCfgMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPPortCfgMask.setStatus("mandatory")
_WfL2TPIpAddr_Type = IpAddress
_WfL2TPIpAddr_Object = MibTableColumn
wfL2TPIpAddr = _WfL2TPIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 18),
    _WfL2TPIpAddr_Type()
)
wfL2TPIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPIpAddr.setStatus("mandatory")


class _WfL2TPIpCctNum_Type(Integer32):
    """Custom type wfL2TPIpCctNum based on Integer32"""
    defaultValue = 0


_WfL2TPIpCctNum_Object = MibTableColumn
wfL2TPIpCctNum = _WfL2TPIpCctNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 19),
    _WfL2TPIpCctNum_Type()
)
wfL2TPIpCctNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPIpCctNum.setStatus("mandatory")


class _WfL2TPTunnelDataFlowControl_Type(Integer32):
    """Custom type wfL2TPTunnelDataFlowControl based on Integer32"""
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


_WfL2TPTunnelDataFlowControl_Type.__name__ = "Integer32"
_WfL2TPTunnelDataFlowControl_Object = MibTableColumn
wfL2TPTunnelDataFlowControl = _WfL2TPTunnelDataFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 20),
    _WfL2TPTunnelDataFlowControl_Type()
)
wfL2TPTunnelDataFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPTunnelDataFlowControl.setStatus("mandatory")


class _WfL2TPRemoveDomainName_Type(Integer32):
    """Custom type wfL2TPRemoveDomainName based on Integer32"""
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


_WfL2TPRemoveDomainName_Type.__name__ = "Integer32"
_WfL2TPRemoveDomainName_Object = MibTableColumn
wfL2TPRemoveDomainName = _WfL2TPRemoveDomainName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 21),
    _WfL2TPRemoveDomainName_Type()
)
wfL2TPRemoveDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPRemoveDomainName.setStatus("mandatory")


class _WfL2TPDomainNameDelimiter_Type(DisplayString):
    """Custom type wfL2TPDomainNameDelimiter based on DisplayString"""
    defaultValue = OctetString("@")


_WfL2TPDomainNameDelimiter_Object = MibTableColumn
wfL2TPDomainNameDelimiter = _WfL2TPDomainNameDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 22),
    _WfL2TPDomainNameDelimiter_Type()
)
wfL2TPDomainNameDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPDomainNameDelimiter.setStatus("mandatory")


class _WfL2TPNsaOrigin_Type(Integer32):
    """Custom type wfL2TPNsaOrigin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("local", 2),
          ("radius", 3))
    )


_WfL2TPNsaOrigin_Type.__name__ = "Integer32"
_WfL2TPNsaOrigin_Object = MibTableColumn
wfL2TPNsaOrigin = _WfL2TPNsaOrigin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 23),
    _WfL2TPNsaOrigin_Type()
)
wfL2TPNsaOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPNsaOrigin.setStatus("mandatory")
_WfL2TPNsaPrimaryDNS_Type = IpAddress
_WfL2TPNsaPrimaryDNS_Object = MibTableColumn
wfL2TPNsaPrimaryDNS = _WfL2TPNsaPrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 24),
    _WfL2TPNsaPrimaryDNS_Type()
)
wfL2TPNsaPrimaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPNsaPrimaryDNS.setStatus("mandatory")
_WfL2TPNsaSecondaryDNS_Type = IpAddress
_WfL2TPNsaSecondaryDNS_Object = MibTableColumn
wfL2TPNsaSecondaryDNS = _WfL2TPNsaSecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 25),
    _WfL2TPNsaSecondaryDNS_Type()
)
wfL2TPNsaSecondaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPNsaSecondaryDNS.setStatus("mandatory")
_WfL2TPNsaPrimaryNBNS_Type = IpAddress
_WfL2TPNsaPrimaryNBNS_Object = MibTableColumn
wfL2TPNsaPrimaryNBNS = _WfL2TPNsaPrimaryNBNS_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 26),
    _WfL2TPNsaPrimaryNBNS_Type()
)
wfL2TPNsaPrimaryNBNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPNsaPrimaryNBNS.setStatus("mandatory")
_WfL2TPNsaSecondaryNBNS_Type = IpAddress
_WfL2TPNsaSecondaryNBNS_Object = MibTableColumn
wfL2TPNsaSecondaryNBNS = _WfL2TPNsaSecondaryNBNS_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 2, 1, 27),
    _WfL2TPNsaSecondaryNBNS_Type()
)
wfL2TPNsaSecondaryNBNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPNsaSecondaryNBNS.setStatus("mandatory")
_WfTunnelCircuitTable_Object = MibTable
wfTunnelCircuitTable = _WfTunnelCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 3)
)
if mibBuilder.loadTexts:
    wfTunnelCircuitTable.setStatus("mandatory")
_WfTunnelCircuitEntry_Object = MibTableRow
wfTunnelCircuitEntry = _WfTunnelCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 3, 1)
)
wfTunnelCircuitEntry.setIndexNames(
    (0, "Wellfleet-L2TP-MIB", "wfTunnelCircuitNum"),
)
if mibBuilder.loadTexts:
    wfTunnelCircuitEntry.setStatus("mandatory")


class _WfTunnelCircuitDelete_Type(Integer32):
    """Custom type wfTunnelCircuitDelete based on Integer32"""
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


_WfTunnelCircuitDelete_Type.__name__ = "Integer32"
_WfTunnelCircuitDelete_Object = MibTableColumn
wfTunnelCircuitDelete = _WfTunnelCircuitDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 3, 1, 1),
    _WfTunnelCircuitDelete_Type()
)
wfTunnelCircuitDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTunnelCircuitDelete.setStatus("mandatory")
_WfTunnelCircuitNum_Type = Integer32
_WfTunnelCircuitNum_Object = MibTableColumn
wfTunnelCircuitNum = _WfTunnelCircuitNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 3, 1, 2),
    _WfTunnelCircuitNum_Type()
)
wfTunnelCircuitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTunnelCircuitNum.setStatus("mandatory")
_WfTunnelCircuitSlot_Type = Integer32
_WfTunnelCircuitSlot_Object = MibTableColumn
wfTunnelCircuitSlot = _WfTunnelCircuitSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 3, 1, 3),
    _WfTunnelCircuitSlot_Type()
)
wfTunnelCircuitSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTunnelCircuitSlot.setStatus("mandatory")
_WfL2TPStatsTable_Object = MibTable
wfL2TPStatsTable = _WfL2TPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4)
)
if mibBuilder.loadTexts:
    wfL2TPStatsTable.setStatus("mandatory")
_WfL2TPStatsEntry_Object = MibTableRow
wfL2TPStatsEntry = _WfL2TPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1)
)
wfL2TPStatsEntry.setIndexNames(
    (0, "Wellfleet-L2TP-MIB", "wfL2TPStatsSlot"),
)
if mibBuilder.loadTexts:
    wfL2TPStatsEntry.setStatus("mandatory")


class _WfL2TPStatsCreate_Type(Integer32):
    """Custom type wfL2TPStatsCreate based on Integer32"""
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


_WfL2TPStatsCreate_Type.__name__ = "Integer32"
_WfL2TPStatsCreate_Object = MibTableColumn
wfL2TPStatsCreate = _WfL2TPStatsCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 1),
    _WfL2TPStatsCreate_Type()
)
wfL2TPStatsCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfL2TPStatsCreate.setStatus("mandatory")
_WfL2TPStatsSlot_Type = Integer32
_WfL2TPStatsSlot_Object = MibTableColumn
wfL2TPStatsSlot = _WfL2TPStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 2),
    _WfL2TPStatsSlot_Type()
)
wfL2TPStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsSlot.setStatus("mandatory")
_WfL2TPStatsIpAddress_Type = IpAddress
_WfL2TPStatsIpAddress_Object = MibTableColumn
wfL2TPStatsIpAddress = _WfL2TPStatsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 3),
    _WfL2TPStatsIpAddress_Type()
)
wfL2TPStatsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsIpAddress.setStatus("mandatory")
_WfL2TPStatsValidSccrq_Type = Integer32
_WfL2TPStatsValidSccrq_Object = MibTableColumn
wfL2TPStatsValidSccrq = _WfL2TPStatsValidSccrq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 4),
    _WfL2TPStatsValidSccrq_Type()
)
wfL2TPStatsValidSccrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsValidSccrq.setStatus("mandatory")
_WfL2TPStatsValidScccn_Type = Integer32
_WfL2TPStatsValidScccn_Object = MibTableColumn
wfL2TPStatsValidScccn = _WfL2TPStatsValidScccn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 5),
    _WfL2TPStatsValidScccn_Type()
)
wfL2TPStatsValidScccn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsValidScccn.setStatus("mandatory")
_WfL2TPStatsValidIcrq_Type = Integer32
_WfL2TPStatsValidIcrq_Object = MibTableColumn
wfL2TPStatsValidIcrq = _WfL2TPStatsValidIcrq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 6),
    _WfL2TPStatsValidIcrq_Type()
)
wfL2TPStatsValidIcrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsValidIcrq.setStatus("mandatory")
_WfL2TPStatsValidIccn_Type = Integer32
_WfL2TPStatsValidIccn_Object = MibTableColumn
wfL2TPStatsValidIccn = _WfL2TPStatsValidIccn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 7),
    _WfL2TPStatsValidIccn_Type()
)
wfL2TPStatsValidIccn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsValidIccn.setStatus("mandatory")
_WfL2TPStatsInvalidSccrq_Type = Integer32
_WfL2TPStatsInvalidSccrq_Object = MibTableColumn
wfL2TPStatsInvalidSccrq = _WfL2TPStatsInvalidSccrq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 8),
    _WfL2TPStatsInvalidSccrq_Type()
)
wfL2TPStatsInvalidSccrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsInvalidSccrq.setStatus("mandatory")
_WfL2TPStatsInvalidScccn_Type = Integer32
_WfL2TPStatsInvalidScccn_Object = MibTableColumn
wfL2TPStatsInvalidScccn = _WfL2TPStatsInvalidScccn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 9),
    _WfL2TPStatsInvalidScccn_Type()
)
wfL2TPStatsInvalidScccn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsInvalidScccn.setStatus("mandatory")
_WfL2TPStatsInvalidIcrq_Type = Integer32
_WfL2TPStatsInvalidIcrq_Object = MibTableColumn
wfL2TPStatsInvalidIcrq = _WfL2TPStatsInvalidIcrq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 10),
    _WfL2TPStatsInvalidIcrq_Type()
)
wfL2TPStatsInvalidIcrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsInvalidIcrq.setStatus("mandatory")
_WfL2TPStatsInvalidIccn_Type = Integer32
_WfL2TPStatsInvalidIccn_Object = MibTableColumn
wfL2TPStatsInvalidIccn = _WfL2TPStatsInvalidIccn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 11),
    _WfL2TPStatsInvalidIccn_Type()
)
wfL2TPStatsInvalidIccn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsInvalidIccn.setStatus("mandatory")
_WfL2TPStatsSuccessTunnelAuth_Type = Integer32
_WfL2TPStatsSuccessTunnelAuth_Object = MibTableColumn
wfL2TPStatsSuccessTunnelAuth = _WfL2TPStatsSuccessTunnelAuth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 12),
    _WfL2TPStatsSuccessTunnelAuth_Type()
)
wfL2TPStatsSuccessTunnelAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsSuccessTunnelAuth.setStatus("mandatory")
_WfL2TPStatsSuccessSessionAuth_Type = Integer32
_WfL2TPStatsSuccessSessionAuth_Object = MibTableColumn
wfL2TPStatsSuccessSessionAuth = _WfL2TPStatsSuccessSessionAuth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 13),
    _WfL2TPStatsSuccessSessionAuth_Type()
)
wfL2TPStatsSuccessSessionAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsSuccessSessionAuth.setStatus("mandatory")
_WfL2TPStatsFailTunnelAuth_Type = Integer32
_WfL2TPStatsFailTunnelAuth_Object = MibTableColumn
wfL2TPStatsFailTunnelAuth = _WfL2TPStatsFailTunnelAuth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 14),
    _WfL2TPStatsFailTunnelAuth_Type()
)
wfL2TPStatsFailTunnelAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsFailTunnelAuth.setStatus("mandatory")
_WfL2TPStatsFailSessionAuth_Type = Integer32
_WfL2TPStatsFailSessionAuth_Object = MibTableColumn
wfL2TPStatsFailSessionAuth = _WfL2TPStatsFailSessionAuth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 15),
    _WfL2TPStatsFailSessionAuth_Type()
)
wfL2TPStatsFailSessionAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsFailSessionAuth.setStatus("mandatory")
_WfL2TPStatsActiveTunnelCount_Type = Integer32
_WfL2TPStatsActiveTunnelCount_Object = MibTableColumn
wfL2TPStatsActiveTunnelCount = _WfL2TPStatsActiveTunnelCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 16),
    _WfL2TPStatsActiveTunnelCount_Type()
)
wfL2TPStatsActiveTunnelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsActiveTunnelCount.setStatus("mandatory")
_WfL2TPStatsActiveSessionCount_Type = Integer32
_WfL2TPStatsActiveSessionCount_Object = MibTableColumn
wfL2TPStatsActiveSessionCount = _WfL2TPStatsActiveSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 17),
    _WfL2TPStatsActiveSessionCount_Type()
)
wfL2TPStatsActiveSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsActiveSessionCount.setStatus("mandatory")
_WfL2TPStatsDropInCtrlPktCount_Type = Integer32
_WfL2TPStatsDropInCtrlPktCount_Object = MibTableColumn
wfL2TPStatsDropInCtrlPktCount = _WfL2TPStatsDropInCtrlPktCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 18),
    _WfL2TPStatsDropInCtrlPktCount_Type()
)
wfL2TPStatsDropInCtrlPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsDropInCtrlPktCount.setStatus("mandatory")
_WfL2TPStatsDropInPayloadPktCount_Type = Integer32
_WfL2TPStatsDropInPayloadPktCount_Object = MibTableColumn
wfL2TPStatsDropInPayloadPktCount = _WfL2TPStatsDropInPayloadPktCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 19),
    _WfL2TPStatsDropInPayloadPktCount_Type()
)
wfL2TPStatsDropInPayloadPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsDropInPayloadPktCount.setStatus("mandatory")
_WfL2TPStatsHelloPktTxCount_Type = Integer32
_WfL2TPStatsHelloPktTxCount_Object = MibTableColumn
wfL2TPStatsHelloPktTxCount = _WfL2TPStatsHelloPktTxCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 20),
    _WfL2TPStatsHelloPktTxCount_Type()
)
wfL2TPStatsHelloPktTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsHelloPktTxCount.setStatus("mandatory")
_WfL2TPStatsHelloPktRxCount_Type = Integer32
_WfL2TPStatsHelloPktRxCount_Object = MibTableColumn
wfL2TPStatsHelloPktRxCount = _WfL2TPStatsHelloPktRxCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 21),
    _WfL2TPStatsHelloPktRxCount_Type()
)
wfL2TPStatsHelloPktRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsHelloPktRxCount.setStatus("mandatory")
_WfL2TPStatsCdnPktTxCount_Type = Integer32
_WfL2TPStatsCdnPktTxCount_Object = MibTableColumn
wfL2TPStatsCdnPktTxCount = _WfL2TPStatsCdnPktTxCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 22),
    _WfL2TPStatsCdnPktTxCount_Type()
)
wfL2TPStatsCdnPktTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsCdnPktTxCount.setStatus("mandatory")
_WfL2TPStatsCdnPktRxCount_Type = Integer32
_WfL2TPStatsCdnPktRxCount_Object = MibTableColumn
wfL2TPStatsCdnPktRxCount = _WfL2TPStatsCdnPktRxCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 23),
    _WfL2TPStatsCdnPktRxCount_Type()
)
wfL2TPStatsCdnPktRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsCdnPktRxCount.setStatus("mandatory")
_WfL2TPStatsStopCCNPktTxCount_Type = Integer32
_WfL2TPStatsStopCCNPktTxCount_Object = MibTableColumn
wfL2TPStatsStopCCNPktTxCount = _WfL2TPStatsStopCCNPktTxCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 24),
    _WfL2TPStatsStopCCNPktTxCount_Type()
)
wfL2TPStatsStopCCNPktTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsStopCCNPktTxCount.setStatus("mandatory")
_WfL2TPStatsStopCCNPktRxCount_Type = Integer32
_WfL2TPStatsStopCCNPktRxCount_Object = MibTableColumn
wfL2TPStatsStopCCNPktRxCount = _WfL2TPStatsStopCCNPktRxCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 4, 1, 25),
    _WfL2TPStatsStopCCNPktRxCount_Type()
)
wfL2TPStatsStopCCNPktRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPStatsStopCCNPktRxCount.setStatus("mandatory")
_WfL2TPTunnelInfoTable_Object = MibTable
wfL2TPTunnelInfoTable = _WfL2TPTunnelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 5)
)
if mibBuilder.loadTexts:
    wfL2TPTunnelInfoTable.setStatus("mandatory")
_WfL2TPTunnelInfoEntry_Object = MibTableRow
wfL2TPTunnelInfoEntry = _WfL2TPTunnelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 5, 1)
)
wfL2TPTunnelInfoEntry.setIndexNames(
    (0, "Wellfleet-L2TP-MIB", "wfL2TPTunnelInfoSlot"),
    (0, "Wellfleet-L2TP-MIB", "wfL2TPTunnelInfoLnsTunnelId"),
)
if mibBuilder.loadTexts:
    wfL2TPTunnelInfoEntry.setStatus("mandatory")
_WfL2TPTunnelInfoSlot_Type = Integer32
_WfL2TPTunnelInfoSlot_Object = MibTableColumn
wfL2TPTunnelInfoSlot = _WfL2TPTunnelInfoSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 5, 1, 1),
    _WfL2TPTunnelInfoSlot_Type()
)
wfL2TPTunnelInfoSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPTunnelInfoSlot.setStatus("mandatory")
_WfL2TPTunnelInfoLnsTunnelId_Type = Integer32
_WfL2TPTunnelInfoLnsTunnelId_Object = MibTableColumn
wfL2TPTunnelInfoLnsTunnelId = _WfL2TPTunnelInfoLnsTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 5, 1, 2),
    _WfL2TPTunnelInfoLnsTunnelId_Type()
)
wfL2TPTunnelInfoLnsTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPTunnelInfoLnsTunnelId.setStatus("mandatory")
_WfL2TPTunnelInfoLacTunnelId_Type = Integer32
_WfL2TPTunnelInfoLacTunnelId_Object = MibTableColumn
wfL2TPTunnelInfoLacTunnelId = _WfL2TPTunnelInfoLacTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 5, 1, 3),
    _WfL2TPTunnelInfoLacTunnelId_Type()
)
wfL2TPTunnelInfoLacTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPTunnelInfoLacTunnelId.setStatus("mandatory")
_WfL2TPTunnelInfoLnsAddress_Type = IpAddress
_WfL2TPTunnelInfoLnsAddress_Object = MibTableColumn
wfL2TPTunnelInfoLnsAddress = _WfL2TPTunnelInfoLnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 5, 1, 4),
    _WfL2TPTunnelInfoLnsAddress_Type()
)
wfL2TPTunnelInfoLnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPTunnelInfoLnsAddress.setStatus("mandatory")
_WfL2TPTunnelInfoLacAddress_Type = IpAddress
_WfL2TPTunnelInfoLacAddress_Object = MibTableColumn
wfL2TPTunnelInfoLacAddress = _WfL2TPTunnelInfoLacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 5, 1, 5),
    _WfL2TPTunnelInfoLacAddress_Type()
)
wfL2TPTunnelInfoLacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPTunnelInfoLacAddress.setStatus("mandatory")
_WfL2TPTunnelInfoFramingCap_Type = Integer32
_WfL2TPTunnelInfoFramingCap_Object = MibTableColumn
wfL2TPTunnelInfoFramingCap = _WfL2TPTunnelInfoFramingCap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 5, 1, 6),
    _WfL2TPTunnelInfoFramingCap_Type()
)
wfL2TPTunnelInfoFramingCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPTunnelInfoFramingCap.setStatus("mandatory")
_WfL2TPTunnelInfoBearerCap_Type = Integer32
_WfL2TPTunnelInfoBearerCap_Object = MibTableColumn
wfL2TPTunnelInfoBearerCap = _WfL2TPTunnelInfoBearerCap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 5, 1, 7),
    _WfL2TPTunnelInfoBearerCap_Type()
)
wfL2TPTunnelInfoBearerCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPTunnelInfoBearerCap.setStatus("mandatory")
_WfL2TPTunnelInfoLacVendorName_Type = DisplayString
_WfL2TPTunnelInfoLacVendorName_Object = MibTableColumn
wfL2TPTunnelInfoLacVendorName = _WfL2TPTunnelInfoLacVendorName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 5, 1, 8),
    _WfL2TPTunnelInfoLacVendorName_Type()
)
wfL2TPTunnelInfoLacVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPTunnelInfoLacVendorName.setStatus("mandatory")
_WfL2TPTunnelInfoLacHostName_Type = DisplayString
_WfL2TPTunnelInfoLacHostName_Object = MibTableColumn
wfL2TPTunnelInfoLacHostName = _WfL2TPTunnelInfoLacHostName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 5, 1, 9),
    _WfL2TPTunnelInfoLacHostName_Type()
)
wfL2TPTunnelInfoLacHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPTunnelInfoLacHostName.setStatus("mandatory")
_WfL2TPTunnelInfoRecvWindowSize_Type = Integer32
_WfL2TPTunnelInfoRecvWindowSize_Object = MibTableColumn
wfL2TPTunnelInfoRecvWindowSize = _WfL2TPTunnelInfoRecvWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 5, 1, 10),
    _WfL2TPTunnelInfoRecvWindowSize_Type()
)
wfL2TPTunnelInfoRecvWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPTunnelInfoRecvWindowSize.setStatus("mandatory")
_WfL2TPTunnelInfoActiveSessionCount_Type = Integer32
_WfL2TPTunnelInfoActiveSessionCount_Object = MibTableColumn
wfL2TPTunnelInfoActiveSessionCount = _WfL2TPTunnelInfoActiveSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 5, 1, 11),
    _WfL2TPTunnelInfoActiveSessionCount_Type()
)
wfL2TPTunnelInfoActiveSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPTunnelInfoActiveSessionCount.setStatus("mandatory")
_WfL2TPTunnelInfoFirmwareRevision_Type = Integer32
_WfL2TPTunnelInfoFirmwareRevision_Object = MibTableColumn
wfL2TPTunnelInfoFirmwareRevision = _WfL2TPTunnelInfoFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 5, 1, 12),
    _WfL2TPTunnelInfoFirmwareRevision_Type()
)
wfL2TPTunnelInfoFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPTunnelInfoFirmwareRevision.setStatus("mandatory")
_WfL2TPSessionInfoTable_Object = MibTable
wfL2TPSessionInfoTable = _WfL2TPSessionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6)
)
if mibBuilder.loadTexts:
    wfL2TPSessionInfoTable.setStatus("mandatory")
_WfL2TPSessionInfoEntry_Object = MibTableRow
wfL2TPSessionInfoEntry = _WfL2TPSessionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1)
)
wfL2TPSessionInfoEntry.setIndexNames(
    (0, "Wellfleet-L2TP-MIB", "wfL2TPSessionInfoSlot"),
    (0, "Wellfleet-L2TP-MIB", "wfL2TPSessionInfoLnsTunnelId"),
    (0, "Wellfleet-L2TP-MIB", "wfL2TPSessionInfoLnsCallId"),
)
if mibBuilder.loadTexts:
    wfL2TPSessionInfoEntry.setStatus("mandatory")
_WfL2TPSessionInfoSlot_Type = Integer32
_WfL2TPSessionInfoSlot_Object = MibTableColumn
wfL2TPSessionInfoSlot = _WfL2TPSessionInfoSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 1),
    _WfL2TPSessionInfoSlot_Type()
)
wfL2TPSessionInfoSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoSlot.setStatus("mandatory")
_WfL2TPSessionInfoLnsTunnelId_Type = Integer32
_WfL2TPSessionInfoLnsTunnelId_Object = MibTableColumn
wfL2TPSessionInfoLnsTunnelId = _WfL2TPSessionInfoLnsTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 2),
    _WfL2TPSessionInfoLnsTunnelId_Type()
)
wfL2TPSessionInfoLnsTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoLnsTunnelId.setStatus("mandatory")
_WfL2TPSessionInfoLacTunnelId_Type = Integer32
_WfL2TPSessionInfoLacTunnelId_Object = MibTableColumn
wfL2TPSessionInfoLacTunnelId = _WfL2TPSessionInfoLacTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 3),
    _WfL2TPSessionInfoLacTunnelId_Type()
)
wfL2TPSessionInfoLacTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoLacTunnelId.setStatus("mandatory")
_WfL2TPSessionInfoLnsCallId_Type = Integer32
_WfL2TPSessionInfoLnsCallId_Object = MibTableColumn
wfL2TPSessionInfoLnsCallId = _WfL2TPSessionInfoLnsCallId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 4),
    _WfL2TPSessionInfoLnsCallId_Type()
)
wfL2TPSessionInfoLnsCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoLnsCallId.setStatus("mandatory")
_WfL2TPSessionInfoLacCallId_Type = Integer32
_WfL2TPSessionInfoLacCallId_Object = MibTableColumn
wfL2TPSessionInfoLacCallId = _WfL2TPSessionInfoLacCallId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 5),
    _WfL2TPSessionInfoLacCallId_Type()
)
wfL2TPSessionInfoLacCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoLacCallId.setStatus("mandatory")
_WfL2TPSessionInfoCallSerialNum_Type = DisplayString
_WfL2TPSessionInfoCallSerialNum_Object = MibTableColumn
wfL2TPSessionInfoCallSerialNum = _WfL2TPSessionInfoCallSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 6),
    _WfL2TPSessionInfoCallSerialNum_Type()
)
wfL2TPSessionInfoCallSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoCallSerialNum.setStatus("mandatory")
_WfL2TPSessionInfoCallBearerType_Type = Integer32
_WfL2TPSessionInfoCallBearerType_Object = MibTableColumn
wfL2TPSessionInfoCallBearerType = _WfL2TPSessionInfoCallBearerType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 7),
    _WfL2TPSessionInfoCallBearerType_Type()
)
wfL2TPSessionInfoCallBearerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoCallBearerType.setStatus("mandatory")
_WfL2TPSessionInfoDialingNum_Type = DisplayString
_WfL2TPSessionInfoDialingNum_Object = MibTableColumn
wfL2TPSessionInfoDialingNum = _WfL2TPSessionInfoDialingNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 8),
    _WfL2TPSessionInfoDialingNum_Type()
)
wfL2TPSessionInfoDialingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoDialingNum.setStatus("mandatory")
_WfL2TPSessionInfoDialedNum_Type = DisplayString
_WfL2TPSessionInfoDialedNum_Object = MibTableColumn
wfL2TPSessionInfoDialedNum = _WfL2TPSessionInfoDialedNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 9),
    _WfL2TPSessionInfoDialedNum_Type()
)
wfL2TPSessionInfoDialedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoDialedNum.setStatus("mandatory")
_WfL2TPSessionInfoSubAddress_Type = DisplayString
_WfL2TPSessionInfoSubAddress_Object = MibTableColumn
wfL2TPSessionInfoSubAddress = _WfL2TPSessionInfoSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 10),
    _WfL2TPSessionInfoSubAddress_Type()
)
wfL2TPSessionInfoSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoSubAddress.setStatus("mandatory")
_WfL2TPSessionInfoConnectSpeed_Type = Integer32
_WfL2TPSessionInfoConnectSpeed_Object = MibTableColumn
wfL2TPSessionInfoConnectSpeed = _WfL2TPSessionInfoConnectSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 11),
    _WfL2TPSessionInfoConnectSpeed_Type()
)
wfL2TPSessionInfoConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoConnectSpeed.setStatus("mandatory")
_WfL2TPSessionInfoFramingType_Type = Integer32
_WfL2TPSessionInfoFramingType_Object = MibTableColumn
wfL2TPSessionInfoFramingType = _WfL2TPSessionInfoFramingType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 12),
    _WfL2TPSessionInfoFramingType_Type()
)
wfL2TPSessionInfoFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoFramingType.setStatus("mandatory")
_WfL2TPSessionInfoLocalRecvPktWindow_Type = Integer32
_WfL2TPSessionInfoLocalRecvPktWindow_Object = MibTableColumn
wfL2TPSessionInfoLocalRecvPktWindow = _WfL2TPSessionInfoLocalRecvPktWindow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 13),
    _WfL2TPSessionInfoLocalRecvPktWindow_Type()
)
wfL2TPSessionInfoLocalRecvPktWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoLocalRecvPktWindow.setStatus("mandatory")
_WfL2TPSessionInfoRemoteRecvPktWindow_Type = Integer32
_WfL2TPSessionInfoRemoteRecvPktWindow_Object = MibTableColumn
wfL2TPSessionInfoRemoteRecvPktWindow = _WfL2TPSessionInfoRemoteRecvPktWindow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 14),
    _WfL2TPSessionInfoRemoteRecvPktWindow_Type()
)
wfL2TPSessionInfoRemoteRecvPktWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoRemoteRecvPktWindow.setStatus("mandatory")
_WfL2TPSessionInfoPhysicalChannelId_Type = Integer32
_WfL2TPSessionInfoPhysicalChannelId_Object = MibTableColumn
wfL2TPSessionInfoPhysicalChannelId = _WfL2TPSessionInfoPhysicalChannelId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 15),
    _WfL2TPSessionInfoPhysicalChannelId_Type()
)
wfL2TPSessionInfoPhysicalChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoPhysicalChannelId.setStatus("mandatory")
_WfL2TPSessionInfoNextSendSeq_Type = Integer32
_WfL2TPSessionInfoNextSendSeq_Object = MibTableColumn
wfL2TPSessionInfoNextSendSeq = _WfL2TPSessionInfoNextSendSeq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 16),
    _WfL2TPSessionInfoNextSendSeq_Type()
)
wfL2TPSessionInfoNextSendSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoNextSendSeq.setStatus("mandatory")
_WfL2TPSessionInfoNextSendSeqAck_Type = Integer32
_WfL2TPSessionInfoNextSendSeqAck_Object = MibTableColumn
wfL2TPSessionInfoNextSendSeqAck = _WfL2TPSessionInfoNextSendSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 17),
    _WfL2TPSessionInfoNextSendSeqAck_Type()
)
wfL2TPSessionInfoNextSendSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoNextSendSeqAck.setStatus("mandatory")
_WfL2TPSessionInfoNextRecvSeq_Type = Integer32
_WfL2TPSessionInfoNextRecvSeq_Object = MibTableColumn
wfL2TPSessionInfoNextRecvSeq = _WfL2TPSessionInfoNextRecvSeq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 18),
    _WfL2TPSessionInfoNextRecvSeq_Type()
)
wfL2TPSessionInfoNextRecvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoNextRecvSeq.setStatus("mandatory")
_WfL2TPSessionInfoNextRecvSeqAck_Type = Integer32
_WfL2TPSessionInfoNextRecvSeqAck_Object = MibTableColumn
wfL2TPSessionInfoNextRecvSeqAck = _WfL2TPSessionInfoNextRecvSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 19),
    _WfL2TPSessionInfoNextRecvSeqAck_Type()
)
wfL2TPSessionInfoNextRecvSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoNextRecvSeqAck.setStatus("mandatory")
_WfL2TPSessionInfoAssignedIpAddress_Type = IpAddress
_WfL2TPSessionInfoAssignedIpAddress_Object = MibTableColumn
wfL2TPSessionInfoAssignedIpAddress = _WfL2TPSessionInfoAssignedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 20),
    _WfL2TPSessionInfoAssignedIpAddress_Type()
)
wfL2TPSessionInfoAssignedIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoAssignedIpAddress.setStatus("mandatory")
_WfL2TPSessionInfoUsername_Type = DisplayString
_WfL2TPSessionInfoUsername_Object = MibTableColumn
wfL2TPSessionInfoUsername = _WfL2TPSessionInfoUsername_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 21),
    _WfL2TPSessionInfoUsername_Type()
)
wfL2TPSessionInfoUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoUsername.setStatus("mandatory")
_WfL2TPSessionInfoTxPackets_Type = Integer32
_WfL2TPSessionInfoTxPackets_Object = MibTableColumn
wfL2TPSessionInfoTxPackets = _WfL2TPSessionInfoTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 22),
    _WfL2TPSessionInfoTxPackets_Type()
)
wfL2TPSessionInfoTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoTxPackets.setStatus("mandatory")
_WfL2TPSessionInfoRxPackets_Type = Integer32
_WfL2TPSessionInfoRxPackets_Object = MibTableColumn
wfL2TPSessionInfoRxPackets = _WfL2TPSessionInfoRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 23),
    _WfL2TPSessionInfoRxPackets_Type()
)
wfL2TPSessionInfoRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoRxPackets.setStatus("mandatory")
_WfL2TPSessionInfoConnectTime_Type = Integer32
_WfL2TPSessionInfoConnectTime_Object = MibTableColumn
wfL2TPSessionInfoConnectTime = _WfL2TPSessionInfoConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 6, 1, 24),
    _WfL2TPSessionInfoConnectTime_Type()
)
wfL2TPSessionInfoConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfL2TPSessionInfoConnectTime.setStatus("mandatory")
_WfTunnelLineTable_Object = MibTable
wfTunnelLineTable = _WfTunnelLineTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 7)
)
if mibBuilder.loadTexts:
    wfTunnelLineTable.setStatus("mandatory")
_WfTunnelLineEntry_Object = MibTableRow
wfTunnelLineEntry = _WfTunnelLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 7, 1)
)
wfTunnelLineEntry.setIndexNames(
    (0, "Wellfleet-L2TP-MIB", "wfTunnelLineNum"),
)
if mibBuilder.loadTexts:
    wfTunnelLineEntry.setStatus("mandatory")


class _WfTunnelLineDelete_Type(Integer32):
    """Custom type wfTunnelLineDelete based on Integer32"""
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


_WfTunnelLineDelete_Type.__name__ = "Integer32"
_WfTunnelLineDelete_Object = MibTableColumn
wfTunnelLineDelete = _WfTunnelLineDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 7, 1, 1),
    _WfTunnelLineDelete_Type()
)
wfTunnelLineDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTunnelLineDelete.setStatus("mandatory")
_WfTunnelLineNum_Type = Integer32
_WfTunnelLineNum_Object = MibTableColumn
wfTunnelLineNum = _WfTunnelLineNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 7, 1, 2),
    _WfTunnelLineNum_Type()
)
wfTunnelLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTunnelLineNum.setStatus("mandatory")
_WfTunnelLineSlot_Type = Integer32
_WfTunnelLineSlot_Object = MibTableColumn
wfTunnelLineSlot = _WfTunnelLineSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23, 7, 1, 3),
    _WfTunnelLineSlot_Type()
)
wfTunnelLineSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTunnelLineSlot.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-L2TP-MIB",
    **{"wfTunnelAuthTable": wfTunnelAuthTable,
       "wfTunnelAuthEntry": wfTunnelAuthEntry,
       "wfTunnelAuthDelete": wfTunnelAuthDelete,
       "wfTunnelAuthDisable": wfTunnelAuthDisable,
       "wfTunnelAuthSlot": wfTunnelAuthSlot,
       "wfTunnelAuthInstance": wfTunnelAuthInstance,
       "wfTunnelAuthSecret": wfTunnelAuthSecret,
       "wfL2TPTable": wfL2TPTable,
       "wfL2TPEntry": wfL2TPEntry,
       "wfL2TPDelete": wfL2TPDelete,
       "wfL2TPDisable": wfL2TPDisable,
       "wfL2TPLnsAddr": wfL2TPLnsAddr,
       "wfL2TPIPstate": wfL2TPIPstate,
       "wfL2TPSlot": wfL2TPSlot,
       "wfL2TPReceiveWindowSize": wfL2TPReceiveWindowSize,
       "wfL2TPRetransmitTimer": wfL2TPRetransmitTimer,
       "wfL2TPMaxRetransmit": wfL2TPMaxRetransmit,
       "wfL2TPHelloTimer": wfL2TPHelloTimer,
       "wfL2TPAckTimer": wfL2TPAckTimer,
       "wfL2TPAckLastNPkts": wfL2TPAckLastNPkts,
       "wfL2TPLnsHostName": wfL2TPLnsHostName,
       "wfL2TPTunnelInfo": wfL2TPTunnelInfo,
       "wfL2TPSessionInfo": wfL2TPSessionInfo,
       "wfL2TPDebugFlag": wfL2TPDebugFlag,
       "wfL2TPMaxSession": wfL2TPMaxSession,
       "wfL2TPPortCfgMask": wfL2TPPortCfgMask,
       "wfL2TPIpAddr": wfL2TPIpAddr,
       "wfL2TPIpCctNum": wfL2TPIpCctNum,
       "wfL2TPTunnelDataFlowControl": wfL2TPTunnelDataFlowControl,
       "wfL2TPRemoveDomainName": wfL2TPRemoveDomainName,
       "wfL2TPDomainNameDelimiter": wfL2TPDomainNameDelimiter,
       "wfL2TPNsaOrigin": wfL2TPNsaOrigin,
       "wfL2TPNsaPrimaryDNS": wfL2TPNsaPrimaryDNS,
       "wfL2TPNsaSecondaryDNS": wfL2TPNsaSecondaryDNS,
       "wfL2TPNsaPrimaryNBNS": wfL2TPNsaPrimaryNBNS,
       "wfL2TPNsaSecondaryNBNS": wfL2TPNsaSecondaryNBNS,
       "wfTunnelCircuitTable": wfTunnelCircuitTable,
       "wfTunnelCircuitEntry": wfTunnelCircuitEntry,
       "wfTunnelCircuitDelete": wfTunnelCircuitDelete,
       "wfTunnelCircuitNum": wfTunnelCircuitNum,
       "wfTunnelCircuitSlot": wfTunnelCircuitSlot,
       "wfL2TPStatsTable": wfL2TPStatsTable,
       "wfL2TPStatsEntry": wfL2TPStatsEntry,
       "wfL2TPStatsCreate": wfL2TPStatsCreate,
       "wfL2TPStatsSlot": wfL2TPStatsSlot,
       "wfL2TPStatsIpAddress": wfL2TPStatsIpAddress,
       "wfL2TPStatsValidSccrq": wfL2TPStatsValidSccrq,
       "wfL2TPStatsValidScccn": wfL2TPStatsValidScccn,
       "wfL2TPStatsValidIcrq": wfL2TPStatsValidIcrq,
       "wfL2TPStatsValidIccn": wfL2TPStatsValidIccn,
       "wfL2TPStatsInvalidSccrq": wfL2TPStatsInvalidSccrq,
       "wfL2TPStatsInvalidScccn": wfL2TPStatsInvalidScccn,
       "wfL2TPStatsInvalidIcrq": wfL2TPStatsInvalidIcrq,
       "wfL2TPStatsInvalidIccn": wfL2TPStatsInvalidIccn,
       "wfL2TPStatsSuccessTunnelAuth": wfL2TPStatsSuccessTunnelAuth,
       "wfL2TPStatsSuccessSessionAuth": wfL2TPStatsSuccessSessionAuth,
       "wfL2TPStatsFailTunnelAuth": wfL2TPStatsFailTunnelAuth,
       "wfL2TPStatsFailSessionAuth": wfL2TPStatsFailSessionAuth,
       "wfL2TPStatsActiveTunnelCount": wfL2TPStatsActiveTunnelCount,
       "wfL2TPStatsActiveSessionCount": wfL2TPStatsActiveSessionCount,
       "wfL2TPStatsDropInCtrlPktCount": wfL2TPStatsDropInCtrlPktCount,
       "wfL2TPStatsDropInPayloadPktCount": wfL2TPStatsDropInPayloadPktCount,
       "wfL2TPStatsHelloPktTxCount": wfL2TPStatsHelloPktTxCount,
       "wfL2TPStatsHelloPktRxCount": wfL2TPStatsHelloPktRxCount,
       "wfL2TPStatsCdnPktTxCount": wfL2TPStatsCdnPktTxCount,
       "wfL2TPStatsCdnPktRxCount": wfL2TPStatsCdnPktRxCount,
       "wfL2TPStatsStopCCNPktTxCount": wfL2TPStatsStopCCNPktTxCount,
       "wfL2TPStatsStopCCNPktRxCount": wfL2TPStatsStopCCNPktRxCount,
       "wfL2TPTunnelInfoTable": wfL2TPTunnelInfoTable,
       "wfL2TPTunnelInfoEntry": wfL2TPTunnelInfoEntry,
       "wfL2TPTunnelInfoSlot": wfL2TPTunnelInfoSlot,
       "wfL2TPTunnelInfoLnsTunnelId": wfL2TPTunnelInfoLnsTunnelId,
       "wfL2TPTunnelInfoLacTunnelId": wfL2TPTunnelInfoLacTunnelId,
       "wfL2TPTunnelInfoLnsAddress": wfL2TPTunnelInfoLnsAddress,
       "wfL2TPTunnelInfoLacAddress": wfL2TPTunnelInfoLacAddress,
       "wfL2TPTunnelInfoFramingCap": wfL2TPTunnelInfoFramingCap,
       "wfL2TPTunnelInfoBearerCap": wfL2TPTunnelInfoBearerCap,
       "wfL2TPTunnelInfoLacVendorName": wfL2TPTunnelInfoLacVendorName,
       "wfL2TPTunnelInfoLacHostName": wfL2TPTunnelInfoLacHostName,
       "wfL2TPTunnelInfoRecvWindowSize": wfL2TPTunnelInfoRecvWindowSize,
       "wfL2TPTunnelInfoActiveSessionCount": wfL2TPTunnelInfoActiveSessionCount,
       "wfL2TPTunnelInfoFirmwareRevision": wfL2TPTunnelInfoFirmwareRevision,
       "wfL2TPSessionInfoTable": wfL2TPSessionInfoTable,
       "wfL2TPSessionInfoEntry": wfL2TPSessionInfoEntry,
       "wfL2TPSessionInfoSlot": wfL2TPSessionInfoSlot,
       "wfL2TPSessionInfoLnsTunnelId": wfL2TPSessionInfoLnsTunnelId,
       "wfL2TPSessionInfoLacTunnelId": wfL2TPSessionInfoLacTunnelId,
       "wfL2TPSessionInfoLnsCallId": wfL2TPSessionInfoLnsCallId,
       "wfL2TPSessionInfoLacCallId": wfL2TPSessionInfoLacCallId,
       "wfL2TPSessionInfoCallSerialNum": wfL2TPSessionInfoCallSerialNum,
       "wfL2TPSessionInfoCallBearerType": wfL2TPSessionInfoCallBearerType,
       "wfL2TPSessionInfoDialingNum": wfL2TPSessionInfoDialingNum,
       "wfL2TPSessionInfoDialedNum": wfL2TPSessionInfoDialedNum,
       "wfL2TPSessionInfoSubAddress": wfL2TPSessionInfoSubAddress,
       "wfL2TPSessionInfoConnectSpeed": wfL2TPSessionInfoConnectSpeed,
       "wfL2TPSessionInfoFramingType": wfL2TPSessionInfoFramingType,
       "wfL2TPSessionInfoLocalRecvPktWindow": wfL2TPSessionInfoLocalRecvPktWindow,
       "wfL2TPSessionInfoRemoteRecvPktWindow": wfL2TPSessionInfoRemoteRecvPktWindow,
       "wfL2TPSessionInfoPhysicalChannelId": wfL2TPSessionInfoPhysicalChannelId,
       "wfL2TPSessionInfoNextSendSeq": wfL2TPSessionInfoNextSendSeq,
       "wfL2TPSessionInfoNextSendSeqAck": wfL2TPSessionInfoNextSendSeqAck,
       "wfL2TPSessionInfoNextRecvSeq": wfL2TPSessionInfoNextRecvSeq,
       "wfL2TPSessionInfoNextRecvSeqAck": wfL2TPSessionInfoNextRecvSeqAck,
       "wfL2TPSessionInfoAssignedIpAddress": wfL2TPSessionInfoAssignedIpAddress,
       "wfL2TPSessionInfoUsername": wfL2TPSessionInfoUsername,
       "wfL2TPSessionInfoTxPackets": wfL2TPSessionInfoTxPackets,
       "wfL2TPSessionInfoRxPackets": wfL2TPSessionInfoRxPackets,
       "wfL2TPSessionInfoConnectTime": wfL2TPSessionInfoConnectTime,
       "wfTunnelLineTable": wfTunnelLineTable,
       "wfTunnelLineEntry": wfTunnelLineEntry,
       "wfTunnelLineDelete": wfTunnelLineDelete,
       "wfTunnelLineNum": wfTunnelLineNum,
       "wfTunnelLineSlot": wfTunnelLineSlot}
)
