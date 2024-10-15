# SNMP MIB module (CPQHSV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQHSV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:26 2024
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
 NotificationType,
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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Compaq_ObjectIdentity = ObjectIdentity
compaq = _Compaq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232)
)
_CpqElementManager_ObjectIdentity = ObjectIdentity
cpqElementManager = _CpqElementManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136)
)
_CpqHSV_ObjectIdentity = ObjectIdentity
cpqHSV = _CpqHSV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1)
)
_CpqHSVAgent_ObjectIdentity = ObjectIdentity
cpqHSVAgent = _CpqHSVAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1)
)
_AgManufacturer_Type = DisplayString
_AgManufacturer_Object = MibScalar
agManufacturer = _AgManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 1),
    _AgManufacturer_Type()
)
agManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agManufacturer.setStatus("mandatory")
_AgMajVersion_Type = Integer32
_AgMajVersion_Object = MibScalar
agMajVersion = _AgMajVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 2),
    _AgMajVersion_Type()
)
agMajVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMajVersion.setStatus("mandatory")
_AgMinVersion_Type = Integer32
_AgMinVersion_Object = MibScalar
agMinVersion = _AgMinVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 3),
    _AgMinVersion_Type()
)
agMinVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agMinVersion.setStatus("mandatory")
_AgHostName_Type = DisplayString
_AgHostName_Object = MibScalar
agHostName = _AgHostName_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 4),
    _AgHostName_Type()
)
agHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agHostName.setStatus("mandatory")
_AgEnterprise_Type = ObjectIdentifier
_AgEnterprise_Object = MibScalar
agEnterprise = _AgEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 5),
    _AgEnterprise_Type()
)
agEnterprise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agEnterprise.setStatus("mandatory")
_AgDescription_Type = DisplayString
_AgDescription_Object = MibScalar
agDescription = _AgDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 6),
    _AgDescription_Type()
)
agDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agDescription.setStatus("mandatory")
_AgStatusTable_Object = MibTable
agStatusTable = _AgStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7)
)
if mibBuilder.loadTexts:
    agStatusTable.setStatus("mandatory")
_AgentEntry_Object = MibTableRow
agentEntry = _AgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7, 1)
)
agentEntry.setIndexNames(
    (0, "CPQHSV-MIB", "agentEntryIndex"),
)
if mibBuilder.loadTexts:
    agentEntry.setStatus("mandatory")
_AgentEntryIndex_Type = Integer32
_AgentEntryIndex_Object = MibTableColumn
agentEntryIndex = _AgentEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7, 1, 1),
    _AgentEntryIndex_Type()
)
agentEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEntryIndex.setStatus("mandatory")


class _AgentStatus_Type(Integer32):
    """Custom type agentStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_AgentStatus_Type.__name__ = "Integer32"
_AgentStatus_Object = MibTableColumn
agentStatus = _AgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7, 1, 2),
    _AgentStatus_Type()
)
agentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStatus.setStatus("mandatory")
_AgentEventCode_Type = Integer32
_AgentEventCode_Object = MibTableColumn
agentEventCode = _AgentEventCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7, 1, 3),
    _AgentEventCode_Type()
)
agentEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEventCode.setStatus("mandatory")
_AgentEventLevel_Type = Integer32
_AgentEventLevel_Object = MibTableColumn
agentEventLevel = _AgentEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7, 1, 4),
    _AgentEventLevel_Type()
)
agentEventLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEventLevel.setStatus("mandatory")
_AgentEventTimeDate_Type = DisplayString
_AgentEventTimeDate_Object = MibTableColumn
agentEventTimeDate = _AgentEventTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7, 1, 5),
    _AgentEventTimeDate_Type()
)
agentEventTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEventTimeDate.setStatus("mandatory")
_AgentEventDescription_Type = DisplayString
_AgentEventDescription_Object = MibTableColumn
agentEventDescription = _AgentEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 1, 7, 1, 6),
    _AgentEventDescription_Type()
)
agentEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEventDescription.setStatus("mandatory")
_CpqHSVServer_ObjectIdentity = ObjectIdentity
cpqHSVServer = _CpqHSVServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2)
)
_SrvCPU_Type = DisplayString
_SrvCPU_Object = MibScalar
srvCPU = _SrvCPU_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 1),
    _SrvCPU_Type()
)
srvCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCPU.setStatus("mandatory")
_SrvComputerType_Type = DisplayString
_SrvComputerType_Object = MibScalar
srvComputerType = _SrvComputerType_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 2),
    _SrvComputerType_Type()
)
srvComputerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvComputerType.setStatus("mandatory")
_SrvModel_Type = Integer32
_SrvModel_Object = MibScalar
srvModel = _SrvModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 3),
    _SrvModel_Type()
)
srvModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvModel.setStatus("mandatory")
_SrvSubModel_Type = Integer32
_SrvSubModel_Object = MibScalar
srvSubModel = _SrvSubModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 4),
    _SrvSubModel_Type()
)
srvSubModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvSubModel.setStatus("mandatory")
_SrvBiosVersion_Type = DisplayString
_SrvBiosVersion_Object = MibScalar
srvBiosVersion = _SrvBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 5),
    _SrvBiosVersion_Type()
)
srvBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvBiosVersion.setStatus("mandatory")
_SrvOS_Type = DisplayString
_SrvOS_Object = MibScalar
srvOS = _SrvOS_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 6),
    _SrvOS_Type()
)
srvOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvOS.setStatus("mandatory")
_SrvOSMajVersion_Type = Integer32
_SrvOSMajVersion_Object = MibScalar
srvOSMajVersion = _SrvOSMajVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 7),
    _SrvOSMajVersion_Type()
)
srvOSMajVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvOSMajVersion.setStatus("mandatory")
_SrvOSMinVersion_Type = Integer32
_SrvOSMinVersion_Object = MibScalar
srvOSMinVersion = _SrvOSMinVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 2, 8),
    _SrvOSMinVersion_Type()
)
srvOSMinVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvOSMinVersion.setStatus("mandatory")
_HsvObject_ObjectIdentity = ObjectIdentity
hsvObject = _HsvObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3)
)
_Scell_ObjectIdentity = ObjectIdentity
scell = _Scell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1)
)
_ScellTotal_Type = Integer32
_ScellTotal_Object = MibScalar
scellTotal = _ScellTotal_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 1),
    _ScellTotal_Type()
)
scellTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellTotal.setStatus("mandatory")
_ScellStatusTable_Object = MibTable
scellStatusTable = _ScellStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    scellStatusTable.setStatus("mandatory")
_ScellEntry_Object = MibTableRow
scellEntry = _ScellEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1)
)
scellEntry.setIndexNames(
    (0, "CPQHSV-MIB", "scellEntryIndex"),
)
if mibBuilder.loadTexts:
    scellEntry.setStatus("mandatory")
_ScellEntryIndex_Type = Integer32
_ScellEntryIndex_Object = MibTableColumn
scellEntryIndex = _ScellEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 1),
    _ScellEntryIndex_Type()
)
scellEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellEntryIndex.setStatus("mandatory")
_ScellName_Type = DisplayString
_ScellName_Object = MibTableColumn
scellName = _ScellName_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 2),
    _ScellName_Type()
)
scellName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellName.setStatus("mandatory")
_ScellUUID_Type = DisplayString
_ScellUUID_Object = MibTableColumn
scellUUID = _ScellUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 3),
    _ScellUUID_Type()
)
scellUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellUUID.setStatus("mandatory")


class _ScellStatus_Type(Integer32):
    """Custom type scellStatus based on Integer32"""
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
        *(("failed", 4),
          ("informational", 1),
          ("major", 3),
          ("minor", 2))
    )


_ScellStatus_Type.__name__ = "Integer32"
_ScellStatus_Object = MibTableColumn
scellStatus = _ScellStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 4),
    _ScellStatus_Type()
)
scellStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellStatus.setStatus("mandatory")
_ScellEventDescription_Type = DisplayString
_ScellEventDescription_Object = MibTableColumn
scellEventDescription = _ScellEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 5),
    _ScellEventDescription_Type()
)
scellEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellEventDescription.setStatus("mandatory")
_ScellEventTimeDate_Type = DisplayString
_ScellEventTimeDate_Object = MibTableColumn
scellEventTimeDate = _ScellEventTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 6),
    _ScellEventTimeDate_Type()
)
scellEventTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellEventTimeDate.setStatus("mandatory")
_ScellEventCode_Type = DisplayString
_ScellEventCode_Object = MibTableColumn
scellEventCode = _ScellEventCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 7),
    _ScellEventCode_Type()
)
scellEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellEventCode.setStatus("mandatory")
_ScellSWComponent_Type = Integer32
_ScellSWComponent_Object = MibTableColumn
scellSWComponent = _ScellSWComponent_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 8),
    _ScellSWComponent_Type()
)
scellSWComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellSWComponent.setStatus("mandatory")
_ScellECode_Type = Integer32
_ScellECode_Object = MibTableColumn
scellECode = _ScellECode_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 9),
    _ScellECode_Type()
)
scellECode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellECode.setStatus("mandatory")
_ScellCAC_Type = Integer32
_ScellCAC_Object = MibTableColumn
scellCAC = _ScellCAC_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 10),
    _ScellCAC_Type()
)
scellCAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellCAC.setStatus("mandatory")
_ScellEIP_Type = Integer32
_ScellEIP_Object = MibTableColumn
scellEIP = _ScellEIP_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 11),
    _ScellEIP_Type()
)
scellEIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellEIP.setStatus("mandatory")
_ScellNameDateTime_Type = DisplayString
_ScellNameDateTime_Object = MibTableColumn
scellNameDateTime = _ScellNameDateTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 1, 2, 1, 12),
    _ScellNameDateTime_Type()
)
scellNameDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scellNameDateTime.setStatus("mandatory")
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 2)
)
_Host_ObjectIdentity = ObjectIdentity
host = _Host_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3)
)
_HostTotal_Type = Integer32
_HostTotal_Object = MibScalar
hostTotal = _HostTotal_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3, 1),
    _HostTotal_Type()
)
hostTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTotal.setStatus("mandatory")
_HostStatusTable_Object = MibTable
hostStatusTable = _HostStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    hostStatusTable.setStatus("mandatory")
_HostEntry_Object = MibTableRow
hostEntry = _HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3, 2, 1)
)
hostEntry.setIndexNames(
    (0, "CPQHSV-MIB", "hostEntryIndex"),
)
if mibBuilder.loadTexts:
    hostEntry.setStatus("mandatory")
_HostEntryIndex_Type = Integer32
_HostEntryIndex_Object = MibTableColumn
hostEntryIndex = _HostEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3, 2, 1, 1),
    _HostEntryIndex_Type()
)
hostEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostEntryIndex.setStatus("mandatory")
_HostName_Type = DisplayString
_HostName_Object = MibTableColumn
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3, 2, 1, 2),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("mandatory")
_HostUUID_Type = DisplayString
_HostUUID_Object = MibTableColumn
hostUUID = _HostUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3, 2, 1, 3),
    _HostUUID_Type()
)
hostUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostUUID.setStatus("mandatory")


class _HostStatus_Type(Integer32):
    """Custom type hostStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("informational", 0),
          ("major", 2),
          ("minor", 1))
    )


_HostStatus_Type.__name__ = "Integer32"
_HostStatus_Object = MibTableColumn
hostStatus = _HostStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 3, 2, 1, 4),
    _HostStatus_Type()
)
hostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStatus.setStatus("mandatory")
_Nsc_ObjectIdentity = ObjectIdentity
nsc = _Nsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4)
)
_NscTotal_Type = Integer32
_NscTotal_Object = MibScalar
nscTotal = _NscTotal_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4, 1),
    _NscTotal_Type()
)
nscTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscTotal.setStatus("mandatory")
_NscStatusTable_Object = MibTable
nscStatusTable = _NscStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    nscStatusTable.setStatus("mandatory")
_NscEntry_Object = MibTableRow
nscEntry = _NscEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4, 2, 1)
)
nscEntry.setIndexNames(
    (0, "CPQHSV-MIB", "nscEntryIndex"),
)
if mibBuilder.loadTexts:
    nscEntry.setStatus("mandatory")
_NscEntryIndex_Type = Integer32
_NscEntryIndex_Object = MibTableColumn
nscEntryIndex = _NscEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4, 2, 1, 1),
    _NscEntryIndex_Type()
)
nscEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscEntryIndex.setStatus("mandatory")
_NscName_Type = DisplayString
_NscName_Object = MibTableColumn
nscName = _NscName_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4, 2, 1, 2),
    _NscName_Type()
)
nscName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscName.setStatus("mandatory")
_NscUUID_Type = DisplayString
_NscUUID_Object = MibTableColumn
nscUUID = _NscUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4, 2, 1, 3),
    _NscUUID_Type()
)
nscUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscUUID.setStatus("mandatory")


class _NscStatus_Type(Integer32):
    """Custom type nscStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("informational", 0),
          ("major", 2),
          ("minor", 1))
    )


_NscStatus_Type.__name__ = "Integer32"
_NscStatus_Object = MibTableColumn
nscStatus = _NscStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 4, 2, 1, 4),
    _NscStatus_Type()
)
nscStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscStatus.setStatus("mandatory")
_Shelf_ObjectIdentity = ObjectIdentity
shelf = _Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8)
)
_ShelfTotal_Type = Integer32
_ShelfTotal_Object = MibScalar
shelfTotal = _ShelfTotal_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 1),
    _ShelfTotal_Type()
)
shelfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfTotal.setStatus("mandatory")
_ShelfStatusTable_Object = MibTable
shelfStatusTable = _ShelfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2)
)
if mibBuilder.loadTexts:
    shelfStatusTable.setStatus("mandatory")
_ShelfEntry_Object = MibTableRow
shelfEntry = _ShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2, 1)
)
shelfEntry.setIndexNames(
    (0, "CPQHSV-MIB", "shelfEntryIndex"),
)
if mibBuilder.loadTexts:
    shelfEntry.setStatus("mandatory")
_ShelfEntryIndex_Type = Integer32
_ShelfEntryIndex_Object = MibTableColumn
shelfEntryIndex = _ShelfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2, 1, 1),
    _ShelfEntryIndex_Type()
)
shelfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfEntryIndex.setStatus("mandatory")


class _ShelfStatus_Type(Integer32):
    """Custom type shelfStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_ShelfStatus_Type.__name__ = "Integer32"
_ShelfStatus_Object = MibTableColumn
shelfStatus = _ShelfStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2, 1, 2),
    _ShelfStatus_Type()
)
shelfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfStatus.setStatus("mandatory")
_ShelfId_Type = Integer32
_ShelfId_Object = MibTableColumn
shelfId = _ShelfId_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2, 1, 3),
    _ShelfId_Type()
)
shelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfId.setStatus("mandatory")
_ShelfElementType_Type = Integer32
_ShelfElementType_Object = MibTableColumn
shelfElementType = _ShelfElementType_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2, 1, 4),
    _ShelfElementType_Type()
)
shelfElementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfElementType.setStatus("mandatory")
_ShelfElementNum_Type = Integer32
_ShelfElementNum_Object = MibTableColumn
shelfElementNum = _ShelfElementNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2, 1, 5),
    _ShelfElementNum_Type()
)
shelfElementNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfElementNum.setStatus("mandatory")
_ShelfErrorCode_Type = Integer32
_ShelfErrorCode_Object = MibTableColumn
shelfErrorCode = _ShelfErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 3, 8, 2, 1, 6),
    _ShelfErrorCode_Type()
)
shelfErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfErrorCode.setStatus("mandatory")
_MaHSVMibRev_ObjectIdentity = ObjectIdentity
maHSVMibRev = _MaHSVMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 4)
)
_MaHSVMibRevMajor_Type = Integer32
_MaHSVMibRevMajor_Object = MibScalar
maHSVMibRevMajor = _MaHSVMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 4, 1),
    _MaHSVMibRevMajor_Type()
)
maHSVMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maHSVMibRevMajor.setStatus("mandatory")
_MaHSVMibRevMinor_Type = Integer32
_MaHSVMibRevMinor_Object = MibScalar
maHSVMibRevMinor = _MaHSVMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 136, 1, 4, 2),
    _MaHSVMibRevMinor_Type()
)
maHSVMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maHSVMibRevMinor.setStatus("mandatory")

# Managed Objects groups


# Notification objects

emuEventTrapInformative = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001)
)
emuEventTrapInformative.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "shelfId"),
        ("CPQHSV-MIB", "shelfElementType"),
        ("CPQHSV-MIB", "shelfElementNum"),
        ("CPQHSV-MIB", "shelfErrorCode"))
)
if mibBuilder.loadTexts:
    emuEventTrapInformative.setStatus(
        ""
    )

emuEventTrapNoncritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002)
)
emuEventTrapNoncritical.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "shelfId"),
        ("CPQHSV-MIB", "shelfElementType"),
        ("CPQHSV-MIB", "shelfElementNum"),
        ("CPQHSV-MIB", "shelfErrorCode"))
)
if mibBuilder.loadTexts:
    emuEventTrapNoncritical.setStatus(
        ""
    )

emuEventTrapCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003)
)
emuEventTrapCritical.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "shelfId"),
        ("CPQHSV-MIB", "shelfElementType"),
        ("CPQHSV-MIB", "shelfElementNum"),
        ("CPQHSV-MIB", "shelfErrorCode"))
)
if mibBuilder.loadTexts:
    emuEventTrapCritical.setStatus(
        ""
    )

emuEventTrapUnrecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004)
)
emuEventTrapUnrecoverable.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "shelfId"),
        ("CPQHSV-MIB", "shelfElementType"),
        ("CPQHSV-MIB", "shelfElementNum"),
        ("CPQHSV-MIB", "shelfErrorCode"))
)
if mibBuilder.loadTexts:
    emuEventTrapUnrecoverable.setStatus(
        ""
    )

sCellEventTrap_01_02 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13600258)
)
sCellEventTrap_01_02.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_01_02.setStatus(
        ""
    )

sCellEventTrap_03_00 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13600768)
)
sCellEventTrap_03_00.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_03_00.setStatus(
        ""
    )

sCellEventTrap_03_01 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13600769)
)
sCellEventTrap_03_01.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_03_01.setStatus(
        ""
    )

sCellEventTrap_03_02 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13600770)
)
sCellEventTrap_03_02.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_03_02.setStatus(
        ""
    )

sCellEventTrap_03_03 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13600771)
)
sCellEventTrap_03_03.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_03_03.setStatus(
        ""
    )

sCellEventTrap_03_04 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13600772)
)
sCellEventTrap_03_04.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_03_04.setStatus(
        ""
    )

sCellEventTrap_03_05 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13600773)
)
sCellEventTrap_03_05.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_03_05.setStatus(
        ""
    )

sCellEventTrap_03_06 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13600774)
)
sCellEventTrap_03_06.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_03_06.setStatus(
        ""
    )

sCellEventTrap_03_07 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13600775)
)
sCellEventTrap_03_07.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_03_07.setStatus(
        ""
    )

sCellEventTrap_03_08 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13600776)
)
sCellEventTrap_03_08.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_03_08.setStatus(
        ""
    )

sCellEventTrap_03_09 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13600777)
)
sCellEventTrap_03_09.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_03_09.setStatus(
        ""
    )

sCellEventTrap_03_0a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13600778)
)
sCellEventTrap_03_0a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_03_0a.setStatus(
        ""
    )

sCellEventTrap_03_0b = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13600779)
)
sCellEventTrap_03_0b.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_03_0b.setStatus(
        ""
    )

sCellEventTrap_04_00 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601024)
)
sCellEventTrap_04_00.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_00.setStatus(
        ""
    )

sCellEventTrap_04_01 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601025)
)
sCellEventTrap_04_01.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_01.setStatus(
        ""
    )

sCellEventTrap_04_02 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601026)
)
sCellEventTrap_04_02.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_02.setStatus(
        ""
    )

sCellEventTrap_04_03 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601027)
)
sCellEventTrap_04_03.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_03.setStatus(
        ""
    )

sCellEventTrap_04_04 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601028)
)
sCellEventTrap_04_04.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_04.setStatus(
        ""
    )

sCellEventTrap_04_05 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601029)
)
sCellEventTrap_04_05.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_05.setStatus(
        ""
    )

sCellEventTrap_04_06 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601030)
)
sCellEventTrap_04_06.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_06.setStatus(
        ""
    )

sCellEventTrap_04_07 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601031)
)
sCellEventTrap_04_07.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_07.setStatus(
        ""
    )

sCellEventTrap_04_08 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601032)
)
sCellEventTrap_04_08.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_08.setStatus(
        ""
    )

sCellEventTrap_04_09 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601033)
)
sCellEventTrap_04_09.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_09.setStatus(
        ""
    )

sCellEventTrap_04_0a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601034)
)
sCellEventTrap_04_0a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_0a.setStatus(
        ""
    )

sCellEventTrap_04_0b = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601035)
)
sCellEventTrap_04_0b.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_0b.setStatus(
        ""
    )

sCellEventTrap_04_0c = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601036)
)
sCellEventTrap_04_0c.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_0c.setStatus(
        ""
    )

sCellEventTrap_04_0d = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601037)
)
sCellEventTrap_04_0d.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_0d.setStatus(
        ""
    )

sCellEventTrap_04_0e = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601038)
)
sCellEventTrap_04_0e.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_0e.setStatus(
        ""
    )

sCellEventTrap_04_0f = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601039)
)
sCellEventTrap_04_0f.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_0f.setStatus(
        ""
    )

sCellEventTrap_04_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601040)
)
sCellEventTrap_04_10.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_10.setStatus(
        ""
    )

sCellEventTrap_04_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601041)
)
sCellEventTrap_04_11.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_11.setStatus(
        ""
    )

sCellEventTrap_04_12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601042)
)
sCellEventTrap_04_12.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_12.setStatus(
        ""
    )

sCellEventTrap_04_13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601043)
)
sCellEventTrap_04_13.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_04_13.setStatus(
        ""
    )

sCellEventTrap_06_00 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601536)
)
sCellEventTrap_06_00.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_00.setStatus(
        ""
    )

sCellEventTrap_06_01 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601537)
)
sCellEventTrap_06_01.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_01.setStatus(
        ""
    )

sCellEventTrap_06_02 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601538)
)
sCellEventTrap_06_02.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_02.setStatus(
        ""
    )

sCellEventTrap_06_03 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601539)
)
sCellEventTrap_06_03.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_03.setStatus(
        ""
    )

sCellEventTrap_06_04 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601540)
)
sCellEventTrap_06_04.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_04.setStatus(
        ""
    )

sCellEventTrap_06_05 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601541)
)
sCellEventTrap_06_05.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_05.setStatus(
        ""
    )

sCellEventTrap_06_07 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601543)
)
sCellEventTrap_06_07.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_07.setStatus(
        ""
    )

sCellEventTrap_06_08 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601544)
)
sCellEventTrap_06_08.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_08.setStatus(
        ""
    )

sCellEventTrap_06_09 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601545)
)
sCellEventTrap_06_09.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_09.setStatus(
        ""
    )

sCellEventTrap_06_0a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601546)
)
sCellEventTrap_06_0a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_0a.setStatus(
        ""
    )

sCellEventTrap_06_0b = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601547)
)
sCellEventTrap_06_0b.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_0b.setStatus(
        ""
    )

sCellEventTrap_06_0c = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601548)
)
sCellEventTrap_06_0c.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_0c.setStatus(
        ""
    )

sCellEventTrap_06_0d = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601549)
)
sCellEventTrap_06_0d.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_0d.setStatus(
        ""
    )

sCellEventTrap_06_0e = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601550)
)
sCellEventTrap_06_0e.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_0e.setStatus(
        ""
    )

sCellEventTrap_06_0f = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601551)
)
sCellEventTrap_06_0f.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_0f.setStatus(
        ""
    )

sCellEventTrap_06_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601552)
)
sCellEventTrap_06_10.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_10.setStatus(
        ""
    )

sCellEventTrap_06_12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601554)
)
sCellEventTrap_06_12.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_12.setStatus(
        ""
    )

sCellEventTrap_06_13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601555)
)
sCellEventTrap_06_13.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_13.setStatus(
        ""
    )

sCellEventTrap_06_14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601556)
)
sCellEventTrap_06_14.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_14.setStatus(
        ""
    )

sCellEventTrap_06_15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601557)
)
sCellEventTrap_06_15.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_15.setStatus(
        ""
    )

sCellEventTrap_06_16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601558)
)
sCellEventTrap_06_16.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_16.setStatus(
        ""
    )

sCellEventTrap_06_18 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601560)
)
sCellEventTrap_06_18.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_18.setStatus(
        ""
    )

sCellEventTrap_06_19 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601561)
)
sCellEventTrap_06_19.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_19.setStatus(
        ""
    )

sCellEventTrap_06_1a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601562)
)
sCellEventTrap_06_1a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_1a.setStatus(
        ""
    )

sCellEventTrap_06_1b = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601563)
)
sCellEventTrap_06_1b.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_1b.setStatus(
        ""
    )

sCellEventTrap_06_1c = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601564)
)
sCellEventTrap_06_1c.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_1c.setStatus(
        ""
    )

sCellEventTrap_06_1d = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601565)
)
sCellEventTrap_06_1d.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_1d.setStatus(
        ""
    )

sCellEventTrap_06_1e = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601566)
)
sCellEventTrap_06_1e.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_1e.setStatus(
        ""
    )

sCellEventTrap_06_1f = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601567)
)
sCellEventTrap_06_1f.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_1f.setStatus(
        ""
    )

sCellEventTrap_06_20 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601568)
)
sCellEventTrap_06_20.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_20.setStatus(
        ""
    )

sCellEventTrap_06_21 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601569)
)
sCellEventTrap_06_21.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_21.setStatus(
        ""
    )

sCellEventTrap_06_23 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601571)
)
sCellEventTrap_06_23.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_23.setStatus(
        ""
    )

sCellEventTrap_06_24 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601572)
)
sCellEventTrap_06_24.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_24.setStatus(
        ""
    )

sCellEventTrap_06_25 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601573)
)
sCellEventTrap_06_25.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_25.setStatus(
        ""
    )

sCellEventTrap_06_26 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601574)
)
sCellEventTrap_06_26.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_26.setStatus(
        ""
    )

sCellEventTrap_06_27 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601575)
)
sCellEventTrap_06_27.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_27.setStatus(
        ""
    )

sCellEventTrap_06_28 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601576)
)
sCellEventTrap_06_28.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_28.setStatus(
        ""
    )

sCellEventTrap_06_29 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601577)
)
sCellEventTrap_06_29.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_29.setStatus(
        ""
    )

sCellEventTrap_06_2a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601578)
)
sCellEventTrap_06_2a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_2a.setStatus(
        ""
    )

sCellEventTrap_06_2b = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601579)
)
sCellEventTrap_06_2b.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_2b.setStatus(
        ""
    )

sCellEventTrap_06_2c = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601580)
)
sCellEventTrap_06_2c.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_2c.setStatus(
        ""
    )

sCellEventTrap_06_2d = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601581)
)
sCellEventTrap_06_2d.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_2d.setStatus(
        ""
    )

sCellEventTrap_06_2e = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601582)
)
sCellEventTrap_06_2e.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_2e.setStatus(
        ""
    )

sCellEventTrap_06_30 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601584)
)
sCellEventTrap_06_30.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_30.setStatus(
        ""
    )

sCellEventTrap_06_31 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601585)
)
sCellEventTrap_06_31.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_31.setStatus(
        ""
    )

sCellEventTrap_06_32 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601586)
)
sCellEventTrap_06_32.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_32.setStatus(
        ""
    )

sCellEventTrap_06_33 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601587)
)
sCellEventTrap_06_33.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_33.setStatus(
        ""
    )

sCellEventTrap_06_34 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601588)
)
sCellEventTrap_06_34.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_34.setStatus(
        ""
    )

sCellEventTrap_06_35 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601589)
)
sCellEventTrap_06_35.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_35.setStatus(
        ""
    )

sCellEventTrap_06_36 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601590)
)
sCellEventTrap_06_36.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_36.setStatus(
        ""
    )

sCellEventTrap_06_37 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601591)
)
sCellEventTrap_06_37.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_37.setStatus(
        ""
    )

sCellEventTrap_06_38 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601592)
)
sCellEventTrap_06_38.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_38.setStatus(
        ""
    )

sCellEventTrap_06_39 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601593)
)
sCellEventTrap_06_39.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_39.setStatus(
        ""
    )

sCellEventTrap_06_3a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601594)
)
sCellEventTrap_06_3a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_3a.setStatus(
        ""
    )

sCellEventTrap_06_3b = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601595)
)
sCellEventTrap_06_3b.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_3b.setStatus(
        ""
    )

sCellEventTrap_06_3c = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601596)
)
sCellEventTrap_06_3c.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_3c.setStatus(
        ""
    )

sCellEventTrap_06_3d = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601597)
)
sCellEventTrap_06_3d.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_3d.setStatus(
        ""
    )

sCellEventTrap_06_3e = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601598)
)
sCellEventTrap_06_3e.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_3e.setStatus(
        ""
    )

sCellEventTrap_06_3f = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601599)
)
sCellEventTrap_06_3f.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_3f.setStatus(
        ""
    )

sCellEventTrap_06_40 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601600)
)
sCellEventTrap_06_40.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_40.setStatus(
        ""
    )

sCellEventTrap_06_41 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601601)
)
sCellEventTrap_06_41.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_41.setStatus(
        ""
    )

sCellEventTrap_06_42 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601602)
)
sCellEventTrap_06_42.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_42.setStatus(
        ""
    )

sCellEventTrap_06_43 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601603)
)
sCellEventTrap_06_43.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_06_43.setStatus(
        ""
    )

sCellEventTrap_07_00 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601792)
)
sCellEventTrap_07_00.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_07_00.setStatus(
        ""
    )

sCellEventTrap_07_01 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601793)
)
sCellEventTrap_07_01.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_07_01.setStatus(
        ""
    )

sCellEventTrap_07_02 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601794)
)
sCellEventTrap_07_02.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_07_02.setStatus(
        ""
    )

sCellEventTrap_07_03 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601795)
)
sCellEventTrap_07_03.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_07_03.setStatus(
        ""
    )

sCellEventTrap_07_04 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601796)
)
sCellEventTrap_07_04.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_07_04.setStatus(
        ""
    )

sCellEventTrap_07_05 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601797)
)
sCellEventTrap_07_05.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_07_05.setStatus(
        ""
    )

sCellEventTrap_07_06 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601798)
)
sCellEventTrap_07_06.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_07_06.setStatus(
        ""
    )

sCellEventTrap_07_07 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601799)
)
sCellEventTrap_07_07.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_07_07.setStatus(
        ""
    )

sCellEventTrap_07_08 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601800)
)
sCellEventTrap_07_08.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_07_08.setStatus(
        ""
    )

sCellEventTrap_07_09 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601801)
)
sCellEventTrap_07_09.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_07_09.setStatus(
        ""
    )

sCellEventTrap_07_0a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601802)
)
sCellEventTrap_07_0a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_07_0a.setStatus(
        ""
    )

