# SNMP MIB module (LANOPTICS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LANOPTICS-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:16 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LanOptics_ObjectIdentity = ObjectIdentity
lanOptics = _LanOptics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224)
)
_LanOpticsSystem_ObjectIdentity = ObjectIdentity
lanOpticsSystem = _LanOpticsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 2)
)
_SnSysDirectory_Type = DisplayString
_SnSysDirectory_Object = MibScalar
snSysDirectory = _SnSysDirectory_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 1),
    _SnSysDirectory_Type()
)
snSysDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSysDirectory.setStatus("mandatory")
_SnAgentVersion_Type = Integer32
_SnAgentVersion_Object = MibScalar
snAgentVersion = _SnAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 2),
    _SnAgentVersion_Type()
)
snAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentVersion.setStatus("mandatory")
_LanOpticsSystemCMOS_ObjectIdentity = ObjectIdentity
lanOpticsSystemCMOS = _LanOpticsSystemCMOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 2, 3)
)
_LanOpticsSystemCMOSIp_ObjectIdentity = ObjectIdentity
lanOpticsSystemCMOSIp = _LanOpticsSystemCMOSIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 1)
)
_SnSysCMOSIpInterfaceTable_Object = MibTable
snSysCMOSIpInterfaceTable = _SnSysCMOSIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    snSysCMOSIpInterfaceTable.setStatus("mandatory")
_SnSysCMOSIpInterfaceEntry_Object = MibTableRow
snSysCMOSIpInterfaceEntry = _SnSysCMOSIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 1, 1)
)
snSysCMOSIpInterfaceEntry.setIndexNames(
    (0, "LANOPTICS-SYSTEM-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    snSysCMOSIpInterfaceEntry.setStatus("mandatory")
_SnSysCMOSIpIpAddr_Type = IpAddress
_SnSysCMOSIpIpAddr_Object = MibTableColumn
snSysCMOSIpIpAddr = _SnSysCMOSIpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 1, 1, 1),
    _SnSysCMOSIpIpAddr_Type()
)
snSysCMOSIpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSIpIpAddr.setStatus("mandatory")
_SnSysCMOSIpNetMask_Type = IpAddress
_SnSysCMOSIpNetMask_Object = MibTableColumn
snSysCMOSIpNetMask = _SnSysCMOSIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 1, 1, 2),
    _SnSysCMOSIpNetMask_Type()
)
snSysCMOSIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSIpNetMask.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 1, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_SnSysCMOSIpDefGw_Type = IpAddress
_SnSysCMOSIpDefGw_Object = MibScalar
snSysCMOSIpDefGw = _SnSysCMOSIpDefGw_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 2),
    _SnSysCMOSIpDefGw_Type()
)
snSysCMOSIpDefGw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSIpDefGw.setStatus("mandatory")


class _SnSysCMOSIpTFTPOp_Type(Integer32):
    """Custom type snSysCMOSIpTFTPOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("continuous", 3),
          ("limited", 2),
          ("noTFTP", 1))
    )


_SnSysCMOSIpTFTPOp_Type.__name__ = "Integer32"
_SnSysCMOSIpTFTPOp_Object = MibScalar
snSysCMOSIpTFTPOp = _SnSysCMOSIpTFTPOp_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 3),
    _SnSysCMOSIpTFTPOp_Type()
)
snSysCMOSIpTFTPOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSIpTFTPOp.setStatus("mandatory")
_SnSysCMOSIpTFTPAddr_Type = IpAddress
_SnSysCMOSIpTFTPAddr_Object = MibScalar
snSysCMOSIpTFTPAddr = _SnSysCMOSIpTFTPAddr_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 4),
    _SnSysCMOSIpTFTPAddr_Type()
)
snSysCMOSIpTFTPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSIpTFTPAddr.setStatus("mandatory")
_SnSysCMOSIpTFTPFileName_Type = DisplayString
_SnSysCMOSIpTFTPFileName_Object = MibScalar
snSysCMOSIpTFTPFileName = _SnSysCMOSIpTFTPFileName_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 5),
    _SnSysCMOSIpTFTPFileName_Type()
)
snSysCMOSIpTFTPFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSIpTFTPFileName.setStatus("mandatory")


class _SnSysCMOSIpTFTPDrive_Type(Integer32):
    """Custom type snSysCMOSIpTFTPDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("driveA", 41),
          ("driveB", 42),
          ("driveC", 43),
          ("driveD", 44))
    )


