# SNMP MIB module (FH800u-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FH800u-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:50 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlliedTelesyn_ObjectIdentity = ObjectIdentity
alliedTelesyn = _AlliedTelesyn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1)
)
_DualHub_ObjectIdentity = ObjectIdentity
dualHub = _DualHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 10)
)
_Fh812u_ObjectIdentity = ObjectIdentity
fh812u = _Fh812u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 10, 1)
)
_Fh824u_ObjectIdentity = ObjectIdentity
fh824u = _Fh824u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 10, 2)
)
_MibObject_ObjectIdentity = ObjectIdentity
mibObject = _MibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8)
)
_RepeaterMib_ObjectIdentity = ObjectIdentity
repeaterMib = _RepeaterMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1)
)
_NewRepeaterMib_ObjectIdentity = ObjectIdentity
newRepeaterMib = _NewRepeaterMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20)
)
_AcctonHubMIB_ObjectIdentity = ObjectIdentity
acctonHubMIB = _AcctonHubMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3)
)
_AtactDualHubMgt_ObjectIdentity = ObjectIdentity
atactDualHubMgt = _AtactDualHubMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11)
)
_Fh800uMgt_ObjectIdentity = ObjectIdentity
fh800uMgt = _Fh800uMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1)
)
_Fh800uBasicCapability_ObjectIdentity = ObjectIdentity
fh800uBasicCapability = _Fh800uBasicCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1)
)
_Fh800uStackInfo_ObjectIdentity = ObjectIdentity
fh800uStackInfo = _Fh800uStackInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 1)
)
_StackInusedIP_Type = IpAddress
_StackInusedIP_Object = MibScalar
stackInusedIP = _StackInusedIP_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 1, 1),
    _StackInusedIP_Type()
)
stackInusedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackInusedIP.setStatus("mandatory")
_StackInusedNetMask_Type = IpAddress
_StackInusedNetMask_Object = MibScalar
stackInusedNetMask = _StackInusedNetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 1, 2),
    _StackInusedNetMask_Type()
)
stackInusedNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackInusedNetMask.setStatus("mandatory")
_StackInusedGateway_Type = IpAddress
_StackInusedGateway_Object = MibScalar
stackInusedGateway = _StackInusedGateway_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 1, 3),
    _StackInusedGateway_Type()
)
stackInusedGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackInusedGateway.setStatus("mandatory")
_StackInusedServerSlipAddr_Type = IpAddress
_StackInusedServerSlipAddr_Object = MibScalar
stackInusedServerSlipAddr = _StackInusedServerSlipAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 1, 4),
    _StackInusedServerSlipAddr_Type()
)
stackInusedServerSlipAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackInusedServerSlipAddr.setStatus("mandatory")
_StackInusedHostSlipAddr_Type = IpAddress
_StackInusedHostSlipAddr_Object = MibScalar
stackInusedHostSlipAddr = _StackInusedHostSlipAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 1, 5),
    _StackInusedHostSlipAddr_Type()
)
stackInusedHostSlipAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackInusedHostSlipAddr.setStatus("mandatory")
_StackInusedBootUpIP_Type = IpAddress
_StackInusedBootUpIP_Object = MibScalar
stackInusedBootUpIP = _StackInusedBootUpIP_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 1, 6),
    _StackInusedBootUpIP_Type()
)
stackInusedBootUpIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackInusedBootUpIP.setStatus("mandatory")
_StackTemporalIP_Type = IpAddress
_StackTemporalIP_Object = MibScalar
stackTemporalIP = _StackTemporalIP_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 1, 7),
    _StackTemporalIP_Type()
)
stackTemporalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackTemporalIP.setStatus("mandatory")
_StackTemporalNetMask_Type = IpAddress
_StackTemporalNetMask_Object = MibScalar
stackTemporalNetMask = _StackTemporalNetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 1, 8),
    _StackTemporalNetMask_Type()
)
stackTemporalNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackTemporalNetMask.setStatus("mandatory")
_StackTemporalGateway_Type = IpAddress
_StackTemporalGateway_Object = MibScalar
stackTemporalGateway = _StackTemporalGateway_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 1, 9),
    _StackTemporalGateway_Type()
)
stackTemporalGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackTemporalGateway.setStatus("mandatory")
_StackTemporalServerSlipAddr_Type = IpAddress
_StackTemporalServerSlipAddr_Object = MibScalar
stackTemporalServerSlipAddr = _StackTemporalServerSlipAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 1, 10),
    _StackTemporalServerSlipAddr_Type()
)
stackTemporalServerSlipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackTemporalServerSlipAddr.setStatus("mandatory")
_StackTemporalHostSlipAddr_Type = IpAddress
_StackTemporalHostSlipAddr_Object = MibScalar
stackTemporalHostSlipAddr = _StackTemporalHostSlipAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 1, 11),
    _StackTemporalHostSlipAddr_Type()
)
stackTemporalHostSlipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackTemporalHostSlipAddr.setStatus("mandatory")
_StackTemporalBootUpIP_Type = IpAddress
_StackTemporalBootUpIP_Object = MibScalar
stackTemporalBootUpIP = _StackTemporalBootUpIP_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 1, 12),
    _StackTemporalBootUpIP_Type()
)
stackTemporalBootUpIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackTemporalBootUpIP.setStatus("mandatory")