sCellEventTrap_07_0b = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13601803)
)
sCellEventTrap_07_0b.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_07_0b.setStatus(
        ""
    )

sCellEventTrap_09_01 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602305)
)
sCellEventTrap_09_01.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_01.setStatus(
        ""
    )

sCellEventTrap_09_02 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602306)
)
sCellEventTrap_09_02.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_02.setStatus(
        ""
    )

sCellEventTrap_09_03 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602307)
)
sCellEventTrap_09_03.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_03.setStatus(
        ""
    )

sCellEventTrap_09_04 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602308)
)
sCellEventTrap_09_04.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_04.setStatus(
        ""
    )

sCellEventTrap_09_05 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602309)
)
sCellEventTrap_09_05.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_05.setStatus(
        ""
    )

sCellEventTrap_09_06 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602310)
)
sCellEventTrap_09_06.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_06.setStatus(
        ""
    )

sCellEventTrap_09_07 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602311)
)
sCellEventTrap_09_07.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_07.setStatus(
        ""
    )

sCellEventTrap_09_08 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602312)
)
sCellEventTrap_09_08.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_08.setStatus(
        ""
    )

sCellEventTrap_09_09 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602313)
)
sCellEventTrap_09_09.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_09.setStatus(
        ""
    )

sCellEventTrap_09_0a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602314)
)
sCellEventTrap_09_0a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_0a.setStatus(
        ""
    )

sCellEventTrap_09_0c = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602316)
)
sCellEventTrap_09_0c.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_0c.setStatus(
        ""
    )

sCellEventTrap_09_0d = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602317)
)
sCellEventTrap_09_0d.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_0d.setStatus(
        ""
    )

sCellEventTrap_09_0e = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602318)
)
sCellEventTrap_09_0e.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_0e.setStatus(
        ""
    )

sCellEventTrap_09_0f = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602319)
)
sCellEventTrap_09_0f.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_0f.setStatus(
        ""
    )

sCellEventTrap_09_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602321)
)
sCellEventTrap_09_11.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_11.setStatus(
        ""
    )

sCellEventTrap_09_12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602322)
)
sCellEventTrap_09_12.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_12.setStatus(
        ""
    )

sCellEventTrap_09_13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602323)
)
sCellEventTrap_09_13.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_13.setStatus(
        ""
    )

sCellEventTrap_09_14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602324)
)
sCellEventTrap_09_14.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_14.setStatus(
        ""
    )

sCellEventTrap_09_15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602325)
)
sCellEventTrap_09_15.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_15.setStatus(
        ""
    )

sCellEventTrap_09_16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602326)
)
sCellEventTrap_09_16.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_16.setStatus(
        ""
    )

sCellEventTrap_09_17 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602327)
)
sCellEventTrap_09_17.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_17.setStatus(
        ""
    )

sCellEventTrap_09_18 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602328)
)
sCellEventTrap_09_18.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_18.setStatus(
        ""
    )

sCellEventTrap_09_19 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602329)
)
sCellEventTrap_09_19.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_19.setStatus(
        ""
    )

sCellEventTrap_09_1a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602330)
)
sCellEventTrap_09_1a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_1a.setStatus(
        ""
    )

sCellEventTrap_09_1b = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602331)
)
sCellEventTrap_09_1b.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_1b.setStatus(
        ""
    )

sCellEventTrap_09_1c = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602332)
)
sCellEventTrap_09_1c.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_1c.setStatus(
        ""
    )

sCellEventTrap_09_1d = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602333)
)
sCellEventTrap_09_1d.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_1d.setStatus(
        ""
    )

sCellEventTrap_09_1e = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602334)
)
sCellEventTrap_09_1e.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_1e.setStatus(
        ""
    )

sCellEventTrap_09_1f = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602335)
)
sCellEventTrap_09_1f.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_1f.setStatus(
        ""
    )

sCellEventTrap_09_20 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602336)
)
sCellEventTrap_09_20.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_20.setStatus(
        ""
    )

sCellEventTrap_09_21 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602337)
)
sCellEventTrap_09_21.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_21.setStatus(
        ""
    )

sCellEventTrap_09_22 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602338)
)
sCellEventTrap_09_22.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_22.setStatus(
        ""
    )

sCellEventTrap_09_23 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602339)
)
sCellEventTrap_09_23.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_23.setStatus(
        ""
    )

sCellEventTrap_09_24 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602340)
)
sCellEventTrap_09_24.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_24.setStatus(
        ""
    )

sCellEventTrap_09_25 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602341)
)
sCellEventTrap_09_25.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_25.setStatus(
        ""
    )

sCellEventTrap_09_26 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602342)
)
sCellEventTrap_09_26.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_26.setStatus(
        ""
    )

sCellEventTrap_09_27 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602343)
)
sCellEventTrap_09_27.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_27.setStatus(
        ""
    )

sCellEventTrap_09_28 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602344)
)
sCellEventTrap_09_28.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_28.setStatus(
        ""
    )

sCellEventTrap_09_29 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602345)
)
sCellEventTrap_09_29.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_29.setStatus(
        ""
    )

sCellEventTrap_09_2a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602346)
)
sCellEventTrap_09_2a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_2a.setStatus(
        ""
    )

sCellEventTrap_09_2b = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602347)
)
sCellEventTrap_09_2b.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_2b.setStatus(
        ""
    )

sCellEventTrap_09_2c = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602348)
)
sCellEventTrap_09_2c.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_2c.setStatus(
        ""
    )

sCellEventTrap_09_2d = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602349)
)
sCellEventTrap_09_2d.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_2d.setStatus(
        ""
    )

sCellEventTrap_09_2e = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602350)
)
sCellEventTrap_09_2e.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_2e.setStatus(
        ""
    )

sCellEventTrap_09_2f = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602351)
)
sCellEventTrap_09_2f.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_2f.setStatus(
        ""
    )

sCellEventTrap_09_30 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602352)
)
sCellEventTrap_09_30.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_30.setStatus(
        ""
    )

sCellEventTrap_09_31 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602353)
)
sCellEventTrap_09_31.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_31.setStatus(
        ""
    )

sCellEventTrap_09_32 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602354)
)
sCellEventTrap_09_32.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_32.setStatus(
        ""
    )

sCellEventTrap_09_33 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602355)
)
sCellEventTrap_09_33.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_33.setStatus(
        ""
    )

sCellEventTrap_09_34 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602356)
)
sCellEventTrap_09_34.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_34.setStatus(
        ""
    )

sCellEventTrap_09_35 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602357)
)
sCellEventTrap_09_35.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_35.setStatus(
        ""
    )

sCellEventTrap_09_36 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602358)
)
sCellEventTrap_09_36.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_36.setStatus(
        ""
    )

sCellEventTrap_09_37 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602359)
)
sCellEventTrap_09_37.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_37.setStatus(
        ""
    )

sCellEventTrap_09_38 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602360)
)
sCellEventTrap_09_38.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_38.setStatus(
        ""
    )

sCellEventTrap_09_39 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602361)
)
sCellEventTrap_09_39.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_39.setStatus(
        ""
    )

sCellEventTrap_09_3a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602362)
)
sCellEventTrap_09_3a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_3a.setStatus(
        ""
    )

sCellEventTrap_09_3b = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602363)
)
sCellEventTrap_09_3b.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_3b.setStatus(
        ""
    )

sCellEventTrap_09_3c = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602364)
)
sCellEventTrap_09_3c.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_3c.setStatus(
        ""
    )

sCellEventTrap_09_3d = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602365)
)
sCellEventTrap_09_3d.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_3d.setStatus(
        ""
    )

sCellEventTrap_09_3e = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602366)
)
sCellEventTrap_09_3e.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_3e.setStatus(
        ""
    )

sCellEventTrap_09_3f = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602367)
)
sCellEventTrap_09_3f.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_3f.setStatus(
        ""
    )

sCellEventTrap_09_40 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602368)
)
sCellEventTrap_09_40.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_40.setStatus(
        ""
    )

sCellEventTrap_09_41 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602369)
)
sCellEventTrap_09_41.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_41.setStatus(
        ""
    )

sCellEventTrap_09_43 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602371)
)
sCellEventTrap_09_43.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_43.setStatus(
        ""
    )

sCellEventTrap_09_44 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602372)
)
sCellEventTrap_09_44.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_44.setStatus(
        ""
    )

sCellEventTrap_09_45 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602373)
)
sCellEventTrap_09_45.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_45.setStatus(
        ""
    )

sCellEventTrap_09_46 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602374)
)
sCellEventTrap_09_46.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_46.setStatus(
        ""
    )

sCellEventTrap_09_47 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602375)
)
sCellEventTrap_09_47.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_47.setStatus(
        ""
    )

sCellEventTrap_09_48 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602376)
)
sCellEventTrap_09_48.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_48.setStatus(
        ""
    )

sCellEventTrap_09_49 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602377)
)
sCellEventTrap_09_49.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_49.setStatus(
        ""
    )

sCellEventTrap_09_4a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602378)
)
sCellEventTrap_09_4a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_4a.setStatus(
        ""
    )

sCellEventTrap_09_65 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602405)
)
sCellEventTrap_09_65.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_65.setStatus(
        ""
    )

sCellEventTrap_09_66 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602406)
)
sCellEventTrap_09_66.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_66.setStatus(
        ""
    )

sCellEventTrap_09_67 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602407)
)
sCellEventTrap_09_67.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_67.setStatus(
        ""
    )

sCellEventTrap_09_68 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602408)
)
sCellEventTrap_09_68.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_68.setStatus(
        ""
    )

sCellEventTrap_09_69 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602409)
)
sCellEventTrap_09_69.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_69.setStatus(
        ""
    )

sCellEventTrap_09_6a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602410)
)
sCellEventTrap_09_6a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_6a.setStatus(
        ""
    )

sCellEventTrap_09_6b = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602411)
)
sCellEventTrap_09_6b.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_6b.setStatus(
        ""
    )

sCellEventTrap_09_6c = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602412)
)
sCellEventTrap_09_6c.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_6c.setStatus(
        ""
    )

sCellEventTrap_09_6d = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602413)
)
sCellEventTrap_09_6d.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_6d.setStatus(
        ""
    )

sCellEventTrap_09_6e = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602414)
)
sCellEventTrap_09_6e.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_6e.setStatus(
        ""
    )

sCellEventTrap_09_70 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602416)
)
sCellEventTrap_09_70.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_70.setStatus(
        ""
    )

sCellEventTrap_09_71 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602417)
)
sCellEventTrap_09_71.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_71.setStatus(
        ""
    )

sCellEventTrap_09_72 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602418)
)
sCellEventTrap_09_72.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_72.setStatus(
        ""
    )

sCellEventTrap_09_73 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602419)
)
sCellEventTrap_09_73.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_73.setStatus(
        ""
    )

sCellEventTrap_09_74 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602420)
)
sCellEventTrap_09_74.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_74.setStatus(
        ""
    )

sCellEventTrap_09_75 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602421)
)
sCellEventTrap_09_75.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_75.setStatus(
        ""
    )

sCellEventTrap_09_76 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602422)
)
sCellEventTrap_09_76.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_76.setStatus(
        ""
    )

sCellEventTrap_09_77 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602423)
)
sCellEventTrap_09_77.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_77.setStatus(
        ""
    )

sCellEventTrap_09_78 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602424)
)
sCellEventTrap_09_78.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_78.setStatus(
        ""
    )

sCellEventTrap_09_79 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602425)
)
sCellEventTrap_09_79.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_79.setStatus(
        ""
    )

sCellEventTrap_09_7a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602426)
)
sCellEventTrap_09_7a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_7a.setStatus(
        ""
    )

sCellEventTrap_09_7b = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602427)
)
sCellEventTrap_09_7b.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_7b.setStatus(
        ""
    )

sCellEventTrap_09_7c = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602428)
)
sCellEventTrap_09_7c.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_7c.setStatus(
        ""
    )

sCellEventTrap_09_c8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602504)
)
sCellEventTrap_09_c8.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_c8.setStatus(
        ""
    )

sCellEventTrap_09_c9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602505)
)
sCellEventTrap_09_c9.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_c9.setStatus(
        ""
    )

sCellEventTrap_09_ca = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602506)
)
sCellEventTrap_09_ca.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_ca.setStatus(
        ""
    )

sCellEventTrap_09_cb = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602507)
)
sCellEventTrap_09_cb.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_cb.setStatus(
        ""
    )

sCellEventTrap_09_cc = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602508)
)
sCellEventTrap_09_cc.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_cc.setStatus(
        ""
    )

sCellEventTrap_09_cd = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602509)
)
sCellEventTrap_09_cd.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_cd.setStatus(
        ""
    )

sCellEventTrap_09_ce = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602510)
)
sCellEventTrap_09_ce.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_ce.setStatus(
        ""
    )

sCellEventTrap_09_cf = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602511)
)
sCellEventTrap_09_cf.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_cf.setStatus(
        ""
    )

sCellEventTrap_09_d0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602512)
)
sCellEventTrap_09_d0.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_d0.setStatus(
        ""
    )

sCellEventTrap_09_d1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602513)
)
sCellEventTrap_09_d1.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_d1.setStatus(
        ""
    )

sCellEventTrap_09_d2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602514)
)
sCellEventTrap_09_d2.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_d2.setStatus(
        ""
    )

sCellEventTrap_09_d3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602515)
)
sCellEventTrap_09_d3.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_d3.setStatus(
        ""
    )

sCellEventTrap_09_d4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602516)
)
sCellEventTrap_09_d4.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_d4.setStatus(
        ""
    )

sCellEventTrap_09_d5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602517)
)
sCellEventTrap_09_d5.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_d5.setStatus(
        ""
    )

sCellEventTrap_09_d6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602518)
)
sCellEventTrap_09_d6.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_d6.setStatus(
        ""
    )

sCellEventTrap_09_d7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602519)
)
sCellEventTrap_09_d7.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_d7.setStatus(
        ""
    )

sCellEventTrap_09_d8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602520)
)
sCellEventTrap_09_d8.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_d8.setStatus(
        ""
    )

sCellEventTrap_09_d9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602521)
)
sCellEventTrap_09_d9.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_d9.setStatus(
        ""
    )

sCellEventTrap_09_da = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602522)
)
sCellEventTrap_09_da.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_da.setStatus(
        ""
    )

sCellEventTrap_09_db = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602523)
)
sCellEventTrap_09_db.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_09_db.setStatus(
        ""
    )

sCellEventTrap_0b_00 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602816)
)
sCellEventTrap_0b_00.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0b_00.setStatus(
        ""
    )

sCellEventTrap_0b_01 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602817)
)
sCellEventTrap_0b_01.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0b_01.setStatus(
        ""
    )

sCellEventTrap_0b_02 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602818)
)
sCellEventTrap_0b_02.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0b_02.setStatus(
        ""
    )

sCellEventTrap_0b_03 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602819)
)
sCellEventTrap_0b_03.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0b_03.setStatus(
        ""
    )

sCellEventTrap_0b_04 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602820)
)
sCellEventTrap_0b_04.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0b_04.setStatus(
        ""
    )

sCellEventTrap_0b_05 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13602821)
)
sCellEventTrap_0b_05.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0b_05.setStatus(
        ""
    )

sCellEventTrap_0c_03 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603075)
)
sCellEventTrap_0c_03.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_03.setStatus(
        ""
    )

sCellEventTrap_0c_04 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603076)
)
sCellEventTrap_0c_04.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_04.setStatus(
        ""
    )

sCellEventTrap_0c_05 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603077)
)
sCellEventTrap_0c_05.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_05.setStatus(
        ""
    )

sCellEventTrap_0c_06 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603078)
)
sCellEventTrap_0c_06.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_06.setStatus(
        ""
    )

sCellEventTrap_0c_07 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603079)
)
sCellEventTrap_0c_07.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_07.setStatus(
        ""
    )

sCellEventTrap_0c_08 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603080)
)
sCellEventTrap_0c_08.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_08.setStatus(
        ""
    )

sCellEventTrap_0c_09 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603081)
)
sCellEventTrap_0c_09.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_09.setStatus(
        ""
    )

sCellEventTrap_0c_0a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603082)
)
sCellEventTrap_0c_0a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_0a.setStatus(
        ""
    )

sCellEventTrap_0c_0c = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603084)
)
sCellEventTrap_0c_0c.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_0c.setStatus(
        ""
    )

sCellEventTrap_0c_0f = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603087)
)
sCellEventTrap_0c_0f.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_0f.setStatus(
        ""
    )

sCellEventTrap_0c_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603088)
)
sCellEventTrap_0c_10.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_10.setStatus(
        ""
    )

sCellEventTrap_0c_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603089)
)
sCellEventTrap_0c_11.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_11.setStatus(
        ""
    )

sCellEventTrap_0c_12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603090)
)
sCellEventTrap_0c_12.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_12.setStatus(
        ""
    )

sCellEventTrap_0c_15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603093)
)
sCellEventTrap_0c_15.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_15.setStatus(
        ""
    )

sCellEventTrap_0c_16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603094)
)
sCellEventTrap_0c_16.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_16.setStatus(
        ""
    )

sCellEventTrap_0c_17 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603095)
)
sCellEventTrap_0c_17.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_17.setStatus(
        ""
    )

sCellEventTrap_0c_18 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603096)
)
sCellEventTrap_0c_18.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_18.setStatus(
        ""
    )

sCellEventTrap_0c_19 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603097)
)
sCellEventTrap_0c_19.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_19.setStatus(
        ""
    )

sCellEventTrap_0c_1a = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603098)
)
sCellEventTrap_0c_1a.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_1a.setStatus(
        ""
    )

sCellEventTrap_0c_1b = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603099)
)
sCellEventTrap_0c_1b.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_1b.setStatus(
        ""
    )

sCellEventTrap_0c_1c = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603100)
)
sCellEventTrap_0c_1c.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_1c.setStatus(
        ""
    )

sCellEventTrap_0c_1d = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603101)
)
sCellEventTrap_0c_1d.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_1d.setStatus(
        ""
    )

sCellEventTrap_0c_1e = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603102)
)
sCellEventTrap_0c_1e.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_1e.setStatus(
        ""
    )

sCellEventTrap_0c_1f = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603103)
)
sCellEventTrap_0c_1f.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_1f.setStatus(
        ""
    )

sCellEventTrap_0c_20 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603104)
)
sCellEventTrap_0c_20.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_20.setStatus(
        ""
    )

sCellEventTrap_0c_21 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603105)
)
sCellEventTrap_0c_21.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_21.setStatus(
        ""
    )

sCellEventTrap_0c_22 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603106)
)
sCellEventTrap_0c_22.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0c_22.setStatus(
        ""
    )

sCellEventTrap_0d_00 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603328)
)
sCellEventTrap_0d_00.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_00.setStatus(
        ""
    )

sCellEventTrap_0d_01 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603329)
)
sCellEventTrap_0d_01.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_01.setStatus(
        ""
    )

sCellEventTrap_0d_02 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603330)
)
sCellEventTrap_0d_02.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_02.setStatus(
        ""
    )

sCellEventTrap_0d_03 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603331)
)
sCellEventTrap_0d_03.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_03.setStatus(
        ""
    )

sCellEventTrap_0d_04 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603332)
)
sCellEventTrap_0d_04.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_04.setStatus(
        ""
    )

sCellEventTrap_0d_33 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603379)
)
sCellEventTrap_0d_33.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_33.setStatus(
        ""
    )

sCellEventTrap_0d_34 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603380)
)
sCellEventTrap_0d_34.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_34.setStatus(
        ""
    )

sCellEventTrap_0d_35 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603381)
)
sCellEventTrap_0d_35.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_35.setStatus(
        ""
    )

sCellEventTrap_0d_47 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603399)
)
sCellEventTrap_0d_47.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_47.setStatus(
        ""
    )

sCellEventTrap_0d_4b = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603403)
)
sCellEventTrap_0d_4b.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_4b.setStatus(
        ""
    )

sCellEventTrap_0d_4c = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603404)
)
sCellEventTrap_0d_4c.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_4c.setStatus(
        ""
    )

sCellEventTrap_0d_5b = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603419)
)
sCellEventTrap_0d_5b.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_5b.setStatus(
        ""
    )

sCellEventTrap_0d_5f = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603423)
)
sCellEventTrap_0d_5f.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_5f.setStatus(
        ""
    )

sCellEventTrap_0d_6f = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603439)
)
sCellEventTrap_0d_6f.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_6f.setStatus(
        ""
    )

sCellEventTrap_0d_71 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603441)
)
sCellEventTrap_0d_71.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_71.setStatus(
        ""
    )

sCellEventTrap_0d_72 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603442)
)
sCellEventTrap_0d_72.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_72.setStatus(
        ""
    )

sCellEventTrap_0d_7e = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603454)
)
sCellEventTrap_0d_7e.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_7e.setStatus(
        ""
    )

sCellEventTrap_0d_7f = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603455)
)
sCellEventTrap_0d_7f.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_7f.setStatus(
        ""
    )

sCellEventTrap_0d_82 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603458)
)
sCellEventTrap_0d_82.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_82.setStatus(
        ""
    )

sCellEventTrap_0d_83 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603459)
)
sCellEventTrap_0d_83.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_83.setStatus(
        ""
    )

sCellEventTrap_0d_85 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603461)
)
sCellEventTrap_0d_85.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_85.setStatus(
        ""
    )

sCellEventTrap_0d_8d = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603469)
)
sCellEventTrap_0d_8d.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_8d.setStatus(
        ""
    )

sCellEventTrap_0d_a1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603489)
)
sCellEventTrap_0d_a1.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_a1.setStatus(
        ""
    )

sCellEventTrap_0d_b5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603509)
)
sCellEventTrap_0d_b5.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_b5.setStatus(
        ""
    )

sCellEventTrap_0d_d8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603544)
)
sCellEventTrap_0d_d8.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_d8.setStatus(
        ""
    )

sCellEventTrap_0d_d9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603545)
)
sCellEventTrap_0d_d9.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_d9.setStatus(
        ""
    )

sCellEventTrap_0d_dd = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603549)
)
sCellEventTrap_0d_dd.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_dd.setStatus(
        ""
    )

sCellEventTrap_0d_de = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603550)
)
sCellEventTrap_0d_de.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_de.setStatus(
        ""
    )

sCellEventTrap_0d_ec = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603564)
)
sCellEventTrap_0d_ec.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_ec.setStatus(
        ""
    )

sCellEventTrap_0d_f0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13603568)
)
sCellEventTrap_0d_f0.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_0d_f0.setStatus(
        ""
    )

sCellEventTrap_42_00 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13616896)
)
sCellEventTrap_42_00.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_42_00.setStatus(
        ""
    )

sCellEventTrap_42_01 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13616897)
)
sCellEventTrap_42_01.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_42_01.setStatus(
        ""
    )

sCellEventTrap_42_03 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13616899)
)
sCellEventTrap_42_03.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_42_03.setStatus(
        ""
    )

sCellEventTrap_42_04 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13616900)
)
sCellEventTrap_42_04.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_42_04.setStatus(
        ""
    )

sCellEventTrap_42_05 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13616901)
)
sCellEventTrap_42_05.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_42_05.setStatus(
        ""
    )

sCellEventTrap_83_00 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13633536)
)
sCellEventTrap_83_00.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_83_00.setStatus(
        ""
    )

sCellEventTrap_83_01 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13633537)
)
sCellEventTrap_83_01.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_83_01.setStatus(
        ""
    )

sCellEventTrap_83_02 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13633538)
)
sCellEventTrap_83_02.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_83_02.setStatus(
        ""
    )

sCellEventTrap_83_03 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13633539)
)
sCellEventTrap_83_03.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_83_03.setStatus(
        ""
    )

sCellEventTrap_83_04 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13633540)
)
sCellEventTrap_83_04.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_83_04.setStatus(
        ""
    )

sCellEventTrap_83_05 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13633541)
)
sCellEventTrap_83_05.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_83_05.setStatus(
        ""
    )

sCellEventTrap_83_06 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13633542)
)
sCellEventTrap_83_06.setObjects(
      *(("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "scellSWComponent"),
        ("CPQHSV-MIB", "scellECode"),
        ("CPQHSV-MIB", "scellCAC"),
        ("CPQHSV-MIB", "scellEIP"))
)
if mibBuilder.loadTexts:
    sCellEventTrap_83_06.setStatus(
        ""
    )

mngmtAgentTrap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000001)
)
mngmtAgentTrap_1.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1.setStatus(
        ""
    )

mngmtAgentTrap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000002)
)
mngmtAgentTrap_2.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2.setStatus(
        ""
    )

mngmtAgentTrap_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000003)
)
mngmtAgentTrap_3.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3.setStatus(
        ""
    )

mngmtAgentTrap_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000004)
)
mngmtAgentTrap_4.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4.setStatus(
        ""
    )

mngmtAgentTrap_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000005)
)
mngmtAgentTrap_5.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5.setStatus(
        ""
    )

mngmtAgentTrap_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000006)
)
mngmtAgentTrap_6.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6.setStatus(
        ""
    )

mngmtAgentTrap_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000007)
)
mngmtAgentTrap_7.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_7.setStatus(
        ""
    )

mngmtAgentTrap_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000008)
)
mngmtAgentTrap_8.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8.setStatus(
        ""
    )

mngmtAgentTrap_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000009)
)
mngmtAgentTrap_9.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9.setStatus(
        ""
    )

mngmtAgentTrap_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000010)
)
mngmtAgentTrap_10.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10.setStatus(
        ""
    )

mngmtAgentTrap_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000011)
)
mngmtAgentTrap_11.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_11.setStatus(
        ""
    )

mngmtAgentTrap_12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000012)
)
mngmtAgentTrap_12.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_12.setStatus(
        ""
    )

mngmtAgentTrap_13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000013)
)
mngmtAgentTrap_13.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_13.setStatus(
        ""
    )

mngmtAgentTrap_14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000014)
)
mngmtAgentTrap_14.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_14.setStatus(
        ""
    )

mngmtAgentTrap_15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000015)
)
mngmtAgentTrap_15.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_15.setStatus(
        ""
    )

mngmtAgentTrap_16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000016)
)
mngmtAgentTrap_16.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16.setStatus(
        ""
    )

mngmtAgentTrap_17 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000017)
)
mngmtAgentTrap_17.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17.setStatus(
        ""
    )

mngmtAgentTrap_18 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000018)
)
mngmtAgentTrap_18.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18.setStatus(
        ""
    )

mngmtAgentTrap_19 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000019)
)
mngmtAgentTrap_19.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_19.setStatus(
        ""
    )

mngmtAgentTrap_20 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000020)
)
mngmtAgentTrap_20.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20.setStatus(
        ""
    )

mngmtAgentTrap_21 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000021)
)
mngmtAgentTrap_21.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21.setStatus(
        ""
    )

mngmtAgentTrap_22 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000022)
)
mngmtAgentTrap_22.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_22.setStatus(
        ""
    )

mngmtAgentTrap_23 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000023)
)
mngmtAgentTrap_23.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_23.setStatus(
        ""
    )

mngmtAgentTrap_24 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000024)
)
mngmtAgentTrap_24.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_24.setStatus(
        ""
    )

mngmtAgentTrap_25 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000025)
)
mngmtAgentTrap_25.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25.setStatus(
        ""
    )

mngmtAgentTrap_26 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000026)
)
mngmtAgentTrap_26.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26.setStatus(
        ""
    )

mngmtAgentTrap_27 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000027)
)
mngmtAgentTrap_27.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27.setStatus(
        ""
    )

mngmtAgentTrap_28 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000028)
)
mngmtAgentTrap_28.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_28.setStatus(
        ""
    )

mngmtAgentTrap_29 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000029)
)
mngmtAgentTrap_29.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_29.setStatus(
        ""
    )

mngmtAgentTrap_30 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000030)
)
mngmtAgentTrap_30.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_30.setStatus(
        ""
    )

mngmtAgentTrap_31 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000031)
)
mngmtAgentTrap_31.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_31.setStatus(
        ""
    )

mngmtAgentTrap_32 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000032)
)
mngmtAgentTrap_32.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_32.setStatus(
        ""
    )

mngmtAgentTrap_33 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000033)
)
mngmtAgentTrap_33.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_33.setStatus(
        ""
    )

mngmtAgentTrap_34 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000034)
)
mngmtAgentTrap_34.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_34.setStatus(
        ""
    )

mngmtAgentTrap_35 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000035)
)
mngmtAgentTrap_35.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_35.setStatus(
        ""
    )

mngmtAgentTrap_36 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000036)
)
mngmtAgentTrap_36.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_36.setStatus(
        ""
    )

mngmtAgentTrap_37 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000037)
)
mngmtAgentTrap_37.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_37.setStatus(
        ""
    )

mngmtAgentTrap_38 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000038)
)
mngmtAgentTrap_38.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_38.setStatus(
        ""
    )

mngmtAgentTrap_39 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000039)
)
mngmtAgentTrap_39.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_39.setStatus(
        ""
    )

mngmtAgentTrap_40 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000040)
)
mngmtAgentTrap_40.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_40.setStatus(
        ""
    )

mngmtAgentTrap_41 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000041)
)
mngmtAgentTrap_41.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_41.setStatus(
        ""
    )

mngmtAgentTrap_42 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000042)
)
mngmtAgentTrap_42.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_42.setStatus(
        ""
    )

mngmtAgentTrap_43 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000043)
)
mngmtAgentTrap_43.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_43.setStatus(
        ""
    )

mngmtAgentTrap_44 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000044)
)
mngmtAgentTrap_44.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_44.setStatus(
        ""
    )

mngmtAgentTrap_45 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000045)
)
mngmtAgentTrap_45.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_45.setStatus(
        ""
    )

mngmtAgentTrap_46 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000046)
)
mngmtAgentTrap_46.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_46.setStatus(
        ""
    )

mngmtAgentTrap_47 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000047)
)
mngmtAgentTrap_47.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_47.setStatus(
        ""
    )

mngmtAgentTrap_48 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000048)
)
mngmtAgentTrap_48.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_48.setStatus(
        ""
    )

mngmtAgentTrap_49 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000049)
)
mngmtAgentTrap_49.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_49.setStatus(
        ""
    )

mngmtAgentTrap_50 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000050)
)
mngmtAgentTrap_50.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_50.setStatus(
        ""
    )

mngmtAgentTrap_51 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000051)
)
mngmtAgentTrap_51.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_51.setStatus(
        ""
    )

mngmtAgentTrap_52 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000052)
)
mngmtAgentTrap_52.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_52.setStatus(
        ""
    )

mngmtAgentTrap_53 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000053)
)
mngmtAgentTrap_53.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_53.setStatus(
        ""
    )

mngmtAgentTrap_54 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000054)
)
mngmtAgentTrap_54.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_54.setStatus(
        ""
    )

mngmtAgentTrap_55 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000055)
)
mngmtAgentTrap_55.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_55.setStatus(
        ""
    )

mngmtAgentTrap_56 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000056)
)
mngmtAgentTrap_56.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_56.setStatus(
        ""
    )

mngmtAgentTrap_57 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000057)
)
mngmtAgentTrap_57.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_57.setStatus(
        ""
    )

