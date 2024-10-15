# SNMP MIB module (CMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CMC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:49 2024
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



class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class IpxAddress(OctetString):
    """Custom type IpxAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cmc_ObjectIdentity = ObjectIdentity
cmc = _Cmc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44)
)
_Cmc_prod_ObjectIdentity = ObjectIdentity
cmc_prod = _Cmc_prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 1)
)
_Cmc_adapt_ObjectIdentity = ObjectIdentity
cmc_adapt = _Cmc_adapt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 1, 1)
)
_Cmc_system_ObjectIdentity = ObjectIdentity
cmc_system = _Cmc_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 1, 2)
)
_Cmc_soft_ObjectIdentity = ObjectIdentity
cmc_soft = _Cmc_soft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 1, 3)
)
_Cmc_mgmt_ObjectIdentity = ObjectIdentity
cmc_mgmt = _Cmc_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2)
)
_Cmc_mib_ObjectIdentity = ObjectIdentity
cmc_mib = _Cmc_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 1)
)
_Cmc_ip_ObjectIdentity = ObjectIdentity
cmc_ip = _Cmc_ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4)
)
_CmcIpInAdminDiscards_Type = Counter32
_CmcIpInAdminDiscards_Object = MibScalar
cmcIpInAdminDiscards = _CmcIpInAdminDiscards_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 1),
    _CmcIpInAdminDiscards_Type()
)
cmcIpInAdminDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIpInAdminDiscards.setStatus("mandatory")
_CmcIpOutAdminDiscards_Type = Counter32
_CmcIpOutAdminDiscards_Object = MibScalar
cmcIpOutAdminDiscards = _CmcIpOutAdminDiscards_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 3),
    _CmcIpOutAdminDiscards_Type()
)
cmcIpOutAdminDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIpOutAdminDiscards.setStatus("mandatory")


class _CmcIpFiltStatus_Type(Integer32):
    """Custom type cmcIpFiltStatus based on Integer32"""
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


_CmcIpFiltStatus_Type.__name__ = "Integer32"
_CmcIpFiltStatus_Object = MibScalar
cmcIpFiltStatus = _CmcIpFiltStatus_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 4),
    _CmcIpFiltStatus_Type()
)
cmcIpFiltStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltStatus.setStatus("mandatory")
_CmcIpFilterTable_Object = MibTable
cmcIpFilterTable = _CmcIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    cmcIpFilterTable.setStatus("mandatory")
_CmcIpFiltEntry_Object = MibTableRow
cmcIpFiltEntry = _CmcIpFiltEntry_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1)
)
cmcIpFiltEntry.setIndexNames(
    (0, "CMC-MIB", "cmcIpFiltName"),
)
if mibBuilder.loadTexts:
    cmcIpFiltEntry.setStatus("mandatory")
_CmcIpFiltName_Type = OctetString
_CmcIpFiltName_Object = MibTableColumn
cmcIpFiltName = _CmcIpFiltName_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 1),
    _CmcIpFiltName_Type()
)
cmcIpFiltName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltName.setStatus("mandatory")
_CmcIpFiltPriority_Type = Integer32
_CmcIpFiltPriority_Object = MibTableColumn
cmcIpFiltPriority = _CmcIpFiltPriority_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 2),
    _CmcIpFiltPriority_Type()
)
cmcIpFiltPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIpFiltPriority.setStatus("mandatory")
_CmcIpFiltSAddr_Type = IpAddress
_CmcIpFiltSAddr_Object = MibTableColumn
cmcIpFiltSAddr = _CmcIpFiltSAddr_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 3),
    _CmcIpFiltSAddr_Type()
)
cmcIpFiltSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltSAddr.setStatus("mandatory")
_CmcIpFiltSMask_Type = IpAddress
_CmcIpFiltSMask_Object = MibTableColumn
cmcIpFiltSMask = _CmcIpFiltSMask_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 4),
    _CmcIpFiltSMask_Type()
)
cmcIpFiltSMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltSMask.setStatus("mandatory")
_CmcIpFiltSPort_Type = Integer32
_CmcIpFiltSPort_Object = MibTableColumn
cmcIpFiltSPort = _CmcIpFiltSPort_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 5),
    _CmcIpFiltSPort_Type()
)
cmcIpFiltSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltSPort.setStatus("mandatory")
_CmcIpFiltDAddr_Type = IpAddress
_CmcIpFiltDAddr_Object = MibTableColumn
cmcIpFiltDAddr = _CmcIpFiltDAddr_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 6),
    _CmcIpFiltDAddr_Type()
)
cmcIpFiltDAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltDAddr.setStatus("mandatory")
_CmcIpFiltDMask_Type = IpAddress
_CmcIpFiltDMask_Object = MibTableColumn
cmcIpFiltDMask = _CmcIpFiltDMask_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 7),
    _CmcIpFiltDMask_Type()
)
cmcIpFiltDMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltDMask.setStatus("mandatory")
_CmcIpFiltDPort_Type = Integer32
_CmcIpFiltDPort_Object = MibTableColumn
cmcIpFiltDPort = _CmcIpFiltDPort_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 8),
    _CmcIpFiltDPort_Type()
)
cmcIpFiltDPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltDPort.setStatus("mandatory")
_CmcIpFiltProto_Type = Integer32
_CmcIpFiltProto_Object = MibTableColumn
cmcIpFiltProto = _CmcIpFiltProto_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 9),
    _CmcIpFiltProto_Type()
)
cmcIpFiltProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltProto.setStatus("mandatory")


class _CmcIpFiltMode_Type(Integer32):
    """Custom type cmcIpFiltMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2),
          ("nodial", 3))
    )


_CmcIpFiltMode_Type.__name__ = "Integer32"
_CmcIpFiltMode_Object = MibTableColumn
cmcIpFiltMode = _CmcIpFiltMode_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 10),
    _CmcIpFiltMode_Type()
)
cmcIpFiltMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltMode.setStatus("mandatory")


class _CmcIpFiltErrMsg_Type(Integer32):
    """Custom type cmcIpFiltErrMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CmcIpFiltErrMsg_Type.__name__ = "Integer32"
_CmcIpFiltErrMsg_Object = MibTableColumn
cmcIpFiltErrMsg = _CmcIpFiltErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 11),
    _CmcIpFiltErrMsg_Type()
)
cmcIpFiltErrMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltErrMsg.setStatus("mandatory")


class _CmcIpFiltType_Type(Integer32):
    """Custom type cmcIpFiltType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("local", 1),
          ("netmgmt", 3))
    )


_CmcIpFiltType_Type.__name__ = "Integer32"
_CmcIpFiltType_Object = MibTableColumn
cmcIpFiltType = _CmcIpFiltType_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 12),
    _CmcIpFiltType_Type()
)
cmcIpFiltType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltType.setStatus("mandatory")
_CmcIpFiltMoveOper_Type = OctetString
_CmcIpFiltMoveOper_Object = MibTableColumn
cmcIpFiltMoveOper = _CmcIpFiltMoveOper_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 13),
    _CmcIpFiltMoveOper_Type()
)
cmcIpFiltMoveOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltMoveOper.setStatus("mandatory")
_CmcIpFiltUseCount_Type = Integer32
_CmcIpFiltUseCount_Object = MibTableColumn
cmcIpFiltUseCount = _CmcIpFiltUseCount_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 14),
    _CmcIpFiltUseCount_Type()
)
cmcIpFiltUseCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltUseCount.setStatus("mandatory")