_SnSysCMOSIpTFTPDrive_Type.__name__ = "Integer32"
_SnSysCMOSIpTFTPDrive_Object = MibScalar
snSysCMOSIpTFTPDrive = _SnSysCMOSIpTFTPDrive_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 6),
    _SnSysCMOSIpTFTPDrive_Type()
)
snSysCMOSIpTFTPDrive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSIpTFTPDrive.setStatus("mandatory")
_LanOpticsSystemCMOSHub_ObjectIdentity = ObjectIdentity
lanOpticsSystemCMOSHub = _LanOpticsSystemCMOSHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 2)
)
_SnSysCMOSHubSlotConfigTable_Object = MibTable
snSysCMOSHubSlotConfigTable = _SnSysCMOSHubSlotConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    snSysCMOSHubSlotConfigTable.setStatus("mandatory")
_SnSysCMOSHubSlotConfigEntry_Object = MibTableRow
snSysCMOSHubSlotConfigEntry = _SnSysCMOSHubSlotConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 2, 1, 1)
)
snSysCMOSHubSlotConfigEntry.setIndexNames(
    (0, "LANOPTICS-SYSTEM-MIB", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    snSysCMOSHubSlotConfigEntry.setStatus("mandatory")
_SnSysSlotLastOperations_Type = OctetString
_SnSysSlotLastOperations_Object = MibTableColumn
snSysSlotLastOperations = _SnSysSlotLastOperations_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 2, 1, 1, 1),
    _SnSysSlotLastOperations_Type()
)
snSysSlotLastOperations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysSlotLastOperations.setStatus("mandatory")
_SnSysResetSlotQueue_Type = Integer32
_SnSysResetSlotQueue_Object = MibTableColumn
snSysResetSlotQueue = _SnSysResetSlotQueue_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 2, 1, 1, 2),
    _SnSysResetSlotQueue_Type()
)
snSysResetSlotQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysResetSlotQueue.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 2, 1, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")


class _SnSysCMOSHubSaveHubFunctions_Type(Integer32):
    """Custom type snSysCMOSHubSaveHubFunctions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-saved", 1),
          ("saved", 2))
    )


_SnSysCMOSHubSaveHubFunctions_Type.__name__ = "Integer32"
_SnSysCMOSHubSaveHubFunctions_Object = MibScalar
snSysCMOSHubSaveHubFunctions = _SnSysCMOSHubSaveHubFunctions_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 2, 2),
    _SnSysCMOSHubSaveHubFunctions_Type()
)
snSysCMOSHubSaveHubFunctions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSHubSaveHubFunctions.setStatus("mandatory")
_LanOpticsSystemCMOSRPL_ObjectIdentity = ObjectIdentity
lanOpticsSystemCMOSRPL = _LanOpticsSystemCMOSRPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 3)
)


class _SnSysCMOSRPLMode_Type(Integer32):
    """Custom type snSysCMOSRPLMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rpl-off", 1),
          ("rpl-on", 2))
    )


_SnSysCMOSRPLMode_Type.__name__ = "Integer32"
_SnSysCMOSRPLMode_Object = MibScalar
snSysCMOSRPLMode = _SnSysCMOSRPLMode_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 3, 1),
    _SnSysCMOSRPLMode_Type()
)
snSysCMOSRPLMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSRPLMode.setStatus("mandatory")


class _SnSysCMOSFlashMode_Type(Integer32):
    """Custom type snSysCMOSFlashMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash-off", 1),
          ("flash-on", 2))
    )


_SnSysCMOSFlashMode_Type.__name__ = "Integer32"
_SnSysCMOSFlashMode_Object = MibScalar
snSysCMOSFlashMode = _SnSysCMOSFlashMode_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 3, 2),
    _SnSysCMOSFlashMode_Type()
)
snSysCMOSFlashMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSFlashMode.setStatus("mandatory")
_LanOpticsSystemCMOSSerial_ObjectIdentity = ObjectIdentity
lanOpticsSystemCMOSSerial = _LanOpticsSystemCMOSSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 4)
)


class _SnSysCMOSSerialMode_Type(Integer32):
    """Custom type snSysCMOSSerialMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("proprietary", 1),
          ("slip", 2))
    )