mngmtAgentTrap_58 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000058)
)
mngmtAgentTrap_58.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_58.setStatus(
        ""
    )

mngmtAgentTrap_59 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000059)
)
mngmtAgentTrap_59.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_59.setStatus(
        ""
    )

mngmtAgentTrap_60 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000060)
)
mngmtAgentTrap_60.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_60.setStatus(
        ""
    )

mngmtAgentTrap_61 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000061)
)
mngmtAgentTrap_61.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_61.setStatus(
        ""
    )

mngmtAgentTrap_62 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000062)
)
mngmtAgentTrap_62.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_62.setStatus(
        ""
    )

mngmtAgentTrap_63 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000063)
)
mngmtAgentTrap_63.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_63.setStatus(
        ""
    )

mngmtAgentTrap_64 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000064)
)
mngmtAgentTrap_64.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_64.setStatus(
        ""
    )

mngmtAgentTrap_65 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000065)
)
mngmtAgentTrap_65.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_65.setStatus(
        ""
    )

mngmtAgentTrap_66 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000066)
)
mngmtAgentTrap_66.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_66.setStatus(
        ""
    )

mngmtAgentTrap_67 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000067)
)
mngmtAgentTrap_67.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_67.setStatus(
        ""
    )

mngmtAgentTrap_68 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000068)
)
mngmtAgentTrap_68.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_68.setStatus(
        ""
    )

mngmtAgentTrap_69 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000069)
)
mngmtAgentTrap_69.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_69.setStatus(
        ""
    )

mngmtAgentTrap_70 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000070)
)
mngmtAgentTrap_70.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_70.setStatus(
        ""
    )

mngmtAgentTrap_71 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000071)
)
mngmtAgentTrap_71.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_71.setStatus(
        ""
    )

mngmtAgentTrap_72 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000072)
)
mngmtAgentTrap_72.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_72.setStatus(
        ""
    )

mngmtAgentTrap_73 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000073)
)
mngmtAgentTrap_73.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_73.setStatus(
        ""
    )

mngmtAgentTrap_74 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000074)
)
mngmtAgentTrap_74.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_74.setStatus(
        ""
    )

mngmtAgentTrap_75 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000075)
)
mngmtAgentTrap_75.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_75.setStatus(
        ""
    )

mngmtAgentTrap_76 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000076)
)
mngmtAgentTrap_76.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_76.setStatus(
        ""
    )

mngmtAgentTrap_77 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000077)
)
mngmtAgentTrap_77.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_77.setStatus(
        ""
    )

mngmtAgentTrap_78 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000078)
)
mngmtAgentTrap_78.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_78.setStatus(
        ""
    )

mngmtAgentTrap_79 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000079)
)
mngmtAgentTrap_79.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_79.setStatus(
        ""
    )

mngmtAgentTrap_80 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000080)
)
mngmtAgentTrap_80.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_80.setStatus(
        ""
    )

mngmtAgentTrap_81 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000081)
)
mngmtAgentTrap_81.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_81.setStatus(
        ""
    )

mngmtAgentTrap_82 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000082)
)
mngmtAgentTrap_82.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_82.setStatus(
        ""
    )

mngmtAgentTrap_83 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000083)
)
mngmtAgentTrap_83.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_83.setStatus(
        ""
    )

mngmtAgentTrap_84 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000084)
)
mngmtAgentTrap_84.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_84.setStatus(
        ""
    )

mngmtAgentTrap_85 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000085)
)
mngmtAgentTrap_85.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_85.setStatus(
        ""
    )

mngmtAgentTrap_86 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000086)
)
mngmtAgentTrap_86.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_86.setStatus(
        ""
    )

mngmtAgentTrap_87 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000087)
)
mngmtAgentTrap_87.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_87.setStatus(
        ""
    )

mngmtAgentTrap_88 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000088)
)
mngmtAgentTrap_88.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_88.setStatus(
        ""
    )

mngmtAgentTrap_89 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000089)
)
mngmtAgentTrap_89.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_89.setStatus(
        ""
    )

mngmtAgentTrap_90 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000090)
)
mngmtAgentTrap_90.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_90.setStatus(
        ""
    )

mngmtAgentTrap_91 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000091)
)
mngmtAgentTrap_91.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_91.setStatus(
        ""
    )

mngmtAgentTrap_92 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000092)
)
mngmtAgentTrap_92.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_92.setStatus(
        ""
    )

mngmtAgentTrap_93 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000093)
)
mngmtAgentTrap_93.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_93.setStatus(
        ""
    )

mngmtAgentTrap_94 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000094)
)
mngmtAgentTrap_94.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_94.setStatus(
        ""
    )

mngmtAgentTrap_95 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000095)
)
mngmtAgentTrap_95.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_95.setStatus(
        ""
    )

mngmtAgentTrap_96 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000096)
)
mngmtAgentTrap_96.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_96.setStatus(
        ""
    )

mngmtAgentTrap_97 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000097)
)
mngmtAgentTrap_97.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_97.setStatus(
        ""
    )

mngmtAgentTrap_98 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000098)
)
mngmtAgentTrap_98.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_98.setStatus(
        ""
    )

mngmtAgentTrap_99 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000099)
)
mngmtAgentTrap_99.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_99.setStatus(
        ""
    )

mngmtAgentTrap_100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000100)
)
mngmtAgentTrap_100.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_100.setStatus(
        ""
    )

mngmtAgentTrap_101 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000101)
)
mngmtAgentTrap_101.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_101.setStatus(
        ""
    )

mngmtAgentTrap_102 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000102)
)
mngmtAgentTrap_102.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_102.setStatus(
        ""
    )

mngmtAgentTrap_103 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000103)
)
mngmtAgentTrap_103.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_103.setStatus(
        ""
    )

mngmtAgentTrap_104 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000104)
)
mngmtAgentTrap_104.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_104.setStatus(
        ""
    )

mngmtAgentTrap_105 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000105)
)
mngmtAgentTrap_105.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_105.setStatus(
        ""
    )

mngmtAgentTrap_106 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000106)
)
mngmtAgentTrap_106.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_106.setStatus(
        ""
    )

mngmtAgentTrap_107 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000107)
)
mngmtAgentTrap_107.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_107.setStatus(
        ""
    )

mngmtAgentTrap_108 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000108)
)
mngmtAgentTrap_108.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_108.setStatus(
        ""
    )

mngmtAgentTrap_109 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000109)
)
mngmtAgentTrap_109.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_109.setStatus(
        ""
    )

mngmtAgentTrap_110 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000110)
)
mngmtAgentTrap_110.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_110.setStatus(
        ""
    )

mngmtAgentTrap_111 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000111)
)
mngmtAgentTrap_111.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_111.setStatus(
        ""
    )

mngmtAgentTrap_112 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000112)
)
mngmtAgentTrap_112.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_112.setStatus(
        ""
    )

mngmtAgentTrap_113 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000113)
)
mngmtAgentTrap_113.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_113.setStatus(
        ""
    )

mngmtAgentTrap_114 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000114)
)
mngmtAgentTrap_114.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_114.setStatus(
        ""
    )

mngmtAgentTrap_115 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000115)
)
mngmtAgentTrap_115.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_115.setStatus(
        ""
    )

mngmtAgentTrap_116 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000116)
)
mngmtAgentTrap_116.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_116.setStatus(
        ""
    )

mngmtAgentTrap_117 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000117)
)
mngmtAgentTrap_117.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_117.setStatus(
        ""
    )

mngmtAgentTrap_118 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000118)
)
mngmtAgentTrap_118.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_118.setStatus(
        ""
    )

mngmtAgentTrap_119 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000119)
)
mngmtAgentTrap_119.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_119.setStatus(
        ""
    )

mngmtAgentTrap_120 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000120)
)
mngmtAgentTrap_120.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_120.setStatus(
        ""
    )

mngmtAgentTrap_121 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000121)
)
mngmtAgentTrap_121.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_121.setStatus(
        ""
    )

mngmtAgentTrap_122 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000122)
)
mngmtAgentTrap_122.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_122.setStatus(
        ""
    )

mngmtAgentTrap_123 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000123)
)
mngmtAgentTrap_123.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_123.setStatus(
        ""
    )

mngmtAgentTrap_124 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000124)
)
mngmtAgentTrap_124.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_124.setStatus(
        ""
    )

mngmtAgentTrap_125 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000125)
)
mngmtAgentTrap_125.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_125.setStatus(
        ""
    )

mngmtAgentTrap_126 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000126)
)
mngmtAgentTrap_126.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_126.setStatus(
        ""
    )

mngmtAgentTrap_127 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000127)
)
mngmtAgentTrap_127.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_127.setStatus(
        ""
    )

mngmtAgentTrap_128 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000128)
)
mngmtAgentTrap_128.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_128.setStatus(
        ""
    )

mngmtAgentTrap_129 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000129)
)
mngmtAgentTrap_129.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_129.setStatus(
        ""
    )

mngmtAgentTrap_130 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000130)
)
mngmtAgentTrap_130.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_130.setStatus(
        ""
    )

mngmtAgentTrap_131 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000131)
)
mngmtAgentTrap_131.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_131.setStatus(
        ""
    )

mngmtAgentTrap_132 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000132)
)
mngmtAgentTrap_132.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_132.setStatus(
        ""
    )

mngmtAgentTrap_133 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000133)
)
mngmtAgentTrap_133.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_133.setStatus(
        ""
    )

mngmtAgentTrap_134 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000134)
)
mngmtAgentTrap_134.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_134.setStatus(
        ""
    )

mngmtAgentTrap_141 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000141)
)
mngmtAgentTrap_141.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_141.setStatus(
        ""
    )

mngmtAgentTrap_142 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000142)
)
mngmtAgentTrap_142.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_142.setStatus(
        ""
    )

mngmtAgentTrap_148 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000148)
)
mngmtAgentTrap_148.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_148.setStatus(
        ""
    )

mngmtAgentTrap_180 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000180)
)
mngmtAgentTrap_180.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_180.setStatus(
        ""
    )

mngmtAgentTrap_181 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000181)
)
mngmtAgentTrap_181.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_181.setStatus(
        ""
    )

mngmtAgentTrap_182 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000182)
)
mngmtAgentTrap_182.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_182.setStatus(
        ""
    )

mngmtAgentTrap_183 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000183)
)
mngmtAgentTrap_183.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_183.setStatus(
        ""
    )

mngmtAgentTrap_184 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000184)
)
mngmtAgentTrap_184.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_184.setStatus(
        ""
    )

mngmtAgentTrap_195 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000195)
)
mngmtAgentTrap_195.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_195.setStatus(
        ""
    )

mngmtAgentTrap_196 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000196)
)
mngmtAgentTrap_196.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_196.setStatus(
        ""
    )

mngmtAgentTrap_197 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000197)
)
mngmtAgentTrap_197.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_197.setStatus(
        ""
    )

mngmtAgentTrap_198 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000198)
)
mngmtAgentTrap_198.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_198.setStatus(
        ""
    )

mngmtAgentTrap_199 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000199)
)
mngmtAgentTrap_199.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_199.setStatus(
        ""
    )

mngmtAgentTrap_200 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000200)
)
mngmtAgentTrap_200.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_200.setStatus(
        ""
    )

mngmtAgentTrap_201 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000201)
)
mngmtAgentTrap_201.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_201.setStatus(
        ""
    )

mngmtAgentTrap_202 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136000202)
)
mngmtAgentTrap_202.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_202.setStatus(
        ""
    )

mngmtAgentTrap_1000 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001000)
)
mngmtAgentTrap_1000.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1000.setStatus(
        ""
    )

mngmtAgentTrap_1001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001001)
)
mngmtAgentTrap_1001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1001.setStatus(
        ""
    )

mngmtAgentTrap_1002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001002)
)
mngmtAgentTrap_1002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1002.setStatus(
        ""
    )

mngmtAgentTrap_1003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001003)
)
mngmtAgentTrap_1003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1003.setStatus(
        ""
    )

mngmtAgentTrap_1004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001004)
)
mngmtAgentTrap_1004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1004.setStatus(
        ""
    )

mngmtAgentTrap_1005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001005)
)
mngmtAgentTrap_1005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1005.setStatus(
        ""
    )

mngmtAgentTrap_1006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001006)
)
mngmtAgentTrap_1006.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1006.setStatus(
        ""
    )

mngmtAgentTrap_1007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001007)
)
mngmtAgentTrap_1007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1007.setStatus(
        ""
    )

mngmtAgentTrap_1008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001008)
)
mngmtAgentTrap_1008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1008.setStatus(
        ""
    )

mngmtAgentTrap_1009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001009)
)
mngmtAgentTrap_1009.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1009.setStatus(
        ""
    )

mngmtAgentTrap_1010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001010)
)
mngmtAgentTrap_1010.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1010.setStatus(
        ""
    )

mngmtAgentTrap_1011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001011)
)
mngmtAgentTrap_1011.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1011.setStatus(
        ""
    )

mngmtAgentTrap_1012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001012)
)
mngmtAgentTrap_1012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1012.setStatus(
        ""
    )

mngmtAgentTrap_1013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001013)
)
mngmtAgentTrap_1013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1013.setStatus(
        ""
    )

mngmtAgentTrap_1014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136001014)
)
mngmtAgentTrap_1014.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_1014.setStatus(
        ""
    )

mngmtAgentTrap_2001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002001)
)
mngmtAgentTrap_2001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2001.setStatus(
        ""
    )

mngmtAgentTrap_2002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002002)
)
mngmtAgentTrap_2002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2002.setStatus(
        ""
    )

mngmtAgentTrap_2003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002003)
)
mngmtAgentTrap_2003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2003.setStatus(
        ""
    )

mngmtAgentTrap_2004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002004)
)
mngmtAgentTrap_2004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2004.setStatus(
        ""
    )

mngmtAgentTrap_2006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002006)
)
mngmtAgentTrap_2006.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2006.setStatus(
        ""
    )

mngmtAgentTrap_2007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002007)
)
mngmtAgentTrap_2007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2007.setStatus(
        ""
    )

mngmtAgentTrap_2008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002008)
)
mngmtAgentTrap_2008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2008.setStatus(
        ""
    )

mngmtAgentTrap_2010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002010)
)
mngmtAgentTrap_2010.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2010.setStatus(
        ""
    )

mngmtAgentTrap_2011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002011)
)
mngmtAgentTrap_2011.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2011.setStatus(
        ""
    )

mngmtAgentTrap_2012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002012)
)
mngmtAgentTrap_2012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2012.setStatus(
        ""
    )

mngmtAgentTrap_2013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002013)
)
mngmtAgentTrap_2013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2013.setStatus(
        ""
    )

mngmtAgentTrap_2016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002016)
)
mngmtAgentTrap_2016.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2016.setStatus(
        ""
    )

mngmtAgentTrap_2021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002021)
)
mngmtAgentTrap_2021.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2021.setStatus(
        ""
    )

mngmtAgentTrap_2022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002022)
)
mngmtAgentTrap_2022.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2022.setStatus(
        ""
    )

mngmtAgentTrap_2023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002023)
)
mngmtAgentTrap_2023.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2023.setStatus(
        ""
    )

mngmtAgentTrap_2025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002025)
)
mngmtAgentTrap_2025.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2025.setStatus(
        ""
    )

mngmtAgentTrap_2026 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002026)
)
mngmtAgentTrap_2026.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2026.setStatus(
        ""
    )

mngmtAgentTrap_2030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002030)
)
mngmtAgentTrap_2030.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2030.setStatus(
        ""
    )

mngmtAgentTrap_2031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002031)
)
mngmtAgentTrap_2031.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2031.setStatus(
        ""
    )

mngmtAgentTrap_2032 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002032)
)
mngmtAgentTrap_2032.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2032.setStatus(
        ""
    )

mngmtAgentTrap_2033 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002033)
)
mngmtAgentTrap_2033.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2033.setStatus(
        ""
    )

mngmtAgentTrap_2034 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002034)
)
mngmtAgentTrap_2034.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2034.setStatus(
        ""
    )

mngmtAgentTrap_2035 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002035)
)
mngmtAgentTrap_2035.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2035.setStatus(
        ""
    )

mngmtAgentTrap_2036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002036)
)
mngmtAgentTrap_2036.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2036.setStatus(
        ""
    )

mngmtAgentTrap_2038 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002038)
)
mngmtAgentTrap_2038.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2038.setStatus(
        ""
    )

mngmtAgentTrap_2040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002040)
)
mngmtAgentTrap_2040.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2040.setStatus(
        ""
    )

mngmtAgentTrap_2041 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002041)
)
mngmtAgentTrap_2041.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2041.setStatus(
        ""
    )

mngmtAgentTrap_2042 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002042)
)
mngmtAgentTrap_2042.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2042.setStatus(
        ""
    )

mngmtAgentTrap_2047 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002047)
)
mngmtAgentTrap_2047.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2047.setStatus(
        ""
    )

mngmtAgentTrap_2048 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002048)
)
mngmtAgentTrap_2048.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2048.setStatus(
        ""
    )

mngmtAgentTrap_2049 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002049)
)
mngmtAgentTrap_2049.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2049.setStatus(
        ""
    )

mngmtAgentTrap_2050 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002050)
)
mngmtAgentTrap_2050.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2050.setStatus(
        ""
    )

mngmtAgentTrap_2051 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002051)
)
mngmtAgentTrap_2051.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2051.setStatus(
        ""
    )

mngmtAgentTrap_2052 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002052)
)
mngmtAgentTrap_2052.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2052.setStatus(
        ""
    )

mngmtAgentTrap_2057 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002057)
)
mngmtAgentTrap_2057.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2057.setStatus(
        ""
    )

mngmtAgentTrap_2058 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002058)
)
mngmtAgentTrap_2058.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2058.setStatus(
        ""
    )

mngmtAgentTrap_2059 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002059)
)
mngmtAgentTrap_2059.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2059.setStatus(
        ""
    )

mngmtAgentTrap_2060 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002060)
)
mngmtAgentTrap_2060.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2060.setStatus(
        ""
    )

mngmtAgentTrap_2061 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002061)
)
mngmtAgentTrap_2061.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2061.setStatus(
        ""
    )

mngmtAgentTrap_2062 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002062)
)
mngmtAgentTrap_2062.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2062.setStatus(
        ""
    )

mngmtAgentTrap_2063 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002063)
)
mngmtAgentTrap_2063.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2063.setStatus(
        ""
    )

mngmtAgentTrap_2064 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002064)
)
mngmtAgentTrap_2064.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2064.setStatus(
        ""
    )

mngmtAgentTrap_2065 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002065)
)
mngmtAgentTrap_2065.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2065.setStatus(
        ""
    )

mngmtAgentTrap_2066 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002066)
)
mngmtAgentTrap_2066.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2066.setStatus(
        ""
    )

mngmtAgentTrap_2067 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002067)
)
mngmtAgentTrap_2067.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2067.setStatus(
        ""
    )

mngmtAgentTrap_2068 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002068)
)
mngmtAgentTrap_2068.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2068.setStatus(
        ""
    )

mngmtAgentTrap_2069 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002069)
)
mngmtAgentTrap_2069.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2069.setStatus(
        ""
    )

mngmtAgentTrap_2070 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002070)
)
mngmtAgentTrap_2070.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2070.setStatus(
        ""
    )

mngmtAgentTrap_2071 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002071)
)
mngmtAgentTrap_2071.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2071.setStatus(
        ""
    )

mngmtAgentTrap_2072 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002072)
)
mngmtAgentTrap_2072.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2072.setStatus(
        ""
    )

mngmtAgentTrap_2073 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002073)
)
mngmtAgentTrap_2073.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2073.setStatus(
        ""
    )

mngmtAgentTrap_2074 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002074)
)
mngmtAgentTrap_2074.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2074.setStatus(
        ""
    )

mngmtAgentTrap_2075 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002075)
)
mngmtAgentTrap_2075.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2075.setStatus(
        ""
    )

mngmtAgentTrap_2076 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002076)
)
mngmtAgentTrap_2076.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2076.setStatus(
        ""
    )

mngmtAgentTrap_2077 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002077)
)
mngmtAgentTrap_2077.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2077.setStatus(
        ""
    )

mngmtAgentTrap_2078 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002078)
)
mngmtAgentTrap_2078.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2078.setStatus(
        ""
    )

mngmtAgentTrap_2079 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002079)
)
mngmtAgentTrap_2079.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2079.setStatus(
        ""
    )

mngmtAgentTrap_2080 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002080)
)
mngmtAgentTrap_2080.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2080.setStatus(
        ""
    )

mngmtAgentTrap_2081 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002081)
)
mngmtAgentTrap_2081.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2081.setStatus(
        ""
    )

mngmtAgentTrap_2082 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002082)
)
mngmtAgentTrap_2082.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2082.setStatus(
        ""
    )

mngmtAgentTrap_2083 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002083)
)
mngmtAgentTrap_2083.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2083.setStatus(
        ""
    )

mngmtAgentTrap_2084 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002084)
)
mngmtAgentTrap_2084.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2084.setStatus(
        ""
    )

mngmtAgentTrap_2085 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002085)
)
mngmtAgentTrap_2085.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2085.setStatus(
        ""
    )

mngmtAgentTrap_2086 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002086)
)
mngmtAgentTrap_2086.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2086.setStatus(
        ""
    )

mngmtAgentTrap_2087 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002087)
)
mngmtAgentTrap_2087.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2087.setStatus(
        ""
    )

mngmtAgentTrap_2088 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002088)
)
mngmtAgentTrap_2088.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2088.setStatus(
        ""
    )

mngmtAgentTrap_2089 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002089)
)
mngmtAgentTrap_2089.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2089.setStatus(
        ""
    )

mngmtAgentTrap_2090 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002090)
)
mngmtAgentTrap_2090.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2090.setStatus(
        ""
    )

mngmtAgentTrap_2091 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002091)
)
mngmtAgentTrap_2091.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2091.setStatus(
        ""
    )

mngmtAgentTrap_2092 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002092)
)
mngmtAgentTrap_2092.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2092.setStatus(
        ""
    )

mngmtAgentTrap_2093 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002093)
)
mngmtAgentTrap_2093.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2093.setStatus(
        ""
    )

mngmtAgentTrap_2095 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002095)
)
mngmtAgentTrap_2095.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2095.setStatus(
        ""
    )

mngmtAgentTrap_2096 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002096)
)
mngmtAgentTrap_2096.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2096.setStatus(
        ""
    )

mngmtAgentTrap_2097 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002097)
)
mngmtAgentTrap_2097.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2097.setStatus(
        ""
    )

mngmtAgentTrap_2098 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002098)
)
mngmtAgentTrap_2098.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2098.setStatus(
        ""
    )

mngmtAgentTrap_2099 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002099)
)
mngmtAgentTrap_2099.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2099.setStatus(
        ""
    )

mngmtAgentTrap_2100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002100)
)
mngmtAgentTrap_2100.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2100.setStatus(
        ""
    )

mngmtAgentTrap_2102 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002102)
)
mngmtAgentTrap_2102.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2102.setStatus(
        ""
    )

mngmtAgentTrap_2103 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002103)
)
mngmtAgentTrap_2103.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2103.setStatus(
        ""
    )

mngmtAgentTrap_2104 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002104)
)
mngmtAgentTrap_2104.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2104.setStatus(
        ""
    )

mngmtAgentTrap_2105 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136002105)
)
mngmtAgentTrap_2105.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_2105.setStatus(
        ""
    )

mngmtAgentTrap_3001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003001)
)
mngmtAgentTrap_3001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3001.setStatus(
        ""
    )

mngmtAgentTrap_3002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003002)
)
mngmtAgentTrap_3002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3002.setStatus(
        ""
    )

mngmtAgentTrap_3003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003003)
)
mngmtAgentTrap_3003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3003.setStatus(
        ""
    )

mngmtAgentTrap_3004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003004)
)
mngmtAgentTrap_3004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3004.setStatus(
        ""
    )

mngmtAgentTrap_3007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003007)
)
mngmtAgentTrap_3007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3007.setStatus(
        ""
    )

mngmtAgentTrap_3009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003009)
)
mngmtAgentTrap_3009.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3009.setStatus(
        ""
    )

mngmtAgentTrap_3012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003012)
)
mngmtAgentTrap_3012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3012.setStatus(
        ""
    )

mngmtAgentTrap_3013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003013)
)
mngmtAgentTrap_3013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3013.setStatus(
        ""
    )

mngmtAgentTrap_3015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003015)
)
mngmtAgentTrap_3015.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3015.setStatus(
        ""
    )

mngmtAgentTrap_3016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003016)
)
mngmtAgentTrap_3016.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3016.setStatus(
        ""
    )

mngmtAgentTrap_3017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003017)
)
mngmtAgentTrap_3017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3017.setStatus(
        ""
    )

mngmtAgentTrap_3019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003019)
)
mngmtAgentTrap_3019.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3019.setStatus(
        ""
    )

mngmtAgentTrap_3020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003020)
)
mngmtAgentTrap_3020.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3020.setStatus(
        ""
    )

mngmtAgentTrap_3021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003021)
)
mngmtAgentTrap_3021.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3021.setStatus(
        ""
    )

mngmtAgentTrap_3022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003022)
)
mngmtAgentTrap_3022.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3022.setStatus(
        ""
    )

mngmtAgentTrap_3024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003024)
)
mngmtAgentTrap_3024.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3024.setStatus(
        ""
    )

mngmtAgentTrap_3025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003025)
)
mngmtAgentTrap_3025.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3025.setStatus(
        ""
    )

mngmtAgentTrap_3028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003028)
)
mngmtAgentTrap_3028.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3028.setStatus(
        ""
    )

mngmtAgentTrap_3029 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003029)
)
mngmtAgentTrap_3029.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3029.setStatus(
        ""
    )

mngmtAgentTrap_3035 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003035)
)
mngmtAgentTrap_3035.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3035.setStatus(
        ""
    )

mngmtAgentTrap_3036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003036)
)
mngmtAgentTrap_3036.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3036.setStatus(
        ""
    )

mngmtAgentTrap_3037 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003037)
)
mngmtAgentTrap_3037.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3037.setStatus(
        ""
    )

mngmtAgentTrap_3038 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003038)
)
mngmtAgentTrap_3038.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3038.setStatus(
        ""
    )

mngmtAgentTrap_3039 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003039)
)
mngmtAgentTrap_3039.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3039.setStatus(
        ""
    )

mngmtAgentTrap_3044 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003044)
)
mngmtAgentTrap_3044.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3044.setStatus(
        ""
    )

mngmtAgentTrap_3045 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003045)
)
mngmtAgentTrap_3045.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3045.setStatus(
        ""
    )

mngmtAgentTrap_3046 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003046)
)
mngmtAgentTrap_3046.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3046.setStatus(
        ""
    )

mngmtAgentTrap_3047 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003047)
)
mngmtAgentTrap_3047.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3047.setStatus(
        ""
    )

mngmtAgentTrap_3048 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003048)
)
mngmtAgentTrap_3048.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3048.setStatus(
        ""
    )

mngmtAgentTrap_3049 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003049)
)
mngmtAgentTrap_3049.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3049.setStatus(
        ""
    )

mngmtAgentTrap_3050 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003050)
)
mngmtAgentTrap_3050.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3050.setStatus(
        ""
    )

mngmtAgentTrap_3051 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003051)
)
mngmtAgentTrap_3051.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3051.setStatus(
        ""
    )

mngmtAgentTrap_3053 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003053)
)
mngmtAgentTrap_3053.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3053.setStatus(
        ""
    )

mngmtAgentTrap_3054 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003054)
)
mngmtAgentTrap_3054.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3054.setStatus(
        ""
    )

mngmtAgentTrap_3055 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003055)
)
mngmtAgentTrap_3055.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3055.setStatus(
        ""
    )

mngmtAgentTrap_3056 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003056)
)
mngmtAgentTrap_3056.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3056.setStatus(
        ""
    )

mngmtAgentTrap_3057 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003057)
)
mngmtAgentTrap_3057.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3057.setStatus(
        ""
    )

mngmtAgentTrap_3058 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003058)
)
mngmtAgentTrap_3058.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3058.setStatus(
        ""
    )

mngmtAgentTrap_3059 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003059)
)
mngmtAgentTrap_3059.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3059.setStatus(
        ""
    )

mngmtAgentTrap_3060 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003060)
)
mngmtAgentTrap_3060.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3060.setStatus(
        ""
    )

mngmtAgentTrap_3061 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003061)
)
mngmtAgentTrap_3061.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3061.setStatus(
        ""
    )

mngmtAgentTrap_3062 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003062)
)
mngmtAgentTrap_3062.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3062.setStatus(
        ""
    )

mngmtAgentTrap_3063 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003063)
)
mngmtAgentTrap_3063.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3063.setStatus(
        ""
    )

mngmtAgentTrap_3064 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003064)
)
mngmtAgentTrap_3064.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3064.setStatus(
        ""
    )

mngmtAgentTrap_3065 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003065)
)
mngmtAgentTrap_3065.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3065.setStatus(
        ""
    )

mngmtAgentTrap_3066 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003066)
)
mngmtAgentTrap_3066.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3066.setStatus(
        ""
    )

mngmtAgentTrap_3067 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003067)
)
mngmtAgentTrap_3067.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3067.setStatus(
        ""
    )

mngmtAgentTrap_3068 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003068)
)
mngmtAgentTrap_3068.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3068.setStatus(
        ""
    )

mngmtAgentTrap_3069 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003069)
)
mngmtAgentTrap_3069.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3069.setStatus(
        ""
    )

mngmtAgentTrap_3070 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003070)
)
mngmtAgentTrap_3070.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3070.setStatus(
        ""
    )

mngmtAgentTrap_3071 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003071)
)
mngmtAgentTrap_3071.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3071.setStatus(
        ""
    )

mngmtAgentTrap_3072 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003072)
)
mngmtAgentTrap_3072.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3072.setStatus(
        ""
    )

mngmtAgentTrap_3075 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003075)
)
mngmtAgentTrap_3075.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3075.setStatus(
        ""
    )

mngmtAgentTrap_3076 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003076)
)
mngmtAgentTrap_3076.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3076.setStatus(
        ""
    )

mngmtAgentTrap_3077 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003077)
)
mngmtAgentTrap_3077.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3077.setStatus(
        ""
    )

mngmtAgentTrap_3078 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003078)
)
mngmtAgentTrap_3078.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3078.setStatus(
        ""
    )

mngmtAgentTrap_3079 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003079)
)
mngmtAgentTrap_3079.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3079.setStatus(
        ""
    )

mngmtAgentTrap_3080 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003080)
)
mngmtAgentTrap_3080.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3080.setStatus(
        ""
    )

mngmtAgentTrap_3081 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003081)
)
mngmtAgentTrap_3081.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3081.setStatus(
        ""
    )

mngmtAgentTrap_3083 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003083)
)
mngmtAgentTrap_3083.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3083.setStatus(
        ""
    )

mngmtAgentTrap_3084 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003084)
)
mngmtAgentTrap_3084.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3084.setStatus(
        ""
    )

mngmtAgentTrap_3086 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003086)
)
mngmtAgentTrap_3086.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3086.setStatus(
        ""
    )

mngmtAgentTrap_3090 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003090)
)
mngmtAgentTrap_3090.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3090.setStatus(
        ""
    )