class _CmcIpFiltDirection_Type(Integer32):
    """Custom type cmcIpFiltDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("incoming", 2),
          ("outgoing", 3))
    )


_CmcIpFiltDirection_Type.__name__ = "Integer32"
_CmcIpFiltDirection_Object = MibTableColumn
cmcIpFiltDirection = _CmcIpFiltDirection_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 15),
    _CmcIpFiltDirection_Type()
)
cmcIpFiltDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltDirection.setStatus("mandatory")
_CmcIpFiltIfIndex_Type = Integer32
_CmcIpFiltIfIndex_Object = MibTableColumn
cmcIpFiltIfIndex = _CmcIpFiltIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 4, 5, 1, 16),
    _CmcIpFiltIfIndex_Type()
)
cmcIpFiltIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpFiltIfIndex.setStatus("mandatory")
_Cmc_ipx_ObjectIdentity = ObjectIdentity
cmc_ipx = _Cmc_ipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5)
)
_Cmc_ipx_ipx_ObjectIdentity = ObjectIdentity
cmc_ipx_ipx = _Cmc_ipx_ipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1)
)
_Cmc_ipx_ipxSystem_ObjectIdentity = ObjectIdentity
cmc_ipx_ipxSystem = _Cmc_ipx_ipxSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1)
)
_IpxSysTable_Object = MibTable
ipxSysTable = _IpxSysTable_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipxSysTable.setStatus("mandatory")
_IpxSysEntry_Object = MibTableRow
ipxSysEntry = _IpxSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1)
)
ipxSysEntry.setIndexNames(
    (0, "CMC-MIB", "ipxSysInstance"),
)
if mibBuilder.loadTexts:
    ipxSysEntry.setStatus("mandatory")
_IpxSysInstance_Type = Integer32
_IpxSysInstance_Object = MibTableColumn
ipxSysInstance = _IpxSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 1),
    _IpxSysInstance_Type()
)
ipxSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSysInstance.setStatus("mandatory")


class _IpxSysExistState_Type(Integer32):
    """Custom type ipxSysExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxSysExistState_Type.__name__ = "Integer32"
_IpxSysExistState_Object = MibTableColumn
ipxSysExistState = _IpxSysExistState_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 2),
    _IpxSysExistState_Type()
)
ipxSysExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSysExistState.setStatus("mandatory")


class _IpxSysIntNetNumExists_Type(Integer32):
    """Custom type ipxSysIntNetNumExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxSysIntNetNumExists_Type.__name__ = "Integer32"
_IpxSysIntNetNumExists_Object = MibTableColumn
ipxSysIntNetNumExists = _IpxSysIntNetNumExists_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 3),
    _IpxSysIntNetNumExists_Type()
)
ipxSysIntNetNumExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysIntNetNumExists.setStatus("mandatory")
_IpxSysIntNetNum_Type = NetNumber
_IpxSysIntNetNum_Object = MibTableColumn
ipxSysIntNetNum = _IpxSysIntNetNum_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 4),
    _IpxSysIntNetNum_Type()
)
ipxSysIntNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSysIntNetNum.setStatus("mandatory")


class _IpxSysName_Type(OctetString):
    """Custom type ipxSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_IpxSysName_Type.__name__ = "OctetString"
_IpxSysName_Object = MibTableColumn
ipxSysName = _IpxSysName_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 5),
    _IpxSysName_Type()
)
ipxSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSysName.setStatus("mandatory")


class _IpxSysMaxPathSplits_Type(Integer32):
    """Custom type ipxSysMaxPathSplits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IpxSysMaxPathSplits_Type.__name__ = "Integer32"
_IpxSysMaxPathSplits_Object = MibTableColumn
ipxSysMaxPathSplits = _IpxSysMaxPathSplits_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 6),
    _IpxSysMaxPathSplits_Type()
)
ipxSysMaxPathSplits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSysMaxPathSplits.setStatus("mandatory")
_IpxSysMaxHops_Type = Integer32
_IpxSysMaxHops_Object = MibTableColumn
ipxSysMaxHops = _IpxSysMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 7),
    _IpxSysMaxHops_Type()
)
ipxSysMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSysMaxHops.setStatus("mandatory")
_IpxSysVersionMajor_Type = Integer32
_IpxSysVersionMajor_Object = MibTableColumn
ipxSysVersionMajor = _IpxSysVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 8),
    _IpxSysVersionMajor_Type()
)
ipxSysVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysVersionMajor.setStatus("mandatory")
_IpxSysVersionMinor_Type = Integer32
_IpxSysVersionMinor_Object = MibTableColumn
ipxSysVersionMinor = _IpxSysVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 9),
    _IpxSysVersionMinor_Type()
)
ipxSysVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysVersionMinor.setStatus("mandatory")
_IpxSysInReceives_Type = Counter32
_IpxSysInReceives_Object = MibTableColumn
ipxSysInReceives = _IpxSysInReceives_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 10),
    _IpxSysInReceives_Type()
)
ipxSysInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysInReceives.setStatus("mandatory")
_IpxSysInTooManyHops_Type = Counter32
_IpxSysInTooManyHops_Object = MibTableColumn
ipxSysInTooManyHops = _IpxSysInTooManyHops_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 11),
    _IpxSysInTooManyHops_Type()
)
ipxSysInTooManyHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysInTooManyHops.setStatus("mandatory")
_IpxSysInHdrErrors_Type = Counter32
_IpxSysInHdrErrors_Object = MibTableColumn
ipxSysInHdrErrors = _IpxSysInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 12),
    _IpxSysInHdrErrors_Type()
)
ipxSysInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysInHdrErrors.setStatus("mandatory")
_IpxSysInUnknownSockets_Type = Counter32
_IpxSysInUnknownSockets_Object = MibTableColumn
ipxSysInUnknownSockets = _IpxSysInUnknownSockets_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 13),
    _IpxSysInUnknownSockets_Type()
)
ipxSysInUnknownSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysInUnknownSockets.setStatus("mandatory")
_IpxSysInFiltered_Type = Counter32
_IpxSysInFiltered_Object = MibTableColumn
ipxSysInFiltered = _IpxSysInFiltered_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 14),
    _IpxSysInFiltered_Type()
)
ipxSysInFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysInFiltered.setStatus("mandatory")
_IpxSysInCompressDiscards_Type = Counter32
_IpxSysInCompressDiscards_Object = MibTableColumn
ipxSysInCompressDiscards = _IpxSysInCompressDiscards_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 15),
    _IpxSysInCompressDiscards_Type()
)
ipxSysInCompressDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysInCompressDiscards.setStatus("mandatory")
_IpxSysInDiscards_Type = Counter32
_IpxSysInDiscards_Object = MibTableColumn
ipxSysInDiscards = _IpxSysInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 16),
    _IpxSysInDiscards_Type()
)
ipxSysInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysInDiscards.setStatus("mandatory")
_IpxSysInDelivers_Type = Counter32
_IpxSysInDelivers_Object = MibTableColumn
ipxSysInDelivers = _IpxSysInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 17),
    _IpxSysInDelivers_Type()
)
ipxSysInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysInDelivers.setStatus("mandatory")
_IpxSysNETBIOSPackets_Type = Counter32
_IpxSysNETBIOSPackets_Object = MibTableColumn
ipxSysNETBIOSPackets = _IpxSysNETBIOSPackets_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 18),
    _IpxSysNETBIOSPackets_Type()
)
ipxSysNETBIOSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysNETBIOSPackets.setStatus("mandatory")
_IpxSysForwPackets_Type = Counter32
_IpxSysForwPackets_Object = MibTableColumn
ipxSysForwPackets = _IpxSysForwPackets_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 19),
    _IpxSysForwPackets_Type()
)
ipxSysForwPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysForwPackets.setStatus("mandatory")
_IpxSysOutRequests_Type = Counter32
_IpxSysOutRequests_Object = MibTableColumn
ipxSysOutRequests = _IpxSysOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 20),
    _IpxSysOutRequests_Type()
)
ipxSysOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysOutRequests.setStatus("mandatory")
_IpxSysOutNoRoutes_Type = Counter32
_IpxSysOutNoRoutes_Object = MibTableColumn
ipxSysOutNoRoutes = _IpxSysOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 21),
    _IpxSysOutNoRoutes_Type()
)
ipxSysOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysOutNoRoutes.setStatus("mandatory")
_IpxSysOutFiltered_Type = Counter32
_IpxSysOutFiltered_Object = MibTableColumn
ipxSysOutFiltered = _IpxSysOutFiltered_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 22),
    _IpxSysOutFiltered_Type()
)
ipxSysOutFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysOutFiltered.setStatus("mandatory")
_IpxSysOutCompressDiscards_Type = Counter32
_IpxSysOutCompressDiscards_Object = MibTableColumn
ipxSysOutCompressDiscards = _IpxSysOutCompressDiscards_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 23),
    _IpxSysOutCompressDiscards_Type()
)
ipxSysOutCompressDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysOutCompressDiscards.setStatus("mandatory")
_IpxSysOutMalformedRequests_Type = Counter32
_IpxSysOutMalformedRequests_Object = MibTableColumn
ipxSysOutMalformedRequests = _IpxSysOutMalformedRequests_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 24),
    _IpxSysOutMalformedRequests_Type()
)
ipxSysOutMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysOutMalformedRequests.setStatus("mandatory")
_IpxSysOutDiscards_Type = Counter32
_IpxSysOutDiscards_Object = MibTableColumn
ipxSysOutDiscards = _IpxSysOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 25),
    _IpxSysOutDiscards_Type()
)
ipxSysOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysOutDiscards.setStatus("mandatory")
_IpxSysOutPackets_Type = Counter32
_IpxSysOutPackets_Object = MibTableColumn
ipxSysOutPackets = _IpxSysOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 26),
    _IpxSysOutPackets_Type()
)
ipxSysOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysOutPackets.setStatus("mandatory")
_IpxSysCircCount_Type = Counter32
_IpxSysCircCount_Object = MibTableColumn
ipxSysCircCount = _IpxSysCircCount_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 27),
    _IpxSysCircCount_Type()
)
ipxSysCircCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysCircCount.setStatus("mandatory")
_IpxSysDestCount_Type = Counter32
_IpxSysDestCount_Object = MibTableColumn
ipxSysDestCount = _IpxSysDestCount_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 28),
    _IpxSysDestCount_Type()
)
ipxSysDestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysDestCount.setStatus("mandatory")
_IpxSysServCount_Type = Counter32
_IpxSysServCount_Object = MibTableColumn
ipxSysServCount = _IpxSysServCount_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 29),
    _IpxSysServCount_Type()
)
ipxSysServCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysServCount.setStatus("mandatory")
_IpxSysResourceFailures_Type = Counter32
_IpxSysResourceFailures_Object = MibTableColumn
ipxSysResourceFailures = _IpxSysResourceFailures_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 30),
    _IpxSysResourceFailures_Type()
)
ipxSysResourceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysResourceFailures.setStatus("mandatory")
_IpxSysConfigSockets_Type = Counter32
_IpxSysConfigSockets_Object = MibTableColumn
ipxSysConfigSockets = _IpxSysConfigSockets_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 31),
    _IpxSysConfigSockets_Type()
)
ipxSysConfigSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysConfigSockets.setStatus("mandatory")
_IpxSysMaxOpenSockets_Type = Counter32
_IpxSysMaxOpenSockets_Object = MibTableColumn
ipxSysMaxOpenSockets = _IpxSysMaxOpenSockets_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 32),
    _IpxSysMaxOpenSockets_Type()
)
ipxSysMaxOpenSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysMaxOpenSockets.setStatus("mandatory")
_IpxSysOpenSocketFails_Type = Counter32
_IpxSysOpenSocketFails_Object = MibTableColumn
ipxSysOpenSocketFails = _IpxSysOpenSocketFails_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 1, 1, 1, 33),
    _IpxSysOpenSocketFails_Type()
)
ipxSysOpenSocketFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysOpenSocketFails.setStatus("mandatory")
_Cmc_ipx_ipxCircuit_ObjectIdentity = ObjectIdentity
cmc_ipx_ipxCircuit = _Cmc_ipx_ipxCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2)
)
_IpxCircTable_Object = MibTable
ipxCircTable = _IpxCircTable_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipxCircTable.setStatus("mandatory")
_IpxCircEntry_Object = MibTableRow
ipxCircEntry = _IpxCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1)
)
ipxCircEntry.setIndexNames(
    (0, "CMC-MIB", "ipxCircSysInstance"),
    (0, "CMC-MIB", "ipxCircIndex"),
)
if mibBuilder.loadTexts:
    ipxCircEntry.setStatus("mandatory")
_IpxCircSysInstance_Type = Integer32
_IpxCircSysInstance_Object = MibTableColumn
ipxCircSysInstance = _IpxCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 1),
    _IpxCircSysInstance_Type()
)
ipxCircSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircSysInstance.setStatus("mandatory")
_IpxCircIndex_Type = Integer32
_IpxCircIndex_Object = MibTableColumn
ipxCircIndex = _IpxCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 2),
    _IpxCircIndex_Type()
)
ipxCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircIndex.setStatus("mandatory")


class _IpxCircExistState_Type(Integer32):
    """Custom type ipxCircExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxCircExistState_Type.__name__ = "Integer32"
