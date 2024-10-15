# SNMP MIB module (EDB-snmp) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EDB-snmp
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:32 2024
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
 internet,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "internet",
    "iso",
    "mgmt")

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

_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Fibronics_ObjectIdentity = ObjectIdentity
fibronics = _Fibronics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22)
)
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 3)
)
_Traprun_ObjectIdentity = ObjectIdentity
traprun = _Traprun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 3, 1)
)
_RTrapAddrTbl_Object = MibTable
rTrapAddrTbl = _RTrapAddrTbl_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rTrapAddrTbl.setStatus("mandatory")
_RTrapAddrEntry_Object = MibTableRow
rTrapAddrEntry = _RTrapAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1)
)
rTrapAddrEntry.setIndexNames(
    (0, "EDB-snmp", "rTrapAddrAddr"),
)
if mibBuilder.loadTexts:
    rTrapAddrEntry.setStatus("mandatory")
_RTrapAddrAddr_Type = IpAddress
_RTrapAddrAddr_Object = MibTableColumn
rTrapAddrAddr = _RTrapAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 1),
    _RTrapAddrAddr_Type()
)
rTrapAddrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rTrapAddrAddr.setStatus("mandatory")
_RTrapAddrComm_Type = OctetString
_RTrapAddrComm_Object = MibTableColumn
rTrapAddrComm = _RTrapAddrComm_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 2),
    _RTrapAddrComm_Type()
)
rTrapAddrComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rTrapAddrComm.setStatus("mandatory")
_RTrapAddrVer_Type = Integer32
_RTrapAddrVer_Object = MibTableColumn
rTrapAddrVer = _RTrapAddrVer_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 3),
    _RTrapAddrVer_Type()
)
rTrapAddrVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rTrapAddrVer.setStatus("mandatory")
_RTrapAddrType_Type = OctetString
_RTrapAddrType_Object = MibTableColumn
rTrapAddrType = _RTrapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 4),
    _RTrapAddrType_Type()
)
rTrapAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rTrapAddrType.setStatus("mandatory")


class _RTrapAddrState_Type(Integer32):
    """Custom type rTrapAddrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RTrapAddrState_Type.__name__ = "Integer32"
_RTrapAddrState_Object = MibTableColumn
rTrapAddrState = _RTrapAddrState_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 5),
    _RTrapAddrState_Type()
)
rTrapAddrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rTrapAddrState.setStatus("mandatory")


class _RTrapAddrFlag_Type(Integer32):
    """Custom type rTrapAddrFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("removable", 1))
    )


_RTrapAddrFlag_Type.__name__ = "Integer32"
_RTrapAddrFlag_Object = MibTableColumn
rTrapAddrFlag = _RTrapAddrFlag_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 6),
    _RTrapAddrFlag_Type()
)
rTrapAddrFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rTrapAddrFlag.setStatus("mandatory")
_RTrapAddrAge_Type = Integer32
_RTrapAddrAge_Object = MibTableColumn
rTrapAddrAge = _RTrapAddrAge_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 7),
    _RTrapAddrAge_Type()
)
rTrapAddrAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTrapAddrAge.setStatus("mandatory")


class _RTrapLearning_Type(Integer32):
    """Custom type rTrapLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RTrapLearning_Type.__name__ = "Integer32"
_RTrapLearning_Object = MibScalar
rTrapLearning = _RTrapLearning_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 2),
    _RTrapLearning_Type()
)
rTrapLearning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTrapLearning.setStatus("mandatory")
_RTrapAging_Type = Integer32
_RTrapAging_Object = MibScalar
rTrapAging = _RTrapAging_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 3),
    _RTrapAging_Type()
)
rTrapAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTrapAging.setStatus("mandatory")
_Traperm_ObjectIdentity = ObjectIdentity
traperm = _Traperm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 3, 2)
)
_PTrapAddrTbl_Object = MibTable
pTrapAddrTbl = _PTrapAddrTbl_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 1)
)
if mibBuilder.loadTexts:
    pTrapAddrTbl.setStatus("mandatory")
_PTrapAddrEntry_Object = MibTableRow
pTrapAddrEntry = _PTrapAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 1, 1)
)
pTrapAddrEntry.setIndexNames(
    (0, "EDB-snmp", "pTrapAddrAddr"),
)
if mibBuilder.loadTexts:
    pTrapAddrEntry.setStatus("mandatory")
_PTrapAddrAddr_Type = IpAddress
_PTrapAddrAddr_Object = MibTableColumn
pTrapAddrAddr = _PTrapAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 1, 1, 1),
    _PTrapAddrAddr_Type()
)
pTrapAddrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapAddrAddr.setStatus("mandatory")
_PTrapAddrComm_Type = OctetString
_PTrapAddrComm_Object = MibTableColumn
pTrapAddrComm = _PTrapAddrComm_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 1, 1, 2),
    _PTrapAddrComm_Type()
)
pTrapAddrComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapAddrComm.setStatus("mandatory")
_PTrapAddrVer_Type = Integer32
_PTrapAddrVer_Object = MibTableColumn
pTrapAddrVer = _PTrapAddrVer_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 1, 1, 3),
    _PTrapAddrVer_Type()
)
pTrapAddrVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapAddrVer.setStatus("mandatory")
_PTrapAddrType_Type = OctetString
_PTrapAddrType_Object = MibTableColumn
pTrapAddrType = _PTrapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 1, 1, 4),
    _PTrapAddrType_Type()
)
pTrapAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapAddrType.setStatus("mandatory")


class _PTrapAddrState_Type(Integer32):
    """Custom type pTrapAddrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_PTrapAddrState_Type.__name__ = "Integer32"