_SnSysCMOSSerialMode_Type.__name__ = "Integer32"
_SnSysCMOSSerialMode_Object = MibScalar
snSysCMOSSerialMode = _SnSysCMOSSerialMode_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 4, 1),
    _SnSysCMOSSerialMode_Type()
)
snSysCMOSSerialMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSSerialMode.setStatus("mandatory")


class _SnSysCMOSSerialComSelect_Type(Integer32):
    """Custom type snSysCMOSSerialComSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sr-COM1", 1),
          ("sr-COM2", 2))
    )


_SnSysCMOSSerialComSelect_Type.__name__ = "Integer32"
_SnSysCMOSSerialComSelect_Object = MibScalar
snSysCMOSSerialComSelect = _SnSysCMOSSerialComSelect_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 4, 2),
    _SnSysCMOSSerialComSelect_Type()
)
snSysCMOSSerialComSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSSerialComSelect.setStatus("mandatory")


class _SnSysCMOSSerialBaudRate_Type(Integer32):
    """Custom type snSysCMOSSerialBaudRate based on Integer32"""
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
        *(("baud1200", 1),
          ("baud19200", 5),
          ("baud2400", 2),
          ("baud38300", 6),
          ("baud4800", 3),
          ("baud57600", 7),
          ("baud9600", 4))
    )


_SnSysCMOSSerialBaudRate_Type.__name__ = "Integer32"
_SnSysCMOSSerialBaudRate_Object = MibScalar
snSysCMOSSerialBaudRate = _SnSysCMOSSerialBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 4, 3),
    _SnSysCMOSSerialBaudRate_Type()
)
snSysCMOSSerialBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSSerialBaudRate.setStatus("mandatory")


class _SnSysCMOSSerialWordLength_Type(Integer32):
    """Custom type snSysCMOSSerialWordLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bits-7", 1),
          ("bits-8", 2))
    )


_SnSysCMOSSerialWordLength_Type.__name__ = "Integer32"
_SnSysCMOSSerialWordLength_Object = MibScalar
snSysCMOSSerialWordLength = _SnSysCMOSSerialWordLength_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 4, 4),
    _SnSysCMOSSerialWordLength_Type()
)
snSysCMOSSerialWordLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSSerialWordLength.setStatus("mandatory")


class _SnSysCMOSSerialStopBits_Type(Integer32):
    """Custom type snSysCMOSSerialStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bits-1", 1),
          ("bits-15", 2),
          ("bits-2", 3))
    )


_SnSysCMOSSerialStopBits_Type.__name__ = "Integer32"
_SnSysCMOSSerialStopBits_Object = MibScalar
snSysCMOSSerialStopBits = _SnSysCMOSSerialStopBits_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 4, 5),
    _SnSysCMOSSerialStopBits_Type()
)
snSysCMOSSerialStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSSerialStopBits.setStatus("mandatory")


class _SnSysCMOSSerialParityCheck_Type(Integer32):
    """Custom type snSysCMOSSerialParityCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 1),
          ("none", 3),
          ("odd", 2))
    )