class _IpInformationReset_Type(Integer32):
    """Custom type ipInformationReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_IpInformationReset_Type.__name__ = "Integer32"
_IpInformationReset_Object = MibScalar
ipInformationReset = _IpInformationReset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 1, 13),
    _IpInformationReset_Type()
)
ipInformationReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInformationReset.setStatus("mandatory")


class _StackHealthMonitor_Type(OctetString):
    """Custom type stackHealthMonitor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_StackHealthMonitor_Type.__name__ = "OctetString"
_StackHealthMonitor_Object = MibScalar
stackHealthMonitor = _StackHealthMonitor_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 1, 14),
    _StackHealthMonitor_Type()
)
stackHealthMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackHealthMonitor.setStatus("mandatory")
_Fh800uGroupInfo_ObjectIdentity = ObjectIdentity
fh800uGroupInfo = _Fh800uGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2)
)
_GroupTable_Object = MibTable
groupTable = _GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    groupTable.setStatus("mandatory")
_GroupEntry_Object = MibTableRow
groupEntry = _GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1)
)
groupEntry.setIndexNames(
    (0, "FH800u-MIB", "groupID"),
)
if mibBuilder.loadTexts:
    groupEntry.setStatus("mandatory")


class _GroupID_Type(Integer32):
    """Custom type groupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GroupID_Type.__name__ = "Integer32"
_GroupID_Object = MibTableColumn
groupID = _GroupID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 1),
    _GroupID_Type()
)
groupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupID.setStatus("mandatory")


class _GroupType_Type(Integer32):
    """Custom type groupType based on Integer32"""
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
        *(("eh3012a", 4),
          ("eh3024a", 3),
          ("fh812u", 2),
          ("fh824u", 1))
    )


_GroupType_Type.__name__ = "Integer32"
_GroupType_Object = MibTableColumn
groupType = _GroupType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 2),
    _GroupType_Type()
)
groupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupType.setStatus("mandatory")


class _GroupCounterReset_Type(Integer32):
    """Custom type groupCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_GroupCounterReset_Type.__name__ = "Integer32"
_GroupCounterReset_Object = MibTableColumn
groupCounterReset = _GroupCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 3),
    _GroupCounterReset_Type()
)
groupCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupCounterReset.setStatus("mandatory")
_GroupPosition_Type = Integer32
_GroupPosition_Object = MibTableColumn
groupPosition = _GroupPosition_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 4),
    _GroupPosition_Type()
)
groupPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPosition.setStatus("mandatory")
_GroupRptrHwVer_Type = Integer32
_GroupRptrHwVer_Object = MibTableColumn
groupRptrHwVer = _GroupRptrHwVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 5),
    _GroupRptrHwVer_Type()
)
groupRptrHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRptrHwVer.setStatus("mandatory")
_GroupRptrSerialNo_Type = PhysAddress
_GroupRptrSerialNo_Object = MibTableColumn
groupRptrSerialNo = _GroupRptrSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 6),
    _GroupRptrSerialNo_Type()
)
groupRptrSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRptrSerialNo.setStatus("mandatory")
_GroupSysMajorVer_Type = Integer32
_GroupSysMajorVer_Object = MibTableColumn
groupSysMajorVer = _GroupSysMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 7),
    _GroupSysMajorVer_Type()
)
groupSysMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupSysMajorVer.setStatus("mandatory")
_GroupSysMinorVer_Type = Integer32
_GroupSysMinorVer_Object = MibTableColumn
groupSysMinorVer = _GroupSysMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 8),
    _GroupSysMinorVer_Type()
)
groupSysMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupSysMinorVer.setStatus("mandatory")
_GroupPostCodeMajorVer_Type = Integer32
_GroupPostCodeMajorVer_Object = MibTableColumn
groupPostCodeMajorVer = _GroupPostCodeMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 9),
    _GroupPostCodeMajorVer_Type()
)
groupPostCodeMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPostCodeMajorVer.setStatus("mandatory")
_GroupPostCodeMinorVer_Type = Integer32
_GroupPostCodeMinorVer_Object = MibTableColumn
groupPostCodeMinorVer = _GroupPostCodeMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 10),
    _GroupPostCodeMinorVer_Type()
)
groupPostCodeMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPostCodeMinorVer.setStatus("mandatory")