_PTrapAddrState_Object = MibTableColumn
pTrapAddrState = _PTrapAddrState_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 1, 1, 5),
    _PTrapAddrState_Type()
)
pTrapAddrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapAddrState.setStatus("mandatory")


class _PTrapLearning_Type(Integer32):
    """Custom type pTrapLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PTrapLearning_Type.__name__ = "Integer32"
_PTrapLearning_Object = MibScalar
pTrapLearning = _PTrapLearning_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 2),
    _PTrapLearning_Type()
)
pTrapLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapLearning.setStatus("mandatory")
_PTrapAging_Type = Integer32
_PTrapAging_Object = MibScalar
pTrapAging = _PTrapAging_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 3),
    _PTrapAging_Type()
)
pTrapAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapAging.setStatus("mandatory")
_Trapvar_ObjectIdentity = ObjectIdentity
trapvar = _Trapvar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 3, 3)
)
_Fm800_ObjectIdentity = ObjectIdentity
fm800 = _Fm800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51)
)
_Fmsystem_ObjectIdentity = ObjectIdentity
fmsystem = _Fmsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 1)
)
_Fmsystemrun_ObjectIdentity = ObjectIdentity
fmsystemrun = _Fmsystemrun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1)
)


class _FmSystemPSAdmin_Type(Integer32):
    """Custom type fmSystemPSAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary-power", 1),
          ("secondary-power", 2))
    )


_FmSystemPSAdmin_Type.__name__ = "Integer32"
_FmSystemPSAdmin_Object = MibScalar
fmSystemPSAdmin = _FmSystemPSAdmin_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 1),
    _FmSystemPSAdmin_Type()
)
fmSystemPSAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmSystemPSAdmin.setStatus("mandatory")


class _FmSystemPSOper_Type(Integer32):
    """Custom type fmSystemPSOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary-power", 1),
          ("secondary-power", 2))
    )


_FmSystemPSOper_Type.__name__ = "Integer32"
_FmSystemPSOper_Object = MibScalar
fmSystemPSOper = _FmSystemPSOper_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 2),
    _FmSystemPSOper_Type()
)
fmSystemPSOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSystemPSOper.setStatus("mandatory")


class _FmSystemPSCfg_Type(Integer32):
    """Custom type fmSystemPSCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary-and-secondary-power", 3),
          ("primary-power", 1),
          ("secondary-power", 2))
    )


_FmSystemPSCfg_Type.__name__ = "Integer32"
_FmSystemPSCfg_Object = MibScalar
fmSystemPSCfg = _FmSystemPSCfg_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 3),
    _FmSystemPSCfg_Type()
)
fmSystemPSCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmSystemPSCfg.setStatus("mandatory")


class _FmSystemReset_Type(Integer32):
    """Custom type fmSystemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              127)
        )
    )
    namedValues = NamedValues(
        *(("cold-reset", 0),
          ("meaning-less-value", 127),
          ("power-up", 2),
          ("warm-reset", 1))
    )


_FmSystemReset_Type.__name__ = "Integer32"
_FmSystemReset_Object = MibScalar
fmSystemReset = _FmSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 4),
    _FmSystemReset_Type()
)
fmSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmSystemReset.setStatus("mandatory")


class _FmSystemSelfTestLevel_Type(Integer32):
    """Custom type fmSystemSelfTestLevel based on Integer32"""
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
        *(("extended", 3),
          ("full", 2),
          ("none", 0),
          ("partial", 1))
    )


_FmSystemSelfTestLevel_Type.__name__ = "Integer32"
_FmSystemSelfTestLevel_Object = MibScalar
fmSystemSelfTestLevel = _FmSystemSelfTestLevel_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 5),
    _FmSystemSelfTestLevel_Type()
)
fmSystemSelfTestLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmSystemSelfTestLevel.setStatus("mandatory")
_FmSystemVersion_Type = OctetString
_FmSystemVersion_Object = MibScalar
fmSystemVersion = _FmSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 6),
    _FmSystemVersion_Type()
)
fmSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSystemVersion.setStatus("mandatory")
_FmSystemIpAddr_Type = IpAddress
_FmSystemIpAddr_Object = MibScalar
fmSystemIpAddr = _FmSystemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 7),
    _FmSystemIpAddr_Type()
)
fmSystemIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSystemIpAddr.setStatus("mandatory")
_FmSystemIPNetMask_Type = IpAddress
_FmSystemIPNetMask_Object = MibScalar
fmSystemIPNetMask = _FmSystemIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 8),
    _FmSystemIPNetMask_Type()
)
fmSystemIPNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSystemIPNetMask.setStatus("mandatory")
_FmSystemIPDefGway_Type = IpAddress
_FmSystemIPDefGway_Object = MibScalar
fmSystemIPDefGway = _FmSystemIPDefGway_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 9),
    _FmSystemIPDefGway_Type()
)
fmSystemIPDefGway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSystemIPDefGway.setStatus("mandatory")
_FmSystemFileServer_Type = IpAddress
_FmSystemFileServer_Object = MibScalar
fmSystemFileServer = _FmSystemFileServer_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 10),
    _FmSystemFileServer_Type()
)
fmSystemFileServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmSystemFileServer.setStatus("mandatory")
_FmSystemBootFile_Type = OctetString
_FmSystemBootFile_Object = MibScalar
fmSystemBootFile = _FmSystemBootFile_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 11),
    _FmSystemBootFile_Type()
)
fmSystemBootFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSystemBootFile.setStatus("mandatory")


class _FmSystemBootMode_Type(Integer32):
    """Custom type fmSystemBootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("internal-memory", 1))
    )