mngmtAgentTrap_3091 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003091)
)
mngmtAgentTrap_3091.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3091.setStatus(
        ""
    )

mngmtAgentTrap_3092 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003092)
)
mngmtAgentTrap_3092.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3092.setStatus(
        ""
    )

mngmtAgentTrap_3094 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003094)
)
mngmtAgentTrap_3094.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3094.setStatus(
        ""
    )

mngmtAgentTrap_3095 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136003095)
)
mngmtAgentTrap_3095.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_3095.setStatus(
        ""
    )

mngmtAgentTrap_4000 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004000)
)
mngmtAgentTrap_4000.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4000.setStatus(
        ""
    )

mngmtAgentTrap_4001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004001)
)
mngmtAgentTrap_4001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4001.setStatus(
        ""
    )

mngmtAgentTrap_4004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004004)
)
mngmtAgentTrap_4004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4004.setStatus(
        ""
    )

mngmtAgentTrap_4005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004005)
)
mngmtAgentTrap_4005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4005.setStatus(
        ""
    )

mngmtAgentTrap_4007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004007)
)
mngmtAgentTrap_4007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4007.setStatus(
        ""
    )

mngmtAgentTrap_4011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004011)
)
mngmtAgentTrap_4011.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4011.setStatus(
        ""
    )

mngmtAgentTrap_4012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004012)
)
mngmtAgentTrap_4012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4012.setStatus(
        ""
    )

mngmtAgentTrap_4013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004013)
)
mngmtAgentTrap_4013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4013.setStatus(
        ""
    )

mngmtAgentTrap_4014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004014)
)
mngmtAgentTrap_4014.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4014.setStatus(
        ""
    )

mngmtAgentTrap_4015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004015)
)
mngmtAgentTrap_4015.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4015.setStatus(
        ""
    )

mngmtAgentTrap_4016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004016)
)
mngmtAgentTrap_4016.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4016.setStatus(
        ""
    )

mngmtAgentTrap_4017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004017)
)
mngmtAgentTrap_4017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4017.setStatus(
        ""
    )

mngmtAgentTrap_4018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004018)
)
mngmtAgentTrap_4018.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4018.setStatus(
        ""
    )

mngmtAgentTrap_4020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004020)
)
mngmtAgentTrap_4020.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4020.setStatus(
        ""
    )

mngmtAgentTrap_4021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004021)
)
mngmtAgentTrap_4021.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4021.setStatus(
        ""
    )

mngmtAgentTrap_4023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004023)
)
mngmtAgentTrap_4023.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4023.setStatus(
        ""
    )

mngmtAgentTrap_4024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004024)
)
mngmtAgentTrap_4024.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4024.setStatus(
        ""
    )

mngmtAgentTrap_4025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004025)
)
mngmtAgentTrap_4025.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4025.setStatus(
        ""
    )

mngmtAgentTrap_4027 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004027)
)
mngmtAgentTrap_4027.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4027.setStatus(
        ""
    )

mngmtAgentTrap_4028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004028)
)
mngmtAgentTrap_4028.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4028.setStatus(
        ""
    )

mngmtAgentTrap_4029 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004029)
)
mngmtAgentTrap_4029.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4029.setStatus(
        ""
    )

mngmtAgentTrap_4030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004030)
)
mngmtAgentTrap_4030.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4030.setStatus(
        ""
    )

mngmtAgentTrap_4031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004031)
)
mngmtAgentTrap_4031.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4031.setStatus(
        ""
    )

mngmtAgentTrap_4032 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004032)
)
mngmtAgentTrap_4032.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4032.setStatus(
        ""
    )

mngmtAgentTrap_4033 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004033)
)
mngmtAgentTrap_4033.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4033.setStatus(
        ""
    )

mngmtAgentTrap_4034 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004034)
)
mngmtAgentTrap_4034.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4034.setStatus(
        ""
    )

mngmtAgentTrap_4035 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004035)
)
mngmtAgentTrap_4035.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4035.setStatus(
        ""
    )

mngmtAgentTrap_4036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004036)
)
mngmtAgentTrap_4036.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4036.setStatus(
        ""
    )

mngmtAgentTrap_4037 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004037)
)
mngmtAgentTrap_4037.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4037.setStatus(
        ""
    )

mngmtAgentTrap_4040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004040)
)
mngmtAgentTrap_4040.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4040.setStatus(
        ""
    )

mngmtAgentTrap_4041 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004041)
)
mngmtAgentTrap_4041.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4041.setStatus(
        ""
    )

mngmtAgentTrap_4042 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004042)
)
mngmtAgentTrap_4042.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4042.setStatus(
        ""
    )

mngmtAgentTrap_4043 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004043)
)
mngmtAgentTrap_4043.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4043.setStatus(
        ""
    )

mngmtAgentTrap_4047 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004047)
)
mngmtAgentTrap_4047.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4047.setStatus(
        ""
    )

mngmtAgentTrap_4048 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004048)
)
mngmtAgentTrap_4048.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4048.setStatus(
        ""
    )

mngmtAgentTrap_4049 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004049)
)
mngmtAgentTrap_4049.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4049.setStatus(
        ""
    )

mngmtAgentTrap_4050 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004050)
)
mngmtAgentTrap_4050.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4050.setStatus(
        ""
    )

mngmtAgentTrap_4051 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004051)
)
mngmtAgentTrap_4051.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4051.setStatus(
        ""
    )

mngmtAgentTrap_4052 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004052)
)
mngmtAgentTrap_4052.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4052.setStatus(
        ""
    )

mngmtAgentTrap_4053 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004053)
)
mngmtAgentTrap_4053.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4053.setStatus(
        ""
    )

mngmtAgentTrap_4054 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004054)
)
mngmtAgentTrap_4054.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4054.setStatus(
        ""
    )

mngmtAgentTrap_4058 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004058)
)
mngmtAgentTrap_4058.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4058.setStatus(
        ""
    )

mngmtAgentTrap_4059 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136004059)
)
mngmtAgentTrap_4059.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_4059.setStatus(
        ""
    )

mngmtAgentTrap_5001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005001)
)
mngmtAgentTrap_5001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5001.setStatus(
        ""
    )

mngmtAgentTrap_5002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005002)
)
mngmtAgentTrap_5002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5002.setStatus(
        ""
    )

mngmtAgentTrap_5003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005003)
)
mngmtAgentTrap_5003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5003.setStatus(
        ""
    )

mngmtAgentTrap_5004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005004)
)
mngmtAgentTrap_5004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5004.setStatus(
        ""
    )

mngmtAgentTrap_5005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005005)
)
mngmtAgentTrap_5005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5005.setStatus(
        ""
    )

mngmtAgentTrap_5006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005006)
)
mngmtAgentTrap_5006.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5006.setStatus(
        ""
    )

mngmtAgentTrap_5007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005007)
)
mngmtAgentTrap_5007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5007.setStatus(
        ""
    )

mngmtAgentTrap_5008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005008)
)
mngmtAgentTrap_5008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5008.setStatus(
        ""
    )

mngmtAgentTrap_5010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005010)
)
mngmtAgentTrap_5010.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5010.setStatus(
        ""
    )

mngmtAgentTrap_5011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005011)
)
mngmtAgentTrap_5011.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5011.setStatus(
        ""
    )

mngmtAgentTrap_5012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005012)
)
mngmtAgentTrap_5012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5012.setStatus(
        ""
    )

mngmtAgentTrap_5013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005013)
)
mngmtAgentTrap_5013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5013.setStatus(
        ""
    )

mngmtAgentTrap_5014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005014)
)
mngmtAgentTrap_5014.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5014.setStatus(
        ""
    )

mngmtAgentTrap_5015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005015)
)
mngmtAgentTrap_5015.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5015.setStatus(
        ""
    )

mngmtAgentTrap_5016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005016)
)
mngmtAgentTrap_5016.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5016.setStatus(
        ""
    )

mngmtAgentTrap_5017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005017)
)
mngmtAgentTrap_5017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5017.setStatus(
        ""
    )

mngmtAgentTrap_5018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005018)
)
mngmtAgentTrap_5018.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5018.setStatus(
        ""
    )

mngmtAgentTrap_5019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136005019)
)
mngmtAgentTrap_5019.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_5019.setStatus(
        ""
    )

mngmtAgentTrap_6001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006001)
)
mngmtAgentTrap_6001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6001.setStatus(
        ""
    )

mngmtAgentTrap_6002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006002)
)
mngmtAgentTrap_6002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6002.setStatus(
        ""
    )

mngmtAgentTrap_6003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006003)
)
mngmtAgentTrap_6003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6003.setStatus(
        ""
    )

mngmtAgentTrap_6004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006004)
)
mngmtAgentTrap_6004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6004.setStatus(
        ""
    )

mngmtAgentTrap_6005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006005)
)
mngmtAgentTrap_6005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6005.setStatus(
        ""
    )

mngmtAgentTrap_6006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006006)
)
mngmtAgentTrap_6006.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6006.setStatus(
        ""
    )

mngmtAgentTrap_6007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006007)
)
mngmtAgentTrap_6007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6007.setStatus(
        ""
    )

mngmtAgentTrap_6008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006008)
)
mngmtAgentTrap_6008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6008.setStatus(
        ""
    )

mngmtAgentTrap_6009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006009)
)
mngmtAgentTrap_6009.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6009.setStatus(
        ""
    )

mngmtAgentTrap_6010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006010)
)
mngmtAgentTrap_6010.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6010.setStatus(
        ""
    )

mngmtAgentTrap_6011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006011)
)
mngmtAgentTrap_6011.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6011.setStatus(
        ""
    )

mngmtAgentTrap_6012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006012)
)
mngmtAgentTrap_6012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6012.setStatus(
        ""
    )

mngmtAgentTrap_6013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006013)
)
mngmtAgentTrap_6013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6013.setStatus(
        ""
    )

mngmtAgentTrap_6014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006014)
)
mngmtAgentTrap_6014.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6014.setStatus(
        ""
    )

mngmtAgentTrap_6015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006015)
)
mngmtAgentTrap_6015.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6015.setStatus(
        ""
    )

mngmtAgentTrap_6016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006016)
)
mngmtAgentTrap_6016.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6016.setStatus(
        ""
    )

mngmtAgentTrap_6017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006017)
)
mngmtAgentTrap_6017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6017.setStatus(
        ""
    )

mngmtAgentTrap_6018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006018)
)
mngmtAgentTrap_6018.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6018.setStatus(
        ""
    )

mngmtAgentTrap_6019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006019)
)
mngmtAgentTrap_6019.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6019.setStatus(
        ""
    )

mngmtAgentTrap_6020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006020)
)
mngmtAgentTrap_6020.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6020.setStatus(
        ""
    )

mngmtAgentTrap_6021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006021)
)
mngmtAgentTrap_6021.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6021.setStatus(
        ""
    )

mngmtAgentTrap_6022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006022)
)
mngmtAgentTrap_6022.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6022.setStatus(
        ""
    )

mngmtAgentTrap_6023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006023)
)
mngmtAgentTrap_6023.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6023.setStatus(
        ""
    )

mngmtAgentTrap_6024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006024)
)
mngmtAgentTrap_6024.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6024.setStatus(
        ""
    )

mngmtAgentTrap_6025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006025)
)
mngmtAgentTrap_6025.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6025.setStatus(
        ""
    )

mngmtAgentTrap_6026 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006026)
)
mngmtAgentTrap_6026.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6026.setStatus(
        ""
    )

mngmtAgentTrap_6027 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006027)
)
mngmtAgentTrap_6027.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6027.setStatus(
        ""
    )

mngmtAgentTrap_6028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006028)
)
mngmtAgentTrap_6028.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6028.setStatus(
        ""
    )

mngmtAgentTrap_6029 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006029)
)
mngmtAgentTrap_6029.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6029.setStatus(
        ""
    )

mngmtAgentTrap_6030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006030)
)
mngmtAgentTrap_6030.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6030.setStatus(
        ""
    )

mngmtAgentTrap_6031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006031)
)
mngmtAgentTrap_6031.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6031.setStatus(
        ""
    )

mngmtAgentTrap_6032 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006032)
)
mngmtAgentTrap_6032.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6032.setStatus(
        ""
    )

mngmtAgentTrap_6033 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006033)
)
mngmtAgentTrap_6033.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6033.setStatus(
        ""
    )

mngmtAgentTrap_6034 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006034)
)
mngmtAgentTrap_6034.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6034.setStatus(
        ""
    )

mngmtAgentTrap_6035 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006035)
)
mngmtAgentTrap_6035.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6035.setStatus(
        ""
    )

mngmtAgentTrap_6036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006036)
)
mngmtAgentTrap_6036.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6036.setStatus(
        ""
    )

mngmtAgentTrap_6037 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006037)
)
mngmtAgentTrap_6037.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6037.setStatus(
        ""
    )

mngmtAgentTrap_6038 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136006038)
)
mngmtAgentTrap_6038.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_6038.setStatus(
        ""
    )

mngmtAgentTrap_8001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008001)
)
mngmtAgentTrap_8001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8001.setStatus(
        ""
    )

mngmtAgentTrap_8002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008002)
)
mngmtAgentTrap_8002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8002.setStatus(
        ""
    )

mngmtAgentTrap_8003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008003)
)
mngmtAgentTrap_8003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8003.setStatus(
        ""
    )

mngmtAgentTrap_8004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008004)
)
mngmtAgentTrap_8004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8004.setStatus(
        ""
    )

mngmtAgentTrap_8005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008005)
)
mngmtAgentTrap_8005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8005.setStatus(
        ""
    )

mngmtAgentTrap_8006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008006)
)
mngmtAgentTrap_8006.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8006.setStatus(
        ""
    )

mngmtAgentTrap_8007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008007)
)
mngmtAgentTrap_8007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8007.setStatus(
        ""
    )

mngmtAgentTrap_8008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008008)
)
mngmtAgentTrap_8008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8008.setStatus(
        ""
    )

mngmtAgentTrap_8009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008009)
)
mngmtAgentTrap_8009.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8009.setStatus(
        ""
    )

mngmtAgentTrap_8010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008010)
)
mngmtAgentTrap_8010.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8010.setStatus(
        ""
    )

mngmtAgentTrap_8011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008011)
)
mngmtAgentTrap_8011.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8011.setStatus(
        ""
    )

mngmtAgentTrap_8012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008012)
)
mngmtAgentTrap_8012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8012.setStatus(
        ""
    )

mngmtAgentTrap_8013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008013)
)
mngmtAgentTrap_8013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8013.setStatus(
        ""
    )

mngmtAgentTrap_8014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008014)
)
mngmtAgentTrap_8014.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8014.setStatus(
        ""
    )

mngmtAgentTrap_8015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008015)
)
mngmtAgentTrap_8015.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8015.setStatus(
        ""
    )

mngmtAgentTrap_8016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008016)
)
mngmtAgentTrap_8016.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8016.setStatus(
        ""
    )

mngmtAgentTrap_8017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008017)
)
mngmtAgentTrap_8017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8017.setStatus(
        ""
    )

mngmtAgentTrap_8018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008018)
)
mngmtAgentTrap_8018.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8018.setStatus(
        ""
    )

mngmtAgentTrap_8019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008019)
)
mngmtAgentTrap_8019.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8019.setStatus(
        ""
    )

mngmtAgentTrap_8020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008020)
)
mngmtAgentTrap_8020.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8020.setStatus(
        ""
    )

mngmtAgentTrap_8021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008021)
)
mngmtAgentTrap_8021.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8021.setStatus(
        ""
    )

mngmtAgentTrap_8022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008022)
)
mngmtAgentTrap_8022.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8022.setStatus(
        ""
    )

mngmtAgentTrap_8023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008023)
)
mngmtAgentTrap_8023.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8023.setStatus(
        ""
    )

mngmtAgentTrap_8024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008024)
)
mngmtAgentTrap_8024.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8024.setStatus(
        ""
    )

mngmtAgentTrap_8025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008025)
)
mngmtAgentTrap_8025.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8025.setStatus(
        ""
    )

mngmtAgentTrap_8026 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008026)
)
mngmtAgentTrap_8026.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8026.setStatus(
        ""
    )

mngmtAgentTrap_8027 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008027)
)
mngmtAgentTrap_8027.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8027.setStatus(
        ""
    )

mngmtAgentTrap_8028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008028)
)
mngmtAgentTrap_8028.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8028.setStatus(
        ""
    )

mngmtAgentTrap_8029 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008029)
)
mngmtAgentTrap_8029.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8029.setStatus(
        ""
    )

mngmtAgentTrap_8030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008030)
)
mngmtAgentTrap_8030.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8030.setStatus(
        ""
    )

mngmtAgentTrap_8031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008031)
)
mngmtAgentTrap_8031.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8031.setStatus(
        ""
    )

mngmtAgentTrap_8032 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008032)
)
mngmtAgentTrap_8032.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8032.setStatus(
        ""
    )

mngmtAgentTrap_8033 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008033)
)
mngmtAgentTrap_8033.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8033.setStatus(
        ""
    )

mngmtAgentTrap_8034 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008034)
)
mngmtAgentTrap_8034.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8034.setStatus(
        ""
    )

mngmtAgentTrap_8035 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008035)
)
mngmtAgentTrap_8035.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8035.setStatus(
        ""
    )

mngmtAgentTrap_8036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008036)
)
mngmtAgentTrap_8036.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8036.setStatus(
        ""
    )

mngmtAgentTrap_8037 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008037)
)
mngmtAgentTrap_8037.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8037.setStatus(
        ""
    )

mngmtAgentTrap_8038 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008038)
)
mngmtAgentTrap_8038.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8038.setStatus(
        ""
    )

mngmtAgentTrap_8039 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008039)
)
mngmtAgentTrap_8039.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8039.setStatus(
        ""
    )

mngmtAgentTrap_8040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008040)
)
mngmtAgentTrap_8040.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8040.setStatus(
        ""
    )

mngmtAgentTrap_8041 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008041)
)
mngmtAgentTrap_8041.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8041.setStatus(
        ""
    )

mngmtAgentTrap_8042 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008042)
)
mngmtAgentTrap_8042.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8042.setStatus(
        ""
    )

mngmtAgentTrap_8043 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008043)
)
mngmtAgentTrap_8043.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8043.setStatus(
        ""
    )

mngmtAgentTrap_8044 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008044)
)
mngmtAgentTrap_8044.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8044.setStatus(
        ""
    )

mngmtAgentTrap_8045 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008045)
)
mngmtAgentTrap_8045.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8045.setStatus(
        ""
    )

mngmtAgentTrap_8046 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008046)
)
mngmtAgentTrap_8046.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8046.setStatus(
        ""
    )

mngmtAgentTrap_8047 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008047)
)
mngmtAgentTrap_8047.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8047.setStatus(
        ""
    )

mngmtAgentTrap_8048 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008048)
)
mngmtAgentTrap_8048.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8048.setStatus(
        ""
    )

mngmtAgentTrap_8049 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008049)
)
mngmtAgentTrap_8049.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8049.setStatus(
        ""
    )

mngmtAgentTrap_8050 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008050)
)
mngmtAgentTrap_8050.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8050.setStatus(
        ""
    )

mngmtAgentTrap_8051 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008051)
)
mngmtAgentTrap_8051.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8051.setStatus(
        ""
    )

mngmtAgentTrap_8052 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008052)
)
mngmtAgentTrap_8052.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8052.setStatus(
        ""
    )

mngmtAgentTrap_8053 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008053)
)
mngmtAgentTrap_8053.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8053.setStatus(
        ""
    )

mngmtAgentTrap_8054 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008054)
)
mngmtAgentTrap_8054.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8054.setStatus(
        ""
    )

mngmtAgentTrap_8055 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008055)
)
mngmtAgentTrap_8055.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8055.setStatus(
        ""
    )

mngmtAgentTrap_8056 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008056)
)
mngmtAgentTrap_8056.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8056.setStatus(
        ""
    )

mngmtAgentTrap_8057 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008057)
)
mngmtAgentTrap_8057.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8057.setStatus(
        ""
    )

mngmtAgentTrap_8058 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008058)
)
mngmtAgentTrap_8058.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8058.setStatus(
        ""
    )

mngmtAgentTrap_8059 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008059)
)
mngmtAgentTrap_8059.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8059.setStatus(
        ""
    )

mngmtAgentTrap_8060 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008060)
)
mngmtAgentTrap_8060.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8060.setStatus(
        ""
    )

mngmtAgentTrap_8061 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008061)
)
mngmtAgentTrap_8061.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8061.setStatus(
        ""
    )

mngmtAgentTrap_8062 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008062)
)
mngmtAgentTrap_8062.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8062.setStatus(
        ""
    )

mngmtAgentTrap_8063 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008063)
)
mngmtAgentTrap_8063.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8063.setStatus(
        ""
    )

mngmtAgentTrap_8064 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008064)
)
mngmtAgentTrap_8064.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8064.setStatus(
        ""
    )

mngmtAgentTrap_8065 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008065)
)
mngmtAgentTrap_8065.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8065.setStatus(
        ""
    )

mngmtAgentTrap_8066 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008066)
)
mngmtAgentTrap_8066.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8066.setStatus(
        ""
    )

mngmtAgentTrap_8067 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008067)
)
mngmtAgentTrap_8067.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8067.setStatus(
        ""
    )

mngmtAgentTrap_8068 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008068)
)
mngmtAgentTrap_8068.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8068.setStatus(
        ""
    )

mngmtAgentTrap_8069 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008069)
)
mngmtAgentTrap_8069.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8069.setStatus(
        ""
    )

mngmtAgentTrap_8070 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008070)
)
mngmtAgentTrap_8070.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8070.setStatus(
        ""
    )

mngmtAgentTrap_8071 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008071)
)
mngmtAgentTrap_8071.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8071.setStatus(
        ""
    )

mngmtAgentTrap_8073 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008073)
)
mngmtAgentTrap_8073.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8073.setStatus(
        ""
    )

mngmtAgentTrap_8074 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008074)
)
mngmtAgentTrap_8074.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8074.setStatus(
        ""
    )

mngmtAgentTrap_8075 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008075)
)
mngmtAgentTrap_8075.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8075.setStatus(
        ""
    )

mngmtAgentTrap_8076 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008076)
)
mngmtAgentTrap_8076.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8076.setStatus(
        ""
    )

mngmtAgentTrap_8077 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008077)
)
mngmtAgentTrap_8077.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8077.setStatus(
        ""
    )

mngmtAgentTrap_8078 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008078)
)
mngmtAgentTrap_8078.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8078.setStatus(
        ""
    )

mngmtAgentTrap_8079 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008079)
)
mngmtAgentTrap_8079.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8079.setStatus(
        ""
    )

mngmtAgentTrap_8080 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008080)
)
mngmtAgentTrap_8080.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8080.setStatus(
        ""
    )

mngmtAgentTrap_8081 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008081)
)
mngmtAgentTrap_8081.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8081.setStatus(
        ""
    )

mngmtAgentTrap_8082 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008082)
)
mngmtAgentTrap_8082.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8082.setStatus(
        ""
    )

mngmtAgentTrap_8083 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008083)
)
mngmtAgentTrap_8083.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8083.setStatus(
        ""
    )

mngmtAgentTrap_8084 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008084)
)
mngmtAgentTrap_8084.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8084.setStatus(
        ""
    )

mngmtAgentTrap_8085 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008085)
)
mngmtAgentTrap_8085.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8085.setStatus(
        ""
    )

mngmtAgentTrap_8086 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008086)
)
mngmtAgentTrap_8086.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8086.setStatus(
        ""
    )

mngmtAgentTrap_8087 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008087)
)
mngmtAgentTrap_8087.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8087.setStatus(
        ""
    )

mngmtAgentTrap_8088 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008088)
)
mngmtAgentTrap_8088.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8088.setStatus(
        ""
    )

mngmtAgentTrap_8089 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008089)
)
mngmtAgentTrap_8089.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8089.setStatus(
        ""
    )

mngmtAgentTrap_8090 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008090)
)
mngmtAgentTrap_8090.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8090.setStatus(
        ""
    )

mngmtAgentTrap_8091 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008091)
)
mngmtAgentTrap_8091.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8091.setStatus(
        ""
    )

mngmtAgentTrap_8092 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008092)
)
mngmtAgentTrap_8092.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8092.setStatus(
        ""
    )

mngmtAgentTrap_8093 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008093)
)
mngmtAgentTrap_8093.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8093.setStatus(
        ""
    )

mngmtAgentTrap_8094 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008094)
)
mngmtAgentTrap_8094.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8094.setStatus(
        ""
    )

mngmtAgentTrap_8095 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136008095)
)
mngmtAgentTrap_8095.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_8095.setStatus(
        ""
    )

mngmtAgentTrap_9001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009001)
)
mngmtAgentTrap_9001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9001.setStatus(
        ""
    )

mngmtAgentTrap_9002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009002)
)
mngmtAgentTrap_9002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9002.setStatus(
        ""
    )

mngmtAgentTrap_9003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009003)
)
mngmtAgentTrap_9003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9003.setStatus(
        ""
    )

mngmtAgentTrap_9004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009004)
)
mngmtAgentTrap_9004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9004.setStatus(
        ""
    )

mngmtAgentTrap_9005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009005)
)
mngmtAgentTrap_9005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9005.setStatus(
        ""
    )

mngmtAgentTrap_9006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009006)
)
mngmtAgentTrap_9006.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9006.setStatus(
        ""
    )

mngmtAgentTrap_9007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009007)
)
mngmtAgentTrap_9007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9007.setStatus(
        ""
    )

mngmtAgentTrap_9008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009008)
)
mngmtAgentTrap_9008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9008.setStatus(
        ""
    )

mngmtAgentTrap_9009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009009)
)
mngmtAgentTrap_9009.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9009.setStatus(
        ""
    )

mngmtAgentTrap_9010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009010)
)
mngmtAgentTrap_9010.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9010.setStatus(
        ""
    )

mngmtAgentTrap_9011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009011)
)
mngmtAgentTrap_9011.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9011.setStatus(
        ""
    )

mngmtAgentTrap_9012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009012)
)
mngmtAgentTrap_9012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9012.setStatus(
        ""
    )

mngmtAgentTrap_9013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009013)
)
mngmtAgentTrap_9013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9013.setStatus(
        ""
    )

mngmtAgentTrap_9014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009014)
)
mngmtAgentTrap_9014.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9014.setStatus(
        ""
    )

mngmtAgentTrap_9015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009015)
)
mngmtAgentTrap_9015.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9015.setStatus(
        ""
    )

mngmtAgentTrap_9016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009016)
)
mngmtAgentTrap_9016.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9016.setStatus(
        ""
    )

mngmtAgentTrap_9017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009017)
)
mngmtAgentTrap_9017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9017.setStatus(
        ""
    )

mngmtAgentTrap_9018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009018)
)
mngmtAgentTrap_9018.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9018.setStatus(
        ""
    )

mngmtAgentTrap_9019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009019)
)
mngmtAgentTrap_9019.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9019.setStatus(
        ""
    )

mngmtAgentTrap_9020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009020)
)
mngmtAgentTrap_9020.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9020.setStatus(
        ""
    )

mngmtAgentTrap_9021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009021)
)
mngmtAgentTrap_9021.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9021.setStatus(
        ""
    )

mngmtAgentTrap_9022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009022)
)
mngmtAgentTrap_9022.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9022.setStatus(
        ""
    )

mngmtAgentTrap_9023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009023)
)
mngmtAgentTrap_9023.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9023.setStatus(
        ""
    )

mngmtAgentTrap_9025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009025)
)
mngmtAgentTrap_9025.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9025.setStatus(
        ""
    )

mngmtAgentTrap_9026 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009026)
)
mngmtAgentTrap_9026.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9026.setStatus(
        ""
    )

mngmtAgentTrap_9027 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009027)
)
mngmtAgentTrap_9027.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9027.setStatus(
        ""
    )

mngmtAgentTrap_9028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009028)
)
mngmtAgentTrap_9028.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9028.setStatus(
        ""
    )

mngmtAgentTrap_9029 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009029)
)
mngmtAgentTrap_9029.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9029.setStatus(
        ""
    )

mngmtAgentTrap_9030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009030)
)
mngmtAgentTrap_9030.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9030.setStatus(
        ""
    )

mngmtAgentTrap_9031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009031)
)
mngmtAgentTrap_9031.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9031.setStatus(
        ""
    )

mngmtAgentTrap_9032 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009032)
)
mngmtAgentTrap_9032.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9032.setStatus(
        ""
    )

mngmtAgentTrap_9033 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009033)
)
mngmtAgentTrap_9033.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9033.setStatus(
        ""
    )

mngmtAgentTrap_9034 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009034)
)
mngmtAgentTrap_9034.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9034.setStatus(
        ""
    )

mngmtAgentTrap_9035 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009035)
)
mngmtAgentTrap_9035.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9035.setStatus(
        ""
    )

mngmtAgentTrap_9036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009036)
)
mngmtAgentTrap_9036.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9036.setStatus(
        ""
    )

mngmtAgentTrap_9037 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009037)
)
mngmtAgentTrap_9037.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9037.setStatus(
        ""
    )

mngmtAgentTrap_9038 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009038)
)
mngmtAgentTrap_9038.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9038.setStatus(
        ""
    )

mngmtAgentTrap_9039 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009039)
)
mngmtAgentTrap_9039.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9039.setStatus(
        ""
    )

mngmtAgentTrap_9040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009040)
)
mngmtAgentTrap_9040.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9040.setStatus(
        ""
    )

mngmtAgentTrap_9041 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009041)
)
mngmtAgentTrap_9041.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9041.setStatus(
        ""
    )

mngmtAgentTrap_9042 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136009042)
)
mngmtAgentTrap_9042.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_9042.setStatus(
        ""
    )

mngmtAgentTrap_10001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010001)
)
mngmtAgentTrap_10001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10001.setStatus(
        ""
    )

mngmtAgentTrap_10004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010004)
)
mngmtAgentTrap_10004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10004.setStatus(
        ""
    )

mngmtAgentTrap_10006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010006)
)
mngmtAgentTrap_10006.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10006.setStatus(
        ""
    )

mngmtAgentTrap_10010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010010)
)
mngmtAgentTrap_10010.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10010.setStatus(
        ""
    )

mngmtAgentTrap_10011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010011)
)
mngmtAgentTrap_10011.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10011.setStatus(
        ""
    )

mngmtAgentTrap_10012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010012)
)
mngmtAgentTrap_10012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10012.setStatus(
        ""
    )

mngmtAgentTrap_10013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010013)
)
mngmtAgentTrap_10013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10013.setStatus(
        ""
    )

mngmtAgentTrap_10014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010014)
)
mngmtAgentTrap_10014.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10014.setStatus(
        ""
    )

mngmtAgentTrap_10015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010015)
)
mngmtAgentTrap_10015.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10015.setStatus(
        ""
    )

mngmtAgentTrap_10017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010017)
)
mngmtAgentTrap_10017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10017.setStatus(
        ""
    )

mngmtAgentTrap_10018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010018)
)
mngmtAgentTrap_10018.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10018.setStatus(
        ""
    )