class _GroupAgentStatus_Type(Integer32):
    """Custom type groupAgentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 3),
          ("not-present", 1),
          ("primary", 2))
    )


_GroupAgentStatus_Type.__name__ = "Integer32"
_GroupAgentStatus_Object = MibTableColumn
groupAgentStatus = _GroupAgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 11),
    _GroupAgentStatus_Type()
)
groupAgentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupAgentStatus.setStatus("mandatory")
_GroupAgentHwVer_Type = Integer32
_GroupAgentHwVer_Object = MibTableColumn
groupAgentHwVer = _GroupAgentHwVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 12),
    _GroupAgentHwVer_Type()
)
groupAgentHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupAgentHwVer.setStatus("mandatory")
_GroupAgentSerialNo_Type = PhysAddress
_GroupAgentSerialNo_Object = MibTableColumn
groupAgentSerialNo = _GroupAgentSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 13),
    _GroupAgentSerialNo_Type()
)
groupAgentSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupAgentSerialNo.setStatus("mandatory")
_GroupAgentPhysAddr_Type = PhysAddress
_GroupAgentPhysAddr_Object = MibTableColumn
groupAgentPhysAddr = _GroupAgentPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 14),
    _GroupAgentPhysAddr_Type()
)
groupAgentPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupAgentPhysAddr.setStatus("mandatory")


class _GroupAgentBootupOption_Type(Integer32):
    """Custom type groupAgentBootupOption based on Integer32"""
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
        *(("bootp-download", 4),
          ("bootp-get-ip", 3),
          ("bootp-upgrade", 5),
          ("normal", 1),
          ("tftp-download", 2))
    )


_GroupAgentBootupOption_Type.__name__ = "Integer32"
_GroupAgentBootupOption_Object = MibTableColumn
groupAgentBootupOption = _GroupAgentBootupOption_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 15),
    _GroupAgentBootupOption_Type()
)
groupAgentBootupOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupAgentBootupOption.setStatus("mandatory")


class _GroupAgentBaudrate_Type(Integer32):
    """Custom type groupAgentBaudrate based on Integer32"""
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
        *(("baud-115200", 6),
          ("baud-14400", 2),
          ("baud-19200", 3),
          ("baud-38400", 4),
          ("baud-57600", 5),
          ("baud-9600", 1))
    )


_GroupAgentBaudrate_Type.__name__ = "Integer32"
_GroupAgentBaudrate_Object = MibTableColumn
groupAgentBaudrate = _GroupAgentBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 2, 1, 1, 16),
    _GroupAgentBaudrate_Type()
)
groupAgentBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupAgentBaudrate.setStatus("mandatory")
_Fh800uPortInfo_ObjectIdentity = ObjectIdentity
fh800uPortInfo = _Fh800uPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 3)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 3, 1, 1)
)
portEntry.setIndexNames(
    (0, "FH800u-MIB", "portGroupID"),
    (0, "FH800u-MIB", "portID"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")


class _PortGroupID_Type(Integer32):
    """Custom type portGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortGroupID_Type.__name__ = "Integer32"
_PortGroupID_Object = MibTableColumn
portGroupID = _PortGroupID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 3, 1, 1, 1),
    _PortGroupID_Type()
)
portGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupID.setStatus("mandatory")