_IpxCircExistState_Object = MibTableColumn
ipxCircExistState = _IpxCircExistState_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 3),
    _IpxCircExistState_Type()
)
ipxCircExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircExistState.setStatus("mandatory")


class _IpxCircOperState_Type(Integer32):
    """Custom type ipxCircOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxCircOperState_Type.__name__ = "Integer32"
_IpxCircOperState_Object = MibTableColumn
ipxCircOperState = _IpxCircOperState_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 4),
    _IpxCircOperState_Type()
)
ipxCircOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircOperState.setStatus("mandatory")
_IpxCircIfIndex_Type = Integer32
_IpxCircIfIndex_Object = MibTableColumn
ipxCircIfIndex = _IpxCircIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 5),
    _IpxCircIfIndex_Type()
)
ipxCircIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircIfIndex.setStatus("mandatory")


class _IpxCircName_Type(OctetString):
    """Custom type ipxCircName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IpxCircName_Type.__name__ = "OctetString"
_IpxCircName_Object = MibTableColumn
ipxCircName = _IpxCircName_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 6),
    _IpxCircName_Type()
)
ipxCircName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircName.setStatus("mandatory")


class _IpxCircInfo_Type(OctetString):
    """Custom type ipxCircInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IpxCircInfo_Type.__name__ = "OctetString"
_IpxCircInfo_Object = MibTableColumn
ipxCircInfo = _IpxCircInfo_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 7),
    _IpxCircInfo_Type()
)
ipxCircInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircInfo.setStatus("mandatory")


class _IpxCircType_Type(Integer32):
    """Custom type ipxCircType based on Integer32"""
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
        *(("broadcast", 2),
          ("dynamic", 6),
          ("other", 1),
          ("ptTopt", 3),
          ("unnumberedRIP", 5),
          ("wanRIP", 4),
          ("wanWS", 7))
    )


_IpxCircType_Type.__name__ = "Integer32"
_IpxCircType_Object = MibTableColumn
ipxCircType = _IpxCircType_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 8),
    _IpxCircType_Type()
)
ipxCircType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircType.setStatus("mandatory")
_IpxCircLocalMaxPacketSize_Type = Integer32
_IpxCircLocalMaxPacketSize_Object = MibTableColumn
ipxCircLocalMaxPacketSize = _IpxCircLocalMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 9),
    _IpxCircLocalMaxPacketSize_Type()
)
ipxCircLocalMaxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircLocalMaxPacketSize.setStatus("mandatory")


class _IpxCircCompressState_Type(Integer32):
    """Custom type ipxCircCompressState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxCircCompressState_Type.__name__ = "Integer32"
_IpxCircCompressState_Object = MibTableColumn
ipxCircCompressState = _IpxCircCompressState_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 10),
    _IpxCircCompressState_Type()
)
ipxCircCompressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircCompressState.setStatus("mandatory")
_IpxCircCompressSlots_Type = Integer32
_IpxCircCompressSlots_Object = MibTableColumn
ipxCircCompressSlots = _IpxCircCompressSlots_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 11),
    _IpxCircCompressSlots_Type()
)
ipxCircCompressSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircCompressSlots.setStatus("mandatory")
_IpxCircCompressedSent_Type = Counter32
_IpxCircCompressedSent_Object = MibTableColumn
ipxCircCompressedSent = _IpxCircCompressedSent_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 12),
    _IpxCircCompressedSent_Type()
)
ipxCircCompressedSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircCompressedSent.setStatus("mandatory")
_IpxCircUncompressedSent_Type = Counter32
_IpxCircUncompressedSent_Object = MibTableColumn
ipxCircUncompressedSent = _IpxCircUncompressedSent_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 13),
    _IpxCircUncompressedSent_Type()
)
ipxCircUncompressedSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircUncompressedSent.setStatus("mandatory")