_SnSysCMOSSerialParityCheck_Type.__name__ = "Integer32"
_SnSysCMOSSerialParityCheck_Object = MibScalar
snSysCMOSSerialParityCheck = _SnSysCMOSSerialParityCheck_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 4, 6),
    _SnSysCMOSSerialParityCheck_Type()
)
snSysCMOSSerialParityCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSSerialParityCheck.setStatus("mandatory")
_LanOpticsSystemCMOSSRAM_ObjectIdentity = ObjectIdentity
lanOpticsSystemCMOSSRAM = _LanOpticsSystemCMOSSRAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 5)
)
_SnSysCMOSSRAMKeepAliveSecInterval_Type = Integer32
_SnSysCMOSSRAMKeepAliveSecInterval_Object = MibScalar
snSysCMOSSRAMKeepAliveSecInterval = _SnSysCMOSSRAMKeepAliveSecInterval_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 5, 1),
    _SnSysCMOSSRAMKeepAliveSecInterval_Type()
)
snSysCMOSSRAMKeepAliveSecInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSSRAMKeepAliveSecInterval.setStatus("mandatory")
_LanOpticsSystemCMOSSNMP_ObjectIdentity = ObjectIdentity
lanOpticsSystemCMOSSNMP = _LanOpticsSystemCMOSSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 6)
)
_SnSysCMOSSNMPCommunitiesNum_Type = Integer32
_SnSysCMOSSNMPCommunitiesNum_Object = MibScalar
snSysCMOSSNMPCommunitiesNum = _SnSysCMOSSNMPCommunitiesNum_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 1),
    _SnSysCMOSSNMPCommunitiesNum_Type()
)
snSysCMOSSNMPCommunitiesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSysCMOSSNMPCommunitiesNum.setStatus("mandatory")
_SnSysCMOSSNMPTrapManagersNum_Type = Integer32
_SnSysCMOSSNMPTrapManagersNum_Object = MibScalar
snSysCMOSSNMPTrapManagersNum = _SnSysCMOSSNMPTrapManagersNum_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 2),
    _SnSysCMOSSNMPTrapManagersNum_Type()
)
snSysCMOSSNMPTrapManagersNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSysCMOSSNMPTrapManagersNum.setStatus("mandatory")
_SnSysCMOSSNMPCommunitiesTable_Object = MibTable
snSysCMOSSNMPCommunitiesTable = _SnSysCMOSSNMPCommunitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 3)
)
if mibBuilder.loadTexts:
    snSysCMOSSNMPCommunitiesTable.setStatus("mandatory")
_SnSysCMOSSNMPCommunitiesEntry_Object = MibTableRow
snSysCMOSSNMPCommunitiesEntry = _SnSysCMOSSNMPCommunitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 3, 1)
)
snSysCMOSSNMPCommunitiesEntry.setIndexNames(
    (0, "LANOPTICS-SYSTEM-MIB", "pysmiFakeCol3"),
)
if mibBuilder.loadTexts:
    snSysCMOSSNMPCommunitiesEntry.setStatus("mandatory")
_SnSysCMOSSNMPCommunityName_Type = DisplayString
_SnSysCMOSSNMPCommunityName_Object = MibTableColumn
snSysCMOSSNMPCommunityName = _SnSysCMOSSNMPCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 3, 1, 1),
    _SnSysCMOSSNMPCommunityName_Type()
)
snSysCMOSSNMPCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSSNMPCommunityName.setStatus("mandatory")


