# SNMP MIB module (EXPAND-ACCELERATOROS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXPAND-ACCELERATOROS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:10 2024
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

(acceleratorOs,) = mibBuilder.importSymbols(
    "EXPAND-NETWORKS-SMI",
    "acceleratorOs")

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

_AccProductId_Type = ObjectIdentifier
_AccProductId_Object = MibScalar
accProductId = _AccProductId_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 1),
    _AccProductId_Type()
)
accProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accProductId.setStatus("mandatory")
_AccSystem_ObjectIdentity = ObjectIdentity
accSystem = _AccSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3405, 3, 2)
)
_AccSysUpTime_Type = TimeTicks
_AccSysUpTime_Object = MibScalar
accSysUpTime = _AccSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 2, 1),
    _AccSysUpTime_Type()
)
accSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysUpTime.setStatus("mandatory")
_AccSoftwareVersion_Type = OctetString
_AccSoftwareVersion_Object = MibScalar
accSoftwareVersion = _AccSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 2, 2),
    _AccSoftwareVersion_Type()
)
accSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSoftwareVersion.setStatus("mandatory")
_AccSysHostName_Type = OctetString
_AccSysHostName_Object = MibScalar
accSysHostName = _AccSysHostName_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 2, 3),
    _AccSysHostName_Type()
)
accSysHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysHostName.setStatus("mandatory")
_AccSysLocation_Type = OctetString
_AccSysLocation_Object = MibScalar
accSysLocation = _AccSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 2, 4),
    _AccSysLocation_Type()
)
accSysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysLocation.setStatus("mandatory")
_AccSysContact_Type = OctetString
_AccSysContact_Object = MibScalar
accSysContact = _AccSysContact_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 2, 5),
    _AccSysContact_Type()
)
accSysContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysContact.setStatus("mandatory")
_AccSerialNumber_Type = OctetString
_AccSerialNumber_Object = MibScalar
accSerialNumber = _AccSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 2, 6),
    _AccSerialNumber_Type()
)
accSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSerialNumber.setStatus("mandatory")
_AccPerformance_ObjectIdentity = ObjectIdentity
accPerformance = _AccPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3405, 3, 3)
)
_AccHardware_ObjectIdentity = ObjectIdentity
accHardware = _AccHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3405, 3, 3, 1)
)
_AccCpu_ObjectIdentity = ObjectIdentity
accCpu = _AccCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3405, 3, 3, 1, 1)
)
_AccCpuTotalEntries_Type = Integer32
_AccCpuTotalEntries_Object = MibScalar
accCpuTotalEntries = _AccCpuTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 3, 1, 1, 1),
    _AccCpuTotalEntries_Type()
)
accCpuTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCpuTotalEntries.setStatus("mandatory")
_AccCpuTable_Object = MibTable
accCpuTable = _AccCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    accCpuTable.setStatus("mandatory")
_AccCpuEntry_Object = MibTableRow
accCpuEntry = _AccCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 3, 1, 1, 2, 1)
)
accCpuEntry.setIndexNames(
    (0, "EXPAND-ACCELERATOROS-MIB", "accCpuIndex"),
)
if mibBuilder.loadTexts:
    accCpuEntry.setStatus("mandatory")
_AccCpuIndex_Type = Integer32
_AccCpuIndex_Object = MibTableColumn
accCpuIndex = _AccCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 3, 1, 1, 2, 1, 1),
    _AccCpuIndex_Type()
)
accCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCpuIndex.setStatus("mandatory")
_AccCpuDesc_Type = OctetString
_AccCpuDesc_Object = MibTableColumn
accCpuDesc = _AccCpuDesc_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 3, 1, 1, 2, 1, 2),
    _AccCpuDesc_Type()
)
accCpuDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCpuDesc.setStatus("mandatory")


class _AccCpuUtilization_Type(Integer32):
    """Custom type accCpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AccCpuUtilization_Type.__name__ = "Integer32"
_AccCpuUtilization_Object = MibTableColumn
accCpuUtilization = _AccCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 3, 1, 1, 2, 1, 3),
    _AccCpuUtilization_Type()
)
accCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCpuUtilization.setStatus("mandatory")
_AccSoftware_ObjectIdentity = ObjectIdentity
accSoftware = _AccSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3405, 3, 3, 2)
)
_AccBuffer_ObjectIdentity = ObjectIdentity
accBuffer = _AccBuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3405, 3, 3, 2, 1)
)


class _AccSystemWide_Type(Integer32):
    """Custom type accSystemWide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AccSystemWide_Type.__name__ = "Integer32"
_AccSystemWide_Object = MibScalar
accSystemWide = _AccSystemWide_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 3, 2, 1, 1),
    _AccSystemWide_Type()
)
accSystemWide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSystemWide.setStatus("mandatory")
_AccInterfaces_ObjectIdentity = ObjectIdentity
accInterfaces = _AccInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4)
)
_AccInterfaceTotalEntries_Type = Integer32
_AccInterfaceTotalEntries_Object = MibScalar
accInterfaceTotalEntries = _AccInterfaceTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 1),
    _AccInterfaceTotalEntries_Type()
)
accInterfaceTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceTotalEntries.setStatus("mandatory")
_AccInterfaceTable_Object = MibTable
accInterfaceTable = _AccInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2)
)
if mibBuilder.loadTexts:
    accInterfaceTable.setStatus("mandatory")
_AccInterfaceEntry_Object = MibTableRow
accInterfaceEntry = _AccInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1)
)
accInterfaceEntry.setIndexNames(
    (0, "EXPAND-ACCELERATOROS-MIB", "accInterfaceIndex"),
)
if mibBuilder.loadTexts:
    accInterfaceEntry.setStatus("mandatory")