mngmtAgentTrap_10019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010019)
)
mngmtAgentTrap_10019.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10019.setStatus(
        ""
    )

mngmtAgentTrap_10020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010020)
)
mngmtAgentTrap_10020.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10020.setStatus(
        ""
    )

mngmtAgentTrap_10021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010021)
)
mngmtAgentTrap_10021.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10021.setStatus(
        ""
    )

mngmtAgentTrap_10022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010022)
)
mngmtAgentTrap_10022.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10022.setStatus(
        ""
    )

mngmtAgentTrap_10023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010023)
)
mngmtAgentTrap_10023.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10023.setStatus(
        ""
    )

mngmtAgentTrap_10024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010024)
)
mngmtAgentTrap_10024.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10024.setStatus(
        ""
    )

mngmtAgentTrap_10025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010025)
)
mngmtAgentTrap_10025.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10025.setStatus(
        ""
    )

mngmtAgentTrap_10026 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010026)
)
mngmtAgentTrap_10026.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10026.setStatus(
        ""
    )

mngmtAgentTrap_10027 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010027)
)
mngmtAgentTrap_10027.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10027.setStatus(
        ""
    )

mngmtAgentTrap_10028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010028)
)
mngmtAgentTrap_10028.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10028.setStatus(
        ""
    )

mngmtAgentTrap_10029 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010029)
)
mngmtAgentTrap_10029.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10029.setStatus(
        ""
    )

mngmtAgentTrap_10030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010030)
)
mngmtAgentTrap_10030.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10030.setStatus(
        ""
    )

mngmtAgentTrap_10031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010031)
)
mngmtAgentTrap_10031.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10031.setStatus(
        ""
    )

mngmtAgentTrap_10035 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010035)
)
mngmtAgentTrap_10035.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10035.setStatus(
        ""
    )

mngmtAgentTrap_10036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010036)
)
mngmtAgentTrap_10036.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10036.setStatus(
        ""
    )

mngmtAgentTrap_10037 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010037)
)
mngmtAgentTrap_10037.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10037.setStatus(
        ""
    )

mngmtAgentTrap_10038 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010038)
)
mngmtAgentTrap_10038.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10038.setStatus(
        ""
    )

mngmtAgentTrap_10039 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010039)
)
mngmtAgentTrap_10039.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10039.setStatus(
        ""
    )

mngmtAgentTrap_10040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010040)
)
mngmtAgentTrap_10040.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10040.setStatus(
        ""
    )

mngmtAgentTrap_10041 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010041)
)
mngmtAgentTrap_10041.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10041.setStatus(
        ""
    )

mngmtAgentTrap_10042 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010042)
)
mngmtAgentTrap_10042.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10042.setStatus(
        ""
    )

mngmtAgentTrap_10043 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010043)
)
mngmtAgentTrap_10043.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10043.setStatus(
        ""
    )

mngmtAgentTrap_10044 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136010044)
)
mngmtAgentTrap_10044.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_10044.setStatus(
        ""
    )

mngmtAgentTrap_11001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136011001)
)
mngmtAgentTrap_11001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_11001.setStatus(
        ""
    )

mngmtAgentTrap_11002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136011002)
)
mngmtAgentTrap_11002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_11002.setStatus(
        ""
    )

mngmtAgentTrap_11003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136011003)
)
mngmtAgentTrap_11003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_11003.setStatus(
        ""
    )

mngmtAgentTrap_11004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136011004)
)
mngmtAgentTrap_11004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_11004.setStatus(
        ""
    )

mngmtAgentTrap_12001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136012001)
)
mngmtAgentTrap_12001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_12001.setStatus(
        ""
    )

mngmtAgentTrap_12002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136012002)
)
mngmtAgentTrap_12002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_12002.setStatus(
        ""
    )

mngmtAgentTrap_12003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136012003)
)
mngmtAgentTrap_12003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_12003.setStatus(
        ""
    )

mngmtAgentTrap_12004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136012004)
)
mngmtAgentTrap_12004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_12004.setStatus(
        ""
    )

mngmtAgentTrap_12005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136012005)
)
mngmtAgentTrap_12005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_12005.setStatus(
        ""
    )

mngmtAgentTrap_12008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136012008)
)
mngmtAgentTrap_12008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_12008.setStatus(
        ""
    )

mngmtAgentTrap_13002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136013002)
)
mngmtAgentTrap_13002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_13002.setStatus(
        ""
    )

mngmtAgentTrap_13003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136013003)
)
mngmtAgentTrap_13003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_13003.setStatus(
        ""
    )

mngmtAgentTrap_13004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136013004)
)
mngmtAgentTrap_13004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_13004.setStatus(
        ""
    )

mngmtAgentTrap_13007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136013007)
)
mngmtAgentTrap_13007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_13007.setStatus(
        ""
    )

mngmtAgentTrap_13009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136013009)
)
mngmtAgentTrap_13009.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_13009.setStatus(
        ""
    )

mngmtAgentTrap_13012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136013012)
)
mngmtAgentTrap_13012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_13012.setStatus(
        ""
    )

mngmtAgentTrap_13015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136013015)
)
mngmtAgentTrap_13015.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_13015.setStatus(
        ""
    )

mngmtAgentTrap_13017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136013017)
)
mngmtAgentTrap_13017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_13017.setStatus(
        ""
    )

mngmtAgentTrap_13018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136013018)
)
mngmtAgentTrap_13018.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_13018.setStatus(
        ""
    )

mngmtAgentTrap_13019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136013019)
)
mngmtAgentTrap_13019.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_13019.setStatus(
        ""
    )

mngmtAgentTrap_13020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136013020)
)
mngmtAgentTrap_13020.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_13020.setStatus(
        ""
    )

mngmtAgentTrap_14001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136014001)
)
mngmtAgentTrap_14001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_14001.setStatus(
        ""
    )

mngmtAgentTrap_14002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136014002)
)
mngmtAgentTrap_14002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_14002.setStatus(
        ""
    )

mngmtAgentTrap_14003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136014003)
)
mngmtAgentTrap_14003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_14003.setStatus(
        ""
    )

mngmtAgentTrap_14004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136014004)
)
mngmtAgentTrap_14004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_14004.setStatus(
        ""
    )

mngmtAgentTrap_14005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136014005)
)
mngmtAgentTrap_14005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_14005.setStatus(
        ""
    )

mngmtAgentTrap_14006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136014006)
)
mngmtAgentTrap_14006.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_14006.setStatus(
        ""
    )

mngmtAgentTrap_14007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136014007)
)
mngmtAgentTrap_14007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_14007.setStatus(
        ""
    )

mngmtAgentTrap_14008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136014008)
)
mngmtAgentTrap_14008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_14008.setStatus(
        ""
    )

mngmtAgentTrap_14009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136014009)
)
mngmtAgentTrap_14009.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_14009.setStatus(
        ""
    )

mngmtAgentTrap_14010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136014010)
)
mngmtAgentTrap_14010.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_14010.setStatus(
        ""
    )

mngmtAgentTrap_14012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136014012)
)
mngmtAgentTrap_14012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_14012.setStatus(
        ""
    )

mngmtAgentTrap_14013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136014013)
)
mngmtAgentTrap_14013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_14013.setStatus(
        ""
    )

mngmtAgentTrap_14017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136014017)
)
mngmtAgentTrap_14017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_14017.setStatus(
        ""
    )

mngmtAgentTrap_15001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136015001)
)
mngmtAgentTrap_15001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_15001.setStatus(
        ""
    )

mngmtAgentTrap_15002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136015002)
)
mngmtAgentTrap_15002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_15002.setStatus(
        ""
    )

mngmtAgentTrap_15003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136015003)
)
mngmtAgentTrap_15003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_15003.setStatus(
        ""
    )

mngmtAgentTrap_15004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136015004)
)
mngmtAgentTrap_15004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_15004.setStatus(
        ""
    )

mngmtAgentTrap_15005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136015005)
)
mngmtAgentTrap_15005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_15005.setStatus(
        ""
    )

mngmtAgentTrap_15006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136015006)
)
mngmtAgentTrap_15006.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_15006.setStatus(
        ""
    )

mngmtAgentTrap_15007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136015007)
)
mngmtAgentTrap_15007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_15007.setStatus(
        ""
    )

mngmtAgentTrap_15008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136015008)
)
mngmtAgentTrap_15008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_15008.setStatus(
        ""
    )

mngmtAgentTrap_15009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136015009)
)
mngmtAgentTrap_15009.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_15009.setStatus(
        ""
    )

mngmtAgentTrap_16001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016001)
)
mngmtAgentTrap_16001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16001.setStatus(
        ""
    )

mngmtAgentTrap_16004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016004)
)
mngmtAgentTrap_16004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16004.setStatus(
        ""
    )

mngmtAgentTrap_16005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016005)
)
mngmtAgentTrap_16005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16005.setStatus(
        ""
    )

mngmtAgentTrap_16008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016008)
)
mngmtAgentTrap_16008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16008.setStatus(
        ""
    )

mngmtAgentTrap_16010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016010)
)
mngmtAgentTrap_16010.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16010.setStatus(
        ""
    )

mngmtAgentTrap_16012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016012)
)
mngmtAgentTrap_16012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16012.setStatus(
        ""
    )

mngmtAgentTrap_16013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016013)
)
mngmtAgentTrap_16013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16013.setStatus(
        ""
    )

mngmtAgentTrap_16014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016014)
)
mngmtAgentTrap_16014.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16014.setStatus(
        ""
    )

mngmtAgentTrap_16015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016015)
)
mngmtAgentTrap_16015.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16015.setStatus(
        ""
    )

mngmtAgentTrap_16016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016016)
)
mngmtAgentTrap_16016.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16016.setStatus(
        ""
    )

mngmtAgentTrap_16017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016017)
)
mngmtAgentTrap_16017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16017.setStatus(
        ""
    )

mngmtAgentTrap_16018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016018)
)
mngmtAgentTrap_16018.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16018.setStatus(
        ""
    )

mngmtAgentTrap_16019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016019)
)
mngmtAgentTrap_16019.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16019.setStatus(
        ""
    )

mngmtAgentTrap_16020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016020)
)
mngmtAgentTrap_16020.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16020.setStatus(
        ""
    )

mngmtAgentTrap_16021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016021)
)
mngmtAgentTrap_16021.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16021.setStatus(
        ""
    )

mngmtAgentTrap_16022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016022)
)
mngmtAgentTrap_16022.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16022.setStatus(
        ""
    )

mngmtAgentTrap_16023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016023)
)
mngmtAgentTrap_16023.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16023.setStatus(
        ""
    )

mngmtAgentTrap_16024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016024)
)
mngmtAgentTrap_16024.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16024.setStatus(
        ""
    )

mngmtAgentTrap_16025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016025)
)
mngmtAgentTrap_16025.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16025.setStatus(
        ""
    )

mngmtAgentTrap_16026 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016026)
)
mngmtAgentTrap_16026.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16026.setStatus(
        ""
    )

mngmtAgentTrap_16027 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016027)
)
mngmtAgentTrap_16027.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16027.setStatus(
        ""
    )

mngmtAgentTrap_16028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016028)
)
mngmtAgentTrap_16028.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16028.setStatus(
        ""
    )

mngmtAgentTrap_16029 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016029)
)
mngmtAgentTrap_16029.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16029.setStatus(
        ""
    )

mngmtAgentTrap_16030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016030)
)
mngmtAgentTrap_16030.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16030.setStatus(
        ""
    )

mngmtAgentTrap_16031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016031)
)
mngmtAgentTrap_16031.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16031.setStatus(
        ""
    )

mngmtAgentTrap_16032 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016032)
)
mngmtAgentTrap_16032.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16032.setStatus(
        ""
    )

mngmtAgentTrap_16033 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016033)
)
mngmtAgentTrap_16033.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16033.setStatus(
        ""
    )

mngmtAgentTrap_16034 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016034)
)
mngmtAgentTrap_16034.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16034.setStatus(
        ""
    )

mngmtAgentTrap_16035 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016035)
)
mngmtAgentTrap_16035.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16035.setStatus(
        ""
    )

mngmtAgentTrap_16036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016036)
)
mngmtAgentTrap_16036.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16036.setStatus(
        ""
    )

mngmtAgentTrap_16037 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016037)
)
mngmtAgentTrap_16037.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16037.setStatus(
        ""
    )

mngmtAgentTrap_16038 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016038)
)
mngmtAgentTrap_16038.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16038.setStatus(
        ""
    )

mngmtAgentTrap_16039 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016039)
)
mngmtAgentTrap_16039.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16039.setStatus(
        ""
    )

mngmtAgentTrap_16040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136016040)
)
mngmtAgentTrap_16040.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_16040.setStatus(
        ""
    )

mngmtAgentTrap_17001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136017001)
)
mngmtAgentTrap_17001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17001.setStatus(
        ""
    )

mngmtAgentTrap_17002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136017002)
)
mngmtAgentTrap_17002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17002.setStatus(
        ""
    )

mngmtAgentTrap_17003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136017003)
)
mngmtAgentTrap_17003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17003.setStatus(
        ""
    )

mngmtAgentTrap_17004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136017004)
)
mngmtAgentTrap_17004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17004.setStatus(
        ""
    )

mngmtAgentTrap_17005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136017005)
)
mngmtAgentTrap_17005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17005.setStatus(
        ""
    )

mngmtAgentTrap_17006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136017006)
)
mngmtAgentTrap_17006.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17006.setStatus(
        ""
    )

mngmtAgentTrap_17007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136017007)
)
mngmtAgentTrap_17007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17007.setStatus(
        ""
    )

mngmtAgentTrap_17008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136017008)
)
mngmtAgentTrap_17008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17008.setStatus(
        ""
    )

mngmtAgentTrap_17009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136017009)
)
mngmtAgentTrap_17009.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17009.setStatus(
        ""
    )

mngmtAgentTrap_17012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136017012)
)
mngmtAgentTrap_17012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17012.setStatus(
        ""
    )

mngmtAgentTrap_17013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136017013)
)
mngmtAgentTrap_17013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17013.setStatus(
        ""
    )

mngmtAgentTrap_17014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136017014)
)
mngmtAgentTrap_17014.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17014.setStatus(
        ""
    )

mngmtAgentTrap_17015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136017015)
)
mngmtAgentTrap_17015.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17015.setStatus(
        ""
    )

mngmtAgentTrap_17016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136017016)
)
mngmtAgentTrap_17016.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17016.setStatus(
        ""
    )

mngmtAgentTrap_17017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136017017)
)
mngmtAgentTrap_17017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_17017.setStatus(
        ""
    )

mngmtAgentTrap_18001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018001)
)
mngmtAgentTrap_18001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18001.setStatus(
        ""
    )

mngmtAgentTrap_18002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018002)
)
mngmtAgentTrap_18002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18002.setStatus(
        ""
    )

mngmtAgentTrap_18003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018003)
)
mngmtAgentTrap_18003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18003.setStatus(
        ""
    )

mngmtAgentTrap_18004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018004)
)
mngmtAgentTrap_18004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18004.setStatus(
        ""
    )

mngmtAgentTrap_18005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018005)
)
mngmtAgentTrap_18005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18005.setStatus(
        ""
    )

mngmtAgentTrap_18006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018006)
)
mngmtAgentTrap_18006.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18006.setStatus(
        ""
    )

mngmtAgentTrap_18007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018007)
)
mngmtAgentTrap_18007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18007.setStatus(
        ""
    )

mngmtAgentTrap_18008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018008)
)
mngmtAgentTrap_18008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18008.setStatus(
        ""
    )

mngmtAgentTrap_18009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018009)
)
mngmtAgentTrap_18009.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18009.setStatus(
        ""
    )

mngmtAgentTrap_18010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018010)
)
mngmtAgentTrap_18010.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18010.setStatus(
        ""
    )

mngmtAgentTrap_18018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018018)
)
mngmtAgentTrap_18018.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18018.setStatus(
        ""
    )

mngmtAgentTrap_18019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018019)
)
mngmtAgentTrap_18019.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18019.setStatus(
        ""
    )

mngmtAgentTrap_18022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018022)
)
mngmtAgentTrap_18022.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18022.setStatus(
        ""
    )

mngmtAgentTrap_18024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018024)
)
mngmtAgentTrap_18024.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18024.setStatus(
        ""
    )

mngmtAgentTrap_18025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018025)
)
mngmtAgentTrap_18025.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18025.setStatus(
        ""
    )

mngmtAgentTrap_18028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018028)
)
mngmtAgentTrap_18028.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18028.setStatus(
        ""
    )

mngmtAgentTrap_18034 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018034)
)
mngmtAgentTrap_18034.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18034.setStatus(
        ""
    )

mngmtAgentTrap_18036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018036)
)
mngmtAgentTrap_18036.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18036.setStatus(
        ""
    )

mngmtAgentTrap_18038 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018038)
)
mngmtAgentTrap_18038.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18038.setStatus(
        ""
    )

mngmtAgentTrap_18039 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018039)
)
mngmtAgentTrap_18039.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18039.setStatus(
        ""
    )

mngmtAgentTrap_18040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018040)
)
mngmtAgentTrap_18040.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18040.setStatus(
        ""
    )

mngmtAgentTrap_18041 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018041)
)
mngmtAgentTrap_18041.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18041.setStatus(
        ""
    )

mngmtAgentTrap_18042 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018042)
)
mngmtAgentTrap_18042.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18042.setStatus(
        ""
    )

mngmtAgentTrap_18045 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018045)
)
mngmtAgentTrap_18045.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18045.setStatus(
        ""
    )

mngmtAgentTrap_18047 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018047)
)
mngmtAgentTrap_18047.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18047.setStatus(
        ""
    )

mngmtAgentTrap_18048 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018048)
)
mngmtAgentTrap_18048.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18048.setStatus(
        ""
    )

mngmtAgentTrap_18049 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018049)
)
mngmtAgentTrap_18049.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18049.setStatus(
        ""
    )

mngmtAgentTrap_18050 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018050)
)
mngmtAgentTrap_18050.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18050.setStatus(
        ""
    )

mngmtAgentTrap_18051 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018051)
)
mngmtAgentTrap_18051.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18051.setStatus(
        ""
    )

mngmtAgentTrap_18052 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018052)
)
mngmtAgentTrap_18052.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18052.setStatus(
        ""
    )

mngmtAgentTrap_18059 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018059)
)
mngmtAgentTrap_18059.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18059.setStatus(
        ""
    )

mngmtAgentTrap_18060 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018060)
)
mngmtAgentTrap_18060.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18060.setStatus(
        ""
    )

mngmtAgentTrap_18063 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018063)
)
mngmtAgentTrap_18063.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18063.setStatus(
        ""
    )

mngmtAgentTrap_18065 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018065)
)
mngmtAgentTrap_18065.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18065.setStatus(
        ""
    )

mngmtAgentTrap_18066 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018066)
)
mngmtAgentTrap_18066.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18066.setStatus(
        ""
    )

mngmtAgentTrap_18067 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018067)
)
mngmtAgentTrap_18067.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18067.setStatus(
        ""
    )

mngmtAgentTrap_18068 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018068)
)
mngmtAgentTrap_18068.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18068.setStatus(
        ""
    )

mngmtAgentTrap_18070 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018070)
)
mngmtAgentTrap_18070.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18070.setStatus(
        ""
    )

mngmtAgentTrap_18071 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018071)
)
mngmtAgentTrap_18071.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18071.setStatus(
        ""
    )

mngmtAgentTrap_18073 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018073)
)
mngmtAgentTrap_18073.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18073.setStatus(
        ""
    )

mngmtAgentTrap_18074 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018074)
)
mngmtAgentTrap_18074.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18074.setStatus(
        ""
    )

mngmtAgentTrap_18075 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018075)
)
mngmtAgentTrap_18075.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18075.setStatus(
        ""
    )

mngmtAgentTrap_18076 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018076)
)
mngmtAgentTrap_18076.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18076.setStatus(
        ""
    )

mngmtAgentTrap_18080 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018080)
)
mngmtAgentTrap_18080.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18080.setStatus(
        ""
    )

mngmtAgentTrap_18081 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136018081)
)
mngmtAgentTrap_18081.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_18081.setStatus(
        ""
    )

mngmtAgentTrap_20001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020001)
)
mngmtAgentTrap_20001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20001.setStatus(
        ""
    )

mngmtAgentTrap_20002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020002)
)
mngmtAgentTrap_20002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20002.setStatus(
        ""
    )

mngmtAgentTrap_20003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020003)
)
mngmtAgentTrap_20003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20003.setStatus(
        ""
    )

mngmtAgentTrap_20004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020004)
)
mngmtAgentTrap_20004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20004.setStatus(
        ""
    )

mngmtAgentTrap_20005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020005)
)
mngmtAgentTrap_20005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20005.setStatus(
        ""
    )

mngmtAgentTrap_20011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020011)
)
mngmtAgentTrap_20011.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20011.setStatus(
        ""
    )

mngmtAgentTrap_20013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020013)
)
mngmtAgentTrap_20013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20013.setStatus(
        ""
    )

mngmtAgentTrap_20015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020015)
)
mngmtAgentTrap_20015.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20015.setStatus(
        ""
    )

mngmtAgentTrap_20016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020016)
)
mngmtAgentTrap_20016.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20016.setStatus(
        ""
    )

mngmtAgentTrap_20017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020017)
)
mngmtAgentTrap_20017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20017.setStatus(
        ""
    )

mngmtAgentTrap_20018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020018)
)
mngmtAgentTrap_20018.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20018.setStatus(
        ""
    )

mngmtAgentTrap_20019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020019)
)
mngmtAgentTrap_20019.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20019.setStatus(
        ""
    )

mngmtAgentTrap_20020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020020)
)
mngmtAgentTrap_20020.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20020.setStatus(
        ""
    )

mngmtAgentTrap_20021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020021)
)
mngmtAgentTrap_20021.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20021.setStatus(
        ""
    )

mngmtAgentTrap_20022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020022)
)
mngmtAgentTrap_20022.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20022.setStatus(
        ""
    )

mngmtAgentTrap_20023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136020023)
)
mngmtAgentTrap_20023.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_20023.setStatus(
        ""
    )

mngmtAgentTrap_21001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021001)
)
mngmtAgentTrap_21001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21001.setStatus(
        ""
    )

mngmtAgentTrap_21002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021002)
)
mngmtAgentTrap_21002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21002.setStatus(
        ""
    )

mngmtAgentTrap_21003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021003)
)
mngmtAgentTrap_21003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21003.setStatus(
        ""
    )

mngmtAgentTrap_21004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021004)
)
mngmtAgentTrap_21004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21004.setStatus(
        ""
    )

mngmtAgentTrap_21006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021006)
)
mngmtAgentTrap_21006.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21006.setStatus(
        ""
    )

mngmtAgentTrap_21007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021007)
)
mngmtAgentTrap_21007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21007.setStatus(
        ""
    )

mngmtAgentTrap_21008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021008)
)
mngmtAgentTrap_21008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21008.setStatus(
        ""
    )

mngmtAgentTrap_21009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021009)
)
mngmtAgentTrap_21009.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21009.setStatus(
        ""
    )

mngmtAgentTrap_21010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021010)
)
mngmtAgentTrap_21010.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21010.setStatus(
        ""
    )

mngmtAgentTrap_21011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021011)
)
mngmtAgentTrap_21011.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21011.setStatus(
        ""
    )

mngmtAgentTrap_21012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021012)
)
mngmtAgentTrap_21012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21012.setStatus(
        ""
    )

mngmtAgentTrap_21013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021013)
)
mngmtAgentTrap_21013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21013.setStatus(
        ""
    )

mngmtAgentTrap_21014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021014)
)
mngmtAgentTrap_21014.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21014.setStatus(
        ""
    )

mngmtAgentTrap_21015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021015)
)
mngmtAgentTrap_21015.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21015.setStatus(
        ""
    )

mngmtAgentTrap_21016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021016)
)
mngmtAgentTrap_21016.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21016.setStatus(
        ""
    )

mngmtAgentTrap_21017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021017)
)
mngmtAgentTrap_21017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21017.setStatus(
        ""
    )

mngmtAgentTrap_21018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021018)
)
mngmtAgentTrap_21018.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21018.setStatus(
        ""
    )

mngmtAgentTrap_21019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136021019)
)
mngmtAgentTrap_21019.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_21019.setStatus(
        ""
    )

mngmtAgentTrap_22001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136022001)
)
mngmtAgentTrap_22001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_22001.setStatus(
        ""
    )

mngmtAgentTrap_22002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136022002)
)
mngmtAgentTrap_22002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_22002.setStatus(
        ""
    )

mngmtAgentTrap_23002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136023002)
)
mngmtAgentTrap_23002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_23002.setStatus(
        ""
    )

mngmtAgentTrap_23003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136023003)
)
mngmtAgentTrap_23003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_23003.setStatus(
        ""
    )

mngmtAgentTrap_24001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136024001)
)
mngmtAgentTrap_24001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_24001.setStatus(
        ""
    )

mngmtAgentTrap_24002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136024002)
)
mngmtAgentTrap_24002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_24002.setStatus(
        ""
    )

mngmtAgentTrap_24003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136024003)
)
mngmtAgentTrap_24003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_24003.setStatus(
        ""
    )

mngmtAgentTrap_24004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136024004)
)
mngmtAgentTrap_24004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_24004.setStatus(
        ""
    )

mngmtAgentTrap_25001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025001)
)
mngmtAgentTrap_25001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25001.setStatus(
        ""
    )

mngmtAgentTrap_25002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025002)
)
mngmtAgentTrap_25002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25002.setStatus(
        ""
    )

mngmtAgentTrap_25003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025003)
)
mngmtAgentTrap_25003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25003.setStatus(
        ""
    )

mngmtAgentTrap_25004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025004)
)
mngmtAgentTrap_25004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25004.setStatus(
        ""
    )

mngmtAgentTrap_25005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025005)
)
mngmtAgentTrap_25005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25005.setStatus(
        ""
    )

mngmtAgentTrap_25006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025006)
)
mngmtAgentTrap_25006.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25006.setStatus(
        ""
    )

mngmtAgentTrap_25007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025007)
)
mngmtAgentTrap_25007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25007.setStatus(
        ""
    )

mngmtAgentTrap_25008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025008)
)
mngmtAgentTrap_25008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25008.setStatus(
        ""
    )

mngmtAgentTrap_25009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025009)
)
mngmtAgentTrap_25009.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25009.setStatus(
        ""
    )

mngmtAgentTrap_25010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025010)
)
mngmtAgentTrap_25010.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25010.setStatus(
        ""
    )

mngmtAgentTrap_25011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025011)
)
mngmtAgentTrap_25011.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25011.setStatus(
        ""
    )

mngmtAgentTrap_25012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025012)
)
mngmtAgentTrap_25012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25012.setStatus(
        ""
    )

mngmtAgentTrap_25013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025013)
)
mngmtAgentTrap_25013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25013.setStatus(
        ""
    )

mngmtAgentTrap_25014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025014)
)
mngmtAgentTrap_25014.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25014.setStatus(
        ""
    )

mngmtAgentTrap_25015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025015)
)
mngmtAgentTrap_25015.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25015.setStatus(
        ""
    )

mngmtAgentTrap_25016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025016)
)
mngmtAgentTrap_25016.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25016.setStatus(
        ""
    )

mngmtAgentTrap_25017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025017)
)
mngmtAgentTrap_25017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25017.setStatus(
        ""
    )

mngmtAgentTrap_25018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025018)
)
mngmtAgentTrap_25018.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25018.setStatus(
        ""
    )

mngmtAgentTrap_25019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136025019)
)
mngmtAgentTrap_25019.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_25019.setStatus(
        ""
    )

mngmtAgentTrap_26002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026002)
)
mngmtAgentTrap_26002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26002.setStatus(
        ""
    )

mngmtAgentTrap_26005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026005)
)
mngmtAgentTrap_26005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26005.setStatus(
        ""
    )

mngmtAgentTrap_26006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026006)
)
mngmtAgentTrap_26006.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26006.setStatus(
        ""
    )

mngmtAgentTrap_26007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026007)
)
mngmtAgentTrap_26007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26007.setStatus(
        ""
    )

mngmtAgentTrap_26008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026008)
)
mngmtAgentTrap_26008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26008.setStatus(
        ""
    )

mngmtAgentTrap_26009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026009)
)
mngmtAgentTrap_26009.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26009.setStatus(
        ""
    )

mngmtAgentTrap_26010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026010)
)
mngmtAgentTrap_26010.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26010.setStatus(
        ""
    )

mngmtAgentTrap_26011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026011)
)
mngmtAgentTrap_26011.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26011.setStatus(
        ""
    )

mngmtAgentTrap_26012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026012)
)
mngmtAgentTrap_26012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26012.setStatus(
        ""
    )

mngmtAgentTrap_26013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026013)
)
mngmtAgentTrap_26013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26013.setStatus(
        ""
    )

mngmtAgentTrap_26014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026014)
)
mngmtAgentTrap_26014.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26014.setStatus(
        ""
    )

mngmtAgentTrap_26015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026015)
)
mngmtAgentTrap_26015.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26015.setStatus(
        ""
    )

mngmtAgentTrap_26016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026016)
)
mngmtAgentTrap_26016.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26016.setStatus(
        ""
    )

mngmtAgentTrap_26017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026017)
)
mngmtAgentTrap_26017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26017.setStatus(
        ""
    )

mngmtAgentTrap_26018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026018)
)
mngmtAgentTrap_26018.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26018.setStatus(
        ""
    )

mngmtAgentTrap_26019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136026019)
)
mngmtAgentTrap_26019.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_26019.setStatus(
        ""
    )

mngmtAgentTrap_27001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027001)
)
mngmtAgentTrap_27001.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27001.setStatus(
        ""
    )

mngmtAgentTrap_27002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027002)
)
mngmtAgentTrap_27002.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27002.setStatus(
        ""
    )

mngmtAgentTrap_27003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027003)
)
mngmtAgentTrap_27003.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27003.setStatus(
        ""
    )

mngmtAgentTrap_27004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027004)
)
mngmtAgentTrap_27004.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27004.setStatus(
        ""
    )

mngmtAgentTrap_27005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027005)
)
mngmtAgentTrap_27005.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27005.setStatus(
        ""
    )

mngmtAgentTrap_27006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027006)
)
mngmtAgentTrap_27006.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27006.setStatus(
        ""
    )

mngmtAgentTrap_27007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027007)
)
mngmtAgentTrap_27007.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27007.setStatus(
        ""
    )

mngmtAgentTrap_27008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027008)
)
mngmtAgentTrap_27008.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27008.setStatus(
        ""
    )

mngmtAgentTrap_27009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027009)
)
mngmtAgentTrap_27009.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27009.setStatus(
        ""
    )

mngmtAgentTrap_27010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027010)
)
mngmtAgentTrap_27010.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27010.setStatus(
        ""
    )

mngmtAgentTrap_27011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027011)
)
mngmtAgentTrap_27011.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27011.setStatus(
        ""
    )

mngmtAgentTrap_27012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027012)
)
mngmtAgentTrap_27012.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27012.setStatus(
        ""
    )

mngmtAgentTrap_27013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027013)
)
mngmtAgentTrap_27013.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27013.setStatus(
        ""
    )