class _PortID_Type(Integer32):
    """Custom type portID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortID_Type.__name__ = "Integer32"
_PortID_Object = MibTableColumn
portID = _PortID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 3, 1, 1, 2),
    _PortID_Type()
)
portID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portID.setStatus("mandatory")


class _PortSpeed_Type(Integer32):
    """Custom type portSpeed based on Integer32"""
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
        *(("onehundredMbClassI", 2),
          ("onehundredMbClassII", 3),
          ("other", 4),
          ("tenMb", 1))
    )


_PortSpeed_Type.__name__ = "Integer32"
_PortSpeed_Object = MibTableColumn
portSpeed = _PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 3, 1, 1, 3),
    _PortSpeed_Type()
)
portSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSpeed.setStatus("mandatory")


class _PortSpeedConfig_Type(Integer32):
    """Custom type portSpeedConfig based on Integer32"""
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
        *(("autoDetected", 4),
          ("onehundredMbClassI", 2),
          ("onehundredMbClassII", 3),
          ("tenMb", 1))
    )


_PortSpeedConfig_Type.__name__ = "Integer32"
_PortSpeedConfig_Object = MibTableColumn
portSpeedConfig = _PortSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 3, 1, 1, 4),
    _PortSpeedConfig_Type()
)
portSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeedConfig.setStatus("mandatory")


class _PortSegmtID_Type(Integer32):
    """Custom type portSegmtID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortSegmtID_Type.__name__ = "Integer32"
_PortSegmtID_Object = MibTableColumn
portSegmtID = _PortSegmtID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 3, 1, 1, 5),
    _PortSegmtID_Type()
)
portSegmtID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSegmtID.setStatus("mandatory")
_Fh800uSegmentInfo_ObjectIdentity = ObjectIdentity
fh800uSegmentInfo = _Fh800uSegmentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 4)
)
_Fh800uRmonConfig_ObjectIdentity = ObjectIdentity
fh800uRmonConfig = _Fh800uRmonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 5)
)


class _NicAttachSegment_Type(Integer32):
    """Custom type nicAttachSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NicAttachSegment_Type.__name__ = "Integer32"
_NicAttachSegment_Object = MibScalar
nicAttachSegment = _NicAttachSegment_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 5, 1),
    _NicAttachSegment_Type()
)
nicAttachSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicAttachSegment.setStatus("mandatory")


class _FullRmonSegment_Type(Integer32):
    """Custom type fullRmonSegment based on Integer32"""
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


_FullRmonSegment_Type.__name__ = "Integer32"
_FullRmonSegment_Object = MibScalar
fullRmonSegment = _FullRmonSegment_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 5, 2),
    _FullRmonSegment_Type()
)
fullRmonSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fullRmonSegment.setStatus("mandatory")
_RmonConfigTable_Object = MibTable
rmonConfigTable = _RmonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    rmonConfigTable.setStatus("mandatory")
_RmonConfigEntry_Object = MibTableRow
rmonConfigEntry = _RmonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 5, 3, 1)
)
rmonConfigEntry.setIndexNames(
    (0, "FH800u-MIB", "rmonConfigSegmtID"),
)
if mibBuilder.loadTexts:
    rmonConfigEntry.setStatus("mandatory")


class _RmonConfigSegmtID_Type(Integer32):
    """Custom type rmonConfigSegmtID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmonConfigSegmtID_Type.__name__ = "Integer32"
_RmonConfigSegmtID_Object = MibTableColumn
rmonConfigSegmtID = _RmonConfigSegmtID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 5, 3, 1, 1),
    _RmonConfigSegmtID_Type()
)
rmonConfigSegmtID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonConfigSegmtID.setStatus("mandatory")


class _RmonConfigStatus_Type(Integer32):
    """Custom type rmonConfigStatus based on Integer32"""
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