class _IpxCircMediaType_Type(OctetString):
    """Custom type ipxCircMediaType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxCircMediaType_Type.__name__ = "OctetString"
_IpxCircMediaType_Object = MibTableColumn
ipxCircMediaType = _IpxCircMediaType_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 14),
    _IpxCircMediaType_Type()
)
ipxCircMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircMediaType.setStatus("mandatory")
_IpxCircNetNumber_Type = NetNumber
_IpxCircNetNumber_Object = MibTableColumn
ipxCircNetNumber = _IpxCircNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 15),
    _IpxCircNetNumber_Type()
)
ipxCircNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircNetNumber.setStatus("mandatory")
_IpxCircStateChanges_Type = Counter32
_IpxCircStateChanges_Object = MibTableColumn
ipxCircStateChanges = _IpxCircStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 16),
    _IpxCircStateChanges_Type()
)
ipxCircStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircStateChanges.setStatus("mandatory")
_IpxCircInitFails_Type = Counter32
_IpxCircInitFails_Object = MibTableColumn
ipxCircInitFails = _IpxCircInitFails_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 17),
    _IpxCircInitFails_Type()
)
ipxCircInitFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircInitFails.setStatus("mandatory")
_IpxCircDelay_Type = Integer32
_IpxCircDelay_Object = MibTableColumn
ipxCircDelay = _IpxCircDelay_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 18),
    _IpxCircDelay_Type()
)
ipxCircDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircDelay.setStatus("mandatory")
_IpxCircThroughput_Type = Integer32
_IpxCircThroughput_Object = MibTableColumn
ipxCircThroughput = _IpxCircThroughput_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 2, 1, 1, 19),
    _IpxCircThroughput_Type()
)
ipxCircThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircThroughput.setStatus("mandatory")
_Cmc_ipx_ipxForwarding_ObjectIdentity = ObjectIdentity
cmc_ipx_ipxForwarding = _Cmc_ipx_ipxForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 3)
)
_IpxDestTable_Object = MibTable
ipxDestTable = _IpxDestTable_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ipxDestTable.setStatus("mandatory")
_IpxDestEntry_Object = MibTableRow
ipxDestEntry = _IpxDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 3, 1, 1)
)
ipxDestEntry.setIndexNames(
    (0, "CMC-MIB", "ipxDestSysInstance"),
    (0, "CMC-MIB", "ipxDestNetNum"),
)
if mibBuilder.loadTexts:
    ipxDestEntry.setStatus("mandatory")
_IpxDestSysInstance_Type = Integer32
_IpxDestSysInstance_Object = MibTableColumn
ipxDestSysInstance = _IpxDestSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 3, 1, 1, 1),
    _IpxDestSysInstance_Type()
)
ipxDestSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestSysInstance.setStatus("mandatory")
_IpxDestNetNum_Type = NetNumber
_IpxDestNetNum_Object = MibTableColumn
ipxDestNetNum = _IpxDestNetNum_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 3, 1, 1, 2),
    _IpxDestNetNum_Type()
)
ipxDestNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNetNum.setStatus("mandatory")


class _IpxDestProtocol_Type(Integer32):
    """Custom type ipxDestProtocol based on Integer32"""
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
        *(("local", 2),
          ("nlsp", 4),
          ("other", 1),
          ("rip", 3),
          ("static", 5))
    )


_IpxDestProtocol_Type.__name__ = "Integer32"
_IpxDestProtocol_Object = MibTableColumn
ipxDestProtocol = _IpxDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 3, 1, 1, 3),
    _IpxDestProtocol_Type()
)
ipxDestProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestProtocol.setStatus("mandatory")
_IpxDestCost_Type = Integer32
_IpxDestCost_Object = MibTableColumn
ipxDestCost = _IpxDestCost_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 3, 1, 1, 4),
    _IpxDestCost_Type()
)
ipxDestCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestCost.setStatus("mandatory")
_IpxDestHopCount_Type = Integer32
_IpxDestHopCount_Object = MibTableColumn
ipxDestHopCount = _IpxDestHopCount_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 3, 1, 1, 5),
    _IpxDestHopCount_Type()
)
ipxDestHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestHopCount.setStatus("mandatory")
_IpxDestNextHopCircIndex_Type = Integer32
_IpxDestNextHopCircIndex_Object = MibTableColumn
ipxDestNextHopCircIndex = _IpxDestNextHopCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 3, 1, 1, 6),
    _IpxDestNextHopCircIndex_Type()
)
ipxDestNextHopCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNextHopCircIndex.setStatus("mandatory")
_IpxDestNextHopNICAddress_Type = OctetString
_IpxDestNextHopNICAddress_Object = MibTableColumn
ipxDestNextHopNICAddress = _IpxDestNextHopNICAddress_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 3, 1, 1, 7),
    _IpxDestNextHopNICAddress_Type()
)
ipxDestNextHopNICAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNextHopNICAddress.setStatus("mandatory")
_IpxDestNextHopNetNum_Type = NetNumber
_IpxDestNextHopNetNum_Object = MibTableColumn
ipxDestNextHopNetNum = _IpxDestNextHopNetNum_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 3, 1, 1, 8),
    _IpxDestNextHopNetNum_Type()
)
ipxDestNextHopNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNextHopNetNum.setStatus("mandatory")


class _IpxDestType_Type(Integer32):
    """Custom type ipxDestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("network", 5),
          ("nlspLevel1Router", 2),
          ("router", 4),
          ("unknown", 1))
    )


_IpxDestType_Type.__name__ = "Integer32"
_IpxDestType_Object = MibTableColumn
ipxDestType = _IpxDestType_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 3, 1, 1, 9),
    _IpxDestType_Type()
)
ipxDestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestType.setStatus("mandatory")
_Cmc_ipx_ipxServices_ObjectIdentity = ObjectIdentity
cmc_ipx_ipxServices = _Cmc_ipx_ipxServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 4)
)
_IpxServTable_Object = MibTable
ipxServTable = _IpxServTable_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipxServTable.setStatus("mandatory")
_IpxServEntry_Object = MibTableRow
ipxServEntry = _IpxServEntry_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 4, 1, 1)
)
ipxServEntry.setIndexNames(
    (0, "CMC-MIB", "ipxServSysInstance"),
    (0, "CMC-MIB", "ipxServName"),
    (0, "CMC-MIB", "ipxServTypeValue"),
)
if mibBuilder.loadTexts:
    ipxServEntry.setStatus("mandatory")
_IpxServSysInstance_Type = Integer32
_IpxServSysInstance_Object = MibTableColumn
ipxServSysInstance = _IpxServSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 4, 1, 1, 1),
    _IpxServSysInstance_Type()
)
ipxServSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServSysInstance.setStatus("mandatory")


class _IpxServName_Type(OctetString):
    """Custom type ipxServName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IpxServName_Type.__name__ = "OctetString"
_IpxServName_Object = MibTableColumn
ipxServName = _IpxServName_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 4, 1, 1, 2),
    _IpxServName_Type()
)
ipxServName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServName.setStatus("mandatory")


class _IpxServTypeValue_Type(OctetString):
    """Custom type ipxServTypeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxServTypeValue_Type.__name__ = "OctetString"
_IpxServTypeValue_Object = MibTableColumn
ipxServTypeValue = _IpxServTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 4, 1, 1, 3),
    _IpxServTypeValue_Type()
)
ipxServTypeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServTypeValue.setStatus("mandatory")


class _IpxServType_Type(Integer32):
    """Custom type ipxServType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unknown", 1)
    )


_IpxServType_Type.__name__ = "Integer32"
_IpxServType_Object = MibTableColumn
ipxServType = _IpxServType_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 4, 1, 1, 4),
    _IpxServType_Type()
)
ipxServType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServType.setStatus("mandatory")


class _IpxServProtocol_Type(Integer32):
    """Custom type ipxServProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("nlsp", 4),
          ("other", 1),
          ("sap", 6),
          ("static", 5))
    )