_AccInterfaceIndex_Type = Integer32
_AccInterfaceIndex_Object = MibTableColumn
accInterfaceIndex = _AccInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 1),
    _AccInterfaceIndex_Type()
)
accInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceIndex.setStatus("mandatory")
_AccInterfaceDescription_Type = OctetString
_AccInterfaceDescription_Object = MibTableColumn
accInterfaceDescription = _AccInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 2),
    _AccInterfaceDescription_Type()
)
accInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceDescription.setStatus("mandatory")


class _AccInterfaceEncapsulation_Type(Integer32):
    """Custom type accInterfaceEncapsulation based on Integer32"""
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
        *(("ethernet", 8),
          ("expand-special", 9),
          ("frame-relay-cisco", 5),
          ("frame-relay-ietf", 4),
          ("hdlc-cisco", 3),
          ("lapb-128", 7),
          ("lapb-8", 6),
          ("other", 1),
          ("ppp", 2),
          ("raw-hdlc", 10))
    )


_AccInterfaceEncapsulation_Type.__name__ = "Integer32"
_AccInterfaceEncapsulation_Object = MibTableColumn
accInterfaceEncapsulation = _AccInterfaceEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 3),
    _AccInterfaceEncapsulation_Type()
)
accInterfaceEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceEncapsulation.setStatus("mandatory")
_AccInterfaceFrameRelayDlci_Type = Integer32
_AccInterfaceFrameRelayDlci_Object = MibTableColumn
accInterfaceFrameRelayDlci = _AccInterfaceFrameRelayDlci_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 4),
    _AccInterfaceFrameRelayDlci_Type()
)
accInterfaceFrameRelayDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceFrameRelayDlci.setStatus("mandatory")


class _AccInterfaceType_Type(Integer32):
    """Custom type accInterfaceType based on Integer32"""
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
        *(("cable", 10),
          ("e1", 8),
          ("none", 1),
          ("rs-232", 2),
          ("rs-422", 3),
          ("rs-449", 4),
          ("rs-530", 5),
          ("t1", 9),
          ("v-35", 6),
          ("x-21", 7))
    )


_AccInterfaceType_Type.__name__ = "Integer32"
_AccInterfaceType_Object = MibTableColumn
accInterfaceType = _AccInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 6),
    _AccInterfaceType_Type()
)
accInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceType.setStatus("mandatory")


class _AccInterfaceOperStatus_Type(Integer32):
    """Custom type accInterfaceOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_AccInterfaceOperStatus_Type.__name__ = "Integer32"
_AccInterfaceOperStatus_Object = MibTableColumn
accInterfaceOperStatus = _AccInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 7),
    _AccInterfaceOperStatus_Type()
)
accInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceOperStatus.setStatus("mandatory")


class _AccInterfaceAdminStatus_Type(Integer32):
    """Custom type accInterfaceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_AccInterfaceAdminStatus_Type.__name__ = "Integer32"
_AccInterfaceAdminStatus_Object = MibTableColumn
accInterfaceAdminStatus = _AccInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 8),
    _AccInterfaceAdminStatus_Type()
)
accInterfaceAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceAdminStatus.setStatus("mandatory")
_AccInterfaceMtu_Type = Integer32
_AccInterfaceMtu_Object = MibTableColumn
accInterfaceMtu = _AccInterfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 9),
    _AccInterfaceMtu_Type()
)
accInterfaceMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceMtu.setStatus("mandatory")
_AccInterfaceSpeed_Type = Gauge32
_AccInterfaceSpeed_Object = MibTableColumn
accInterfaceSpeed = _AccInterfaceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 10),
    _AccInterfaceSpeed_Type()
)
accInterfaceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceSpeed.setStatus("mandatory")
_AccInterfaceOutQlength_Type = Gauge32
_AccInterfaceOutQlength_Object = MibTableColumn
accInterfaceOutQlength = _AccInterfaceOutQlength_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 11),
    _AccInterfaceOutQlength_Type()
)
accInterfaceOutQlength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceOutQlength.setStatus("mandatory")


class _AccInterfaceBufferUtil_Type(Integer32):
    """Custom type accInterfaceBufferUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AccInterfaceBufferUtil_Type.__name__ = "Integer32"
_AccInterfaceBufferUtil_Object = MibTableColumn
accInterfaceBufferUtil = _AccInterfaceBufferUtil_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 12),
    _AccInterfaceBufferUtil_Type()
)
accInterfaceBufferUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceBufferUtil.setStatus("mandatory")


class _AccInterfaceAccelerationAdminStatus_Type(Integer32):
    """Custom type accInterfaceAccelerationAdminStatus based on Integer32"""
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


_AccInterfaceAccelerationAdminStatus_Type.__name__ = "Integer32"
_AccInterfaceAccelerationAdminStatus_Object = MibTableColumn
accInterfaceAccelerationAdminStatus = _AccInterfaceAccelerationAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 13),
    _AccInterfaceAccelerationAdminStatus_Type()
)
accInterfaceAccelerationAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceAccelerationAdminStatus.setStatus("mandatory")


class _AccInterfaceQueuingStrategy_Type(Integer32):
    """Custom type accInterfaceQueuingStrategy based on Integer32"""
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
        *(("custom", 4),
          ("fifo", 1),
          ("priority", 3),
          ("wfq", 2))
    )


_AccInterfaceQueuingStrategy_Type.__name__ = "Integer32"
_AccInterfaceQueuingStrategy_Object = MibTableColumn
accInterfaceQueuingStrategy = _AccInterfaceQueuingStrategy_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 14),
    _AccInterfaceQueuingStrategy_Type()
)
accInterfaceQueuingStrategy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceQueuingStrategy.setStatus("mandatory")
_AccInterfaceIpAddress_Type = IpAddress
_AccInterfaceIpAddress_Object = MibTableColumn
accInterfaceIpAddress = _AccInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 15),
    _AccInterfaceIpAddress_Type()
)
accInterfaceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceIpAddress.setStatus("mandatory")
_AccInterfaceIpMask_Type = IpAddress
_AccInterfaceIpMask_Object = MibTableColumn
accInterfaceIpMask = _AccInterfaceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 16),
    _AccInterfaceIpMask_Type()
)
accInterfaceIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceIpMask.setStatus("mandatory")


class _AccInterfaceChunkSizeMethod_Type(Integer32):
    """Custom type accInterfaceChunkSizeMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1))
    )