_RmonConfigStatus_Type.__name__ = "Integer32"
_RmonConfigStatus_Object = MibTableColumn
rmonConfigStatus = _RmonConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 1, 5, 3, 1, 2),
    _RmonConfigStatus_Type()
)
rmonConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonConfigStatus.setStatus("mandatory")
_Fh800uPerfMonCapability_ObjectIdentity = ObjectIdentity
fh800uPerfMonCapability = _Fh800uPerfMonCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 2)
)
_Fh800uPerfMonSegmentInfo_ObjectIdentity = ObjectIdentity
fh800uPerfMonSegmentInfo = _Fh800uPerfMonSegmentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 2, 3)
)
_PerfMonSegmentTable_Object = MibTable
perfMonSegmentTable = _PerfMonSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    perfMonSegmentTable.setStatus("optional")
_PerfMonSegmentEntry_Object = MibTableRow
perfMonSegmentEntry = _PerfMonSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 2, 3, 1, 1)
)
perfMonSegmentEntry.setIndexNames(
    (0, "FH800u-MIB", "segmentPerfID"),
)
if mibBuilder.loadTexts:
    perfMonSegmentEntry.setStatus("mandatory")


class _SegmentPerfID_Type(Integer32):
    """Custom type segmentPerfID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SegmentPerfID_Type.__name__ = "Integer32"
_SegmentPerfID_Object = MibTableColumn
segmentPerfID = _SegmentPerfID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 2, 3, 1, 1, 1),
    _SegmentPerfID_Type()
)
segmentPerfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentPerfID.setStatus("mandatory")
_SegmentCRCErrors_Type = Counter32
_SegmentCRCErrors_Object = MibTableColumn
segmentCRCErrors = _SegmentCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 2, 3, 1, 1, 2),
    _SegmentCRCErrors_Type()
)
segmentCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentCRCErrors.setStatus("mandatory")
_SegmentAlignmentErrors_Type = Counter32
_SegmentAlignmentErrors_Object = MibTableColumn
segmentAlignmentErrors = _SegmentAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 2, 3, 1, 1, 3),
    _SegmentAlignmentErrors_Type()
)
segmentAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentAlignmentErrors.setStatus("mandatory")
_SegmentCollisions_Type = Counter32
_SegmentCollisions_Object = MibTableColumn
segmentCollisions = _SegmentCollisions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 2, 3, 1, 1, 4),
    _SegmentCollisions_Type()
)
segmentCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentCollisions.setStatus("mandatory")
_SegmentTotalPortIsolates_Type = Counter32
_SegmentTotalPortIsolates_Object = MibTableColumn
segmentTotalPortIsolates = _SegmentTotalPortIsolates_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 2, 3, 1, 1, 5),
    _SegmentTotalPortIsolates_Type()
)
segmentTotalPortIsolates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentTotalPortIsolates.setStatus("mandatory")
_SegmentSymbolErrors_Type = Counter32
_SegmentSymbolErrors_Object = MibTableColumn
segmentSymbolErrors = _SegmentSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 2, 3, 1, 1, 6),
    _SegmentSymbolErrors_Type()
)
segmentSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentSymbolErrors.setStatus("mandatory")
_Fh800uSwitchCapability_ObjectIdentity = ObjectIdentity
fh800uSwitchCapability = _Fh800uSwitchCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3)
)
_Fh800uSwitchStatsInfo_ObjectIdentity = ObjectIdentity
fh800uSwitchStatsInfo = _Fh800uSwitchStatsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1)
)
_SwitchPortStatsTable_Object = MibTable
switchPortStatsTable = _SwitchPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    switchPortStatsTable.setStatus("mandatory")
_SwitchPortStatsEntry_Object = MibTableRow
switchPortStatsEntry = _SwitchPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1)
)
switchPortStatsEntry.setIndexNames(
    (0, "FH800u-MIB", "switchPortStatsGroupID"),
    (0, "FH800u-MIB", "switchPortStatsID"),
)
if mibBuilder.loadTexts:
    switchPortStatsEntry.setStatus("mandatory")
_SwitchPortStatsGroupID_Type = Integer32
_SwitchPortStatsGroupID_Object = MibTableColumn
switchPortStatsGroupID = _SwitchPortStatsGroupID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1, 1),
    _SwitchPortStatsGroupID_Type()
)
switchPortStatsGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortStatsGroupID.setStatus("mandatory")


class _SwitchPortStatsID_Type(Integer32):
    """Custom type switchPortStatsID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SwitchPortStatsID_Type.__name__ = "Integer32"