_IpxServProtocol_Type.__name__ = "Integer32"
_IpxServProtocol_Object = MibTableColumn
ipxServProtocol = _IpxServProtocol_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 4, 1, 1, 5),
    _IpxServProtocol_Type()
)
ipxServProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServProtocol.setStatus("mandatory")
_IpxServNetNum_Type = NetNumber
_IpxServNetNum_Object = MibTableColumn
ipxServNetNum = _IpxServNetNum_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 4, 1, 1, 6),
    _IpxServNetNum_Type()
)
ipxServNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServNetNum.setStatus("mandatory")


class _IpxServNode_Type(OctetString):
    """Custom type ipxServNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxServNode_Type.__name__ = "OctetString"
_IpxServNode_Object = MibTableColumn
ipxServNode = _IpxServNode_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 4, 1, 1, 7),
    _IpxServNode_Type()
)
ipxServNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServNode.setStatus("mandatory")


class _IpxServSocket_Type(OctetString):
    """Custom type ipxServSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxServSocket_Type.__name__ = "OctetString"
_IpxServSocket_Object = MibTableColumn
ipxServSocket = _IpxServSocket_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 1, 4, 1, 1, 8),
    _IpxServSocket_Type()
)
ipxServSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServSocket.setStatus("mandatory")
_Cmc_ipx_filter_ObjectIdentity = ObjectIdentity
cmc_ipx_filter = _Cmc_ipx_filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2)
)


class _CmcIpxFiltStatus_Type(Integer32):
    """Custom type cmcIpxFiltStatus based on Integer32"""
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


_CmcIpxFiltStatus_Type.__name__ = "Integer32"
_CmcIpxFiltStatus_Object = MibScalar
cmcIpxFiltStatus = _CmcIpxFiltStatus_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 1),
    _CmcIpxFiltStatus_Type()
)
cmcIpxFiltStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltStatus.setStatus("mandatory")
_Cmc_ipx_filt_packet_ObjectIdentity = ObjectIdentity
cmc_ipx_filt_packet = _Cmc_ipx_filt_packet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 2)
)
_CmcIpxFilterTable_Object = MibTable
cmcIpxFilterTable = _CmcIpxFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cmcIpxFilterTable.setStatus("mandatory")
_CmcIpxFiltEntry_Object = MibTableRow
cmcIpxFiltEntry = _CmcIpxFiltEntry_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 2, 1, 1)
)
cmcIpxFiltEntry.setIndexNames(
    (0, "CMC-MIB", "cmcIpxFiltName"),
)
if mibBuilder.loadTexts:
    cmcIpxFiltEntry.setStatus("mandatory")
_CmcIpxFiltName_Type = OctetString
_CmcIpxFiltName_Object = MibTableColumn
cmcIpxFiltName = _CmcIpxFiltName_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 2, 1, 1, 1),
    _CmcIpxFiltName_Type()
)
cmcIpxFiltName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltName.setStatus("mandatory")
_CmcIpxFiltSAddr_Type = IpxAddress
_CmcIpxFiltSAddr_Object = MibTableColumn
cmcIpxFiltSAddr = _CmcIpxFiltSAddr_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 2, 1, 1, 2),
    _CmcIpxFiltSAddr_Type()
)
cmcIpxFiltSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltSAddr.setStatus("mandatory")
_CmcIpxFiltDAddr_Type = IpxAddress
_CmcIpxFiltDAddr_Object = MibTableColumn
cmcIpxFiltDAddr = _CmcIpxFiltDAddr_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 2, 1, 1, 3),
    _CmcIpxFiltDAddr_Type()
)
cmcIpxFiltDAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltDAddr.setStatus("mandatory")
_CmcIpxFiltPktType_Type = Integer32
_CmcIpxFiltPktType_Object = MibTableColumn
cmcIpxFiltPktType = _CmcIpxFiltPktType_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 2, 1, 1, 4),
    _CmcIpxFiltPktType_Type()
)
cmcIpxFiltPktType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltPktType.setStatus("mandatory")


class _CmcIpxFiltMode_Type(Integer32):
    """Custom type cmcIpxFiltMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2),
          ("nodial", 3))
    )


_CmcIpxFiltMode_Type.__name__ = "Integer32"
_CmcIpxFiltMode_Object = MibTableColumn
cmcIpxFiltMode = _CmcIpxFiltMode_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 2, 1, 1, 5),
    _CmcIpxFiltMode_Type()
)
cmcIpxFiltMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltMode.setStatus("mandatory")


class _CmcIpxFiltType_Type(Integer32):
    """Custom type cmcIpxFiltType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("local", 1),
          ("netmgmt", 3))
    )


_CmcIpxFiltType_Type.__name__ = "Integer32"
_CmcIpxFiltType_Object = MibTableColumn
cmcIpxFiltType = _CmcIpxFiltType_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 2, 1, 1, 6),
    _CmcIpxFiltType_Type()
)
cmcIpxFiltType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltType.setStatus("mandatory")
_CmcIpxFiltMoveOper_Type = OctetString
_CmcIpxFiltMoveOper_Object = MibTableColumn
cmcIpxFiltMoveOper = _CmcIpxFiltMoveOper_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 2, 1, 1, 7),
    _CmcIpxFiltMoveOper_Type()
)
cmcIpxFiltMoveOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltMoveOper.setStatus("mandatory")
_CmcIpxFiltUseCount_Type = Integer32
_CmcIpxFiltUseCount_Object = MibTableColumn
cmcIpxFiltUseCount = _CmcIpxFiltUseCount_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 2, 1, 1, 8),
    _CmcIpxFiltUseCount_Type()
)
cmcIpxFiltUseCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltUseCount.setStatus("mandatory")


class _CmcIpxFiltDirection_Type(Integer32):
    """Custom type cmcIpxFiltDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("incoming", 2),
          ("outgoing", 3))
    )


_CmcIpxFiltDirection_Type.__name__ = "Integer32"
_CmcIpxFiltDirection_Object = MibTableColumn
cmcIpxFiltDirection = _CmcIpxFiltDirection_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 2, 1, 1, 9),
    _CmcIpxFiltDirection_Type()
)
cmcIpxFiltDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltDirection.setStatus("mandatory")
_CmcIpxFiltIfIndex_Type = Integer32
_CmcIpxFiltIfIndex_Object = MibTableColumn
cmcIpxFiltIfIndex = _CmcIpxFiltIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 2, 1, 1, 10),
    _CmcIpxFiltIfIndex_Type()
)
cmcIpxFiltIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltIfIndex.setStatus("mandatory")
_CmcIpxFiltPriority_Type = Integer32
_CmcIpxFiltPriority_Object = MibTableColumn
cmcIpxFiltPriority = _CmcIpxFiltPriority_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 2, 1, 1, 11),
    _CmcIpxFiltPriority_Type()
)
cmcIpxFiltPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIpxFiltPriority.setStatus("mandatory")


class _CmcIpxFiltState_Type(Integer32):
    """Custom type cmcIpxFiltState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmcIpxFiltState_Type.__name__ = "Integer32"
_CmcIpxFiltState_Object = MibTableColumn
cmcIpxFiltState = _CmcIpxFiltState_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 2, 1, 1, 12),
    _CmcIpxFiltState_Type()
)
cmcIpxFiltState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltState.setStatus("mandatory")


class _CmcIpxFiltRIPStatus_Type(Integer32):
    """Custom type cmcIpxFiltRIPStatus based on Integer32"""
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


_CmcIpxFiltRIPStatus_Type.__name__ = "Integer32"
_CmcIpxFiltRIPStatus_Object = MibScalar
cmcIpxFiltRIPStatus = _CmcIpxFiltRIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 3),
    _CmcIpxFiltRIPStatus_Type()
)
cmcIpxFiltRIPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltRIPStatus.setStatus("mandatory")
_Cmc_ipx_filt_rip_ObjectIdentity = ObjectIdentity
cmc_ipx_filt_rip = _Cmc_ipx_filt_rip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 4)
)
_CmcIpxFilterRIPTable_Object = MibTable
cmcIpxFilterRIPTable = _CmcIpxFilterRIPTable_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cmcIpxFilterRIPTable.setStatus("mandatory")
_CmcIpxFiltRIPEntry_Object = MibTableRow
cmcIpxFiltRIPEntry = _CmcIpxFiltRIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 4, 1, 1)
)
cmcIpxFiltRIPEntry.setIndexNames(
    (0, "CMC-MIB", "cmcIpxFiltRIPName"),
)
if mibBuilder.loadTexts:
    cmcIpxFiltRIPEntry.setStatus("mandatory")