_FmSystemBootMode_Type.__name__ = "Integer32"
_FmSystemBootMode_Object = MibScalar
fmSystemBootMode = _FmSystemBootMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 12),
    _FmSystemBootMode_Type()
)
fmSystemBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSystemBootMode.setStatus("deprecated")


class _FmSystemDownLoad_Type(Integer32):
    """Custom type fmSystemDownLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              127)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("meaning-less-value", 127))
    )


_FmSystemDownLoad_Type.__name__ = "Integer32"
_FmSystemDownLoad_Object = MibScalar
fmSystemDownLoad = _FmSystemDownLoad_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 13),
    _FmSystemDownLoad_Type()
)
fmSystemDownLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmSystemDownLoad.setStatus("mandatory")
_FmSystemSlipIpAddr_Type = IpAddress
_FmSystemSlipIpAddr_Object = MibScalar
fmSystemSlipIpAddr = _FmSystemSlipIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 14),
    _FmSystemSlipIpAddr_Type()
)
fmSystemSlipIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSystemSlipIpAddr.setStatus("mandatory")
_FmSystemSlipIPNetMask_Type = IpAddress
_FmSystemSlipIPNetMask_Object = MibScalar
fmSystemSlipIPNetMask = _FmSystemSlipIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 15),
    _FmSystemSlipIPNetMask_Type()
)
fmSystemSlipIPNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSystemSlipIPNetMask.setStatus("mandatory")


class _FmSystemSlipBaudRate_Type(Integer32):
    """Custom type fmSystemSlipBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("baud1200", 0),
          ("baud19200", 4),
          ("baud2400", 1),
          ("baud38400", 5),
          ("baud4800", 2),
          ("baud9600", 3))
    )


_FmSystemSlipBaudRate_Type.__name__ = "Integer32"
_FmSystemSlipBaudRate_Object = MibScalar
fmSystemSlipBaudRate = _FmSystemSlipBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 16),
    _FmSystemSlipBaudRate_Type()
)
fmSystemSlipBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSystemSlipBaudRate.setStatus("mandatory")


class _FmSystemSlipParity_Type(Integer32):
    """Custom type fmSystemSlipParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 0),
          ("odd", 1))
    )


_FmSystemSlipParity_Type.__name__ = "Integer32"
_FmSystemSlipParity_Object = MibScalar
fmSystemSlipParity = _FmSystemSlipParity_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 17),
    _FmSystemSlipParity_Type()
)
fmSystemSlipParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSystemSlipParity.setStatus("mandatory")


class _FmSystemSlipStopBits_Type(Integer32):
    """Custom type fmSystemSlipStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("one", 0),
          ("two", 1))
    )


_FmSystemSlipStopBits_Type.__name__ = "Integer32"
_FmSystemSlipStopBits_Object = MibScalar
fmSystemSlipStopBits = _FmSystemSlipStopBits_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 18),
    _FmSystemSlipStopBits_Type()
)
fmSystemSlipStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSystemSlipStopBits.setStatus("mandatory")
_Fmsystemperm_ObjectIdentity = ObjectIdentity
fmsystemperm = _Fmsystemperm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 2)
)
_PfmSystemIpAddr_Type = IpAddress
_PfmSystemIpAddr_Object = MibScalar
pfmSystemIpAddr = _PfmSystemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 2, 7),
    _PfmSystemIpAddr_Type()
)
pfmSystemIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfmSystemIpAddr.setStatus("mandatory")
_PfmSystemIPNetMask_Type = IpAddress
_PfmSystemIPNetMask_Object = MibScalar
pfmSystemIPNetMask = _PfmSystemIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 2, 8),
    _PfmSystemIPNetMask_Type()
)
pfmSystemIPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfmSystemIPNetMask.setStatus("mandatory")
_PfmSystemIPDefGway_Type = IpAddress
_PfmSystemIPDefGway_Object = MibScalar
pfmSystemIPDefGway = _PfmSystemIPDefGway_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 2, 9),
    _PfmSystemIPDefGway_Type()
)
pfmSystemIPDefGway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfmSystemIPDefGway.setStatus("mandatory")
_PfmSystemFileServer_Type = IpAddress
_PfmSystemFileServer_Object = MibScalar
pfmSystemFileServer = _PfmSystemFileServer_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 2, 10),
    _PfmSystemFileServer_Type()
)
pfmSystemFileServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfmSystemFileServer.setStatus("mandatory")
_PfmSystemBootFile_Type = OctetString
_PfmSystemBootFile_Object = MibScalar
pfmSystemBootFile = _PfmSystemBootFile_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 2, 11),
    _PfmSystemBootFile_Type()
)
pfmSystemBootFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfmSystemBootFile.setStatus("mandatory")