class _SnSysCMOSSNMPCommunityPrivs_Type(Integer32):
    """Custom type snSysCMOSSNMPCommunityPrivs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-Only", 1),
          ("read-Write", 2))
    )


_SnSysCMOSSNMPCommunityPrivs_Type.__name__ = "Integer32"
_SnSysCMOSSNMPCommunityPrivs_Object = MibTableColumn
snSysCMOSSNMPCommunityPrivs = _SnSysCMOSSNMPCommunityPrivs_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 3, 1, 2),
    _SnSysCMOSSNMPCommunityPrivs_Type()
)
snSysCMOSSNMPCommunityPrivs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSSNMPCommunityPrivs.setStatus("mandatory")
_PysmiFakeCol3_Type = Integer32
_PysmiFakeCol3_Object = MibTableColumn
pysmiFakeCol3 = _PysmiFakeCol3_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 3, 1, 4294967295),
    _PysmiFakeCol3_Type()
)
pysmiFakeCol3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol3.setStatus("mandatory")
_SnSysCMOSSNMPTrapCommunitiesTable_Object = MibTable
snSysCMOSSNMPTrapCommunitiesTable = _SnSysCMOSSNMPTrapCommunitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 4)
)
if mibBuilder.loadTexts:
    snSysCMOSSNMPTrapCommunitiesTable.setStatus("mandatory")
_SnSysCMOSSNMPTrapCommunitiesEntry_Object = MibTableRow
snSysCMOSSNMPTrapCommunitiesEntry = _SnSysCMOSSNMPTrapCommunitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 4, 1)
)
snSysCMOSSNMPTrapCommunitiesEntry.setIndexNames(
    (0, "LANOPTICS-SYSTEM-MIB", "pysmiFakeCol4"),
)
if mibBuilder.loadTexts:
    snSysCMOSSNMPTrapCommunitiesEntry.setStatus("mandatory")
_SnSysCMOSSNMPTrapCommunityIpAddr_Type = IpAddress
_SnSysCMOSSNMPTrapCommunityIpAddr_Object = MibTableColumn
snSysCMOSSNMPTrapCommunityIpAddr = _SnSysCMOSSNMPTrapCommunityIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 4, 1, 1),
    _SnSysCMOSSNMPTrapCommunityIpAddr_Type()
)
snSysCMOSSNMPTrapCommunityIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSSNMPTrapCommunityIpAddr.setStatus("mandatory")
_PysmiFakeCol4_Type = Integer32
_PysmiFakeCol4_Object = MibTableColumn
pysmiFakeCol4 = _PysmiFakeCol4_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 4, 1, 4294967295),
    _PysmiFakeCol4_Type()
)
pysmiFakeCol4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol4.setStatus("mandatory")
_LanOpticsSystemCMOSACCESS_ObjectIdentity = ObjectIdentity
lanOpticsSystemCMOSACCESS = _LanOpticsSystemCMOSACCESS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 7)
)
_SnSysCMOSACCESSOffset_Type = Integer32
_SnSysCMOSACCESSOffset_Object = MibScalar
snSysCMOSACCESSOffset = _SnSysCMOSACCESSOffset_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 7, 1),
    _SnSysCMOSACCESSOffset_Type()
)
snSysCMOSACCESSOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSACCESSOffset.setStatus("mandatory")
_SnSysCMOSACCESSLength_Type = Integer32
_SnSysCMOSACCESSLength_Object = MibScalar
snSysCMOSACCESSLength = _SnSysCMOSACCESSLength_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 7, 2),
    _SnSysCMOSACCESSLength_Type()
)
snSysCMOSACCESSLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSACCESSLength.setStatus("mandatory")
_SnSysCMOSACCESSSequence_Type = Integer32
_SnSysCMOSACCESSSequence_Object = MibScalar
snSysCMOSACCESSSequence = _SnSysCMOSACCESSSequence_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 7, 3),
    _SnSysCMOSACCESSSequence_Type()
)
snSysCMOSACCESSSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSACCESSSequence.setStatus("mandatory")
_LanOpticsSystemCMOSBRDG_ObjectIdentity = ObjectIdentity
lanOpticsSystemCMOSBRDG = _LanOpticsSystemCMOSBRDG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 8)
)
_SnSysCMOSBRDGradius_Type = Integer32
_SnSysCMOSBRDGradius_Object = MibScalar
snSysCMOSBRDGradius = _SnSysCMOSBRDGradius_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 8, 1),
    _SnSysCMOSBRDGradius_Type()
)
snSysCMOSBRDGradius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSBRDGradius.setStatus("mandatory")


class _SnSysCMOSBRDGlinkNumber_Type(Integer32):
    """Custom type snSysCMOSBRDGlinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SnSysCMOSBRDGlinkNumber_Type.__name__ = "Integer32"