_SwitchPortStatsID_Object = MibTableColumn
switchPortStatsID = _SwitchPortStatsID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1, 2),
    _SwitchPortStatsID_Type()
)
switchPortStatsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortStatsID.setStatus("mandatory")
_SwitchPortReadableFrames_Type = Counter32
_SwitchPortReadableFrames_Object = MibTableColumn
switchPortReadableFrames = _SwitchPortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1, 3),
    _SwitchPortReadableFrames_Type()
)
switchPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortReadableFrames.setStatus("mandatory")
_SwitchPortReadableOctets_Type = Counter32
_SwitchPortReadableOctets_Object = MibTableColumn
switchPortReadableOctets = _SwitchPortReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1, 4),
    _SwitchPortReadableOctets_Type()
)
switchPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortReadableOctets.setStatus("mandatory")
_SwitchPortFCSErrors_Type = Counter32
_SwitchPortFCSErrors_Object = MibTableColumn
switchPortFCSErrors = _SwitchPortFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1, 5),
    _SwitchPortFCSErrors_Type()
)
switchPortFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortFCSErrors.setStatus("mandatory")
_SwitchPortAlignmentErrors_Type = Counter32
_SwitchPortAlignmentErrors_Object = MibTableColumn
switchPortAlignmentErrors = _SwitchPortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1, 6),
    _SwitchPortAlignmentErrors_Type()
)
switchPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortAlignmentErrors.setStatus("mandatory")
_SwitchPortFramesTooLong_Type = Counter32
_SwitchPortFramesTooLong_Object = MibTableColumn
switchPortFramesTooLong = _SwitchPortFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1, 7),
    _SwitchPortFramesTooLong_Type()
)
switchPortFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortFramesTooLong.setStatus("mandatory")
_SwitchPortShortEvents_Type = Counter32
_SwitchPortShortEvents_Object = MibTableColumn
switchPortShortEvents = _SwitchPortShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1, 8),
    _SwitchPortShortEvents_Type()
)
switchPortShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortShortEvents.setStatus("mandatory")
_SwitchPortRunts_Type = Counter32
_SwitchPortRunts_Object = MibTableColumn
switchPortRunts = _SwitchPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1, 9),
    _SwitchPortRunts_Type()
)
switchPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortRunts.setStatus("mandatory")
_SwitchPortCollisions_Type = Counter32
_SwitchPortCollisions_Object = MibTableColumn
switchPortCollisions = _SwitchPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1, 10),
    _SwitchPortCollisions_Type()
)
switchPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortCollisions.setStatus("mandatory")
_SwitchPortLateEvents_Type = Counter32
_SwitchPortLateEvents_Object = MibTableColumn
switchPortLateEvents = _SwitchPortLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1, 11),
    _SwitchPortLateEvents_Type()
)
switchPortLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortLateEvents.setStatus("mandatory")
_SwitchPortVeryLongEvents_Type = Counter32
_SwitchPortVeryLongEvents_Object = MibTableColumn
switchPortVeryLongEvents = _SwitchPortVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1, 12),
    _SwitchPortVeryLongEvents_Type()
)
switchPortVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortVeryLongEvents.setStatus("mandatory")
_SwitchPortDataRateMismatches_Type = Counter32
_SwitchPortDataRateMismatches_Object = MibTableColumn
switchPortDataRateMismatches = _SwitchPortDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1, 13),
    _SwitchPortDataRateMismatches_Type()
)
switchPortDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortDataRateMismatches.setStatus("mandatory")
_SwitchPortBroadcastPackets_Type = Counter32
_SwitchPortBroadcastPackets_Object = MibTableColumn
switchPortBroadcastPackets = _SwitchPortBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1, 14),
    _SwitchPortBroadcastPackets_Type()
)
switchPortBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortBroadcastPackets.setStatus("mandatory")
_SwitchPortMulticastPackets_Type = Counter32
_SwitchPortMulticastPackets_Object = MibTableColumn
switchPortMulticastPackets = _SwitchPortMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 3, 1, 1, 1, 15),
    _SwitchPortMulticastPackets_Type()
)
switchPortMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortMulticastPackets.setStatus("mandatory")
_Fh800uSecurityCapability_ObjectIdentity = ObjectIdentity
fh800uSecurityCapability = _Fh800uSecurityCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 5)
)
_Fh800uSecurityInfo_ObjectIdentity = ObjectIdentity
fh800uSecurityInfo = _Fh800uSecurityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 5, 3)
)
_SecurityPortTable_Object = MibTable
securityPortTable = _SecurityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    securityPortTable.setStatus("mandatory")
_SecurityPortEntry_Object = MibTableRow
securityPortEntry = _SecurityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 5, 3, 3, 1)
)
securityPortEntry.setIndexNames(
    (0, "FH800u-MIB", "securityPortGroupID"),
    (0, "FH800u-MIB", "securityPortID"),
)
if mibBuilder.loadTexts:
    securityPortEntry.setStatus("mandatory")