mngmtAgentTrap_27014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027014)
)
mngmtAgentTrap_27014.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27014.setStatus(
        ""
    )

mngmtAgentTrap_27015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027015)
)
mngmtAgentTrap_27015.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27015.setStatus(
        ""
    )

mngmtAgentTrap_27016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027016)
)
mngmtAgentTrap_27016.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27016.setStatus(
        ""
    )

mngmtAgentTrap_27017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027017)
)
mngmtAgentTrap_27017.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27017.setStatus(
        ""
    )

mngmtAgentTrap_27018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027018)
)
mngmtAgentTrap_27018.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27018.setStatus(
        ""
    )

mngmtAgentTrap_27019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027019)
)
mngmtAgentTrap_27019.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27019.setStatus(
        ""
    )

mngmtAgentTrap_27020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027020)
)
mngmtAgentTrap_27020.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27020.setStatus(
        ""
    )

mngmtAgentTrap_27021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027021)
)
mngmtAgentTrap_27021.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27021.setStatus(
        ""
    )

mngmtAgentTrap_27022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027022)
)
mngmtAgentTrap_27022.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27022.setStatus(
        ""
    )

mngmtAgentTrap_27023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027023)
)
mngmtAgentTrap_27023.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27023.setStatus(
        ""
    )

mngmtAgentTrap_27024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027024)
)
mngmtAgentTrap_27024.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27024.setStatus(
        ""
    )

mngmtAgentTrap_27025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027025)
)
mngmtAgentTrap_27025.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27025.setStatus(
        ""
    )

mngmtAgentTrap_27026 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027026)
)
mngmtAgentTrap_27026.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27026.setStatus(
        ""
    )

mngmtAgentTrap_27027 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027027)
)
mngmtAgentTrap_27027.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27027.setStatus(
        ""
    )

mngmtAgentTrap_27028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027028)
)
mngmtAgentTrap_27028.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27028.setStatus(
        ""
    )

mngmtAgentTrap_27029 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027029)
)
mngmtAgentTrap_27029.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27029.setStatus(
        ""
    )

mngmtAgentTrap_27030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027030)
)
mngmtAgentTrap_27030.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27030.setStatus(
        ""
    )

mngmtAgentTrap_27031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027031)
)
mngmtAgentTrap_27031.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27031.setStatus(
        ""
    )

mngmtAgentTrap_27032 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027032)
)
mngmtAgentTrap_27032.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27032.setStatus(
        ""
    )

mngmtAgentTrap_27033 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027033)
)
mngmtAgentTrap_27033.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27033.setStatus(
        ""
    )

mngmtAgentTrap_27034 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027034)
)
mngmtAgentTrap_27034.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27034.setStatus(
        ""
    )

mngmtAgentTrap_27035 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027035)
)
mngmtAgentTrap_27035.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27035.setStatus(
        ""
    )

mngmtAgentTrap_27036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027036)
)
mngmtAgentTrap_27036.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27036.setStatus(
        ""
    )

mngmtAgentTrap_27037 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027037)
)
mngmtAgentTrap_27037.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27037.setStatus(
        ""
    )

mngmtAgentTrap_27038 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027038)
)
mngmtAgentTrap_27038.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27038.setStatus(
        ""
    )

mngmtAgentTrap_27039 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027039)
)
mngmtAgentTrap_27039.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27039.setStatus(
        ""
    )

mngmtAgentTrap_27040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027040)
)
mngmtAgentTrap_27040.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27040.setStatus(
        ""
    )

mngmtAgentTrap_27041 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027041)
)
mngmtAgentTrap_27041.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27041.setStatus(
        ""
    )

mngmtAgentTrap_27042 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027042)
)
mngmtAgentTrap_27042.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27042.setStatus(
        ""
    )

mngmtAgentTrap_27043 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027043)
)
mngmtAgentTrap_27043.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27043.setStatus(
        ""
    )

mngmtAgentTrap_27044 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027044)
)
mngmtAgentTrap_27044.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27044.setStatus(
        ""
    )

mngmtAgentTrap_27045 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027045)
)
mngmtAgentTrap_27045.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27045.setStatus(
        ""
    )

mngmtAgentTrap_27046 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027046)
)
mngmtAgentTrap_27046.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27046.setStatus(
        ""
    )

mngmtAgentTrap_27047 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027047)
)
mngmtAgentTrap_27047.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27047.setStatus(
        ""
    )

mngmtAgentTrap_27048 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027048)
)
mngmtAgentTrap_27048.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27048.setStatus(
        ""
    )

mngmtAgentTrap_27049 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027049)
)
mngmtAgentTrap_27049.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27049.setStatus(
        ""
    )

mngmtAgentTrap_27050 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027050)
)
mngmtAgentTrap_27050.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27050.setStatus(
        ""
    )

mngmtAgentTrap_27051 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027051)
)
mngmtAgentTrap_27051.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27051.setStatus(
        ""
    )