class _PfmSystemBootMode_Type(Integer32):
    """Custom type pfmSystemBootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("internal-memory", 1))
    )


_PfmSystemBootMode_Type.__name__ = "Integer32"
_PfmSystemBootMode_Object = MibScalar
pfmSystemBootMode = _PfmSystemBootMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 2, 12),
    _PfmSystemBootMode_Type()
)
pfmSystemBootMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfmSystemBootMode.setStatus("mandatory")
_PfmSystemReadCommunity_Type = OctetString
_PfmSystemReadCommunity_Object = MibScalar
pfmSystemReadCommunity = _PfmSystemReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 2, 13),
    _PfmSystemReadCommunity_Type()
)
pfmSystemReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfmSystemReadCommunity.setStatus("mandatory")
_PfmSystemWriteCommunity_Type = OctetString
_PfmSystemWriteCommunity_Object = MibScalar
pfmSystemWriteCommunity = _PfmSystemWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 2, 14),
    _PfmSystemWriteCommunity_Type()
)
pfmSystemWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfmSystemWriteCommunity.setStatus("mandatory")
_PfmSystemSlipIpAddr_Type = IpAddress
_PfmSystemSlipIpAddr_Object = MibScalar
pfmSystemSlipIpAddr = _PfmSystemSlipIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 2, 15),
    _PfmSystemSlipIpAddr_Type()
)
pfmSystemSlipIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfmSystemSlipIpAddr.setStatus("mandatory")
_PfmSystemSlipIPNetMask_Type = IpAddress
_PfmSystemSlipIPNetMask_Object = MibScalar
pfmSystemSlipIPNetMask = _PfmSystemSlipIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 2, 16),
    _PfmSystemSlipIPNetMask_Type()
)
pfmSystemSlipIPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfmSystemSlipIPNetMask.setStatus("mandatory")


class _PfmSystemSlipBaudRate_Type(Integer32):
    """Custom type pfmSystemSlipBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("baud1200", 0),
          ("baud19200", 4),
          ("baud2400", 1),
          ("baud38400", 5),
          ("baud4800", 2),
          ("baud9600", 3))
    )


_PfmSystemSlipBaudRate_Type.__name__ = "Integer32"
_PfmSystemSlipBaudRate_Object = MibScalar
pfmSystemSlipBaudRate = _PfmSystemSlipBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 2, 17),
    _PfmSystemSlipBaudRate_Type()
)
pfmSystemSlipBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfmSystemSlipBaudRate.setStatus("mandatory")


class _PfmSystemSlipParity_Type(Integer32):
    """Custom type pfmSystemSlipParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 0),
          ("odd", 1))
    )


_PfmSystemSlipParity_Type.__name__ = "Integer32"
_PfmSystemSlipParity_Object = MibScalar
pfmSystemSlipParity = _PfmSystemSlipParity_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 2, 18),
    _PfmSystemSlipParity_Type()
)
pfmSystemSlipParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfmSystemSlipParity.setStatus("mandatory")


class _PfmSystemSlipStopBits_Type(Integer32):
    """Custom type pfmSystemSlipStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("one", 0),
          ("two", 1))
    )


_PfmSystemSlipStopBits_Type.__name__ = "Integer32"
_PfmSystemSlipStopBits_Object = MibScalar
pfmSystemSlipStopBits = _PfmSystemSlipStopBits_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 2, 19),
    _PfmSystemSlipStopBits_Type()
)
pfmSystemSlipStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfmSystemSlipStopBits.setStatus("mandatory")
_Fmslot_ObjectIdentity = ObjectIdentity
fmslot = _Fmslot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 2)
)
_FmSlotMasterClear_Type = Integer32
_FmSlotMasterClear_Object = MibScalar
fmSlotMasterClear = _FmSlotMasterClear_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 2, 1),
    _FmSlotMasterClear_Type()
)
fmSlotMasterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmSlotMasterClear.setStatus("mandatory")
_FmSlotTable_Object = MibTable
fmSlotTable = _FmSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 2, 2)
)
if mibBuilder.loadTexts:
    fmSlotTable.setStatus("mandatory")
_FmSlotEntry_Object = MibTableRow
fmSlotEntry = _FmSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 2, 2, 1)
)
fmSlotEntry.setIndexNames(
    (0, "EDB-snmp", "fmSlotIndex"),
)
if mibBuilder.loadTexts:
    fmSlotEntry.setStatus("mandatory")
_FmSlotIndex_Type = Integer32
_FmSlotIndex_Object = MibTableColumn
fmSlotIndex = _FmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 2, 2, 1, 1),
    _FmSlotIndex_Type()
)
fmSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSlotIndex.setStatus("mandatory")