_SnSysCMOSBRDGlinkNumber_Object = MibScalar
snSysCMOSBRDGlinkNumber = _SnSysCMOSBRDGlinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 8, 2),
    _SnSysCMOSBRDGlinkNumber_Type()
)
snSysCMOSBRDGlinkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSBRDGlinkNumber.setStatus("mandatory")
_SnSysCMOSBRDGpassword_Type = DisplayString
_SnSysCMOSBRDGpassword_Object = MibScalar
snSysCMOSBRDGpassword = _SnSysCMOSBRDGpassword_Object(
    (1, 3, 6, 1, 4, 1, 224, 2, 3, 8, 3),
    _SnSysCMOSBRDGpassword_Type()
)
snSysCMOSBRDGpassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSysCMOSBRDGpassword.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANOPTICS-SYSTEM-MIB",
    **{"lanOptics": lanOptics,
       "lanOpticsSystem": lanOpticsSystem,
       "snSysDirectory": snSysDirectory,
       "snAgentVersion": snAgentVersion,
       "lanOpticsSystemCMOS": lanOpticsSystemCMOS,
       "lanOpticsSystemCMOSIp": lanOpticsSystemCMOSIp,
       "snSysCMOSIpInterfaceTable": snSysCMOSIpInterfaceTable,
       "snSysCMOSIpInterfaceEntry": snSysCMOSIpInterfaceEntry,
       "snSysCMOSIpIpAddr": snSysCMOSIpIpAddr,
       "snSysCMOSIpNetMask": snSysCMOSIpNetMask,
       "pysmiFakeCol1": pysmiFakeCol1,
       "snSysCMOSIpDefGw": snSysCMOSIpDefGw,
       "snSysCMOSIpTFTPOp": snSysCMOSIpTFTPOp,
       "snSysCMOSIpTFTPAddr": snSysCMOSIpTFTPAddr,
       "snSysCMOSIpTFTPFileName": snSysCMOSIpTFTPFileName,
       "snSysCMOSIpTFTPDrive": snSysCMOSIpTFTPDrive,
       "lanOpticsSystemCMOSHub": lanOpticsSystemCMOSHub,
       "snSysCMOSHubSlotConfigTable": snSysCMOSHubSlotConfigTable,
       "snSysCMOSHubSlotConfigEntry": snSysCMOSHubSlotConfigEntry,
       "snSysSlotLastOperations": snSysSlotLastOperations,
       "snSysResetSlotQueue": snSysResetSlotQueue,
       "pysmiFakeCol2": pysmiFakeCol2,
       "snSysCMOSHubSaveHubFunctions": snSysCMOSHubSaveHubFunctions,
       "lanOpticsSystemCMOSRPL": lanOpticsSystemCMOSRPL,
       "snSysCMOSRPLMode": snSysCMOSRPLMode,
       "snSysCMOSFlashMode": snSysCMOSFlashMode,
       "lanOpticsSystemCMOSSerial": lanOpticsSystemCMOSSerial,
       "snSysCMOSSerialMode": snSysCMOSSerialMode,
       "snSysCMOSSerialComSelect": snSysCMOSSerialComSelect,
       "snSysCMOSSerialBaudRate": snSysCMOSSerialBaudRate,
       "snSysCMOSSerialWordLength": snSysCMOSSerialWordLength,
       "snSysCMOSSerialStopBits": snSysCMOSSerialStopBits,
       "snSysCMOSSerialParityCheck": snSysCMOSSerialParityCheck,
       "lanOpticsSystemCMOSSRAM": lanOpticsSystemCMOSSRAM,
       "snSysCMOSSRAMKeepAliveSecInterval": snSysCMOSSRAMKeepAliveSecInterval,
       "lanOpticsSystemCMOSSNMP": lanOpticsSystemCMOSSNMP,
       "snSysCMOSSNMPCommunitiesNum": snSysCMOSSNMPCommunitiesNum,
       "snSysCMOSSNMPTrapManagersNum": snSysCMOSSNMPTrapManagersNum,
       "snSysCMOSSNMPCommunitiesTable": snSysCMOSSNMPCommunitiesTable,
       "snSysCMOSSNMPCommunitiesEntry": snSysCMOSSNMPCommunitiesEntry,
       "snSysCMOSSNMPCommunityName": snSysCMOSSNMPCommunityName,
       "snSysCMOSSNMPCommunityPrivs": snSysCMOSSNMPCommunityPrivs,
       "pysmiFakeCol3": pysmiFakeCol3,
       "snSysCMOSSNMPTrapCommunitiesTable": snSysCMOSSNMPTrapCommunitiesTable,
       "snSysCMOSSNMPTrapCommunitiesEntry": snSysCMOSSNMPTrapCommunitiesEntry,
       "snSysCMOSSNMPTrapCommunityIpAddr": snSysCMOSSNMPTrapCommunityIpAddr,
       "pysmiFakeCol4": pysmiFakeCol4,
       "lanOpticsSystemCMOSACCESS": lanOpticsSystemCMOSACCESS,
       "snSysCMOSACCESSOffset": snSysCMOSACCESSOffset,
       "snSysCMOSACCESSLength": snSysCMOSACCESSLength,
       "snSysCMOSACCESSSequence": snSysCMOSACCESSSequence,
       "lanOpticsSystemCMOSBRDG": lanOpticsSystemCMOSBRDG,
       "snSysCMOSBRDGradius": snSysCMOSBRDGradius,
       "snSysCMOSBRDGlinkNumber": snSysCMOSBRDGlinkNumber,
       "snSysCMOSBRDGpassword": snSysCMOSBRDGpassword}
)