mngmtAgentTrap_27052 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 136027052)
)
mngmtAgentTrap_27052.setObjects(
      *(("CPQHSV-MIB", "hostName"),
        ("CPQHSV-MIB", "scellNameDateTime"),
        ("CPQHSV-MIB", "agentEventCode"),
        ("CPQHSV-MIB", "agentEventDescription"))
)
if mibBuilder.loadTexts:
    mngmtAgentTrap_27052.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQHSV-MIB",
    **{"compaq": compaq,
       "emuEventTrapInformative": emuEventTrapInformative,
       "emuEventTrapNoncritical": emuEventTrapNoncritical,
       "emuEventTrapCritical": emuEventTrapCritical,
       "emuEventTrapUnrecoverable": emuEventTrapUnrecoverable,
       "sCellEventTrap-01-02": sCellEventTrap_01_02,
       "sCellEventTrap-03-00": sCellEventTrap_03_00,
       "sCellEventTrap-03-01": sCellEventTrap_03_01,
       "sCellEventTrap-03-02": sCellEventTrap_03_02,
       "sCellEventTrap-03-03": sCellEventTrap_03_03,
       "sCellEventTrap-03-04": sCellEventTrap_03_04,
       "sCellEventTrap-03-05": sCellEventTrap_03_05,
       "sCellEventTrap-03-06": sCellEventTrap_03_06,
       "sCellEventTrap-03-07": sCellEventTrap_03_07,
       "sCellEventTrap-03-08": sCellEventTrap_03_08,
       "sCellEventTrap-03-09": sCellEventTrap_03_09,
       "sCellEventTrap-03-0a": sCellEventTrap_03_0a,
       "sCellEventTrap-03-0b": sCellEventTrap_03_0b,
       "sCellEventTrap-04-00": sCellEventTrap_04_00,
       "sCellEventTrap-04-01": sCellEventTrap_04_01,
       "sCellEventTrap-04-02": sCellEventTrap_04_02,
       "sCellEventTrap-04-03": sCellEventTrap_04_03,
       "sCellEventTrap-04-04": sCellEventTrap_04_04,
       "sCellEventTrap-04-05": sCellEventTrap_04_05,
       "sCellEventTrap-04-06": sCellEventTrap_04_06,
       "sCellEventTrap-04-07": sCellEventTrap_04_07,
       "sCellEventTrap-04-08": sCellEventTrap_04_08,
       "sCellEventTrap-04-09": sCellEventTrap_04_09,
       "sCellEventTrap-04-0a": sCellEventTrap_04_0a,
       "sCellEventTrap-04-0b": sCellEventTrap_04_0b,
       "sCellEventTrap-04-0c": sCellEventTrap_04_0c,
       "sCellEventTrap-04-0d": sCellEventTrap_04_0d,
       "sCellEventTrap-04-0e": sCellEventTrap_04_0e,
       "sCellEventTrap-04-0f": sCellEventTrap_04_0f,
       "sCellEventTrap-04-10": sCellEventTrap_04_10,
       "sCellEventTrap-04-11": sCellEventTrap_04_11,
       "sCellEventTrap-04-12": sCellEventTrap_04_12,
       "sCellEventTrap-04-13": sCellEventTrap_04_13,
       "sCellEventTrap-06-00": sCellEventTrap_06_00,
       "sCellEventTrap-06-01": sCellEventTrap_06_01,
       "sCellEventTrap-06-02": sCellEventTrap_06_02,
       "sCellEventTrap-06-03": sCellEventTrap_06_03,
       "sCellEventTrap-06-04": sCellEventTrap_06_04,
       "sCellEventTrap-06-05": sCellEventTrap_06_05,
       "sCellEventTrap-06-07": sCellEventTrap_06_07,
       "sCellEventTrap-06-08": sCellEventTrap_06_08,
       "sCellEventTrap-06-09": sCellEventTrap_06_09,
       "sCellEventTrap-06-0a": sCellEventTrap_06_0a,
       "sCellEventTrap-06-0b": sCellEventTrap_06_0b,
       "sCellEventTrap-06-0c": sCellEventTrap_06_0c,
       "sCellEventTrap-06-0d": sCellEventTrap_06_0d,
       "sCellEventTrap-06-0e": sCellEventTrap_06_0e,
       "sCellEventTrap-06-0f": sCellEventTrap_06_0f,
       "sCellEventTrap-06-10": sCellEventTrap_06_10,
       "sCellEventTrap-06-12": sCellEventTrap_06_12,
       "sCellEventTrap-06-13": sCellEventTrap_06_13,
       "sCellEventTrap-06-14": sCellEventTrap_06_14,
       "sCellEventTrap-06-15": sCellEventTrap_06_15,
       "sCellEventTrap-06-16": sCellEventTrap_06_16,
       "sCellEventTrap-06-18": sCellEventTrap_06_18,
       "sCellEventTrap-06-19": sCellEventTrap_06_19,
       "sCellEventTrap-06-1a": sCellEventTrap_06_1a,
       "sCellEventTrap-06-1b": sCellEventTrap_06_1b,
       "sCellEventTrap-06-1c": sCellEventTrap_06_1c,
       "sCellEventTrap-06-1d": sCellEventTrap_06_1d,
       "sCellEventTrap-06-1e": sCellEventTrap_06_1e,
       "sCellEventTrap-06-1f": sCellEventTrap_06_1f,
       "sCellEventTrap-06-20": sCellEventTrap_06_20,
       "sCellEventTrap-06-21": sCellEventTrap_06_21,
       "sCellEventTrap-06-23": sCellEventTrap_06_23,
       "sCellEventTrap-06-24": sCellEventTrap_06_24,
       "sCellEventTrap-06-25": sCellEventTrap_06_25,
       "sCellEventTrap-06-26": sCellEventTrap_06_26,
       "sCellEventTrap-06-27": sCellEventTrap_06_27,
       "sCellEventTrap-06-28": sCellEventTrap_06_28,
       "sCellEventTrap-06-29": sCellEventTrap_06_29,
       "sCellEventTrap-06-2a": sCellEventTrap_06_2a,
       "sCellEventTrap-06-2b": sCellEventTrap_06_2b,
       "sCellEventTrap-06-2c": sCellEventTrap_06_2c,
       "sCellEventTrap-06-2d": sCellEventTrap_06_2d,
       "sCellEventTrap-06-2e": sCellEventTrap_06_2e,
       "sCellEventTrap-06-30": sCellEventTrap_06_30,
       "sCellEventTrap-06-31": sCellEventTrap_06_31,
       "sCellEventTrap-06-32": sCellEventTrap_06_32,
       "sCellEventTrap-06-33": sCellEventTrap_06_33,
       "sCellEventTrap-06-34": sCellEventTrap_06_34,
       "sCellEventTrap-06-35": sCellEventTrap_06_35,
       "sCellEventTrap-06-36": sCellEventTrap_06_36,
       "sCellEventTrap-06-37": sCellEventTrap_06_37,
       "sCellEventTrap-06-38": sCellEventTrap_06_38,
       "sCellEventTrap-06-39": sCellEventTrap_06_39,
       "sCellEventTrap-06-3a": sCellEventTrap_06_3a,
       "sCellEventTrap-06-3b": sCellEventTrap_06_3b,
       "sCellEventTrap-06-3c": sCellEventTrap_06_3c,
       "sCellEventTrap-06-3d": sCellEventTrap_06_3d,
       "sCellEventTrap-06-3e": sCellEventTrap_06_3e,
       "sCellEventTrap-06-3f": sCellEventTrap_06_3f,
       "sCellEventTrap-06-40": sCellEventTrap_06_40,
       "sCellEventTrap-06-41": sCellEventTrap_06_41,
       "sCellEventTrap-06-42": sCellEventTrap_06_42,
       "sCellEventTrap-06-43": sCellEventTrap_06_43,
       "sCellEventTrap-07-00": sCellEventTrap_07_00,
       "sCellEventTrap-07-01": sCellEventTrap_07_01,
       "sCellEventTrap-07-02": sCellEventTrap_07_02,
       "sCellEventTrap-07-03": sCellEventTrap_07_03,
       "sCellEventTrap-07-04": sCellEventTrap_07_04,
       "sCellEventTrap-07-05": sCellEventTrap_07_05,
       "sCellEventTrap-07-06": sCellEventTrap_07_06,
       "sCellEventTrap-07-07": sCellEventTrap_07_07,
       "sCellEventTrap-07-08": sCellEventTrap_07_08,
       "sCellEventTrap-07-09": sCellEventTrap_07_09,
       "sCellEventTrap-07-0a": sCellEventTrap_07_0a,
       "sCellEventTrap-07-0b": sCellEventTrap_07_0b,
       "sCellEventTrap-09-01": sCellEventTrap_09_01,
       "sCellEventTrap-09-02": sCellEventTrap_09_02,
       "sCellEventTrap-09-03": sCellEventTrap_09_03,
       "sCellEventTrap-09-04": sCellEventTrap_09_04,
       "sCellEventTrap-09-05": sCellEventTrap_09_05,
       "sCellEventTrap-09-06": sCellEventTrap_09_06,
       "sCellEventTrap-09-07": sCellEventTrap_09_07,
       "sCellEventTrap-09-08": sCellEventTrap_09_08,
       "sCellEventTrap-09-09": sCellEventTrap_09_09,
       "sCellEventTrap-09-0a": sCellEventTrap_09_0a,
       "sCellEventTrap-09-0c": sCellEventTrap_09_0c,
       "sCellEventTrap-09-0d": sCellEventTrap_09_0d,
       "sCellEventTrap-09-0e": sCellEventTrap_09_0e,
       "sCellEventTrap-09-0f": sCellEventTrap_09_0f,
       "sCellEventTrap-09-11": sCellEventTrap_09_11,
       "sCellEventTrap-09-12": sCellEventTrap_09_12,
       "sCellEventTrap-09-13": sCellEventTrap_09_13,
       "sCellEventTrap-09-14": sCellEventTrap_09_14,
       "sCellEventTrap-09-15": sCellEventTrap_09_15,
       "sCellEventTrap-09-16": sCellEventTrap_09_16,
       "sCellEventTrap-09-17": sCellEventTrap_09_17,
       "sCellEventTrap-09-18": sCellEventTrap_09_18,
       "sCellEventTrap-09-19": sCellEventTrap_09_19,
       "sCellEventTrap-09-1a": sCellEventTrap_09_1a,
       "sCellEventTrap-09-1b": sCellEventTrap_09_1b,
       "sCellEventTrap-09-1c": sCellEventTrap_09_1c,
       "sCellEventTrap-09-1d": sCellEventTrap_09_1d,
       "sCellEventTrap-09-1e": sCellEventTrap_09_1e,
       "sCellEventTrap-09-1f": sCellEventTrap_09_1f,
       "sCellEventTrap-09-20": sCellEventTrap_09_20,
       "sCellEventTrap-09-21": sCellEventTrap_09_21,
       "sCellEventTrap-09-22": sCellEventTrap_09_22,
       "sCellEventTrap-09-23": sCellEventTrap_09_23,
       "sCellEventTrap-09-24": sCellEventTrap_09_24,
       "sCellEventTrap-09-25": sCellEventTrap_09_25,
       "sCellEventTrap-09-26": sCellEventTrap_09_26,
       "sCellEventTrap-09-27": sCellEventTrap_09_27,
       "sCellEventTrap-09-28": sCellEventTrap_09_28,
       "sCellEventTrap-09-29": sCellEventTrap_09_29,
       "sCellEventTrap-09-2a": sCellEventTrap_09_2a,
       "sCellEventTrap-09-2b": sCellEventTrap_09_2b,
       "sCellEventTrap-09-2c": sCellEventTrap_09_2c,
       "sCellEventTrap-09-2d": sCellEventTrap_09_2d,
       "sCellEventTrap-09-2e": sCellEventTrap_09_2e,
       "sCellEventTrap-09-2f": sCellEventTrap_09_2f,
       "sCellEventTrap-09-30": sCellEventTrap_09_30,
       "sCellEventTrap-09-31": sCellEventTrap_09_31,
       "sCellEventTrap-09-32": sCellEventTrap_09_32,
       "sCellEventTrap-09-33": sCellEventTrap_09_33,
       "sCellEventTrap-09-34": sCellEventTrap_09_34,
       "sCellEventTrap-09-35": sCellEventTrap_09_35,
       "sCellEventTrap-09-36": sCellEventTrap_09_36,
       "sCellEventTrap-09-37": sCellEventTrap_09_37,
       "sCellEventTrap-09-38": sCellEventTrap_09_38,
       "sCellEventTrap-09-39": sCellEventTrap_09_39,
       "sCellEventTrap-09-3a": sCellEventTrap_09_3a,
       "sCellEventTrap-09-3b": sCellEventTrap_09_3b,
       "sCellEventTrap-09-3c": sCellEventTrap_09_3c,
       "sCellEventTrap-09-3d": sCellEventTrap_09_3d,
       "sCellEventTrap-09-3e": sCellEventTrap_09_3e,
       "sCellEventTrap-09-3f": sCellEventTrap_09_3f,
       "sCellEventTrap-09-40": sCellEventTrap_09_40,
       "sCellEventTrap-09-41": sCellEventTrap_09_41,
       "sCellEventTrap-09-43": sCellEventTrap_09_43,
       "sCellEventTrap-09-44": sCellEventTrap_09_44,
       "sCellEventTrap-09-45": sCellEventTrap_09_45,
       "sCellEventTrap-09-46": sCellEventTrap_09_46,
       "sCellEventTrap-09-47": sCellEventTrap_09_47,
       "sCellEventTrap-09-48": sCellEventTrap_09_48,
       "sCellEventTrap-09-49": sCellEventTrap_09_49,
       "sCellEventTrap-09-4a": sCellEventTrap_09_4a,
       "sCellEventTrap-09-65": sCellEventTrap_09_65,
       "sCellEventTrap-09-66": sCellEventTrap_09_66,
       "sCellEventTrap-09-67": sCellEventTrap_09_67,
       "sCellEventTrap-09-68": sCellEventTrap_09_68,
       "sCellEventTrap-09-69": sCellEventTrap_09_69,
       "sCellEventTrap-09-6a": sCellEventTrap_09_6a,
       "sCellEventTrap-09-6b": sCellEventTrap_09_6b,
       "sCellEventTrap-09-6c": sCellEventTrap_09_6c,
       "sCellEventTrap-09-6d": sCellEventTrap_09_6d,
       "sCellEventTrap-09-6e": sCellEventTrap_09_6e,
       "sCellEventTrap-09-70": sCellEventTrap_09_70,
       "sCellEventTrap-09-71": sCellEventTrap_09_71,
       "sCellEventTrap-09-72": sCellEventTrap_09_72,
       "sCellEventTrap-09-73": sCellEventTrap_09_73,
       "sCellEventTrap-09-74": sCellEventTrap_09_74,
       "sCellEventTrap-09-75": sCellEventTrap_09_75,
       "sCellEventTrap-09-76": sCellEventTrap_09_76,
       "sCellEventTrap-09-77": sCellEventTrap_09_77,
       "sCellEventTrap-09-78": sCellEventTrap_09_78,
       "sCellEventTrap-09-79": sCellEventTrap_09_79,
       "sCellEventTrap-09-7a": sCellEventTrap_09_7a,
       "sCellEventTrap-09-7b": sCellEventTrap_09_7b,
       "sCellEventTrap-09-7c": sCellEventTrap_09_7c,
       "sCellEventTrap-09-c8": sCellEventTrap_09_c8,
       "sCellEventTrap-09-c9": sCellEventTrap_09_c9,
       "sCellEventTrap-09-ca": sCellEventTrap_09_ca,
       "sCellEventTrap-09-cb": sCellEventTrap_09_cb,
       "sCellEventTrap-09-cc": sCellEventTrap_09_cc,
       "sCellEventTrap-09-cd": sCellEventTrap_09_cd,
       "sCellEventTrap-09-ce": sCellEventTrap_09_ce,
       "sCellEventTrap-09-cf": sCellEventTrap_09_cf,
       "sCellEventTrap-09-d0": sCellEventTrap_09_d0,
       "sCellEventTrap-09-d1": sCellEventTrap_09_d1,
       "sCellEventTrap-09-d2": sCellEventTrap_09_d2,
       "sCellEventTrap-09-d3": sCellEventTrap_09_d3,
       "sCellEventTrap-09-d4": sCellEventTrap_09_d4,
       "sCellEventTrap-09-d5": sCellEventTrap_09_d5,
       "sCellEventTrap-09-d6": sCellEventTrap_09_d6,
       "sCellEventTrap-09-d7": sCellEventTrap_09_d7,
       "sCellEventTrap-09-d8": sCellEventTrap_09_d8,
       "sCellEventTrap-09-d9": sCellEventTrap_09_d9,
       "sCellEventTrap-09-da": sCellEventTrap_09_da,
       "sCellEventTrap-09-db": sCellEventTrap_09_db,
       "sCellEventTrap-0b-00": sCellEventTrap_0b_00,
       "sCellEventTrap-0b-01": sCellEventTrap_0b_01,
       "sCellEventTrap-0b-02": sCellEventTrap_0b_02,
       "sCellEventTrap-0b-03": sCellEventTrap_0b_03,
       "sCellEventTrap-0b-04": sCellEventTrap_0b_04,
       "sCellEventTrap-0b-05": sCellEventTrap_0b_05,
       "sCellEventTrap-0c-03": sCellEventTrap_0c_03,
       "sCellEventTrap-0c-04": sCellEventTrap_0c_04,
       "sCellEventTrap-0c-05": sCellEventTrap_0c_05,
       "sCellEventTrap-0c-06": sCellEventTrap_0c_06,
       "sCellEventTrap-0c-07": sCellEventTrap_0c_07,
       "sCellEventTrap-0c-08": sCellEventTrap_0c_08,
       "sCellEventTrap-0c-09": sCellEventTrap_0c_09,
       "sCellEventTrap-0c-0a": sCellEventTrap_0c_0a,
       "sCellEventTrap-0c-0c": sCellEventTrap_0c_0c,
       "sCellEventTrap-0c-0f": sCellEventTrap_0c_0f,
       "sCellEventTrap-0c-10": sCellEventTrap_0c_10,
       "sCellEventTrap-0c-11": sCellEventTrap_0c_11,
       "sCellEventTrap-0c-12": sCellEventTrap_0c_12,
       "sCellEventTrap-0c-15": sCellEventTrap_0c_15,
       "sCellEventTrap-0c-16": sCellEventTrap_0c_16,
       "sCellEventTrap-0c-17": sCellEventTrap_0c_17,
       "sCellEventTrap-0c-18": sCellEventTrap_0c_18,
       "sCellEventTrap-0c-19": sCellEventTrap_0c_19,
       "sCellEventTrap-0c-1a": sCellEventTrap_0c_1a,
       "sCellEventTrap-0c-1b": sCellEventTrap_0c_1b,
       "sCellEventTrap-0c-1c": sCellEventTrap_0c_1c,
       "sCellEventTrap-0c-1d": sCellEventTrap_0c_1d,
       "sCellEventTrap-0c-1e": sCellEventTrap_0c_1e,
       "sCellEventTrap-0c-1f": sCellEventTrap_0c_1f,
       "sCellEventTrap-0c-20": sCellEventTrap_0c_20,
       "sCellEventTrap-0c-21": sCellEventTrap_0c_21,
       "sCellEventTrap-0c-22": sCellEventTrap_0c_22,
       "sCellEventTrap-0d-00": sCellEventTrap_0d_00,
       "sCellEventTrap-0d-01": sCellEventTrap_0d_01,
       "sCellEventTrap-0d-02": sCellEventTrap_0d_02,
       "sCellEventTrap-0d-03": sCellEventTrap_0d_03,
       "sCellEventTrap-0d-04": sCellEventTrap_0d_04,
       "sCellEventTrap-0d-33": sCellEventTrap_0d_33,
       "sCellEventTrap-0d-34": sCellEventTrap_0d_34,
       "sCellEventTrap-0d-35": sCellEventTrap_0d_35,
       "sCellEventTrap-0d-47": sCellEventTrap_0d_47,
       "sCellEventTrap-0d-4b": sCellEventTrap_0d_4b,
       "sCellEventTrap-0d-4c": sCellEventTrap_0d_4c,
       "sCellEventTrap-0d-5b": sCellEventTrap_0d_5b,
       "sCellEventTrap-0d-5f": sCellEventTrap_0d_5f,
       "sCellEventTrap-0d-6f": sCellEventTrap_0d_6f,
       "sCellEventTrap-0d-71": sCellEventTrap_0d_71,
       "sCellEventTrap-0d-72": sCellEventTrap_0d_72,
       "sCellEventTrap-0d-7e": sCellEventTrap_0d_7e,
       "sCellEventTrap-0d-7f": sCellEventTrap_0d_7f,
       "sCellEventTrap-0d-82": sCellEventTrap_0d_82,
       "sCellEventTrap-0d-83": sCellEventTrap_0d_83,
       "sCellEventTrap-0d-85": sCellEventTrap_0d_85,
       "sCellEventTrap-0d-8d": sCellEventTrap_0d_8d,
       "sCellEventTrap-0d-a1": sCellEventTrap_0d_a1,
       "sCellEventTrap-0d-b5": sCellEventTrap_0d_b5,
       "sCellEventTrap-0d-d8": sCellEventTrap_0d_d8,
       "sCellEventTrap-0d-d9": sCellEventTrap_0d_d9,
       "sCellEventTrap-0d-dd": sCellEventTrap_0d_dd,
       "sCellEventTrap-0d-de": sCellEventTrap_0d_de,
       "sCellEventTrap-0d-ec": sCellEventTrap_0d_ec,
       "sCellEventTrap-0d-f0": sCellEventTrap_0d_f0,
       "sCellEventTrap-42-00": sCellEventTrap_42_00,
       "sCellEventTrap-42-01": sCellEventTrap_42_01,
       "sCellEventTrap-42-03": sCellEventTrap_42_03,
       "sCellEventTrap-42-04": sCellEventTrap_42_04,
       "sCellEventTrap-42-05": sCellEventTrap_42_05,
       "sCellEventTrap-83-00": sCellEventTrap_83_00,
       "sCellEventTrap-83-01": sCellEventTrap_83_01,
       "sCellEventTrap-83-02": sCellEventTrap_83_02,
       "sCellEventTrap-83-03": sCellEventTrap_83_03,
       "sCellEventTrap-83-04": sCellEventTrap_83_04,
       "sCellEventTrap-83-05": sCellEventTrap_83_05,
       "sCellEventTrap-83-06": sCellEventTrap_83_06,
       "mngmtAgentTrap-1": mngmtAgentTrap_1,
       "mngmtAgentTrap-2": mngmtAgentTrap_2,
       "mngmtAgentTrap-3": mngmtAgentTrap_3,
       "mngmtAgentTrap-4": mngmtAgentTrap_4,
       "mngmtAgentTrap-5": mngmtAgentTrap_5,
       "mngmtAgentTrap-6": mngmtAgentTrap_6,
       "mngmtAgentTrap-7": mngmtAgentTrap_7,
       "mngmtAgentTrap-8": mngmtAgentTrap_8,
       "mngmtAgentTrap-9": mngmtAgentTrap_9,
       "mngmtAgentTrap-10": mngmtAgentTrap_10,
       "mngmtAgentTrap-11": mngmtAgentTrap_11,
       "mngmtAgentTrap-12": mngmtAgentTrap_12,
       "mngmtAgentTrap-13": mngmtAgentTrap_13,
       "mngmtAgentTrap-14": mngmtAgentTrap_14,
       "mngmtAgentTrap-15": mngmtAgentTrap_15,
       "mngmtAgentTrap-16": mngmtAgentTrap_16,
       "mngmtAgentTrap-17": mngmtAgentTrap_17,
       "mngmtAgentTrap-18": mngmtAgentTrap_18,
       "mngmtAgentTrap-19": mngmtAgentTrap_19,
       "mngmtAgentTrap-20": mngmtAgentTrap_20,
       "mngmtAgentTrap-21": mngmtAgentTrap_21,
       "mngmtAgentTrap-22": mngmtAgentTrap_22,
       "mngmtAgentTrap-23": mngmtAgentTrap_23,
       "mngmtAgentTrap-24": mngmtAgentTrap_24,
       "mngmtAgentTrap-25": mngmtAgentTrap_25,
       "mngmtAgentTrap-26": mngmtAgentTrap_26,
       "mngmtAgentTrap-27": mngmtAgentTrap_27,
       "mngmtAgentTrap-28": mngmtAgentTrap_28,
       "mngmtAgentTrap-29": mngmtAgentTrap_29,
       "mngmtAgentTrap-30": mngmtAgentTrap_30,
       "mngmtAgentTrap-31": mngmtAgentTrap_31,
       "mngmtAgentTrap-32": mngmtAgentTrap_32,
       "mngmtAgentTrap-33": mngmtAgentTrap_33,
       "mngmtAgentTrap-34": mngmtAgentTrap_34,
       "mngmtAgentTrap-35": mngmtAgentTrap_35,
       "mngmtAgentTrap-36": mngmtAgentTrap_36,
       "mngmtAgentTrap-37": mngmtAgentTrap_37,
       "mngmtAgentTrap-38": mngmtAgentTrap_38,
       "mngmtAgentTrap-39": mngmtAgentTrap_39,
       "mngmtAgentTrap-40": mngmtAgentTrap_40,
       "mngmtAgentTrap-41": mngmtAgentTrap_41,
       "mngmtAgentTrap-42": mngmtAgentTrap_42,
       "mngmtAgentTrap-43": mngmtAgentTrap_43,
       "mngmtAgentTrap-44": mngmtAgentTrap_44,
       "mngmtAgentTrap-45": mngmtAgentTrap_45,
       "mngmtAgentTrap-46": mngmtAgentTrap_46,
       "mngmtAgentTrap-47": mngmtAgentTrap_47,
       "mngmtAgentTrap-48": mngmtAgentTrap_48,
       "mngmtAgentTrap-49": mngmtAgentTrap_49,
       "mngmtAgentTrap-50": mngmtAgentTrap_50,
       "mngmtAgentTrap-51": mngmtAgentTrap_51,
       "mngmtAgentTrap-52": mngmtAgentTrap_52,
       "mngmtAgentTrap-53": mngmtAgentTrap_53,
       "mngmtAgentTrap-54": mngmtAgentTrap_54,
       "mngmtAgentTrap-55": mngmtAgentTrap_55,
       "mngmtAgentTrap-56": mngmtAgentTrap_56,
       "mngmtAgentTrap-57": mngmtAgentTrap_57,
       "mngmtAgentTrap-58": mngmtAgentTrap_58,
       "mngmtAgentTrap-59": mngmtAgentTrap_59,
       "mngmtAgentTrap-60": mngmtAgentTrap_60,
       "mngmtAgentTrap-61": mngmtAgentTrap_61,
       "mngmtAgentTrap-62": mngmtAgentTrap_62,
       "mngmtAgentTrap-63": mngmtAgentTrap_63,
       "mngmtAgentTrap-64": mngmtAgentTrap_64,
       "mngmtAgentTrap-65": mngmtAgentTrap_65,
       "mngmtAgentTrap-66": mngmtAgentTrap_66,
       "mngmtAgentTrap-67": mngmtAgentTrap_67,
       "mngmtAgentTrap-68": mngmtAgentTrap_68,
       "mngmtAgentTrap-69": mngmtAgentTrap_69,
       "mngmtAgentTrap-70": mngmtAgentTrap_70,
       "mngmtAgentTrap-71": mngmtAgentTrap_71,
       "mngmtAgentTrap-72": mngmtAgentTrap_72,
       "mngmtAgentTrap-73": mngmtAgentTrap_73,
       "mngmtAgentTrap-74": mngmtAgentTrap_74,
       "mngmtAgentTrap-75": mngmtAgentTrap_75,
       "mngmtAgentTrap-76": mngmtAgentTrap_76,
       "mngmtAgentTrap-77": mngmtAgentTrap_77,
       "mngmtAgentTrap-78": mngmtAgentTrap_78,
       "mngmtAgentTrap-79": mngmtAgentTrap_79,
       "mngmtAgentTrap-80": mngmtAgentTrap_80,
       "mngmtAgentTrap-81": mngmtAgentTrap_81,
       "mngmtAgentTrap-82": mngmtAgentTrap_82,
       "mngmtAgentTrap-83": mngmtAgentTrap_83,
       "mngmtAgentTrap-84": mngmtAgentTrap_84,
       "mngmtAgentTrap-85": mngmtAgentTrap_85,
       "mngmtAgentTrap-86": mngmtAgentTrap_86,
       "mngmtAgentTrap-87": mngmtAgentTrap_87,
       "mngmtAgentTrap-88": mngmtAgentTrap_88,
       "mngmtAgentTrap-89": mngmtAgentTrap_89,
       "mngmtAgentTrap-90": mngmtAgentTrap_90,
       "mngmtAgentTrap-91": mngmtAgentTrap_91,
       "mngmtAgentTrap-92": mngmtAgentTrap_92,
       "mngmtAgentTrap-93": mngmtAgentTrap_93,
       "mngmtAgentTrap-94": mngmtAgentTrap_94,
       "mngmtAgentTrap-95": mngmtAgentTrap_95,
       "mngmtAgentTrap-96": mngmtAgentTrap_96,
       "mngmtAgentTrap-97": mngmtAgentTrap_97,
       "mngmtAgentTrap-98": mngmtAgentTrap_98,
       "mngmtAgentTrap-99": mngmtAgentTrap_99,
       "mngmtAgentTrap-100": mngmtAgentTrap_100,
       "mngmtAgentTrap-101": mngmtAgentTrap_101,
       "mngmtAgentTrap-102": mngmtAgentTrap_102,
       "mngmtAgentTrap-103": mngmtAgentTrap_103,
       "mngmtAgentTrap-104": mngmtAgentTrap_104,
       "mngmtAgentTrap-105": mngmtAgentTrap_105,
       "mngmtAgentTrap-106": mngmtAgentTrap_106,
       "mngmtAgentTrap-107": mngmtAgentTrap_107,
       "mngmtAgentTrap-108": mngmtAgentTrap_108,
       "mngmtAgentTrap-109": mngmtAgentTrap_109,
       "mngmtAgentTrap-110": mngmtAgentTrap_110,
       "mngmtAgentTrap-111": mngmtAgentTrap_111,
       "mngmtAgentTrap-112": mngmtAgentTrap_112,
       "mngmtAgentTrap-113": mngmtAgentTrap_113,
       "mngmtAgentTrap-114": mngmtAgentTrap_114,
       "mngmtAgentTrap-115": mngmtAgentTrap_115,
       "mngmtAgentTrap-116": mngmtAgentTrap_116,
       "mngmtAgentTrap-117": mngmtAgentTrap_117,
       "mngmtAgentTrap-118": mngmtAgentTrap_118,
       "mngmtAgentTrap-119": mngmtAgentTrap_119,
       "mngmtAgentTrap-120": mngmtAgentTrap_120,
       "mngmtAgentTrap-121": mngmtAgentTrap_121,
       "mngmtAgentTrap-122": mngmtAgentTrap_122,
       "mngmtAgentTrap-123": mngmtAgentTrap_123,
       "mngmtAgentTrap-124": mngmtAgentTrap_124,
       "mngmtAgentTrap-125": mngmtAgentTrap_125,
       "mngmtAgentTrap-126": mngmtAgentTrap_126,
       "mngmtAgentTrap-127": mngmtAgentTrap_127,
       "mngmtAgentTrap-128": mngmtAgentTrap_128,
       "mngmtAgentTrap-129": mngmtAgentTrap_129,
       "mngmtAgentTrap-130": mngmtAgentTrap_130,
       "mngmtAgentTrap-131": mngmtAgentTrap_131,
       "mngmtAgentTrap-132": mngmtAgentTrap_132,
       "mngmtAgentTrap-133": mngmtAgentTrap_133,
       "mngmtAgentTrap-134": mngmtAgentTrap_134,
       "mngmtAgentTrap-141": mngmtAgentTrap_141,
       "mngmtAgentTrap-142": mngmtAgentTrap_142,
       "mngmtAgentTrap-148": mngmtAgentTrap_148,
       "mngmtAgentTrap-180": mngmtAgentTrap_180,
       "mngmtAgentTrap-181": mngmtAgentTrap_181,
       "mngmtAgentTrap-182": mngmtAgentTrap_182,
       "mngmtAgentTrap-183": mngmtAgentTrap_183,
       "mngmtAgentTrap-184": mngmtAgentTrap_184,
       "mngmtAgentTrap-195": mngmtAgentTrap_195,
       "mngmtAgentTrap-196": mngmtAgentTrap_196,
       "mngmtAgentTrap-197": mngmtAgentTrap_197,
       "mngmtAgentTrap-198": mngmtAgentTrap_198,
       "mngmtAgentTrap-199": mngmtAgentTrap_199,
       "mngmtAgentTrap-200": mngmtAgentTrap_200,
       "mngmtAgentTrap-201": mngmtAgentTrap_201,
       "mngmtAgentTrap-202": mngmtAgentTrap_202,
       "mngmtAgentTrap-1000": mngmtAgentTrap_1000,
       "mngmtAgentTrap-1001": mngmtAgentTrap_1001,
       "mngmtAgentTrap-1002": mngmtAgentTrap_1002,
       "mngmtAgentTrap-1003": mngmtAgentTrap_1003,
       "mngmtAgentTrap-1004": mngmtAgentTrap_1004,
       "mngmtAgentTrap-1005": mngmtAgentTrap_1005,
       "mngmtAgentTrap-1006": mngmtAgentTrap_1006,
       "mngmtAgentTrap-1007": mngmtAgentTrap_1007,
       "mngmtAgentTrap-1008": mngmtAgentTrap_1008,
       "mngmtAgentTrap-1009": mngmtAgentTrap_1009,
       "mngmtAgentTrap-1010": mngmtAgentTrap_1010,
       "mngmtAgentTrap-1011": mngmtAgentTrap_1011,
       "mngmtAgentTrap-1012": mngmtAgentTrap_1012,
       "mngmtAgentTrap-1013": mngmtAgentTrap_1013,
       "mngmtAgentTrap-1014": mngmtAgentTrap_1014,
       "mngmtAgentTrap-2001": mngmtAgentTrap_2001,
       "mngmtAgentTrap-2002": mngmtAgentTrap_2002,
       "mngmtAgentTrap-2003": mngmtAgentTrap_2003,
       "mngmtAgentTrap-2004": mngmtAgentTrap_2004,
       "mngmtAgentTrap-2006": mngmtAgentTrap_2006,
       "mngmtAgentTrap-2007": mngmtAgentTrap_2007,
       "mngmtAgentTrap-2008": mngmtAgentTrap_2008,
       "mngmtAgentTrap-2010": mngmtAgentTrap_2010,
       "mngmtAgentTrap-2011": mngmtAgentTrap_2011,
       "mngmtAgentTrap-2012": mngmtAgentTrap_2012,
       "mngmtAgentTrap-2013": mngmtAgentTrap_2013,
       "mngmtAgentTrap-2016": mngmtAgentTrap_2016,
       "mngmtAgentTrap-2021": mngmtAgentTrap_2021,
       "mngmtAgentTrap-2022": mngmtAgentTrap_2022,
       "mngmtAgentTrap-2023": mngmtAgentTrap_2023,
       "mngmtAgentTrap-2025": mngmtAgentTrap_2025,
       "mngmtAgentTrap-2026": mngmtAgentTrap_2026,
       "mngmtAgentTrap-2030": mngmtAgentTrap_2030,
       "mngmtAgentTrap-2031": mngmtAgentTrap_2031,
       "mngmtAgentTrap-2032": mngmtAgentTrap_2032,
       "mngmtAgentTrap-2033": mngmtAgentTrap_2033,
       "mngmtAgentTrap-2034": mngmtAgentTrap_2034,
       "mngmtAgentTrap-2035": mngmtAgentTrap_2035,
       "mngmtAgentTrap-2036": mngmtAgentTrap_2036,
       "mngmtAgentTrap-2038": mngmtAgentTrap_2038,
       "mngmtAgentTrap-2040": mngmtAgentTrap_2040,
       "mngmtAgentTrap-2041": mngmtAgentTrap_2041,
       "mngmtAgentTrap-2042": mngmtAgentTrap_2042,
       "mngmtAgentTrap-2047": mngmtAgentTrap_2047,
       "mngmtAgentTrap-2048": mngmtAgentTrap_2048,
       "mngmtAgentTrap-2049": mngmtAgentTrap_2049,
       "mngmtAgentTrap-2050": mngmtAgentTrap_2050,
       "mngmtAgentTrap-2051": mngmtAgentTrap_2051,
       "mngmtAgentTrap-2052": mngmtAgentTrap_2052,
       "mngmtAgentTrap-2057": mngmtAgentTrap_2057,
       "mngmtAgentTrap-2058": mngmtAgentTrap_2058,
       "mngmtAgentTrap-2059": mngmtAgentTrap_2059,
       "mngmtAgentTrap-2060": mngmtAgentTrap_2060,
       "mngmtAgentTrap-2061": mngmtAgentTrap_2061,
       "mngmtAgentTrap-2062": mngmtAgentTrap_2062,
       "mngmtAgentTrap-2063": mngmtAgentTrap_2063,
       "mngmtAgentTrap-2064": mngmtAgentTrap_2064,
       "mngmtAgentTrap-2065": mngmtAgentTrap_2065,
       "mngmtAgentTrap-2066": mngmtAgentTrap_2066,
       "mngmtAgentTrap-2067": mngmtAgentTrap_2067,
       "mngmtAgentTrap-2068": mngmtAgentTrap_2068,
       "mngmtAgentTrap-2069": mngmtAgentTrap_2069,
       "mngmtAgentTrap-2070": mngmtAgentTrap_2070,
       "mngmtAgentTrap-2071": mngmtAgentTrap_2071,
       "mngmtAgentTrap-2072": mngmtAgentTrap_2072,
       "mngmtAgentTrap-2073": mngmtAgentTrap_2073,
       "mngmtAgentTrap-2074": mngmtAgentTrap_2074,
       "mngmtAgentTrap-2075": mngmtAgentTrap_2075,
       "mngmtAgentTrap-2076": mngmtAgentTrap_2076,
       "mngmtAgentTrap-2077": mngmtAgentTrap_2077,
       "mngmtAgentTrap-2078": mngmtAgentTrap_2078,
       "mngmtAgentTrap-2079": mngmtAgentTrap_2079,
       "mngmtAgentTrap-2080": mngmtAgentTrap_2080,
       "mngmtAgentTrap-2081": mngmtAgentTrap_2081,
       "mngmtAgentTrap-2082": mngmtAgentTrap_2082,
       "mngmtAgentTrap-2083": mngmtAgentTrap_2083,
       "mngmtAgentTrap-2084": mngmtAgentTrap_2084,
       "mngmtAgentTrap-2085": mngmtAgentTrap_2085,
       "mngmtAgentTrap-2086": mngmtAgentTrap_2086,
       "mngmtAgentTrap-2087": mngmtAgentTrap_2087,
       "mngmtAgentTrap-2088": mngmtAgentTrap_2088,
       "mngmtAgentTrap-2089": mngmtAgentTrap_2089,
       "mngmtAgentTrap-2090": mngmtAgentTrap_2090,
       "mngmtAgentTrap-2091": mngmtAgentTrap_2091,
       "mngmtAgentTrap-2092": mngmtAgentTrap_2092,
       "mngmtAgentTrap-2093": mngmtAgentTrap_2093,
       "mngmtAgentTrap-2095": mngmtAgentTrap_2095,
       "mngmtAgentTrap-2096": mngmtAgentTrap_2096,
       "mngmtAgentTrap-2097": mngmtAgentTrap_2097,
       "mngmtAgentTrap-2098": mngmtAgentTrap_2098,
       "mngmtAgentTrap-2099": mngmtAgentTrap_2099,
       "mngmtAgentTrap-2100": mngmtAgentTrap_2100,
       "mngmtAgentTrap-2102": mngmtAgentTrap_2102,
       "mngmtAgentTrap-2103": mngmtAgentTrap_2103,
       "mngmtAgentTrap-2104": mngmtAgentTrap_2104,
       "mngmtAgentTrap-2105": mngmtAgentTrap_2105,
       "mngmtAgentTrap-3001": mngmtAgentTrap_3001,
       "mngmtAgentTrap-3002": mngmtAgentTrap_3002,
       "mngmtAgentTrap-3003": mngmtAgentTrap_3003,
       "mngmtAgentTrap-3004": mngmtAgentTrap_3004,
       "mngmtAgentTrap-3007": mngmtAgentTrap_3007,
       "mngmtAgentTrap-3009": mngmtAgentTrap_3009,
       "mngmtAgentTrap-3012": mngmtAgentTrap_3012,
       "mngmtAgentTrap-3013": mngmtAgentTrap_3013,
       "mngmtAgentTrap-3015": mngmtAgentTrap_3015,
       "mngmtAgentTrap-3016": mngmtAgentTrap_3016,
       "mngmtAgentTrap-3017": mngmtAgentTrap_3017,
       "mngmtAgentTrap-3019": mngmtAgentTrap_3019,
       "mngmtAgentTrap-3020": mngmtAgentTrap_3020,
       "mngmtAgentTrap-3021": mngmtAgentTrap_3021,
       "mngmtAgentTrap-3022": mngmtAgentTrap_3022,
       "mngmtAgentTrap-3024": mngmtAgentTrap_3024,
       "mngmtAgentTrap-3025": mngmtAgentTrap_3025,
       "mngmtAgentTrap-3028": mngmtAgentTrap_3028,
       "mngmtAgentTrap-3029": mngmtAgentTrap_3029,
       "mngmtAgentTrap-3035": mngmtAgentTrap_3035,
       "mngmtAgentTrap-3036": mngmtAgentTrap_3036,
       "mngmtAgentTrap-3037": mngmtAgentTrap_3037,
       "mngmtAgentTrap-3038": mngmtAgentTrap_3038,
       "mngmtAgentTrap-3039": mngmtAgentTrap_3039,
       "mngmtAgentTrap-3044": mngmtAgentTrap_3044,
       "mngmtAgentTrap-3045": mngmtAgentTrap_3045,
       "mngmtAgentTrap-3046": mngmtAgentTrap_3046,
       "mngmtAgentTrap-3047": mngmtAgentTrap_3047,
       "mngmtAgentTrap-3048": mngmtAgentTrap_3048,
       "mngmtAgentTrap-3049": mngmtAgentTrap_3049,
       "mngmtAgentTrap-3050": mngmtAgentTrap_3050,
       "mngmtAgentTrap-3051": mngmtAgentTrap_3051,
       "mngmtAgentTrap-3053": mngmtAgentTrap_3053,
       "mngmtAgentTrap-3054": mngmtAgentTrap_3054,
       "mngmtAgentTrap-3055": mngmtAgentTrap_3055,
       "mngmtAgentTrap-3056": mngmtAgentTrap_3056,
       "mngmtAgentTrap-3057": mngmtAgentTrap_3057,
       "mngmtAgentTrap-3058": mngmtAgentTrap_3058,
       "mngmtAgentTrap-3059": mngmtAgentTrap_3059,
       "mngmtAgentTrap-3060": mngmtAgentTrap_3060,
       "mngmtAgentTrap-3061": mngmtAgentTrap_3061,
       "mngmtAgentTrap-3062": mngmtAgentTrap_3062,
       "mngmtAgentTrap-3063": mngmtAgentTrap_3063,
       "mngmtAgentTrap-3064": mngmtAgentTrap_3064,
       "mngmtAgentTrap-3065": mngmtAgentTrap_3065,
       "mngmtAgentTrap-3066": mngmtAgentTrap_3066,
       "mngmtAgentTrap-3067": mngmtAgentTrap_3067,
       "mngmtAgentTrap-3068": mngmtAgentTrap_3068,
       "mngmtAgentTrap-3069": mngmtAgentTrap_3069,
       "mngmtAgentTrap-3070": mngmtAgentTrap_3070,
       "mngmtAgentTrap-3071": mngmtAgentTrap_3071,
       "mngmtAgentTrap-3072": mngmtAgentTrap_3072,
       "mngmtAgentTrap-3075": mngmtAgentTrap_3075,
       "mngmtAgentTrap-3076": mngmtAgentTrap_3076,
       "mngmtAgentTrap-3077": mngmtAgentTrap_3077,
       "mngmtAgentTrap-3078": mngmtAgentTrap_3078,
       "mngmtAgentTrap-3079": mngmtAgentTrap_3079,
       "mngmtAgentTrap-3080": mngmtAgentTrap_3080,
       "mngmtAgentTrap-3081": mngmtAgentTrap_3081,
       "mngmtAgentTrap-3083": mngmtAgentTrap_3083,
       "mngmtAgentTrap-3084": mngmtAgentTrap_3084,
       "mngmtAgentTrap-3086": mngmtAgentTrap_3086,
       "mngmtAgentTrap-3090": mngmtAgentTrap_3090,
       "mngmtAgentTrap-3091": mngmtAgentTrap_3091,
       "mngmtAgentTrap-3092": mngmtAgentTrap_3092,
       "mngmtAgentTrap-3094": mngmtAgentTrap_3094,
       "mngmtAgentTrap-3095": mngmtAgentTrap_3095,
       "mngmtAgentTrap-4000": mngmtAgentTrap_4000,
       "mngmtAgentTrap-4001": mngmtAgentTrap_4001,
       "mngmtAgentTrap-4004": mngmtAgentTrap_4004,
       "mngmtAgentTrap-4005": mngmtAgentTrap_4005,
       "mngmtAgentTrap-4007": mngmtAgentTrap_4007,
       "mngmtAgentTrap-4011": mngmtAgentTrap_4011,
       "mngmtAgentTrap-4012": mngmtAgentTrap_4012,
       "mngmtAgentTrap-4013": mngmtAgentTrap_4013,
       "mngmtAgentTrap-4014": mngmtAgentTrap_4014,
       "mngmtAgentTrap-4015": mngmtAgentTrap_4015,
       "mngmtAgentTrap-4016": mngmtAgentTrap_4016,
       "mngmtAgentTrap-4017": mngmtAgentTrap_4017,
       "mngmtAgentTrap-4018": mngmtAgentTrap_4018,
       "mngmtAgentTrap-4020": mngmtAgentTrap_4020,
       "mngmtAgentTrap-4021": mngmtAgentTrap_4021,
       "mngmtAgentTrap-4023": mngmtAgentTrap_4023,
       "mngmtAgentTrap-4024": mngmtAgentTrap_4024,
       "mngmtAgentTrap-4025": mngmtAgentTrap_4025,
       "mngmtAgentTrap-4027": mngmtAgentTrap_4027,
       "mngmtAgentTrap-4028": mngmtAgentTrap_4028,
       "mngmtAgentTrap-4029": mngmtAgentTrap_4029,
       "mngmtAgentTrap-4030": mngmtAgentTrap_4030,
       "mngmtAgentTrap-4031": mngmtAgentTrap_4031,
       "mngmtAgentTrap-4032": mngmtAgentTrap_4032,
       "mngmtAgentTrap-4033": mngmtAgentTrap_4033,
       "mngmtAgentTrap-4034": mngmtAgentTrap_4034,
       "mngmtAgentTrap-4035": mngmtAgentTrap_4035,
       "mngmtAgentTrap-4036": mngmtAgentTrap_4036,
       "mngmtAgentTrap-4037": mngmtAgentTrap_4037,
       "mngmtAgentTrap-4040": mngmtAgentTrap_4040,
       "mngmtAgentTrap-4041": mngmtAgentTrap_4041,
       "mngmtAgentTrap-4042": mngmtAgentTrap_4042,
       "mngmtAgentTrap-4043": mngmtAgentTrap_4043,
       "mngmtAgentTrap-4047": mngmtAgentTrap_4047,
       "mngmtAgentTrap-4048": mngmtAgentTrap_4048,
       "mngmtAgentTrap-4049": mngmtAgentTrap_4049,
       "mngmtAgentTrap-4050": mngmtAgentTrap_4050,
       "mngmtAgentTrap-4051": mngmtAgentTrap_4051,
       "mngmtAgentTrap-4052": mngmtAgentTrap_4052,
       "mngmtAgentTrap-4053": mngmtAgentTrap_4053,
       "mngmtAgentTrap-4054": mngmtAgentTrap_4054,
       "mngmtAgentTrap-4058": mngmtAgentTrap_4058,
       "mngmtAgentTrap-4059": mngmtAgentTrap_4059,
       "mngmtAgentTrap-5001": mngmtAgentTrap_5001,
       "mngmtAgentTrap-5002": mngmtAgentTrap_5002,
       "mngmtAgentTrap-5003": mngmtAgentTrap_5003,
       "mngmtAgentTrap-5004": mngmtAgentTrap_5004,
       "mngmtAgentTrap-5005": mngmtAgentTrap_5005,
       "mngmtAgentTrap-5006": mngmtAgentTrap_5006,
       "mngmtAgentTrap-5007": mngmtAgentTrap_5007,
       "mngmtAgentTrap-5008": mngmtAgentTrap_5008,
       "mngmtAgentTrap-5010": mngmtAgentTrap_5010,
       "mngmtAgentTrap-5011": mngmtAgentTrap_5011,
       "mngmtAgentTrap-5012": mngmtAgentTrap_5012,
       "mngmtAgentTrap-5013": mngmtAgentTrap_5013,
       "mngmtAgentTrap-5014": mngmtAgentTrap_5014,
       "mngmtAgentTrap-5015": mngmtAgentTrap_5015,
       "mngmtAgentTrap-5016": mngmtAgentTrap_5016,
       "mngmtAgentTrap-5017": mngmtAgentTrap_5017,
       "mngmtAgentTrap-5018": mngmtAgentTrap_5018,
       "mngmtAgentTrap-5019": mngmtAgentTrap_5019,
       "mngmtAgentTrap-6001": mngmtAgentTrap_6001,
       "mngmtAgentTrap-6002": mngmtAgentTrap_6002,
       "mngmtAgentTrap-6003": mngmtAgentTrap_6003,
       "mngmtAgentTrap-6004": mngmtAgentTrap_6004,
       "mngmtAgentTrap-6005": mngmtAgentTrap_6005,
       "mngmtAgentTrap-6006": mngmtAgentTrap_6006,
       "mngmtAgentTrap-6007": mngmtAgentTrap_6007,
       "mngmtAgentTrap-6008": mngmtAgentTrap_6008,
       "mngmtAgentTrap-6009": mngmtAgentTrap_6009,
       "mngmtAgentTrap-6010": mngmtAgentTrap_6010,
       "mngmtAgentTrap-6011": mngmtAgentTrap_6011,
       "mngmtAgentTrap-6012": mngmtAgentTrap_6012,
       "mngmtAgentTrap-6013": mngmtAgentTrap_6013,
       "mngmtAgentTrap-6014": mngmtAgentTrap_6014,
       "mngmtAgentTrap-6015": mngmtAgentTrap_6015,
       "mngmtAgentTrap-6016": mngmtAgentTrap_6016,
       "mngmtAgentTrap-6017": mngmtAgentTrap_6017,
       "mngmtAgentTrap-6018": mngmtAgentTrap_6018,
       "mngmtAgentTrap-6019": mngmtAgentTrap_6019,
       "mngmtAgentTrap-6020": mngmtAgentTrap_6020,
       "mngmtAgentTrap-6021": mngmtAgentTrap_6021,
       "mngmtAgentTrap-6022": mngmtAgentTrap_6022,
       "mngmtAgentTrap-6023": mngmtAgentTrap_6023,
       "mngmtAgentTrap-6024": mngmtAgentTrap_6024,
       "mngmtAgentTrap-6025": mngmtAgentTrap_6025,
       "mngmtAgentTrap-6026": mngmtAgentTrap_6026,
       "mngmtAgentTrap-6027": mngmtAgentTrap_6027,
       "mngmtAgentTrap-6028": mngmtAgentTrap_6028,
       "mngmtAgentTrap-6029": mngmtAgentTrap_6029,
       "mngmtAgentTrap-6030": mngmtAgentTrap_6030,
       "mngmtAgentTrap-6031": mngmtAgentTrap_6031,
       "mngmtAgentTrap-6032": mngmtAgentTrap_6032,
       "mngmtAgentTrap-6033": mngmtAgentTrap_6033,
       "mngmtAgentTrap-6034": mngmtAgentTrap_6034,
       "mngmtAgentTrap-6035": mngmtAgentTrap_6035,
       "mngmtAgentTrap-6036": mngmtAgentTrap_6036,
       "mngmtAgentTrap-6037": mngmtAgentTrap_6037,
       "mngmtAgentTrap-6038": mngmtAgentTrap_6038,
       "mngmtAgentTrap-8001": mngmtAgentTrap_8001,
       "mngmtAgentTrap-8002": mngmtAgentTrap_8002,
       "mngmtAgentTrap-8003": mngmtAgentTrap_8003,
       "mngmtAgentTrap-8004": mngmtAgentTrap_8004,
       "mngmtAgentTrap-8005": mngmtAgentTrap_8005,
       "mngmtAgentTrap-8006": mngmtAgentTrap_8006,
       "mngmtAgentTrap-8007": mngmtAgentTrap_8007,
       "mngmtAgentTrap-8008": mngmtAgentTrap_8008,
       "mngmtAgentTrap-8009": mngmtAgentTrap_8009,
       "mngmtAgentTrap-8010": mngmtAgentTrap_8010,
       "mngmtAgentTrap-8011": mngmtAgentTrap_8011,
       "mngmtAgentTrap-8012": mngmtAgentTrap_8012,
       "mngmtAgentTrap-8013": mngmtAgentTrap_8013,
       "mngmtAgentTrap-8014": mngmtAgentTrap_8014,
       "mngmtAgentTrap-8015": mngmtAgentTrap_8015,
       "mngmtAgentTrap-8016": mngmtAgentTrap_8016,
       "mngmtAgentTrap-8017": mngmtAgentTrap_8017,
       "mngmtAgentTrap-8018": mngmtAgentTrap_8018,
       "mngmtAgentTrap-8019": mngmtAgentTrap_8019,
       "mngmtAgentTrap-8020": mngmtAgentTrap_8020,
       "mngmtAgentTrap-8021": mngmtAgentTrap_8021,
       "mngmtAgentTrap-8022": mngmtAgentTrap_8022,
       "mngmtAgentTrap-8023": mngmtAgentTrap_8023,
       "mngmtAgentTrap-8024": mngmtAgentTrap_8024,
       "mngmtAgentTrap-8025": mngmtAgentTrap_8025,
       "mngmtAgentTrap-8026": mngmtAgentTrap_8026,
       "mngmtAgentTrap-8027": mngmtAgentTrap_8027,
       "mngmtAgentTrap-8028": mngmtAgentTrap_8028,
       "mngmtAgentTrap-8029": mngmtAgentTrap_8029,
       "mngmtAgentTrap-8030": mngmtAgentTrap_8030,
       "mngmtAgentTrap-8031": mngmtAgentTrap_8031,
       "mngmtAgentTrap-8032": mngmtAgentTrap_8032,
       "mngmtAgentTrap-8033": mngmtAgentTrap_8033,
       "mngmtAgentTrap-8034": mngmtAgentTrap_8034,
       "mngmtAgentTrap-8035": mngmtAgentTrap_8035,
       "mngmtAgentTrap-8036": mngmtAgentTrap_8036,
       "mngmtAgentTrap-8037": mngmtAgentTrap_8037,
       "mngmtAgentTrap-8038": mngmtAgentTrap_8038,
       "mngmtAgentTrap-8039": mngmtAgentTrap_8039,
       "mngmtAgentTrap-8040": mngmtAgentTrap_8040,
       "mngmtAgentTrap-8041": mngmtAgentTrap_8041,
       "mngmtAgentTrap-8042": mngmtAgentTrap_8042,
       "mngmtAgentTrap-8043": mngmtAgentTrap_8043,
       "mngmtAgentTrap-8044": mngmtAgentTrap_8044,
       "mngmtAgentTrap-8045": mngmtAgentTrap_8045,
       "mngmtAgentTrap-8046": mngmtAgentTrap_8046,
       "mngmtAgentTrap-8047": mngmtAgentTrap_8047,
       "mngmtAgentTrap-8048": mngmtAgentTrap_8048,
       "mngmtAgentTrap-8049": mngmtAgentTrap_8049,
       "mngmtAgentTrap-8050": mngmtAgentTrap_8050,
       "mngmtAgentTrap-8051": mngmtAgentTrap_8051,
       "mngmtAgentTrap-8052": mngmtAgentTrap_8052,
       "mngmtAgentTrap-8053": mngmtAgentTrap_8053,
       "mngmtAgentTrap-8054": mngmtAgentTrap_8054,
       "mngmtAgentTrap-8055": mngmtAgentTrap_8055,
       "mngmtAgentTrap-8056": mngmtAgentTrap_8056,
       "mngmtAgentTrap-8057": mngmtAgentTrap_8057,
       "mngmtAgentTrap-8058": mngmtAgentTrap_8058,
       "mngmtAgentTrap-8059": mngmtAgentTrap_8059,
       "mngmtAgentTrap-8060": mngmtAgentTrap_8060,
       "mngmtAgentTrap-8061": mngmtAgentTrap_8061,
       "mngmtAgentTrap-8062": mngmtAgentTrap_8062,
       "mngmtAgentTrap-8063": mngmtAgentTrap_8063,
       "mngmtAgentTrap-8064": mngmtAgentTrap_8064,
       "mngmtAgentTrap-8065": mngmtAgentTrap_8065,
       "mngmtAgentTrap-8066": mngmtAgentTrap_8066,
       "mngmtAgentTrap-8067": mngmtAgentTrap_8067,
       "mngmtAgentTrap-8068": mngmtAgentTrap_8068,
       "mngmtAgentTrap-8069": mngmtAgentTrap_8069,
       "mngmtAgentTrap-8070": mngmtAgentTrap_8070,
       "mngmtAgentTrap-8071": mngmtAgentTrap_8071,
       "mngmtAgentTrap-8073": mngmtAgentTrap_8073,
       "mngmtAgentTrap-8074": mngmtAgentTrap_8074,
       "mngmtAgentTrap-8075": mngmtAgentTrap_8075,
       "mngmtAgentTrap-8076": mngmtAgentTrap_8076,
       "mngmtAgentTrap-8077": mngmtAgentTrap_8077,
       "mngmtAgentTrap-8078": mngmtAgentTrap_8078,
       "mngmtAgentTrap-8079": mngmtAgentTrap_8079,
       "mngmtAgentTrap-8080": mngmtAgentTrap_8080,
       "mngmtAgentTrap-8081": mngmtAgentTrap_8081,
       "mngmtAgentTrap-8082": mngmtAgentTrap_8082,
       "mngmtAgentTrap-8083": mngmtAgentTrap_8083,
       "mngmtAgentTrap-8084": mngmtAgentTrap_8084,
       "mngmtAgentTrap-8085": mngmtAgentTrap_8085,
       "mngmtAgentTrap-8086": mngmtAgentTrap_8086,
       "mngmtAgentTrap-8087": mngmtAgentTrap_8087,
       "mngmtAgentTrap-8088": mngmtAgentTrap_8088,
       "mngmtAgentTrap-8089": mngmtAgentTrap_8089,
       "mngmtAgentTrap-8090": mngmtAgentTrap_8090,
       "mngmtAgentTrap-8091": mngmtAgentTrap_8091,
       "mngmtAgentTrap-8092": mngmtAgentTrap_8092,
       "mngmtAgentTrap-8093": mngmtAgentTrap_8093,
       "mngmtAgentTrap-8094": mngmtAgentTrap_8094,
       "mngmtAgentTrap-8095": mngmtAgentTrap_8095,
       "mngmtAgentTrap-9001": mngmtAgentTrap_9001,
       "mngmtAgentTrap-9002": mngmtAgentTrap_9002,
       "mngmtAgentTrap-9003": mngmtAgentTrap_9003,
       "mngmtAgentTrap-9004": mngmtAgentTrap_9004,
       "mngmtAgentTrap-9005": mngmtAgentTrap_9005,
       "mngmtAgentTrap-9006": mngmtAgentTrap_9006,
       "mngmtAgentTrap-9007": mngmtAgentTrap_9007,
       "mngmtAgentTrap-9008": mngmtAgentTrap_9008,
       "mngmtAgentTrap-9009": mngmtAgentTrap_9009,
       "mngmtAgentTrap-9010": mngmtAgentTrap_9010,
       "mngmtAgentTrap-9011": mngmtAgentTrap_9011,
       "mngmtAgentTrap-9012": mngmtAgentTrap_9012,
       "mngmtAgentTrap-9013": mngmtAgentTrap_9013,
       "mngmtAgentTrap-9014": mngmtAgentTrap_9014,
       "mngmtAgentTrap-9015": mngmtAgentTrap_9015,
       "mngmtAgentTrap-9016": mngmtAgentTrap_9016,
       "mngmtAgentTrap-9017": mngmtAgentTrap_9017,
       "mngmtAgentTrap-9018": mngmtAgentTrap_9018,
       "mngmtAgentTrap-9019": mngmtAgentTrap_9019,
       "mngmtAgentTrap-9020": mngmtAgentTrap_9020,
       "mngmtAgentTrap-9021": mngmtAgentTrap_9021,
       "mngmtAgentTrap-9022": mngmtAgentTrap_9022,
       "mngmtAgentTrap-9023": mngmtAgentTrap_9023,
       "mngmtAgentTrap-9025": mngmtAgentTrap_9025,
       "mngmtAgentTrap-9026": mngmtAgentTrap_9026,
       "mngmtAgentTrap-9027": mngmtAgentTrap_9027,
       "mngmtAgentTrap-9028": mngmtAgentTrap_9028,
       "mngmtAgentTrap-9029": mngmtAgentTrap_9029,
       "mngmtAgentTrap-9030": mngmtAgentTrap_9030,
       "mngmtAgentTrap-9031": mngmtAgentTrap_9031,
       "mngmtAgentTrap-9032": mngmtAgentTrap_9032,
       "mngmtAgentTrap-9033": mngmtAgentTrap_9033,
       "mngmtAgentTrap-9034": mngmtAgentTrap_9034,
       "mngmtAgentTrap-9035": mngmtAgentTrap_9035,
       "mngmtAgentTrap-9036": mngmtAgentTrap_9036,
       "mngmtAgentTrap-9037": mngmtAgentTrap_9037,
       "mngmtAgentTrap-9038": mngmtAgentTrap_9038,
       "mngmtAgentTrap-9039": mngmtAgentTrap_9039,
       "mngmtAgentTrap-9040": mngmtAgentTrap_9040,
       "mngmtAgentTrap-9041": mngmtAgentTrap_9041,
       "mngmtAgentTrap-9042": mngmtAgentTrap_9042,
       "mngmtAgentTrap-10001": mngmtAgentTrap_10001,
       "mngmtAgentTrap-10004": mngmtAgentTrap_10004,
       "mngmtAgentTrap-10006": mngmtAgentTrap_10006,
       "mngmtAgentTrap-10010": mngmtAgentTrap_10010,
       "mngmtAgentTrap-10011": mngmtAgentTrap_10011,
       "mngmtAgentTrap-10012": mngmtAgentTrap_10012,
       "mngmtAgentTrap-10013": mngmtAgentTrap_10013,
       "mngmtAgentTrap-10014": mngmtAgentTrap_10014,
       "mngmtAgentTrap-10015": mngmtAgentTrap_10015,
       "mngmtAgentTrap-10017": mngmtAgentTrap_10017,
       "mngmtAgentTrap-10018": mngmtAgentTrap_10018,
       "mngmtAgentTrap-10019": mngmtAgentTrap_10019,
       "mngmtAgentTrap-10020": mngmtAgentTrap_10020,
       "mngmtAgentTrap-10021": mngmtAgentTrap_10021,
       "mngmtAgentTrap-10022": mngmtAgentTrap_10022,
       "mngmtAgentTrap-10023": mngmtAgentTrap_10023,
       "mngmtAgentTrap-10024": mngmtAgentTrap_10024,
       "mngmtAgentTrap-10025": mngmtAgentTrap_10025,
       "mngmtAgentTrap-10026": mngmtAgentTrap_10026,
       "mngmtAgentTrap-10027": mngmtAgentTrap_10027,
       "mngmtAgentTrap-10028": mngmtAgentTrap_10028,
       "mngmtAgentTrap-10029": mngmtAgentTrap_10029,
       "mngmtAgentTrap-10030": mngmtAgentTrap_10030,
       "mngmtAgentTrap-10031": mngmtAgentTrap_10031,
       "mngmtAgentTrap-10035": mngmtAgentTrap_10035,
       "mngmtAgentTrap-10036": mngmtAgentTrap_10036,
       "mngmtAgentTrap-10037": mngmtAgentTrap_10037,
       "mngmtAgentTrap-10038": mngmtAgentTrap_10038,
       "mngmtAgentTrap-10039": mngmtAgentTrap_10039,
       "mngmtAgentTrap-10040": mngmtAgentTrap_10040,
       "mngmtAgentTrap-10041": mngmtAgentTrap_10041,
       "mngmtAgentTrap-10042": mngmtAgentTrap_10042,
       "mngmtAgentTrap-10043": mngmtAgentTrap_10043,
       "mngmtAgentTrap-10044": mngmtAgentTrap_10044,
       "mngmtAgentTrap-11001": mngmtAgentTrap_11001,
       "mngmtAgentTrap-11002": mngmtAgentTrap_11002,
       "mngmtAgentTrap-11003": mngmtAgentTrap_11003,
       "mngmtAgentTrap-11004": mngmtAgentTrap_11004,
       "mngmtAgentTrap-12001": mngmtAgentTrap_12001,
       "mngmtAgentTrap-12002": mngmtAgentTrap_12002,
       "mngmtAgentTrap-12003": mngmtAgentTrap_12003,
       "mngmtAgentTrap-12004": mngmtAgentTrap_12004,
       "mngmtAgentTrap-12005": mngmtAgentTrap_12005,
       "mngmtAgentTrap-12008": mngmtAgentTrap_12008,
       "mngmtAgentTrap-13002": mngmtAgentTrap_13002,
       "mngmtAgentTrap-13003": mngmtAgentTrap_13003,
       "mngmtAgentTrap-13004": mngmtAgentTrap_13004,
       "mngmtAgentTrap-13007": mngmtAgentTrap_13007,
       "mngmtAgentTrap-13009": mngmtAgentTrap_13009,
       "mngmtAgentTrap-13012": mngmtAgentTrap_13012,
       "mngmtAgentTrap-13015": mngmtAgentTrap_13015,
       "mngmtAgentTrap-13017": mngmtAgentTrap_13017,
       "mngmtAgentTrap-13018": mngmtAgentTrap_13018,
       "mngmtAgentTrap-13019": mngmtAgentTrap_13019,
       "mngmtAgentTrap-13020": mngmtAgentTrap_13020,
       "mngmtAgentTrap-14001": mngmtAgentTrap_14001,
       "mngmtAgentTrap-14002": mngmtAgentTrap_14002,
       "mngmtAgentTrap-14003": mngmtAgentTrap_14003,
       "mngmtAgentTrap-14004": mngmtAgentTrap_14004,
       "mngmtAgentTrap-14005": mngmtAgentTrap_14005,
       "mngmtAgentTrap-14006": mngmtAgentTrap_14006,
       "mngmtAgentTrap-14007": mngmtAgentTrap_14007,
       "mngmtAgentTrap-14008": mngmtAgentTrap_14008,
       "mngmtAgentTrap-14009": mngmtAgentTrap_14009,
       "mngmtAgentTrap-14010": mngmtAgentTrap_14010,
       "mngmtAgentTrap-14012": mngmtAgentTrap_14012,
       "mngmtAgentTrap-14013": mngmtAgentTrap_14013,
       "mngmtAgentTrap-14017": mngmtAgentTrap_14017,
       "mngmtAgentTrap-15001": mngmtAgentTrap_15001,
       "mngmtAgentTrap-15002": mngmtAgentTrap_15002,
       "mngmtAgentTrap-15003": mngmtAgentTrap_15003,
       "mngmtAgentTrap-15004": mngmtAgentTrap_15004,
       "mngmtAgentTrap-15005": mngmtAgentTrap_15005,
       "mngmtAgentTrap-15006": mngmtAgentTrap_15006,
       "mngmtAgentTrap-15007": mngmtAgentTrap_15007,
       "mngmtAgentTrap-15008": mngmtAgentTrap_15008,
       "mngmtAgentTrap-15009": mngmtAgentTrap_15009,
       "mngmtAgentTrap-16001": mngmtAgentTrap_16001,
       "mngmtAgentTrap-16004": mngmtAgentTrap_16004,
       "mngmtAgentTrap-16005": mngmtAgentTrap_16005,
       "mngmtAgentTrap-16008": mngmtAgentTrap_16008,
       "mngmtAgentTrap-16010": mngmtAgentTrap_16010,
       "mngmtAgentTrap-16012": mngmtAgentTrap_16012,
       "mngmtAgentTrap-16013": mngmtAgentTrap_16013,
       "mngmtAgentTrap-16014": mngmtAgentTrap_16014,
       "mngmtAgentTrap-16015": mngmtAgentTrap_16015,
       "mngmtAgentTrap-16016": mngmtAgentTrap_16016,
       "mngmtAgentTrap-16017": mngmtAgentTrap_16017,
       "mngmtAgentTrap-16018": mngmtAgentTrap_16018,
       "mngmtAgentTrap-16019": mngmtAgentTrap_16019,
       "mngmtAgentTrap-16020": mngmtAgentTrap_16020,
       "mngmtAgentTrap-16021": mngmtAgentTrap_16021,
       "mngmtAgentTrap-16022": mngmtAgentTrap_16022,
       "mngmtAgentTrap-16023": mngmtAgentTrap_16023,
       "mngmtAgentTrap-16024": mngmtAgentTrap_16024,
       "mngmtAgentTrap-16025": mngmtAgentTrap_16025,
       "mngmtAgentTrap-16026": mngmtAgentTrap_16026,
       "mngmtAgentTrap-16027": mngmtAgentTrap_16027,
       "mngmtAgentTrap-16028": mngmtAgentTrap_16028,
       "mngmtAgentTrap-16029": mngmtAgentTrap_16029,
       "mngmtAgentTrap-16030": mngmtAgentTrap_16030,
       "mngmtAgentTrap-16031": mngmtAgentTrap_16031,
       "mngmtAgentTrap-16032": mngmtAgentTrap_16032,
       "mngmtAgentTrap-16033": mngmtAgentTrap_16033,
       "mngmtAgentTrap-16034": mngmtAgentTrap_16034,
       "mngmtAgentTrap-16035": mngmtAgentTrap_16035,
       "mngmtAgentTrap-16036": mngmtAgentTrap_16036,
       "mngmtAgentTrap-16037": mngmtAgentTrap_16037,
       "mngmtAgentTrap-16038": mngmtAgentTrap_16038,
       "mngmtAgentTrap-16039": mngmtAgentTrap_16039,
       "mngmtAgentTrap-16040": mngmtAgentTrap_16040,
       "mngmtAgentTrap-17001": mngmtAgentTrap_17001,
       "mngmtAgentTrap-17002": mngmtAgentTrap_17002,
       "mngmtAgentTrap-17003": mngmtAgentTrap_17003,
       "mngmtAgentTrap-17004": mngmtAgentTrap_17004,
       "mngmtAgentTrap-17005": mngmtAgentTrap_17005,
       "mngmtAgentTrap-17006": mngmtAgentTrap_17006,
       "mngmtAgentTrap-17007": mngmtAgentTrap_17007,
       "mngmtAgentTrap-17008": mngmtAgentTrap_17008,
       "mngmtAgentTrap-17009": mngmtAgentTrap_17009,
       "mngmtAgentTrap-17012": mngmtAgentTrap_17012,
       "mngmtAgentTrap-17013": mngmtAgentTrap_17013,
       "mngmtAgentTrap-17014": mngmtAgentTrap_17014,
       "mngmtAgentTrap-17015": mngmtAgentTrap_17015,
       "mngmtAgentTrap-17016": mngmtAgentTrap_17016,
       "mngmtAgentTrap-17017": mngmtAgentTrap_17017,
       "mngmtAgentTrap-18001": mngmtAgentTrap_18001,
       "mngmtAgentTrap-18002": mngmtAgentTrap_18002,
       "mngmtAgentTrap-18003": mngmtAgentTrap_18003,
       "mngmtAgentTrap-18004": mngmtAgentTrap_18004,
       "mngmtAgentTrap-18005": mngmtAgentTrap_18005,
       "mngmtAgentTrap-18006": mngmtAgentTrap_18006,
       "mngmtAgentTrap-18007": mngmtAgentTrap_18007,
       "mngmtAgentTrap-18008": mngmtAgentTrap_18008,
       "mngmtAgentTrap-18009": mngmtAgentTrap_18009,
       "mngmtAgentTrap-18010": mngmtAgentTrap_18010,
       "mngmtAgentTrap-18018": mngmtAgentTrap_18018,
       "mngmtAgentTrap-18019": mngmtAgentTrap_18019,
       "mngmtAgentTrap-18022": mngmtAgentTrap_18022,
       "mngmtAgentTrap-18024": mngmtAgentTrap_18024,
       "mngmtAgentTrap-18025": mngmtAgentTrap_18025,
       "mngmtAgentTrap-18028": mngmtAgentTrap_18028,
       "mngmtAgentTrap-18034": mngmtAgentTrap_18034,
       "mngmtAgentTrap-18036": mngmtAgentTrap_18036,
       "mngmtAgentTrap-18038": mngmtAgentTrap_18038,
       "mngmtAgentTrap-18039": mngmtAgentTrap_18039,
       "mngmtAgentTrap-18040": mngmtAgentTrap_18040,
       "mngmtAgentTrap-18041": mngmtAgentTrap_18041,
       "mngmtAgentTrap-18042": mngmtAgentTrap_18042,
       "mngmtAgentTrap-18045": mngmtAgentTrap_18045,
       "mngmtAgentTrap-18047": mngmtAgentTrap_18047,
       "mngmtAgentTrap-18048": mngmtAgentTrap_18048,
       "mngmtAgentTrap-18049": mngmtAgentTrap_18049,
       "mngmtAgentTrap-18050": mngmtAgentTrap_18050,
       "mngmtAgentTrap-18051": mngmtAgentTrap_18051,
       "mngmtAgentTrap-18052": mngmtAgentTrap_18052,
       "mngmtAgentTrap-18059": mngmtAgentTrap_18059,
       "mngmtAgentTrap-18060": mngmtAgentTrap_18060,
       "mngmtAgentTrap-18063": mngmtAgentTrap_18063,
       "mngmtAgentTrap-18065": mngmtAgentTrap_18065,
       "mngmtAgentTrap-18066": mngmtAgentTrap_18066,
       "mngmtAgentTrap-18067": mngmtAgentTrap_18067,
       "mngmtAgentTrap-18068": mngmtAgentTrap_18068,
       "mngmtAgentTrap-18070": mngmtAgentTrap_18070,
       "mngmtAgentTrap-18071": mngmtAgentTrap_18071,
       "mngmtAgentTrap-18073": mngmtAgentTrap_18073,
       "mngmtAgentTrap-18074": mngmtAgentTrap_18074,
       "mngmtAgentTrap-18075": mngmtAgentTrap_18075,
       "mngmtAgentTrap-18076": mngmtAgentTrap_18076,
       "mngmtAgentTrap-18080": mngmtAgentTrap_18080,
       "mngmtAgentTrap-18081": mngmtAgentTrap_18081,
       "mngmtAgentTrap-20001": mngmtAgentTrap_20001,
       "mngmtAgentTrap-20002": mngmtAgentTrap_20002,
       "mngmtAgentTrap-20003": mngmtAgentTrap_20003,
       "mngmtAgentTrap-20004": mngmtAgentTrap_20004,
       "mngmtAgentTrap-20005": mngmtAgentTrap_20005,
       "mngmtAgentTrap-20011": mngmtAgentTrap_20011,
       "mngmtAgentTrap-20013": mngmtAgentTrap_20013,
       "mngmtAgentTrap-20015": mngmtAgentTrap_20015,
       "mngmtAgentTrap-20016": mngmtAgentTrap_20016,
       "mngmtAgentTrap-20017": mngmtAgentTrap_20017,
       "mngmtAgentTrap-20018": mngmtAgentTrap_20018,
       "mngmtAgentTrap-20019": mngmtAgentTrap_20019,
       "mngmtAgentTrap-20020": mngmtAgentTrap_20020,
       "mngmtAgentTrap-20021": mngmtAgentTrap_20021,
       "mngmtAgentTrap-20022": mngmtAgentTrap_20022,
       "mngmtAgentTrap-20023": mngmtAgentTrap_20023,
       "mngmtAgentTrap-21001": mngmtAgentTrap_21001,
       "mngmtAgentTrap-21002": mngmtAgentTrap_21002,
       "mngmtAgentTrap-21003": mngmtAgentTrap_21003,
       "mngmtAgentTrap-21004": mngmtAgentTrap_21004,
       "mngmtAgentTrap-21006": mngmtAgentTrap_21006,
       "mngmtAgentTrap-21007": mngmtAgentTrap_21007,
       "mngmtAgentTrap-21008": mngmtAgentTrap_21008,
       "mngmtAgentTrap-21009": mngmtAgentTrap_21009,
       "mngmtAgentTrap-21010": mngmtAgentTrap_21010,
       "mngmtAgentTrap-21011": mngmtAgentTrap_21011,
       "mngmtAgentTrap-21012": mngmtAgentTrap_21012,
       "mngmtAgentTrap-21013": mngmtAgentTrap_21013,
       "mngmtAgentTrap-21014": mngmtAgentTrap_21014,
       "mngmtAgentTrap-21015": mngmtAgentTrap_21015,
       "mngmtAgentTrap-21016": mngmtAgentTrap_21016,
       "mngmtAgentTrap-21017": mngmtAgentTrap_21017,
       "mngmtAgentTrap-21018": mngmtAgentTrap_21018,
       "mngmtAgentTrap-21019": mngmtAgentTrap_21019,
       "mngmtAgentTrap-22001": mngmtAgentTrap_22001,
       "mngmtAgentTrap-22002": mngmtAgentTrap_22002,
       "mngmtAgentTrap-23002": mngmtAgentTrap_23002,
       "mngmtAgentTrap-23003": mngmtAgentTrap_23003,
       "mngmtAgentTrap-24001": mngmtAgentTrap_24001,
       "mngmtAgentTrap-24002": mngmtAgentTrap_24002,
       "mngmtAgentTrap-24003": mngmtAgentTrap_24003,
       "mngmtAgentTrap-24004": mngmtAgentTrap_24004,
       "mngmtAgentTrap-25001": mngmtAgentTrap_25001,
       "mngmtAgentTrap-25002": mngmtAgentTrap_25002,
       "mngmtAgentTrap-25003": mngmtAgentTrap_25003,
       "mngmtAgentTrap-25004": mngmtAgentTrap_25004,
       "mngmtAgentTrap-25005": mngmtAgentTrap_25005,
       "mngmtAgentTrap-25006": mngmtAgentTrap_25006,
       "mngmtAgentTrap-25007": mngmtAgentTrap_25007,
       "mngmtAgentTrap-25008": mngmtAgentTrap_25008,
       "mngmtAgentTrap-25009": mngmtAgentTrap_25009,
       "mngmtAgentTrap-25010": mngmtAgentTrap_25010,
       "mngmtAgentTrap-25011": mngmtAgentTrap_25011,
       "mngmtAgentTrap-25012": mngmtAgentTrap_25012,
       "mngmtAgentTrap-25013": mngmtAgentTrap_25013,
       "mngmtAgentTrap-25014": mngmtAgentTrap_25014,
       "mngmtAgentTrap-25015": mngmtAgentTrap_25015,
       "mngmtAgentTrap-25016": mngmtAgentTrap_25016,
       "mngmtAgentTrap-25017": mngmtAgentTrap_25017,
       "mngmtAgentTrap-25018": mngmtAgentTrap_25018,
       "mngmtAgentTrap-25019": mngmtAgentTrap_25019,
       "mngmtAgentTrap-26002": mngmtAgentTrap_26002,
       "mngmtAgentTrap-26005": mngmtAgentTrap_26005,
       "mngmtAgentTrap-26006": mngmtAgentTrap_26006,
       "mngmtAgentTrap-26007": mngmtAgentTrap_26007,
       "mngmtAgentTrap-26008": mngmtAgentTrap_26008,
       "mngmtAgentTrap-26009": mngmtAgentTrap_26009,
       "mngmtAgentTrap-26010": mngmtAgentTrap_26010,
       "mngmtAgentTrap-26011": mngmtAgentTrap_26011,
       "mngmtAgentTrap-26012": mngmtAgentTrap_26012,
       "mngmtAgentTrap-26013": mngmtAgentTrap_26013,
       "mngmtAgentTrap-26014": mngmtAgentTrap_26014,
       "mngmtAgentTrap-26015": mngmtAgentTrap_26015,
       "mngmtAgentTrap-26016": mngmtAgentTrap_26016,
       "mngmtAgentTrap-26017": mngmtAgentTrap_26017,
       "mngmtAgentTrap-26018": mngmtAgentTrap_26018,
       "mngmtAgentTrap-26019": mngmtAgentTrap_26019,
       "mngmtAgentTrap-27001": mngmtAgentTrap_27001,
       "mngmtAgentTrap-27002": mngmtAgentTrap_27002,
       "mngmtAgentTrap-27003": mngmtAgentTrap_27003,
       "mngmtAgentTrap-27004": mngmtAgentTrap_27004,
       "mngmtAgentTrap-27005": mngmtAgentTrap_27005,
       "mngmtAgentTrap-27006": mngmtAgentTrap_27006,
       "mngmtAgentTrap-27007": mngmtAgentTrap_27007,
       "mngmtAgentTrap-27008": mngmtAgentTrap_27008,
       "mngmtAgentTrap-27009": mngmtAgentTrap_27009,
       "mngmtAgentTrap-27010": mngmtAgentTrap_27010,
       "mngmtAgentTrap-27011": mngmtAgentTrap_27011,
       "mngmtAgentTrap-27012": mngmtAgentTrap_27012,
       "mngmtAgentTrap-27013": mngmtAgentTrap_27013,
       "mngmtAgentTrap-27014": mngmtAgentTrap_27014,
       "mngmtAgentTrap-27015": mngmtAgentTrap_27015,
       "mngmtAgentTrap-27016": mngmtAgentTrap_27016,
       "mngmtAgentTrap-27017": mngmtAgentTrap_27017,
       "mngmtAgentTrap-27018": mngmtAgentTrap_27018,
       "mngmtAgentTrap-27019": mngmtAgentTrap_27019,
       "mngmtAgentTrap-27020": mngmtAgentTrap_27020,
       "mngmtAgentTrap-27021": mngmtAgentTrap_27021,
       "mngmtAgentTrap-27022": mngmtAgentTrap_27022,
       "mngmtAgentTrap-27023": mngmtAgentTrap_27023,
       "mngmtAgentTrap-27024": mngmtAgentTrap_27024,
       "mngmtAgentTrap-27025": mngmtAgentTrap_27025,
       "mngmtAgentTrap-27026": mngmtAgentTrap_27026,
       "mngmtAgentTrap-27027": mngmtAgentTrap_27027,
       "mngmtAgentTrap-27028": mngmtAgentTrap_27028,
       "mngmtAgentTrap-27029": mngmtAgentTrap_27029,
       "mngmtAgentTrap-27030": mngmtAgentTrap_27030,
       "mngmtAgentTrap-27031": mngmtAgentTrap_27031,
       "mngmtAgentTrap-27032": mngmtAgentTrap_27032,
       "mngmtAgentTrap-27033": mngmtAgentTrap_27033,
       "mngmtAgentTrap-27034": mngmtAgentTrap_27034,
       "mngmtAgentTrap-27035": mngmtAgentTrap_27035,
       "mngmtAgentTrap-27036": mngmtAgentTrap_27036,
       "mngmtAgentTrap-27037": mngmtAgentTrap_27037,
       "mngmtAgentTrap-27038": mngmtAgentTrap_27038,
       "mngmtAgentTrap-27039": mngmtAgentTrap_27039,
       "mngmtAgentTrap-27040": mngmtAgentTrap_27040,
       "mngmtAgentTrap-27041": mngmtAgentTrap_27041,
       "mngmtAgentTrap-27042": mngmtAgentTrap_27042,
       "mngmtAgentTrap-27043": mngmtAgentTrap_27043,
       "mngmtAgentTrap-27044": mngmtAgentTrap_27044,
       "mngmtAgentTrap-27045": mngmtAgentTrap_27045,
       "mngmtAgentTrap-27046": mngmtAgentTrap_27046,
       "mngmtAgentTrap-27047": mngmtAgentTrap_27047,
       "mngmtAgentTrap-27048": mngmtAgentTrap_27048,
       "mngmtAgentTrap-27049": mngmtAgentTrap_27049,
       "mngmtAgentTrap-27050": mngmtAgentTrap_27050,
       "mngmtAgentTrap-27051": mngmtAgentTrap_27051,
       "mngmtAgentTrap-27052": mngmtAgentTrap_27052,
       "cpqElementManager": cpqElementManager,
       "cpqHSV": cpqHSV,
       "cpqHSVAgent": cpqHSVAgent,
       "agManufacturer": agManufacturer,
       "agMajVersion": agMajVersion,
       "agMinVersion": agMinVersion,
       "agHostName": agHostName,
       "agEnterprise": agEnterprise,
       "agDescription": agDescription,
       "agStatusTable": agStatusTable,
       "agentEntry": agentEntry,
       "agentEntryIndex": agentEntryIndex,
       "agentStatus": agentStatus,
       "agentEventCode": agentEventCode,
       "agentEventLevel": agentEventLevel,
       "agentEventTimeDate": agentEventTimeDate,
       "agentEventDescription": agentEventDescription,
       "cpqHSVServer": cpqHSVServer,
       "srvCPU": srvCPU,
       "srvComputerType": srvComputerType,
       "srvModel": srvModel,
       "srvSubModel": srvSubModel,
       "srvBiosVersion": srvBiosVersion,
       "srvOS": srvOS,
       "srvOSMajVersion": srvOSMajVersion,
       "srvOSMinVersion": srvOSMinVersion,
       "hsvObject": hsvObject,
       "scell": scell,
       "scellTotal": scellTotal,
       "scellStatusTable": scellStatusTable,
       "scellEntry": scellEntry,
       "scellEntryIndex": scellEntryIndex,
       "scellName": scellName,
       "scellUUID": scellUUID,
       "scellStatus": scellStatus,
       "scellEventDescription": scellEventDescription,
       "scellEventTimeDate": scellEventTimeDate,
       "scellEventCode": scellEventCode,
       "scellSWComponent": scellSWComponent,
       "scellECode": scellECode,
       "scellCAC": scellCAC,
       "scellEIP": scellEIP,
       "scellNameDateTime": scellNameDateTime,
       "agent": agent,
       "host": host,
       "hostTotal": hostTotal,
       "hostStatusTable": hostStatusTable,
       "hostEntry": hostEntry,
       "hostEntryIndex": hostEntryIndex,
       "hostName": hostName,
       "hostUUID": hostUUID,
       "hostStatus": hostStatus,
       "nsc": nsc,
       "nscTotal": nscTotal,
       "nscStatusTable": nscStatusTable,
       "nscEntry": nscEntry,
       "nscEntryIndex": nscEntryIndex,
       "nscName": nscName,
       "nscUUID": nscUUID,
       "nscStatus": nscStatus,
       "shelf": shelf,
       "shelfTotal": shelfTotal,
       "shelfStatusTable": shelfStatusTable,
       "shelfEntry": shelfEntry,
       "shelfEntryIndex": shelfEntryIndex,
       "shelfStatus": shelfStatus,
       "shelfId": shelfId,
       "shelfElementType": shelfElementType,
       "shelfElementNum": shelfElementNum,
       "shelfErrorCode": shelfErrorCode,
       "maHSVMibRev": maHSVMibRev,
       "maHSVMibRevMajor": maHSVMibRevMajor,
       "maHSVMibRevMinor": maHSVMibRevMinor}
)