_CmcIpxFiltRIPName_Type = OctetString
_CmcIpxFiltRIPName_Object = MibTableColumn
cmcIpxFiltRIPName = _CmcIpxFiltRIPName_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 4, 1, 1, 1),
    _CmcIpxFiltRIPName_Type()
)
cmcIpxFiltRIPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltRIPName.setStatus("mandatory")
_CmcIpxFiltRIPNetworkNum_Type = NetNumber
_CmcIpxFiltRIPNetworkNum_Object = MibTableColumn
cmcIpxFiltRIPNetworkNum = _CmcIpxFiltRIPNetworkNum_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 4, 1, 1, 2),
    _CmcIpxFiltRIPNetworkNum_Type()
)
cmcIpxFiltRIPNetworkNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltRIPNetworkNum.setStatus("mandatory")
_CmcIpxFiltRIPMoveOper_Type = OctetString
_CmcIpxFiltRIPMoveOper_Object = MibTableColumn
cmcIpxFiltRIPMoveOper = _CmcIpxFiltRIPMoveOper_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 4, 1, 1, 3),
    _CmcIpxFiltRIPMoveOper_Type()
)
cmcIpxFiltRIPMoveOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltRIPMoveOper.setStatus("mandatory")


class _CmcIpxFiltRIPMode_Type(Integer32):
    """Custom type cmcIpxFiltRIPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2),
          ("nodial", 3))
    )


_CmcIpxFiltRIPMode_Type.__name__ = "Integer32"
_CmcIpxFiltRIPMode_Object = MibTableColumn
cmcIpxFiltRIPMode = _CmcIpxFiltRIPMode_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 4, 1, 1, 4),
    _CmcIpxFiltRIPMode_Type()
)
cmcIpxFiltRIPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltRIPMode.setStatus("mandatory")


class _CmcIpxFiltRIPType_Type(Integer32):
    """Custom type cmcIpxFiltRIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("local", 1),
          ("netmgmt", 3))
    )


_CmcIpxFiltRIPType_Type.__name__ = "Integer32"
_CmcIpxFiltRIPType_Object = MibTableColumn
cmcIpxFiltRIPType = _CmcIpxFiltRIPType_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 4, 1, 1, 5),
    _CmcIpxFiltRIPType_Type()
)
cmcIpxFiltRIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltRIPType.setStatus("mandatory")
_CmcIpxFiltRIPUseCount_Type = Integer32
_CmcIpxFiltRIPUseCount_Object = MibTableColumn
cmcIpxFiltRIPUseCount = _CmcIpxFiltRIPUseCount_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 4, 1, 1, 6),
    _CmcIpxFiltRIPUseCount_Type()
)
cmcIpxFiltRIPUseCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltRIPUseCount.setStatus("mandatory")


class _CmcIpxFiltRIPDirection_Type(Integer32):
    """Custom type cmcIpxFiltRIPDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("incoming", 2),
          ("outgoing", 3))
    )


_CmcIpxFiltRIPDirection_Type.__name__ = "Integer32"
_CmcIpxFiltRIPDirection_Object = MibTableColumn
cmcIpxFiltRIPDirection = _CmcIpxFiltRIPDirection_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 4, 1, 1, 7),
    _CmcIpxFiltRIPDirection_Type()
)
cmcIpxFiltRIPDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltRIPDirection.setStatus("mandatory")


class _CmcIpxFiltRIPQueryType_Type(Integer32):
    """Custom type cmcIpxFiltRIPQueryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("request", 1),
          ("response", 2))
    )


_CmcIpxFiltRIPQueryType_Type.__name__ = "Integer32"
_CmcIpxFiltRIPQueryType_Object = MibTableColumn
cmcIpxFiltRIPQueryType = _CmcIpxFiltRIPQueryType_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 4, 1, 1, 8),
    _CmcIpxFiltRIPQueryType_Type()
)
cmcIpxFiltRIPQueryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltRIPQueryType.setStatus("mandatory")
_CmcIpxFiltRIPIfIndex_Type = Integer32
_CmcIpxFiltRIPIfIndex_Object = MibTableColumn
cmcIpxFiltRIPIfIndex = _CmcIpxFiltRIPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 4, 1, 1, 9),
    _CmcIpxFiltRIPIfIndex_Type()
)
cmcIpxFiltRIPIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltRIPIfIndex.setStatus("mandatory")
_CmcIpxFiltRIPPriority_Type = Integer32
_CmcIpxFiltRIPPriority_Object = MibTableColumn
cmcIpxFiltRIPPriority = _CmcIpxFiltRIPPriority_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 4, 1, 1, 10),
    _CmcIpxFiltRIPPriority_Type()
)
cmcIpxFiltRIPPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIpxFiltRIPPriority.setStatus("mandatory")


class _CmcIpxFiltRIPState_Type(Integer32):
    """Custom type cmcIpxFiltRIPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmcIpxFiltRIPState_Type.__name__ = "Integer32"
_CmcIpxFiltRIPState_Object = MibTableColumn
cmcIpxFiltRIPState = _CmcIpxFiltRIPState_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 4, 1, 1, 11),
    _CmcIpxFiltRIPState_Type()
)
cmcIpxFiltRIPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltRIPState.setStatus("mandatory")


class _CmcIpxFiltSAPStatus_Type(Integer32):
    """Custom type cmcIpxFiltSAPStatus based on Integer32"""
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


_CmcIpxFiltSAPStatus_Type.__name__ = "Integer32"
_CmcIpxFiltSAPStatus_Object = MibScalar
cmcIpxFiltSAPStatus = _CmcIpxFiltSAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 5),
    _CmcIpxFiltSAPStatus_Type()
)
cmcIpxFiltSAPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltSAPStatus.setStatus("mandatory")
_Cmc_ipx_filt_sap_ObjectIdentity = ObjectIdentity
cmc_ipx_filt_sap = _Cmc_ipx_filt_sap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 6)
)
_CmcIpxFilterSAPTable_Object = MibTable
cmcIpxFilterSAPTable = _CmcIpxFilterSAPTable_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cmcIpxFilterSAPTable.setStatus("mandatory")
_CmcIpxFiltSAPEntry_Object = MibTableRow
cmcIpxFiltSAPEntry = _CmcIpxFiltSAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 6, 1, 1)
)
cmcIpxFiltSAPEntry.setIndexNames(
    (0, "CMC-MIB", "cmcIpxFiltSAPName"),
)
if mibBuilder.loadTexts:
    cmcIpxFiltSAPEntry.setStatus("mandatory")
_CmcIpxFiltSAPName_Type = OctetString
_CmcIpxFiltSAPName_Object = MibTableColumn
cmcIpxFiltSAPName = _CmcIpxFiltSAPName_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 6, 1, 1, 1),
    _CmcIpxFiltSAPName_Type()
)
cmcIpxFiltSAPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltSAPName.setStatus("mandatory")
_CmcIpxFiltSAPServerName_Type = OctetString
_CmcIpxFiltSAPServerName_Object = MibTableColumn
cmcIpxFiltSAPServerName = _CmcIpxFiltSAPServerName_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 6, 1, 1, 2),
    _CmcIpxFiltSAPServerName_Type()
)
cmcIpxFiltSAPServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltSAPServerName.setStatus("mandatory")
_CmcIpxFiltSAPServerType_Type = Integer32
_CmcIpxFiltSAPServerType_Object = MibTableColumn
cmcIpxFiltSAPServerType = _CmcIpxFiltSAPServerType_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 6, 1, 1, 3),
    _CmcIpxFiltSAPServerType_Type()
)
cmcIpxFiltSAPServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltSAPServerType.setStatus("mandatory")
_CmcIpxFiltSAPMoveOper_Type = OctetString
_CmcIpxFiltSAPMoveOper_Object = MibTableColumn
cmcIpxFiltSAPMoveOper = _CmcIpxFiltSAPMoveOper_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 6, 1, 1, 4),
    _CmcIpxFiltSAPMoveOper_Type()
)
cmcIpxFiltSAPMoveOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltSAPMoveOper.setStatus("mandatory")


class _CmcIpxFiltSAPMode_Type(Integer32):
    """Custom type cmcIpxFiltSAPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2),
          ("nodial", 3))
    )