_AccInterfaceChunkSizeMethod_Type.__name__ = "Integer32"
_AccInterfaceChunkSizeMethod_Object = MibTableColumn
accInterfaceChunkSizeMethod = _AccInterfaceChunkSizeMethod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 17),
    _AccInterfaceChunkSizeMethod_Type()
)
accInterfaceChunkSizeMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceChunkSizeMethod.setStatus("mandatory")
_AccInterfaceChunkSize_Type = Integer32
_AccInterfaceChunkSize_Object = MibTableColumn
accInterfaceChunkSize = _AccInterfaceChunkSize_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 18),
    _AccInterfaceChunkSize_Type()
)
accInterfaceChunkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceChunkSize.setStatus("mandatory")


class _AccInterfaceDrcMode_Type(Integer32):
    """Custom type accInterfaceDrcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("off", 1),
          ("semi", 2))
    )


_AccInterfaceDrcMode_Type.__name__ = "Integer32"
_AccInterfaceDrcMode_Object = MibTableColumn
accInterfaceDrcMode = _AccInterfaceDrcMode_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 19),
    _AccInterfaceDrcMode_Type()
)
accInterfaceDrcMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceDrcMode.setStatus("mandatory")
_AccInterfaceKeepAliveInterval_Type = Integer32
_AccInterfaceKeepAliveInterval_Object = MibTableColumn
accInterfaceKeepAliveInterval = _AccInterfaceKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 20),
    _AccInterfaceKeepAliveInterval_Type()
)
accInterfaceKeepAliveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceKeepAliveInterval.setStatus("mandatory")
_AccInterfaceKeepAliveIterations_Type = Integer32
_AccInterfaceKeepAliveIterations_Object = MibTableColumn
accInterfaceKeepAliveIterations = _AccInterfaceKeepAliveIterations_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 21),
    _AccInterfaceKeepAliveIterations_Type()
)
accInterfaceKeepAliveIterations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceKeepAliveIterations.setStatus("mandatory")
_AccInterfaceProbe_Type = Integer32
_AccInterfaceProbe_Object = MibTableColumn
accInterfaceProbe = _AccInterfaceProbe_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 22),
    _AccInterfaceProbe_Type()
)
accInterfaceProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceProbe.setStatus("mandatory")


class _AccInterfaceInboundStatus_Type(Integer32):
    """Custom type accInterfaceInboundStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("not-connected", 1))
    )


_AccInterfaceInboundStatus_Type.__name__ = "Integer32"
_AccInterfaceInboundStatus_Object = MibTableColumn
accInterfaceInboundStatus = _AccInterfaceInboundStatus_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 23),
    _AccInterfaceInboundStatus_Type()
)
accInterfaceInboundStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceInboundStatus.setStatus("mandatory")
_AccInterfaceInboundCore_Type = Integer32
_AccInterfaceInboundCore_Object = MibTableColumn
accInterfaceInboundCore = _AccInterfaceInboundCore_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 24),
    _AccInterfaceInboundCore_Type()
)
accInterfaceInboundCore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceInboundCore.setStatus("mandatory")


class _AccInterfaceOutboundStatus_Type(Integer32):
    """Custom type accInterfaceOutboundStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("not-connected", 1))
    )


_AccInterfaceOutboundStatus_Type.__name__ = "Integer32"
_AccInterfaceOutboundStatus_Object = MibTableColumn
accInterfaceOutboundStatus = _AccInterfaceOutboundStatus_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 25),
    _AccInterfaceOutboundStatus_Type()
)
accInterfaceOutboundStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceOutboundStatus.setStatus("mandatory")
_AccInterfaceOutboundCore_Type = Integer32
_AccInterfaceOutboundCore_Object = MibTableColumn
accInterfaceOutboundCore = _AccInterfaceOutboundCore_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 26),
    _AccInterfaceOutboundCore_Type()
)
accInterfaceOutboundCore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceOutboundCore.setStatus("mandatory")


class _AccInterfaceTransmitDirection_Type(Integer32):
    """Custom type accInterfaceTransmitDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("duplex", 1),
          ("simplex-receive", 2),
          ("simplex-transmit", 3))
    )