class _FmSlotID_Type(Integer32):
    """Custom type fmSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              65537,
              65540,
              65541,
              65542,
              65543,
              65544,
              65545,
              65548,
              65550,
              65551,
              65552,
              65553,
              65557,
              65558,
              65559,
              65560,
              65562,
              65563,
              65566,
              65567,
              65568,
              65576,
              65578,
              65580,
              65584,
              65588,
              65589,
              65590,
              65591,
              65592,
              65594,
              65595,
              131072,
              131073,
              131075,
              131077)
        )
    )
    namedValues = NamedValues(
        *(("cc832-10", 2),
          ("cc832-10-ID", 65541),
          ("cc832-12", 3),
          ("cc832-12-ID", 65542),
          ("cc832-20", 4),
          ("cc832-20-ID", 65543),
          ("cc832-31", 5),
          ("cc832-32", 6),
          ("cc832-41", 7),
          ("cc832-41-ID", 65557),
          ("cc832-42", 8),
          ("cc832-42-ID", 65558),
          ("cc832-44", 9),
          ("cc832-44-ID", 65559),
          ("cc832-46A", 10),
          ("cc892-201", 65544),
          ("cc892-202", 65545),
          ("cc892-211", 65550),
          ("cc892-212", 65551),
          ("cc892-214", 65548),
          ("cc892-233", 65568),
          ("cc892-240", 65594),
          ("cc892-241", 65595),
          ("cc892-260", 65576),
          ("cc892-301", 65560),
          ("cc892-303", 65562),
          ("cc892-308", 65563),
          ("cc892-321", 65552),
          ("cc892-401", 65592),
          ("cc892-420", 65589),
          ("cc892-421", 65591),
          ("cc892-422", 65590),
          ("cc892-427", 65580),
          ("cc892-432", 65588),
          ("cc892-46B", 65553),
          ("cc892-832", 65537),
          ("empty", 1),
          ("general-smartcard", 131072),
          ("lc303", 65566),
          ("lc303-129", 131075),
          ("lc308", 65567),
          ("lc308-129", 131073),
          ("lc312", 65578),
          ("lc312-129", 131077),
          ("lc322", 65540),
          ("sw892-11X", 65584),
          ("unconfig", 0))
    )


_FmSlotID_Type.__name__ = "Integer32"
_FmSlotID_Object = MibTableColumn
fmSlotID = _FmSlotID_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 2, 2, 1, 2),
    _FmSlotID_Type()
)
fmSlotID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmSlotID.setStatus("mandatory")
_FmSlotDescr_Type = OctetString
_FmSlotDescr_Object = MibTableColumn
fmSlotDescr = _FmSlotDescr_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 2, 2, 1, 3),
    _FmSlotDescr_Type()
)
fmSlotDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSlotDescr.setStatus("mandatory")
_FmSlotInfo_Type = OctetString
_FmSlotInfo_Object = MibTableColumn
fmSlotInfo = _FmSlotInfo_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 2, 2, 1, 4),
    _FmSlotInfo_Type()
)
fmSlotInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmSlotInfo.setStatus("mandatory")
_FmSlotStatus_Type = OctetString
_FmSlotStatus_Object = MibTableColumn
fmSlotStatus = _FmSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 2, 2, 1, 5),
    _FmSlotStatus_Type()
)
fmSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSlotStatus.setStatus("mandatory")
_FmSlotPrevStatus_Type = OctetString
_FmSlotPrevStatus_Object = MibTableColumn
fmSlotPrevStatus = _FmSlotPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 2, 2, 1, 6),
    _FmSlotPrevStatus_Type()
)
fmSlotPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSlotPrevStatus.setStatus("mandatory")
_FmSlotRLBSet_Type = Integer32
_FmSlotRLBSet_Object = MibTableColumn
fmSlotRLBSet = _FmSlotRLBSet_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 2, 2, 1, 7),
    _FmSlotRLBSet_Type()
)
fmSlotRLBSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmSlotRLBSet.setStatus("mandatory")
_FmSlotRLBClear_Type = Integer32
_FmSlotRLBClear_Object = MibTableColumn
fmSlotRLBClear = _FmSlotRLBClear_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 2, 2, 1, 8),
    _FmSlotRLBClear_Type()
)
fmSlotRLBClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmSlotRLBClear.setStatus("mandatory")
_FmSlotExpCode_Type = Integer32
_FmSlotExpCode_Object = MibTableColumn
fmSlotExpCode = _FmSlotExpCode_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 2, 2, 1, 9),
    _FmSlotExpCode_Type()
)
fmSlotExpCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmSlotExpCode.setStatus("mandatory")


class _FmSlotTrapMask_Type(Integer32):
    """Custom type fmSlotTrapMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("no-mask", 0))
    )


_FmSlotTrapMask_Type.__name__ = "Integer32"
_FmSlotTrapMask_Object = MibTableColumn
fmSlotTrapMask = _FmSlotTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 2, 2, 1, 10),
    _FmSlotTrapMask_Type()
)
fmSlotTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmSlotTrapMask.setStatus("mandatory")


class _PfmSlotTrapMask_Type(Integer32):
    """Custom type pfmSlotTrapMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("no-mask", 0))
    )


_PfmSlotTrapMask_Type.__name__ = "Integer32"
_PfmSlotTrapMask_Object = MibTableColumn
pfmSlotTrapMask = _PfmSlotTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 2, 2, 1, 11),
    _PfmSlotTrapMask_Type()
)
pfmSlotTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfmSlotTrapMask.setStatus("mandatory")
_FmSlotIpAddr_Type = IpAddress
_FmSlotIpAddr_Object = MibTableColumn
fmSlotIpAddr = _FmSlotIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 2, 2, 1, 12),
    _FmSlotIpAddr_Type()
)
fmSlotIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSlotIpAddr.setStatus("mandatory")
_Fmlu_ObjectIdentity = ObjectIdentity
fmlu = _Fmlu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 3)
)


class _FmLUID_Type(Integer32):
    """Custom type fmLUID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("lu100", 2),
          ("lu101", 3),
          ("lu102", 4),
          ("lu103", 5),
          ("lu104", 6),
          ("lu105", 7),
          ("lu106", 8),
          ("lu107", 9),
          ("lu108", 10),
          ("none", 1),
          ("unconfig", 0))
    )


_FmLUID_Type.__name__ = "Integer32"
_FmLUID_Object = MibScalar
fmLUID = _FmLUID_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 3, 1),
    _FmLUID_Type()
)
fmLUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmLUID.setStatus("mandatory")
_FmLUDescr_Type = OctetString
_FmLUDescr_Object = MibScalar
fmLUDescr = _FmLUDescr_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 3, 2),
    _FmLUDescr_Type()
)
fmLUDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmLUDescr.setStatus("mandatory")
_FmLUStatus_Type = OctetString
_FmLUStatus_Object = MibScalar
fmLUStatus = _FmLUStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 3, 3),
    _FmLUStatus_Type()
)
fmLUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmLUStatus.setStatus("mandatory")