_CmcIpxFiltSAPMode_Type.__name__ = "Integer32"
_CmcIpxFiltSAPMode_Object = MibTableColumn
cmcIpxFiltSAPMode = _CmcIpxFiltSAPMode_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 6, 1, 1, 5),
    _CmcIpxFiltSAPMode_Type()
)
cmcIpxFiltSAPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltSAPMode.setStatus("mandatory")


class _CmcIpxFiltSAPType_Type(Integer32):
    """Custom type cmcIpxFiltSAPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("local", 1),
          ("netmgmt", 3))
    )


_CmcIpxFiltSAPType_Type.__name__ = "Integer32"
_CmcIpxFiltSAPType_Object = MibTableColumn
cmcIpxFiltSAPType = _CmcIpxFiltSAPType_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 6, 1, 1, 6),
    _CmcIpxFiltSAPType_Type()
)
cmcIpxFiltSAPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltSAPType.setStatus("mandatory")
_CmcIpxFiltSAPUseCount_Type = Integer32
_CmcIpxFiltSAPUseCount_Object = MibTableColumn
cmcIpxFiltSAPUseCount = _CmcIpxFiltSAPUseCount_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 6, 1, 1, 7),
    _CmcIpxFiltSAPUseCount_Type()
)
cmcIpxFiltSAPUseCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltSAPUseCount.setStatus("mandatory")


class _CmcIpxFiltSAPDirection_Type(Integer32):
    """Custom type cmcIpxFiltSAPDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("incoming", 2),
          ("outgoing", 3))
    )


_CmcIpxFiltSAPDirection_Type.__name__ = "Integer32"
_CmcIpxFiltSAPDirection_Object = MibTableColumn
cmcIpxFiltSAPDirection = _CmcIpxFiltSAPDirection_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 6, 1, 1, 8),
    _CmcIpxFiltSAPDirection_Type()
)
cmcIpxFiltSAPDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltSAPDirection.setStatus("mandatory")


class _CmcIpxFiltSAPQueryType_Type(Integer32):
    """Custom type cmcIpxFiltSAPQueryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("request", 1),
          ("response", 2))
    )


_CmcIpxFiltSAPQueryType_Type.__name__ = "Integer32"
_CmcIpxFiltSAPQueryType_Object = MibTableColumn
cmcIpxFiltSAPQueryType = _CmcIpxFiltSAPQueryType_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 6, 1, 1, 9),
    _CmcIpxFiltSAPQueryType_Type()
)
cmcIpxFiltSAPQueryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltSAPQueryType.setStatus("mandatory")
_CmcIpxFiltSAPIfIndex_Type = Integer32
_CmcIpxFiltSAPIfIndex_Object = MibTableColumn
cmcIpxFiltSAPIfIndex = _CmcIpxFiltSAPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 6, 1, 1, 10),
    _CmcIpxFiltSAPIfIndex_Type()
)
cmcIpxFiltSAPIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltSAPIfIndex.setStatus("mandatory")
_CmcIpxFiltSAPPriority_Type = Integer32
_CmcIpxFiltSAPPriority_Object = MibTableColumn
cmcIpxFiltSAPPriority = _CmcIpxFiltSAPPriority_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 6, 1, 1, 11),
    _CmcIpxFiltSAPPriority_Type()
)
cmcIpxFiltSAPPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcIpxFiltSAPPriority.setStatus("mandatory")


class _CmcIpxFiltSAPState_Type(Integer32):
    """Custom type cmcIpxFiltSAPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmcIpxFiltSAPState_Type.__name__ = "Integer32"
_CmcIpxFiltSAPState_Object = MibTableColumn
cmcIpxFiltSAPState = _CmcIpxFiltSAPState_Object(
    (1, 3, 6, 1, 4, 1, 44, 2, 1, 5, 2, 6, 1, 1, 12),
    _CmcIpxFiltSAPState_Type()
)
cmcIpxFiltSAPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcIpxFiltSAPState.setStatus("mandatory")
_Cmc_trapA_ObjectIdentity = ObjectIdentity
cmc_trapA = _Cmc_trapA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 6)
)
_Cmc_trapB_ObjectIdentity = ObjectIdentity
cmc_trapB = _Cmc_trapB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 6, 6)
)
_Cmc_trapC_ObjectIdentity = ObjectIdentity
cmc_trapC = _Cmc_trapC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 6, 6, 5)
)
_Cmc_trapD_ObjectIdentity = ObjectIdentity
cmc_trapD = _Cmc_trapD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 6, 6, 5, 3)
)
_Cmc_trapE_ObjectIdentity = ObjectIdentity
cmc_trapE = _Cmc_trapE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44, 2, 6, 6, 5, 3, 10)
)

# Managed Objects groups


# Notification objects

cmcConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 44, 2, 6, 6, 5, 3, 10, 0, 1)
)
if mibBuilder.loadTexts:
    cmcConnectionEstablished.setStatus(
        ""
    )

cmcConnectionTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 44, 2, 6, 6, 5, 3, 10, 0, 2)
)
if mibBuilder.loadTexts:
    cmcConnectionTerminated.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CMC-MIB",
    **{"NetNumber": NetNumber,
       "IpxAddress": IpxAddress,
       "cmc": cmc,
       "cmc-prod": cmc_prod,
       "cmc-adapt": cmc_adapt,
       "cmc-system": cmc_system,
       "cmc-soft": cmc_soft,
       "cmc-mgmt": cmc_mgmt,
       "cmc-mib": cmc_mib,
       "cmc-ip": cmc_ip,
       "cmcIpInAdminDiscards": cmcIpInAdminDiscards,
       "cmcIpOutAdminDiscards": cmcIpOutAdminDiscards,
       "cmcIpFiltStatus": cmcIpFiltStatus,
       "cmcIpFilterTable": cmcIpFilterTable,
       "cmcIpFiltEntry": cmcIpFiltEntry,
       "cmcIpFiltName": cmcIpFiltName,
       "cmcIpFiltPriority": cmcIpFiltPriority,
       "cmcIpFiltSAddr": cmcIpFiltSAddr,
       "cmcIpFiltSMask": cmcIpFiltSMask,
       "cmcIpFiltSPort": cmcIpFiltSPort,
       "cmcIpFiltDAddr": cmcIpFiltDAddr,
       "cmcIpFiltDMask": cmcIpFiltDMask,
       "cmcIpFiltDPort": cmcIpFiltDPort,
       "cmcIpFiltProto": cmcIpFiltProto,
       "cmcIpFiltMode": cmcIpFiltMode,
       "cmcIpFiltErrMsg": cmcIpFiltErrMsg,
       "cmcIpFiltType": cmcIpFiltType,
       "cmcIpFiltMoveOper": cmcIpFiltMoveOper,
       "cmcIpFiltUseCount": cmcIpFiltUseCount,
       "cmcIpFiltDirection": cmcIpFiltDirection,
       "cmcIpFiltIfIndex": cmcIpFiltIfIndex,
       "cmc-ipx": cmc_ipx,
       "cmc-ipx-ipx": cmc_ipx_ipx,
       "cmc-ipx-ipxSystem": cmc_ipx_ipxSystem,
       "ipxSysTable": ipxSysTable,
       "ipxSysEntry": ipxSysEntry,
       "ipxSysInstance": ipxSysInstance,
       "ipxSysExistState": ipxSysExistState,
       "ipxSysIntNetNumExists": ipxSysIntNetNumExists,
       "ipxSysIntNetNum": ipxSysIntNetNum,
       "ipxSysName": ipxSysName,
       "ipxSysMaxPathSplits": ipxSysMaxPathSplits,
       "ipxSysMaxHops": ipxSysMaxHops,
       "ipxSysVersionMajor": ipxSysVersionMajor,
       "ipxSysVersionMinor": ipxSysVersionMinor,
       "ipxSysInReceives": ipxSysInReceives,
       "ipxSysInTooManyHops": ipxSysInTooManyHops,
       "ipxSysInHdrErrors": ipxSysInHdrErrors,
       "ipxSysInUnknownSockets": ipxSysInUnknownSockets,
       "ipxSysInFiltered": ipxSysInFiltered,
       "ipxSysInCompressDiscards": ipxSysInCompressDiscards,
       "ipxSysInDiscards": ipxSysInDiscards,
       "ipxSysInDelivers": ipxSysInDelivers,
       "ipxSysNETBIOSPackets": ipxSysNETBIOSPackets,
       "ipxSysForwPackets": ipxSysForwPackets,
       "ipxSysOutRequests": ipxSysOutRequests,
       "ipxSysOutNoRoutes": ipxSysOutNoRoutes,
       "ipxSysOutFiltered": ipxSysOutFiltered,
       "ipxSysOutCompressDiscards": ipxSysOutCompressDiscards,
       "ipxSysOutMalformedRequests": ipxSysOutMalformedRequests,
       "ipxSysOutDiscards": ipxSysOutDiscards,
       "ipxSysOutPackets": ipxSysOutPackets,
       "ipxSysCircCount": ipxSysCircCount,
       "ipxSysDestCount": ipxSysDestCount,
       "ipxSysServCount": ipxSysServCount,
       "ipxSysResourceFailures": ipxSysResourceFailures,
       "ipxSysConfigSockets": ipxSysConfigSockets,
       "ipxSysMaxOpenSockets": ipxSysMaxOpenSockets,
       "ipxSysOpenSocketFails": ipxSysOpenSocketFails,
       "cmc-ipx-ipxCircuit": cmc_ipx_ipxCircuit,
       "ipxCircTable": ipxCircTable,
       "ipxCircEntry": ipxCircEntry,
       "ipxCircSysInstance": ipxCircSysInstance,
       "ipxCircIndex": ipxCircIndex,
       "ipxCircExistState": ipxCircExistState,
       "ipxCircOperState": ipxCircOperState,
       "ipxCircIfIndex": ipxCircIfIndex,
       "ipxCircName": ipxCircName,
       "ipxCircInfo": ipxCircInfo,
       "ipxCircType": ipxCircType,
       "ipxCircLocalMaxPacketSize": ipxCircLocalMaxPacketSize,
       "ipxCircCompressState": ipxCircCompressState,
       "ipxCircCompressSlots": ipxCircCompressSlots,
       "ipxCircCompressedSent": ipxCircCompressedSent,
       "ipxCircUncompressedSent": ipxCircUncompressedSent,
       "ipxCircMediaType": ipxCircMediaType,
       "ipxCircNetNumber": ipxCircNetNumber,
       "ipxCircStateChanges": ipxCircStateChanges,
       "ipxCircInitFails": ipxCircInitFails,
       "ipxCircDelay": ipxCircDelay,
       "ipxCircThroughput": ipxCircThroughput,
       "cmc-ipx-ipxForwarding": cmc_ipx_ipxForwarding,
       "ipxDestTable": ipxDestTable,
       "ipxDestEntry": ipxDestEntry,
       "ipxDestSysInstance": ipxDestSysInstance,
       "ipxDestNetNum": ipxDestNetNum,
       "ipxDestProtocol": ipxDestProtocol,
       "ipxDestCost": ipxDestCost,
       "ipxDestHopCount": ipxDestHopCount,
       "ipxDestNextHopCircIndex": ipxDestNextHopCircIndex,
       "ipxDestNextHopNICAddress": ipxDestNextHopNICAddress,
       "ipxDestNextHopNetNum": ipxDestNextHopNetNum,
       "ipxDestType": ipxDestType,
       "cmc-ipx-ipxServices": cmc_ipx_ipxServices,
       "ipxServTable": ipxServTable,
       "ipxServEntry": ipxServEntry,
       "ipxServSysInstance": ipxServSysInstance,
       "ipxServName": ipxServName,
       "ipxServTypeValue": ipxServTypeValue,
       "ipxServType": ipxServType,
       "ipxServProtocol": ipxServProtocol,
       "ipxServNetNum": ipxServNetNum,
       "ipxServNode": ipxServNode,
       "ipxServSocket": ipxServSocket,
       "cmc-ipx-filter": cmc_ipx_filter,
       "cmcIpxFiltStatus": cmcIpxFiltStatus,
       "cmc-ipx-filt-packet": cmc_ipx_filt_packet,
       "cmcIpxFilterTable": cmcIpxFilterTable,
       "cmcIpxFiltEntry": cmcIpxFiltEntry,
       "cmcIpxFiltName": cmcIpxFiltName,
       "cmcIpxFiltSAddr": cmcIpxFiltSAddr,
       "cmcIpxFiltDAddr": cmcIpxFiltDAddr,
       "cmcIpxFiltPktType": cmcIpxFiltPktType,
       "cmcIpxFiltMode": cmcIpxFiltMode,
       "cmcIpxFiltType": cmcIpxFiltType,
       "cmcIpxFiltMoveOper": cmcIpxFiltMoveOper,
       "cmcIpxFiltUseCount": cmcIpxFiltUseCount,
       "cmcIpxFiltDirection": cmcIpxFiltDirection,
       "cmcIpxFiltIfIndex": cmcIpxFiltIfIndex,
       "cmcIpxFiltPriority": cmcIpxFiltPriority,
       "cmcIpxFiltState": cmcIpxFiltState,
       "cmcIpxFiltRIPStatus": cmcIpxFiltRIPStatus,
       "cmc-ipx-filt-rip": cmc_ipx_filt_rip,
       "cmcIpxFilterRIPTable": cmcIpxFilterRIPTable,
       "cmcIpxFiltRIPEntry": cmcIpxFiltRIPEntry,
       "cmcIpxFiltRIPName": cmcIpxFiltRIPName,
       "cmcIpxFiltRIPNetworkNum": cmcIpxFiltRIPNetworkNum,
       "cmcIpxFiltRIPMoveOper": cmcIpxFiltRIPMoveOper,
       "cmcIpxFiltRIPMode": cmcIpxFiltRIPMode,
       "cmcIpxFiltRIPType": cmcIpxFiltRIPType,
       "cmcIpxFiltRIPUseCount": cmcIpxFiltRIPUseCount,
       "cmcIpxFiltRIPDirection": cmcIpxFiltRIPDirection,
       "cmcIpxFiltRIPQueryType": cmcIpxFiltRIPQueryType,
       "cmcIpxFiltRIPIfIndex": cmcIpxFiltRIPIfIndex,
       "cmcIpxFiltRIPPriority": cmcIpxFiltRIPPriority,
       "cmcIpxFiltRIPState": cmcIpxFiltRIPState,
       "cmcIpxFiltSAPStatus": cmcIpxFiltSAPStatus,
       "cmc-ipx-filt-sap": cmc_ipx_filt_sap,
       "cmcIpxFilterSAPTable": cmcIpxFilterSAPTable,
       "cmcIpxFiltSAPEntry": cmcIpxFiltSAPEntry,
       "cmcIpxFiltSAPName": cmcIpxFiltSAPName,
       "cmcIpxFiltSAPServerName": cmcIpxFiltSAPServerName,
       "cmcIpxFiltSAPServerType": cmcIpxFiltSAPServerType,
       "cmcIpxFiltSAPMoveOper": cmcIpxFiltSAPMoveOper,
       "cmcIpxFiltSAPMode": cmcIpxFiltSAPMode,
       "cmcIpxFiltSAPType": cmcIpxFiltSAPType,
       "cmcIpxFiltSAPUseCount": cmcIpxFiltSAPUseCount,
       "cmcIpxFiltSAPDirection": cmcIpxFiltSAPDirection,
       "cmcIpxFiltSAPQueryType": cmcIpxFiltSAPQueryType,
       "cmcIpxFiltSAPIfIndex": cmcIpxFiltSAPIfIndex,
       "cmcIpxFiltSAPPriority": cmcIpxFiltSAPPriority,
       "cmcIpxFiltSAPState": cmcIpxFiltSAPState,
       "cmc-trapA": cmc_trapA,
       "cmc-trapB": cmc_trapB,
       "cmc-trapC": cmc_trapC,
       "cmc-trapD": cmc_trapD,
       "cmc-trapE": cmc_trapE,
       "cmcConnectionEstablished": cmcConnectionEstablished,
       "cmcConnectionTerminated": cmcConnectionTerminated}
)