_AccInterfaceTransmitDirection_Type.__name__ = "Integer32"
_AccInterfaceTransmitDirection_Object = MibTableColumn
accInterfaceTransmitDirection = _AccInterfaceTransmitDirection_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 27),
    _AccInterfaceTransmitDirection_Type()
)
accInterfaceTransmitDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceTransmitDirection.setStatus("mandatory")
_AccInterfacePerformancePeriod_Type = Integer32
_AccInterfacePerformancePeriod_Object = MibTableColumn
accInterfacePerformancePeriod = _AccInterfacePerformancePeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 28),
    _AccInterfacePerformancePeriod_Type()
)
accInterfacePerformancePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformancePeriod.setStatus("mandatory")
_AccInterfacePerformanceInAccelerationUp_Type = Gauge32
_AccInterfacePerformanceInAccelerationUp_Object = MibTableColumn
accInterfacePerformanceInAccelerationUp = _AccInterfacePerformanceInAccelerationUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 29),
    _AccInterfacePerformanceInAccelerationUp_Type()
)
accInterfacePerformanceInAccelerationUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceInAccelerationUp.setStatus("mandatory")
_AccInterfacePerformanceInAccelerationClear_Type = Gauge32
_AccInterfacePerformanceInAccelerationClear_Object = MibTableColumn
accInterfacePerformanceInAccelerationClear = _AccInterfacePerformanceInAccelerationClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 30),
    _AccInterfacePerformanceInAccelerationClear_Type()
)
accInterfacePerformanceInAccelerationClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceInAccelerationClear.setStatus("mandatory")
_AccInterfacePerformanceInAccelerationPeriod_Type = Gauge32
_AccInterfacePerformanceInAccelerationPeriod_Object = MibTableColumn
accInterfacePerformanceInAccelerationPeriod = _AccInterfacePerformanceInAccelerationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 31),
    _AccInterfacePerformanceInAccelerationPeriod_Type()
)
accInterfacePerformanceInAccelerationPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceInAccelerationPeriod.setStatus("mandatory")
_AccInterfacePerformanceOutAccelerationUp_Type = Gauge32
_AccInterfacePerformanceOutAccelerationUp_Object = MibTableColumn
accInterfacePerformanceOutAccelerationUp = _AccInterfacePerformanceOutAccelerationUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 32),
    _AccInterfacePerformanceOutAccelerationUp_Type()
)
accInterfacePerformanceOutAccelerationUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceOutAccelerationUp.setStatus("mandatory")
_AccInterfacePerformanceOutAccelerationClear_Type = Gauge32
_AccInterfacePerformanceOutAccelerationClear_Object = MibTableColumn
accInterfacePerformanceOutAccelerationClear = _AccInterfacePerformanceOutAccelerationClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 33),
    _AccInterfacePerformanceOutAccelerationClear_Type()
)
accInterfacePerformanceOutAccelerationClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceOutAccelerationClear.setStatus("mandatory")
_AccInterfacePerformanceOutAccelerationPeriod_Type = Gauge32
_AccInterfacePerformanceOutAccelerationPeriod_Object = MibTableColumn
accInterfacePerformanceOutAccelerationPeriod = _AccInterfacePerformanceOutAccelerationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 34),
    _AccInterfacePerformanceOutAccelerationPeriod_Type()
)
accInterfacePerformanceOutAccelerationPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceOutAccelerationPeriod.setStatus("mandatory")
_AccInterfacePerformanceDrcResetsUp_Type = Counter32
_AccInterfacePerformanceDrcResetsUp_Object = MibTableColumn
accInterfacePerformanceDrcResetsUp = _AccInterfacePerformanceDrcResetsUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 35),
    _AccInterfacePerformanceDrcResetsUp_Type()
)
accInterfacePerformanceDrcResetsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceDrcResetsUp.setStatus("mandatory")
_AccInterfacePerformanceDrcResetsClear_Type = Gauge32
_AccInterfacePerformanceDrcResetsClear_Object = MibTableColumn
accInterfacePerformanceDrcResetsClear = _AccInterfacePerformanceDrcResetsClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 36),
    _AccInterfacePerformanceDrcResetsClear_Type()
)
accInterfacePerformanceDrcResetsClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceDrcResetsClear.setStatus("mandatory")
_AccInterfacePerformanceDrcResetsPeriod_Type = Gauge32
_AccInterfacePerformanceDrcResetsPeriod_Object = MibTableColumn
accInterfacePerformanceDrcResetsPeriod = _AccInterfacePerformanceDrcResetsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 37),
    _AccInterfacePerformanceDrcResetsPeriod_Type()
)
accInterfacePerformanceDrcResetsPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceDrcResetsPeriod.setStatus("mandatory")
_AccInterfacePerformanceLostPacketsUp_Type = Counter32
_AccInterfacePerformanceLostPacketsUp_Object = MibTableColumn
accInterfacePerformanceLostPacketsUp = _AccInterfacePerformanceLostPacketsUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 38),
    _AccInterfacePerformanceLostPacketsUp_Type()
)
accInterfacePerformanceLostPacketsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceLostPacketsUp.setStatus("mandatory")
_AccInterfacePerformanceLostPacketsClear_Type = Gauge32
_AccInterfacePerformanceLostPacketsClear_Object = MibTableColumn
accInterfacePerformanceLostPacketsClear = _AccInterfacePerformanceLostPacketsClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 39),
    _AccInterfacePerformanceLostPacketsClear_Type()
)
accInterfacePerformanceLostPacketsClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceLostPacketsClear.setStatus("mandatory")
_AccInterfacePerformanceLostPacketsPeriod_Type = Gauge32
_AccInterfacePerformanceLostPacketsPeriod_Object = MibTableColumn
accInterfacePerformanceLostPacketsPeriod = _AccInterfacePerformanceLostPacketsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 40),
    _AccInterfacePerformanceLostPacketsPeriod_Type()
)
accInterfacePerformanceLostPacketsPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceLostPacketsPeriod.setStatus("mandatory")
_AccInterfacePerformanceRetransmitPacketsUp_Type = Counter32
_AccInterfacePerformanceRetransmitPacketsUp_Object = MibTableColumn
accInterfacePerformanceRetransmitPacketsUp = _AccInterfacePerformanceRetransmitPacketsUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 41),
    _AccInterfacePerformanceRetransmitPacketsUp_Type()
)
accInterfacePerformanceRetransmitPacketsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceRetransmitPacketsUp.setStatus("mandatory")
_AccInterfacePerformanceRetransmitPacketsClear_Type = Gauge32
_AccInterfacePerformanceRetransmitPacketsClear_Object = MibTableColumn
accInterfacePerformanceRetransmitPacketsClear = _AccInterfacePerformanceRetransmitPacketsClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 42),
    _AccInterfacePerformanceRetransmitPacketsClear_Type()
)
accInterfacePerformanceRetransmitPacketsClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceRetransmitPacketsClear.setStatus("mandatory")
_AccInterfacePerformanceRetransmitPacketsPeriod_Type = Gauge32
_AccInterfacePerformanceRetransmitPacketsPeriod_Object = MibTableColumn
accInterfacePerformanceRetransmitPacketsPeriod = _AccInterfacePerformanceRetransmitPacketsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 43),
    _AccInterfacePerformanceRetransmitPacketsPeriod_Type()
)
accInterfacePerformanceRetransmitPacketsPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceRetransmitPacketsPeriod.setStatus("mandatory")
_AccInterfacePerformanceRecoveredPacketsUp_Type = Counter32
_AccInterfacePerformanceRecoveredPacketsUp_Object = MibTableColumn
accInterfacePerformanceRecoveredPacketsUp = _AccInterfacePerformanceRecoveredPacketsUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 44),
    _AccInterfacePerformanceRecoveredPacketsUp_Type()
)
accInterfacePerformanceRecoveredPacketsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfacePerformanceRecoveredPacketsUp.setStatus("mandatory")
_AccInterfacePerformanceRecoveredPacketsClear_Type = Gauge32
_AccInterfacePerformanceRecoveredPacketsClear_Object = MibTableColumn
accInterfacePerformanceRecoveredPacketsClear = _AccInterfacePerformanceRecoveredPacketsClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 45),
    _AccInterfacePerformanceRecoveredPacketsClear_Type()
)
accInterfacePerformanceRecoveredPacketsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accInterfacePerformanceRecoveredPacketsClear.setStatus("mandatory")
_AccInterfacePerformanceRecoveredPacketsPeriod_Type = Gauge32
_AccInterfacePerformanceRecoveredPacketsPeriod_Object = MibTableColumn
accInterfacePerformanceRecoveredPacketsPeriod = _AccInterfacePerformanceRecoveredPacketsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 46),
    _AccInterfacePerformanceRecoveredPacketsPeriod_Type()
)
accInterfacePerformanceRecoveredPacketsPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accInterfacePerformanceRecoveredPacketsPeriod.setStatus("mandatory")
_AccInterfaceThroughputPeriod_Type = Integer32
_AccInterfaceThroughputPeriod_Object = MibTableColumn
accInterfaceThroughputPeriod = _AccInterfaceThroughputPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 47),
    _AccInterfaceThroughputPeriod_Type()
)
accInterfaceThroughputPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputPeriod.setStatus("mandatory")
_AccInterfaceThroughputCrcErrUp_Type = Counter32
_AccInterfaceThroughputCrcErrUp_Object = MibTableColumn
accInterfaceThroughputCrcErrUp = _AccInterfaceThroughputCrcErrUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 48),
    _AccInterfaceThroughputCrcErrUp_Type()
)
accInterfaceThroughputCrcErrUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputCrcErrUp.setStatus("mandatory")
_AccInterfaceThroughputCrcErrClear_Type = Gauge32
_AccInterfaceThroughputCrcErrClear_Object = MibTableColumn
accInterfaceThroughputCrcErrClear = _AccInterfaceThroughputCrcErrClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 49),
    _AccInterfaceThroughputCrcErrClear_Type()
)
accInterfaceThroughputCrcErrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputCrcErrClear.setStatus("mandatory")
_AccInterfaceThroughputCrcErrPeriod_Type = Gauge32
_AccInterfaceThroughputCrcErrPeriod_Object = MibTableColumn
accInterfaceThroughputCrcErrPeriod = _AccInterfaceThroughputCrcErrPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 50),
    _AccInterfaceThroughputCrcErrPeriod_Type()
)
accInterfaceThroughputCrcErrPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputCrcErrPeriod.setStatus("mandatory")
_AccInterfaceThroughputDropByteUp_Type = Counter32
_AccInterfaceThroughputDropByteUp_Object = MibTableColumn
accInterfaceThroughputDropByteUp = _AccInterfaceThroughputDropByteUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 51),
    _AccInterfaceThroughputDropByteUp_Type()
)
accInterfaceThroughputDropByteUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputDropByteUp.setStatus("mandatory")
_AccInterfaceThroughputDropByteClear_Type = Gauge32
_AccInterfaceThroughputDropByteClear_Object = MibTableColumn
accInterfaceThroughputDropByteClear = _AccInterfaceThroughputDropByteClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 52),
    _AccInterfaceThroughputDropByteClear_Type()
)
accInterfaceThroughputDropByteClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputDropByteClear.setStatus("mandatory")
_AccInterfaceThroughputDropBytePeriod_Type = Gauge32
_AccInterfaceThroughputDropBytePeriod_Object = MibTableColumn
accInterfaceThroughputDropBytePeriod = _AccInterfaceThroughputDropBytePeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 53),
    _AccInterfaceThroughputDropBytePeriod_Type()
)
accInterfaceThroughputDropBytePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputDropBytePeriod.setStatus("mandatory")
_AccInterfaceThroughputDropPacketsUp_Type = Counter32
_AccInterfaceThroughputDropPacketsUp_Object = MibTableColumn
accInterfaceThroughputDropPacketsUp = _AccInterfaceThroughputDropPacketsUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 54),
    _AccInterfaceThroughputDropPacketsUp_Type()
)
accInterfaceThroughputDropPacketsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputDropPacketsUp.setStatus("mandatory")
_AccInterfaceThroughputDropPacketsClear_Type = Gauge32
_AccInterfaceThroughputDropPacketsClear_Object = MibTableColumn
accInterfaceThroughputDropPacketsClear = _AccInterfaceThroughputDropPacketsClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 55),
    _AccInterfaceThroughputDropPacketsClear_Type()
)
accInterfaceThroughputDropPacketsClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputDropPacketsClear.setStatus("mandatory")
_AccInterfaceThroughputDropPacketsPeriod_Type = Gauge32
_AccInterfaceThroughputDropPacketsPeriod_Object = MibTableColumn
accInterfaceThroughputDropPacketsPeriod = _AccInterfaceThroughputDropPacketsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 56),
    _AccInterfaceThroughputDropPacketsPeriod_Type()
)
accInterfaceThroughputDropPacketsPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputDropPacketsPeriod.setStatus("mandatory")
_AccInterfaceThroughputInBytesUp_Type = Counter32
_AccInterfaceThroughputInBytesUp_Object = MibTableColumn
accInterfaceThroughputInBytesUp = _AccInterfaceThroughputInBytesUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 57),
    _AccInterfaceThroughputInBytesUp_Type()
)
accInterfaceThroughputInBytesUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputInBytesUp.setStatus("mandatory")
_AccInterfaceThroughputInBytesClear_Type = Gauge32
_AccInterfaceThroughputInBytesClear_Object = MibTableColumn
accInterfaceThroughputInBytesClear = _AccInterfaceThroughputInBytesClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 58),
    _AccInterfaceThroughputInBytesClear_Type()
)
accInterfaceThroughputInBytesClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputInBytesClear.setStatus("mandatory")
_AccInterfaceThroughputInBytesPeriod_Type = Gauge32
_AccInterfaceThroughputInBytesPeriod_Object = MibTableColumn
accInterfaceThroughputInBytesPeriod = _AccInterfaceThroughputInBytesPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 59),
    _AccInterfaceThroughputInBytesPeriod_Type()
)
accInterfaceThroughputInBytesPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputInBytesPeriod.setStatus("mandatory")
_AccInterfaceThroughputInPacketsUp_Type = Counter32
_AccInterfaceThroughputInPacketsUp_Object = MibTableColumn
accInterfaceThroughputInPacketsUp = _AccInterfaceThroughputInPacketsUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 60),
    _AccInterfaceThroughputInPacketsUp_Type()
)
accInterfaceThroughputInPacketsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputInPacketsUp.setStatus("mandatory")
_AccInterfaceThroughputInPacketsClear_Type = Gauge32
_AccInterfaceThroughputInPacketsClear_Object = MibTableColumn
accInterfaceThroughputInPacketsClear = _AccInterfaceThroughputInPacketsClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 61),
    _AccInterfaceThroughputInPacketsClear_Type()
)
accInterfaceThroughputInPacketsClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputInPacketsClear.setStatus("mandatory")
_AccInterfaceThroughputInPacketsPeriod_Type = Gauge32
_AccInterfaceThroughputInPacketsPeriod_Object = MibTableColumn
accInterfaceThroughputInPacketsPeriod = _AccInterfaceThroughputInPacketsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 62),
    _AccInterfaceThroughputInPacketsPeriod_Type()
)
accInterfaceThroughputInPacketsPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputInPacketsPeriod.setStatus("mandatory")
_AccInterfaceThroughputOutBytesUp_Type = Counter32
_AccInterfaceThroughputOutBytesUp_Object = MibTableColumn
accInterfaceThroughputOutBytesUp = _AccInterfaceThroughputOutBytesUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 63),
    _AccInterfaceThroughputOutBytesUp_Type()
)
accInterfaceThroughputOutBytesUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputOutBytesUp.setStatus("mandatory")
_AccInterfaceThroughputOutBytesClear_Type = Gauge32
_AccInterfaceThroughputOutBytesClear_Object = MibTableColumn
accInterfaceThroughputOutBytesClear = _AccInterfaceThroughputOutBytesClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 64),
    _AccInterfaceThroughputOutBytesClear_Type()
)
accInterfaceThroughputOutBytesClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputOutBytesClear.setStatus("mandatory")
_AccInterfaceThroughputOutBytesPeriod_Type = Gauge32
_AccInterfaceThroughputOutBytesPeriod_Object = MibTableColumn
accInterfaceThroughputOutBytesPeriod = _AccInterfaceThroughputOutBytesPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 65),
    _AccInterfaceThroughputOutBytesPeriod_Type()
)
accInterfaceThroughputOutBytesPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputOutBytesPeriod.setStatus("mandatory")
_AccInterfaceThroughputOutPacketsUp_Type = Counter32
_AccInterfaceThroughputOutPacketsUp_Object = MibTableColumn
accInterfaceThroughputOutPacketsUp = _AccInterfaceThroughputOutPacketsUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 66),
    _AccInterfaceThroughputOutPacketsUp_Type()
)
accInterfaceThroughputOutPacketsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputOutPacketsUp.setStatus("mandatory")
_AccInterfaceThroughputOutPacketsClear_Type = Gauge32
_AccInterfaceThroughputOutPacketsClear_Object = MibTableColumn
accInterfaceThroughputOutPacketsClear = _AccInterfaceThroughputOutPacketsClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 67),
    _AccInterfaceThroughputOutPacketsClear_Type()
)
accInterfaceThroughputOutPacketsClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputOutPacketsClear.setStatus("mandatory")
_AccInterfaceThroughputOutPacketsPeriod_Type = Gauge32
_AccInterfaceThroughputOutPacketsPeriod_Object = MibTableColumn
accInterfaceThroughputOutPacketsPeriod = _AccInterfaceThroughputOutPacketsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 68),
    _AccInterfaceThroughputOutPacketsPeriod_Type()
)
accInterfaceThroughputOutPacketsPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputOutPacketsPeriod.setStatus("mandatory")
_AccInterfaceThroughputRawInBytesUp_Type = Counter32
_AccInterfaceThroughputRawInBytesUp_Object = MibTableColumn
accInterfaceThroughputRawInBytesUp = _AccInterfaceThroughputRawInBytesUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 69),
    _AccInterfaceThroughputRawInBytesUp_Type()
)
accInterfaceThroughputRawInBytesUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputRawInBytesUp.setStatus("mandatory")
_AccInterfaceThroughputRawInBytesClear_Type = Gauge32
_AccInterfaceThroughputRawInBytesClear_Object = MibTableColumn
accInterfaceThroughputRawInBytesClear = _AccInterfaceThroughputRawInBytesClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 70),
    _AccInterfaceThroughputRawInBytesClear_Type()
)
accInterfaceThroughputRawInBytesClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputRawInBytesClear.setStatus("mandatory")
_AccInterfaceThroughputRawInBytesPeriod_Type = Gauge32
_AccInterfaceThroughputRawInBytesPeriod_Object = MibTableColumn
accInterfaceThroughputRawInBytesPeriod = _AccInterfaceThroughputRawInBytesPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 71),
    _AccInterfaceThroughputRawInBytesPeriod_Type()
)
accInterfaceThroughputRawInBytesPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputRawInBytesPeriod.setStatus("mandatory")
_AccInterfaceThroughputRawOutBytesUp_Type = Counter32
_AccInterfaceThroughputRawOutBytesUp_Object = MibTableColumn
accInterfaceThroughputRawOutBytesUp = _AccInterfaceThroughputRawOutBytesUp_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 72),
    _AccInterfaceThroughputRawOutBytesUp_Type()
)
accInterfaceThroughputRawOutBytesUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputRawOutBytesUp.setStatus("mandatory")
_AccInterfaceThroughputRawOutBytesClear_Type = Gauge32
_AccInterfaceThroughputRawOutBytesClear_Object = MibTableColumn
accInterfaceThroughputRawOutBytesClear = _AccInterfaceThroughputRawOutBytesClear_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 73),
    _AccInterfaceThroughputRawOutBytesClear_Type()
)
accInterfaceThroughputRawOutBytesClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputRawOutBytesClear.setStatus("mandatory")
_AccInterfaceThroughputRawOutBytesPeriod_Type = Gauge32
_AccInterfaceThroughputRawOutBytesPeriod_Object = MibTableColumn
accInterfaceThroughputRawOutBytesPeriod = _AccInterfaceThroughputRawOutBytesPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3405, 3, 4, 2, 1, 74),
    _AccInterfaceThroughputRawOutBytesPeriod_Type()
)
accInterfaceThroughputRawOutBytesPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInterfaceThroughputRawOutBytesPeriod.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXPAND-ACCELERATOROS-MIB",
    **{"accProductId": accProductId,
       "accSystem": accSystem,
       "accSysUpTime": accSysUpTime,
       "accSoftwareVersion": accSoftwareVersion,
       "accSysHostName": accSysHostName,
       "accSysLocation": accSysLocation,
       "accSysContact": accSysContact,
       "accSerialNumber": accSerialNumber,
       "accPerformance": accPerformance,
       "accHardware": accHardware,
       "accCpu": accCpu,
       "accCpuTotalEntries": accCpuTotalEntries,
       "accCpuTable": accCpuTable,
       "accCpuEntry": accCpuEntry,
       "accCpuIndex": accCpuIndex,
       "accCpuDesc": accCpuDesc,
       "accCpuUtilization": accCpuUtilization,
       "accSoftware": accSoftware,
       "accBuffer": accBuffer,
       "accSystemWide": accSystemWide,
       "accInterfaces": accInterfaces,
       "accInterfaceTotalEntries": accInterfaceTotalEntries,
       "accInterfaceTable": accInterfaceTable,
       "accInterfaceEntry": accInterfaceEntry,
       "accInterfaceIndex": accInterfaceIndex,
       "accInterfaceDescription": accInterfaceDescription,
       "accInterfaceEncapsulation": accInterfaceEncapsulation,
       "accInterfaceFrameRelayDlci": accInterfaceFrameRelayDlci,
       "accInterfaceType": accInterfaceType,
       "accInterfaceOperStatus": accInterfaceOperStatus,
       "accInterfaceAdminStatus": accInterfaceAdminStatus,
       "accInterfaceMtu": accInterfaceMtu,
       "accInterfaceSpeed": accInterfaceSpeed,
       "accInterfaceOutQlength": accInterfaceOutQlength,
       "accInterfaceBufferUtil": accInterfaceBufferUtil,
       "accInterfaceAccelerationAdminStatus": accInterfaceAccelerationAdminStatus,
       "accInterfaceQueuingStrategy": accInterfaceQueuingStrategy,
       "accInterfaceIpAddress": accInterfaceIpAddress,
       "accInterfaceIpMask": accInterfaceIpMask,
       "accInterfaceChunkSizeMethod": accInterfaceChunkSizeMethod,
       "accInterfaceChunkSize": accInterfaceChunkSize,
       "accInterfaceDrcMode": accInterfaceDrcMode,
       "accInterfaceKeepAliveInterval": accInterfaceKeepAliveInterval,
       "accInterfaceKeepAliveIterations": accInterfaceKeepAliveIterations,
       "accInterfaceProbe": accInterfaceProbe,
       "accInterfaceInboundStatus": accInterfaceInboundStatus,
       "accInterfaceInboundCore": accInterfaceInboundCore,
       "accInterfaceOutboundStatus": accInterfaceOutboundStatus,
       "accInterfaceOutboundCore": accInterfaceOutboundCore,
       "accInterfaceTransmitDirection": accInterfaceTransmitDirection,
       "accInterfacePerformancePeriod": accInterfacePerformancePeriod,
       "accInterfacePerformanceInAccelerationUp": accInterfacePerformanceInAccelerationUp,
       "accInterfacePerformanceInAccelerationClear": accInterfacePerformanceInAccelerationClear,
       "accInterfacePerformanceInAccelerationPeriod": accInterfacePerformanceInAccelerationPeriod,
       "accInterfacePerformanceOutAccelerationUp": accInterfacePerformanceOutAccelerationUp,
       "accInterfacePerformanceOutAccelerationClear": accInterfacePerformanceOutAccelerationClear,
       "accInterfacePerformanceOutAccelerationPeriod": accInterfacePerformanceOutAccelerationPeriod,
       "accInterfacePerformanceDrcResetsUp": accInterfacePerformanceDrcResetsUp,
       "accInterfacePerformanceDrcResetsClear": accInterfacePerformanceDrcResetsClear,
       "accInterfacePerformanceDrcResetsPeriod": accInterfacePerformanceDrcResetsPeriod,
       "accInterfacePerformanceLostPacketsUp": accInterfacePerformanceLostPacketsUp,
       "accInterfacePerformanceLostPacketsClear": accInterfacePerformanceLostPacketsClear,
       "accInterfacePerformanceLostPacketsPeriod": accInterfacePerformanceLostPacketsPeriod,
       "accInterfacePerformanceRetransmitPacketsUp": accInterfacePerformanceRetransmitPacketsUp,
       "accInterfacePerformanceRetransmitPacketsClear": accInterfacePerformanceRetransmitPacketsClear,
       "accInterfacePerformanceRetransmitPacketsPeriod": accInterfacePerformanceRetransmitPacketsPeriod,
       "accInterfacePerformanceRecoveredPacketsUp": accInterfacePerformanceRecoveredPacketsUp,
       "accInterfacePerformanceRecoveredPacketsClear": accInterfacePerformanceRecoveredPacketsClear,
       "accInterfacePerformanceRecoveredPacketsPeriod": accInterfacePerformanceRecoveredPacketsPeriod,
       "accInterfaceThroughputPeriod": accInterfaceThroughputPeriod,
       "accInterfaceThroughputCrcErrUp": accInterfaceThroughputCrcErrUp,
       "accInterfaceThroughputCrcErrClear": accInterfaceThroughputCrcErrClear,
       "accInterfaceThroughputCrcErrPeriod": accInterfaceThroughputCrcErrPeriod,
       "accInterfaceThroughputDropByteUp": accInterfaceThroughputDropByteUp,
       "accInterfaceThroughputDropByteClear": accInterfaceThroughputDropByteClear,
       "accInterfaceThroughputDropBytePeriod": accInterfaceThroughputDropBytePeriod,
       "accInterfaceThroughputDropPacketsUp": accInterfaceThroughputDropPacketsUp,
       "accInterfaceThroughputDropPacketsClear": accInterfaceThroughputDropPacketsClear,
       "accInterfaceThroughputDropPacketsPeriod": accInterfaceThroughputDropPacketsPeriod,
       "accInterfaceThroughputInBytesUp": accInterfaceThroughputInBytesUp,
       "accInterfaceThroughputInBytesClear": accInterfaceThroughputInBytesClear,
       "accInterfaceThroughputInBytesPeriod": accInterfaceThroughputInBytesPeriod,
       "accInterfaceThroughputInPacketsUp": accInterfaceThroughputInPacketsUp,
       "accInterfaceThroughputInPacketsClear": accInterfaceThroughputInPacketsClear,
       "accInterfaceThroughputInPacketsPeriod": accInterfaceThroughputInPacketsPeriod,
       "accInterfaceThroughputOutBytesUp": accInterfaceThroughputOutBytesUp,
       "accInterfaceThroughputOutBytesClear": accInterfaceThroughputOutBytesClear,
       "accInterfaceThroughputOutBytesPeriod": accInterfaceThroughputOutBytesPeriod,
       "accInterfaceThroughputOutPacketsUp": accInterfaceThroughputOutPacketsUp,
       "accInterfaceThroughputOutPacketsClear": accInterfaceThroughputOutPacketsClear,
       "accInterfaceThroughputOutPacketsPeriod": accInterfaceThroughputOutPacketsPeriod,
       "accInterfaceThroughputRawInBytesUp": accInterfaceThroughputRawInBytesUp,
       "accInterfaceThroughputRawInBytesClear": accInterfaceThroughputRawInBytesClear,
       "accInterfaceThroughputRawInBytesPeriod": accInterfaceThroughputRawInBytesPeriod,
       "accInterfaceThroughputRawOutBytesUp": accInterfaceThroughputRawOutBytesUp,
       "accInterfaceThroughputRawOutBytesClear": accInterfaceThroughputRawOutBytesClear,
       "accInterfaceThroughputRawOutBytesPeriod": accInterfaceThroughputRawOutBytesPeriod}
)