_SecurityPortGroupID_Type = Integer32
_SecurityPortGroupID_Object = MibTableColumn
securityPortGroupID = _SecurityPortGroupID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 5, 3, 3, 1, 1),
    _SecurityPortGroupID_Type()
)
securityPortGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityPortGroupID.setStatus("mandatory")
_SecurityPortID_Type = Integer32
_SecurityPortID_Object = MibTableColumn
securityPortID = _SecurityPortID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 5, 3, 3, 1, 2),
    _SecurityPortID_Type()
)
securityPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityPortID.setStatus("mandatory")
_SecurityPortAddr_Type = PhysAddress
_SecurityPortAddr_Object = MibTableColumn
securityPortAddr = _SecurityPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 5, 3, 3, 1, 3),
    _SecurityPortAddr_Type()
)
securityPortAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityPortAddr.setStatus("mandatory")


class _SecurityAutoLearnAction_Type(Integer32):
    """Custom type securityAutoLearnAction based on Integer32"""
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
          ("inactive", 1),
          ("learned", 3))
    )


_SecurityAutoLearnAction_Type.__name__ = "Integer32"
_SecurityAutoLearnAction_Object = MibTableColumn
securityAutoLearnAction = _SecurityAutoLearnAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 5, 3, 3, 1, 5),
    _SecurityAutoLearnAction_Type()
)
securityAutoLearnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityAutoLearnAction.setStatus("mandatory")