class _FmLULinkSelect_Type(Integer32):
    """Custom type fmLULinkSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("main-link", 0),
          ("sec-link", 1))
    )


_FmLULinkSelect_Type.__name__ = "Integer32"
_FmLULinkSelect_Object = MibScalar
fmLULinkSelect = _FmLULinkSelect_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 3, 4),
    _FmLULinkSelect_Type()
)
fmLULinkSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmLULinkSelect.setStatus("mandatory")
_FmLULoopBackSet_Type = Integer32
_FmLULoopBackSet_Object = MibScalar
fmLULoopBackSet = _FmLULoopBackSet_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 3, 5),
    _FmLULoopBackSet_Type()
)
fmLULoopBackSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmLULoopBackSet.setStatus("mandatory")
_FmLULoopBackClr_Type = Integer32
_FmLULoopBackClr_Object = MibScalar
fmLULoopBackClr = _FmLULoopBackClr_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 3, 6),
    _FmLULoopBackClr_Type()
)
fmLULoopBackClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmLULoopBackClr.setStatus("mandatory")


class _FmLUTrapMask_Type(Integer32):
    """Custom type fmLUTrapMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("no-mask", 0))
    )


_FmLUTrapMask_Type.__name__ = "Integer32"
_FmLUTrapMask_Object = MibScalar
fmLUTrapMask = _FmLUTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 3, 7),
    _FmLUTrapMask_Type()
)
fmLUTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmLUTrapMask.setStatus("mandatory")


class _PfmLUTrapMask_Type(Integer32):
    """Custom type pfmLUTrapMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("no-mask", 0))
    )


_PfmLUTrapMask_Type.__name__ = "Integer32"
_PfmLUTrapMask_Object = MibScalar
pfmLUTrapMask = _PfmLUTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 3, 8),
    _PfmLUTrapMask_Type()
)
pfmLUTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfmLUTrapMask.setStatus("mandatory")
_Fmdiag_ObjectIdentity = ObjectIdentity
fmdiag = _Fmdiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 5)
)
_FmDiagConfig_Type = OctetString
_FmDiagConfig_Object = MibScalar
fmDiagConfig = _FmDiagConfig_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 5, 1),
    _FmDiagConfig_Type()
)
fmDiagConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDiagConfig.setStatus("mandatory")


class _FmDiagTrapInfo_Type(DisplayString):
    """Custom type fmDiagTrapInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FmDiagTrapInfo_Type.__name__ = "DisplayString"
_FmDiagTrapInfo_Object = MibScalar
fmDiagTrapInfo = _FmDiagTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 5, 2),
    _FmDiagTrapInfo_Type()
)
fmDiagTrapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDiagTrapInfo.setStatus("mandatory")
_FmDiagFaultTable_Object = MibTable
fmDiagFaultTable = _FmDiagFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 5, 3)
)
if mibBuilder.loadTexts:
    fmDiagFaultTable.setStatus("optional")
_FmDiagFaultEntry_Object = MibTableRow
fmDiagFaultEntry = _FmDiagFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 5, 3, 1)
)
fmDiagFaultEntry.setIndexNames(
    (0, "EDB-snmp", "fmDiagFaultIndex"),
)
if mibBuilder.loadTexts:
    fmDiagFaultEntry.setStatus("optional")
_FmDiagFaultIndex_Type = Integer32
_FmDiagFaultIndex_Object = MibTableColumn
fmDiagFaultIndex = _FmDiagFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 5, 3, 1, 1),
    _FmDiagFaultIndex_Type()
)
fmDiagFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDiagFaultIndex.setStatus("optional")


class _FmDiagFaultReport_Type(DisplayString):
    """Custom type fmDiagFaultReport based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FmDiagFaultReport_Type.__name__ = "DisplayString"
_FmDiagFaultReport_Object = MibTableColumn
fmDiagFaultReport = _FmDiagFaultReport_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 5, 3, 1, 2),
    _FmDiagFaultReport_Type()
)
fmDiagFaultReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDiagFaultReport.setStatus("optional")


class _FmDiagDebug_Type(Integer32):
    """Custom type fmDiagDebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("debug-mode", 1),
          ("normal-mode", 0))
    )


_FmDiagDebug_Type.__name__ = "Integer32"
_FmDiagDebug_Object = MibScalar
fmDiagDebug = _FmDiagDebug_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 5, 4),
    _FmDiagDebug_Type()
)
fmDiagDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmDiagDebug.setStatus("mandatory")

# Managed Objects groups


# Notification objects

fmPowerSupplyFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 1)
)
fmPowerSupplyFail.setObjects(
    ("EDB-snmp", "fmSystemPSOper")
)
if mibBuilder.loadTexts:
    fmPowerSupplyFail.setStatus(
        ""
    )

fmPrimaryPowerSupplyOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 2)
)
fmPrimaryPowerSupplyOK.setObjects(
    ("EDB-snmp", "fmSystemPSOper")
)
if mibBuilder.loadTexts:
    fmPrimaryPowerSupplyOK.setStatus(
        ""
    )

fmSecondPowerSupplyOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 3)
)
fmSecondPowerSupplyOK.setObjects(
    ("EDB-snmp", "fmSystemPSOper")
)
if mibBuilder.loadTexts:
    fmSecondPowerSupplyOK.setStatus(
        ""
    )

fmPowerSupplyChangeConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 4)
)
fmPowerSupplyChangeConfig.setObjects(
      *(("EDB-snmp", "fmSystemPSCfg"),
        ("EDB-snmp", "fmSystemPSOper"))
)
if mibBuilder.loadTexts:
    fmPowerSupplyChangeConfig.setStatus(
        ""
    )

fmLUOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 7)
)
fmLUOutOfSync.setObjects(
      *(("EDB-snmp", "fmLUID"),
        ("EDB-snmp", "fmLUStatus"))
)
if mibBuilder.loadTexts:
    fmLUOutOfSync.setStatus(
        ""
    )

fmLUReturnToSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 8)
)
fmLUReturnToSync.setObjects(
      *(("EDB-snmp", "fmLUID"),
        ("EDB-snmp", "fmLUStatus"))
)
if mibBuilder.loadTexts:
    fmLUReturnToSync.setStatus(
        ""
    )

fmLUPassToMain = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 9)
)
fmLUPassToMain.setObjects(
      *(("EDB-snmp", "fmLUID"),
        ("EDB-snmp", "fmLUStatus"))
)
if mibBuilder.loadTexts:
    fmLUPassToMain.setStatus(
        ""
    )

fmLUPassToSecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 10)
)
fmLUPassToSecond.setObjects(
      *(("EDB-snmp", "fmLUID"),
        ("EDB-snmp", "fmLUStatus"))
)
if mibBuilder.loadTexts:
    fmLUPassToSecond.setStatus(
        ""
    )

fmLUPrimaryLinkFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 11)
)
fmLUPrimaryLinkFail.setObjects(
      *(("EDB-snmp", "fmLUID"),
        ("EDB-snmp", "fmLUStatus"))
)
if mibBuilder.loadTexts:
    fmLUPrimaryLinkFail.setStatus(
        ""
    )

fmLUPrimaryLinkOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 12)
)
fmLUPrimaryLinkOK.setObjects(
      *(("EDB-snmp", "fmLUID"),
        ("EDB-snmp", "fmLUStatus"))
)
if mibBuilder.loadTexts:
    fmLUPrimaryLinkOK.setStatus(
        ""
    )

fmLUSecondLinkFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 13)
)
fmLUSecondLinkFail.setObjects(
      *(("EDB-snmp", "fmLUID"),
        ("EDB-snmp", "fmLUStatus"))
)
if mibBuilder.loadTexts:
    fmLUSecondLinkFail.setStatus(
        ""
    )

fmLUSecondLinkOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 14)
)
fmLUSecondLinkOK.setObjects(
      *(("EDB-snmp", "fmLUID"),
        ("EDB-snmp", "fmLUStatus"))
)
if mibBuilder.loadTexts:
    fmLUSecondLinkOK.setStatus(
        ""
    )

fmLULLBOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 15)
)
fmLULLBOn.setObjects(
      *(("EDB-snmp", "fmLUID"),
        ("EDB-snmp", "fmLUStatus"))
)
if mibBuilder.loadTexts:
    fmLULLBOn.setStatus(
        ""
    )

fmLULLBOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 16)
)
fmLULLBOff.setObjects(
      *(("EDB-snmp", "fmLUID"),
        ("EDB-snmp", "fmLUStatus"))
)
if mibBuilder.loadTexts:
    fmLULLBOff.setStatus(
        ""
    )

fmLUChangeConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 20)
)
fmLUChangeConfig.setObjects(
      *(("EDB-snmp", "fmLUID"),
        ("EDB-snmp", "fmLUStatus"))
)
if mibBuilder.loadTexts:
    fmLUChangeConfig.setStatus(
        ""
    )

fmSlotTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 25)
)
fmSlotTrap.setObjects(
      *(("EDB-snmp", "fmSlotIndex"),
        ("EDB-snmp", "fmSlotID"),
        ("EDB-snmp", "fmSlotStatus"),
        ("EDB-snmp", "fmSlotPrevStatus"))
)
if mibBuilder.loadTexts:
    fmSlotTrap.setStatus(
        ""
    )

fmSlotChangeConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 26)
)
fmSlotChangeConfig.setObjects(
      *(("EDB-snmp", "fmSlotIndex"),
        ("EDB-snmp", "fmSlotID"),
        ("EDB-snmp", "fmSlotStatus"))
)
if mibBuilder.loadTexts:
    fmSlotChangeConfig.setStatus(
        ""
    )

fmDiagGenericTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 30)
)
fmDiagGenericTrap.setObjects(
    ("EDB-snmp", "fmDiagTrapInfo")
)
if mibBuilder.loadTexts:
    fmDiagGenericTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EDB-snmp",
    **{"private": private,
       "enterprises": enterprises,
       "fibronics": fibronics,
       "trap": trap,
       "traprun": traprun,
       "rTrapAddrTbl": rTrapAddrTbl,
       "rTrapAddrEntry": rTrapAddrEntry,
       "rTrapAddrAddr": rTrapAddrAddr,
       "rTrapAddrComm": rTrapAddrComm,
       "rTrapAddrVer": rTrapAddrVer,
       "rTrapAddrType": rTrapAddrType,
       "rTrapAddrState": rTrapAddrState,
       "rTrapAddrFlag": rTrapAddrFlag,
       "rTrapAddrAge": rTrapAddrAge,
       "rTrapLearning": rTrapLearning,
       "rTrapAging": rTrapAging,
       "traperm": traperm,
       "pTrapAddrTbl": pTrapAddrTbl,
       "pTrapAddrEntry": pTrapAddrEntry,
       "pTrapAddrAddr": pTrapAddrAddr,
       "pTrapAddrComm": pTrapAddrComm,
       "pTrapAddrVer": pTrapAddrVer,
       "pTrapAddrType": pTrapAddrType,
       "pTrapAddrState": pTrapAddrState,
       "pTrapLearning": pTrapLearning,
       "pTrapAging": pTrapAging,
       "trapvar": trapvar,
       "fm800": fm800,
       "fmPowerSupplyFail": fmPowerSupplyFail,
       "fmPrimaryPowerSupplyOK": fmPrimaryPowerSupplyOK,
       "fmSecondPowerSupplyOK": fmSecondPowerSupplyOK,
       "fmPowerSupplyChangeConfig": fmPowerSupplyChangeConfig,
       "fmLUOutOfSync": fmLUOutOfSync,
       "fmLUReturnToSync": fmLUReturnToSync,
       "fmLUPassToMain": fmLUPassToMain,
       "fmLUPassToSecond": fmLUPassToSecond,
       "fmLUPrimaryLinkFail": fmLUPrimaryLinkFail,
       "fmLUPrimaryLinkOK": fmLUPrimaryLinkOK,
       "fmLUSecondLinkFail": fmLUSecondLinkFail,
       "fmLUSecondLinkOK": fmLUSecondLinkOK,
       "fmLULLBOn": fmLULLBOn,
       "fmLULLBOff": fmLULLBOff,
       "fmLUChangeConfig": fmLUChangeConfig,
       "fmSlotTrap": fmSlotTrap,
       "fmSlotChangeConfig": fmSlotChangeConfig,
       "fmDiagGenericTrap": fmDiagGenericTrap,
       "fmsystem": fmsystem,
       "fmsystemrun": fmsystemrun,
       "fmSystemPSAdmin": fmSystemPSAdmin,
       "fmSystemPSOper": fmSystemPSOper,
       "fmSystemPSCfg": fmSystemPSCfg,
       "fmSystemReset": fmSystemReset,
       "fmSystemSelfTestLevel": fmSystemSelfTestLevel,
       "fmSystemVersion": fmSystemVersion,
       "fmSystemIpAddr": fmSystemIpAddr,
       "fmSystemIPNetMask": fmSystemIPNetMask,
       "fmSystemIPDefGway": fmSystemIPDefGway,
       "fmSystemFileServer": fmSystemFileServer,
       "fmSystemBootFile": fmSystemBootFile,
       "fmSystemBootMode": fmSystemBootMode,
       "fmSystemDownLoad": fmSystemDownLoad,
       "fmSystemSlipIpAddr": fmSystemSlipIpAddr,
       "fmSystemSlipIPNetMask": fmSystemSlipIPNetMask,
       "fmSystemSlipBaudRate": fmSystemSlipBaudRate,
       "fmSystemSlipParity": fmSystemSlipParity,
       "fmSystemSlipStopBits": fmSystemSlipStopBits,
       "fmsystemperm": fmsystemperm,
       "pfmSystemIpAddr": pfmSystemIpAddr,
       "pfmSystemIPNetMask": pfmSystemIPNetMask,
       "pfmSystemIPDefGway": pfmSystemIPDefGway,
       "pfmSystemFileServer": pfmSystemFileServer,
       "pfmSystemBootFile": pfmSystemBootFile,
       "pfmSystemBootMode": pfmSystemBootMode,
       "pfmSystemReadCommunity": pfmSystemReadCommunity,
       "pfmSystemWriteCommunity": pfmSystemWriteCommunity,
       "pfmSystemSlipIpAddr": pfmSystemSlipIpAddr,
       "pfmSystemSlipIPNetMask": pfmSystemSlipIPNetMask,
       "pfmSystemSlipBaudRate": pfmSystemSlipBaudRate,
       "pfmSystemSlipParity": pfmSystemSlipParity,
       "pfmSystemSlipStopBits": pfmSystemSlipStopBits,
       "fmslot": fmslot,
       "fmSlotMasterClear": fmSlotMasterClear,
       "fmSlotTable": fmSlotTable,
       "fmSlotEntry": fmSlotEntry,
       "fmSlotIndex": fmSlotIndex,
       "fmSlotID": fmSlotID,
       "fmSlotDescr": fmSlotDescr,
       "fmSlotInfo": fmSlotInfo,
       "fmSlotStatus": fmSlotStatus,
       "fmSlotPrevStatus": fmSlotPrevStatus,
       "fmSlotRLBSet": fmSlotRLBSet,
       "fmSlotRLBClear": fmSlotRLBClear,
       "fmSlotExpCode": fmSlotExpCode,
       "fmSlotTrapMask": fmSlotTrapMask,
       "pfmSlotTrapMask": pfmSlotTrapMask,
       "fmSlotIpAddr": fmSlotIpAddr,
       "fmlu": fmlu,
       "fmLUID": fmLUID,
       "fmLUDescr": fmLUDescr,
       "fmLUStatus": fmLUStatus,
       "fmLULinkSelect": fmLULinkSelect,
       "fmLULoopBackSet": fmLULoopBackSet,
       "fmLULoopBackClr": fmLULoopBackClr,
       "fmLUTrapMask": fmLUTrapMask,
       "pfmLUTrapMask": pfmLUTrapMask,
       "fmdiag": fmdiag,
       "fmDiagConfig": fmDiagConfig,
       "fmDiagTrapInfo": fmDiagTrapInfo,
       "fmDiagFaultTable": fmDiagFaultTable,
       "fmDiagFaultEntry": fmDiagFaultEntry,
       "fmDiagFaultIndex": fmDiagFaultIndex,
       "fmDiagFaultReport": fmDiagFaultReport,
       "fmDiagDebug": fmDiagDebug}
)