class _SecurityPortIntrusion_Type(Integer32):
    """Custom type securityPortIntrusion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("warning-and-disable", 2))
    )


_SecurityPortIntrusion_Type.__name__ = "Integer32"
_SecurityPortIntrusion_Object = MibTableColumn
securityPortIntrusion = _SecurityPortIntrusion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 1, 5, 3, 3, 1, 6),
    _SecurityPortIntrusion_Type()
)
securityPortIntrusion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityPortIntrusion.setStatus("mandatory")

# Managed Objects groups


# Notification objects

fh800uIntrusionHappen = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 11, 0, 1)
)
fh800uIntrusionHappen.setObjects(
      *(("FH800u-MIB", "securityPortIntrusion"),
        ("FH800u-MIB", "securityPortGroupID"),
        ("FH800u-MIB", "securityPortID"))
)
if mibBuilder.loadTexts:
    fh800uIntrusionHappen.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FH800u-MIB",
    **{"alliedTelesyn": alliedTelesyn,
       "products": products,
       "dualHub": dualHub,
       "fh812u": fh812u,
       "fh824u": fh824u,
       "mibObject": mibObject,
       "repeaterMib": repeaterMib,
       "newRepeaterMib": newRepeaterMib,
       "acctonHubMIB": acctonHubMIB,
       "atactDualHubMgt": atactDualHubMgt,
       "fh800uIntrusionHappen": fh800uIntrusionHappen,
       "fh800uMgt": fh800uMgt,
       "fh800uBasicCapability": fh800uBasicCapability,
       "fh800uStackInfo": fh800uStackInfo,
       "stackInusedIP": stackInusedIP,
       "stackInusedNetMask": stackInusedNetMask,
       "stackInusedGateway": stackInusedGateway,
       "stackInusedServerSlipAddr": stackInusedServerSlipAddr,
       "stackInusedHostSlipAddr": stackInusedHostSlipAddr,
       "stackInusedBootUpIP": stackInusedBootUpIP,
       "stackTemporalIP": stackTemporalIP,
       "stackTemporalNetMask": stackTemporalNetMask,
       "stackTemporalGateway": stackTemporalGateway,
       "stackTemporalServerSlipAddr": stackTemporalServerSlipAddr,
       "stackTemporalHostSlipAddr": stackTemporalHostSlipAddr,
       "stackTemporalBootUpIP": stackTemporalBootUpIP,
       "ipInformationReset": ipInformationReset,
       "stackHealthMonitor": stackHealthMonitor,
       "fh800uGroupInfo": fh800uGroupInfo,
       "groupTable": groupTable,
       "groupEntry": groupEntry,
       "groupID": groupID,
       "groupType": groupType,
       "groupCounterReset": groupCounterReset,
       "groupPosition": groupPosition,
       "groupRptrHwVer": groupRptrHwVer,
       "groupRptrSerialNo": groupRptrSerialNo,
       "groupSysMajorVer": groupSysMajorVer,
       "groupSysMinorVer": groupSysMinorVer,
       "groupPostCodeMajorVer": groupPostCodeMajorVer,
       "groupPostCodeMinorVer": groupPostCodeMinorVer,
       "groupAgentStatus": groupAgentStatus,
       "groupAgentHwVer": groupAgentHwVer,
       "groupAgentSerialNo": groupAgentSerialNo,
       "groupAgentPhysAddr": groupAgentPhysAddr,
       "groupAgentBootupOption": groupAgentBootupOption,
       "groupAgentBaudrate": groupAgentBaudrate,
       "fh800uPortInfo": fh800uPortInfo,
       "portTable": portTable,
       "portEntry": portEntry,
       "portGroupID": portGroupID,
       "portID": portID,
       "portSpeed": portSpeed,
       "portSpeedConfig": portSpeedConfig,
       "portSegmtID": portSegmtID,
       "fh800uSegmentInfo": fh800uSegmentInfo,
       "fh800uRmonConfig": fh800uRmonConfig,
       "nicAttachSegment": nicAttachSegment,
       "fullRmonSegment": fullRmonSegment,
       "rmonConfigTable": rmonConfigTable,
       "rmonConfigEntry": rmonConfigEntry,
       "rmonConfigSegmtID": rmonConfigSegmtID,
       "rmonConfigStatus": rmonConfigStatus,
       "fh800uPerfMonCapability": fh800uPerfMonCapability,
       "fh800uPerfMonSegmentInfo": fh800uPerfMonSegmentInfo,
       "perfMonSegmentTable": perfMonSegmentTable,
       "perfMonSegmentEntry": perfMonSegmentEntry,
       "segmentPerfID": segmentPerfID,
       "segmentCRCErrors": segmentCRCErrors,
       "segmentAlignmentErrors": segmentAlignmentErrors,
       "segmentCollisions": segmentCollisions,
       "segmentTotalPortIsolates": segmentTotalPortIsolates,
       "segmentSymbolErrors": segmentSymbolErrors,
       "fh800uSwitchCapability": fh800uSwitchCapability,
       "fh800uSwitchStatsInfo": fh800uSwitchStatsInfo,
       "switchPortStatsTable": switchPortStatsTable,
       "switchPortStatsEntry": switchPortStatsEntry,
       "switchPortStatsGroupID": switchPortStatsGroupID,
       "switchPortStatsID": switchPortStatsID,
       "switchPortReadableFrames": switchPortReadableFrames,
       "switchPortReadableOctets": switchPortReadableOctets,
       "switchPortFCSErrors": switchPortFCSErrors,
       "switchPortAlignmentErrors": switchPortAlignmentErrors,
       "switchPortFramesTooLong": switchPortFramesTooLong,
       "switchPortShortEvents": switchPortShortEvents,
       "switchPortRunts": switchPortRunts,
       "switchPortCollisions": switchPortCollisions,
       "switchPortLateEvents": switchPortLateEvents,
       "switchPortVeryLongEvents": switchPortVeryLongEvents,
       "switchPortDataRateMismatches": switchPortDataRateMismatches,
       "switchPortBroadcastPackets": switchPortBroadcastPackets,
       "switchPortMulticastPackets": switchPortMulticastPackets,
       "fh800uSecurityCapability": fh800uSecurityCapability,
       "fh800uSecurityInfo": fh800uSecurityInfo,
       "securityPortTable": securityPortTable,
       "securityPortEntry": securityPortEntry,
       "securityPortGroupID": securityPortGroupID,
       "securityPortID": securityPortID,
       "securityPortAddr": securityPortAddr,
       "securityAutoLearnAction": securityAutoLearnAction,
       "securityPortIntrusion": securityPortIntrusion}
)
