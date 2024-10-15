# SNMP MIB module (Hub-facs-prvt) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Hub-facs-prvt
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:54 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
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
    (0, "Hub-facs-prvt", "rTrapAddrAddr"),
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
    (0, "Hub-facs-prvt", "pTrapAddrAddr"),
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
_FmSystemLastSourceIpAddr_Type = IpAddress
_FmSystemLastSourceIpAddr_Object = MibScalar
fmSystemLastSourceIpAddr = _FmSystemLastSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 20),
    _FmSystemLastSourceIpAddr_Type()
)
fmSystemLastSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSystemLastSourceIpAddr.setStatus("mandatory")
_FmSystemLastDestinationIpAddr_Type = IpAddress
_FmSystemLastDestinationIpAddr_Object = MibScalar
fmSystemLastDestinationIpAddr = _FmSystemLastDestinationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 1, 1, 21),
    _FmSystemLastDestinationIpAddr_Type()
)
fmSystemLastDestinationIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSystemLastDestinationIpAddr.setStatus("mandatory")
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
_Fmdiag_ObjectIdentity = ObjectIdentity
fmdiag = _Fmdiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 5)
)


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
    (0, "Hub-facs-prvt", "fmDiagFaultIndex"),
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
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("debug-mode", 2),
          ("normal-mode", 1))
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


class _FmDiagDeleteFaults_Type(Integer32):
    """Custom type fmDiagDeleteFaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("no-delete", 1))
    )


_FmDiagDeleteFaults_Type.__name__ = "Integer32"
_FmDiagDeleteFaults_Object = MibScalar
fmDiagDeleteFaults = _FmDiagDeleteFaults_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 5, 5),
    _FmDiagDeleteFaults_Type()
)
fmDiagDeleteFaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmDiagDeleteFaults.setStatus("mandatory")
_Fmdebug_ObjectIdentity = ObjectIdentity
fmdebug = _Fmdebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 51, 6)
)
_FmDebugReadMem_Type = OctetString
_FmDebugReadMem_Object = MibScalar
fmDebugReadMem = _FmDebugReadMem_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 6, 1),
    _FmDebugReadMem_Type()
)
fmDebugReadMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDebugReadMem.setStatus("mandatory")
_FmDebugReadEeprom_Type = OctetString
_FmDebugReadEeprom_Object = MibScalar
fmDebugReadEeprom = _FmDebugReadEeprom_Object(
    (1, 3, 6, 1, 4, 1, 22, 51, 6, 2),
    _FmDebugReadEeprom_Type()
)
fmDebugReadEeprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDebugReadEeprom.setStatus("mandatory")

# Managed Objects groups


# Notification objects

fmDiagGenericTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 30)
)
fmDiagGenericTrap.setObjects(
    ("Hub-facs-prvt", "fmDiagTrapInfo")
)
if mibBuilder.loadTexts:
    fmDiagGenericTrap.setStatus(
        ""
    )

fmDiagDownloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 51, 0, 31)
)
fmDiagDownloadTrap.setObjects(
      *(("Hub-facs-prvt", "fmSystemLastSourceIpAddr"),
        ("Hub-facs-prvt", "fmSystemLastDestinationIpAddr"))
)
if mibBuilder.loadTexts:
    fmDiagDownloadTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Hub-facs-prvt",
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
       "fmDiagGenericTrap": fmDiagGenericTrap,
       "fmDiagDownloadTrap": fmDiagDownloadTrap,
       "fmsystem": fmsystem,
       "fmsystemrun": fmsystemrun,
       "fmSystemReset": fmSystemReset,
       "fmSystemSelfTestLevel": fmSystemSelfTestLevel,
       "fmSystemIpAddr": fmSystemIpAddr,
       "fmSystemIPNetMask": fmSystemIPNetMask,
       "fmSystemIPDefGway": fmSystemIPDefGway,
       "fmSystemFileServer": fmSystemFileServer,
       "fmSystemBootFile": fmSystemBootFile,
       "fmSystemDownLoad": fmSystemDownLoad,
       "fmSystemSlipIpAddr": fmSystemSlipIpAddr,
       "fmSystemSlipIPNetMask": fmSystemSlipIPNetMask,
       "fmSystemSlipBaudRate": fmSystemSlipBaudRate,
       "fmSystemSlipParity": fmSystemSlipParity,
       "fmSystemSlipStopBits": fmSystemSlipStopBits,
       "fmSystemLastSourceIpAddr": fmSystemLastSourceIpAddr,
       "fmSystemLastDestinationIpAddr": fmSystemLastDestinationIpAddr,
       "fmsystemperm": fmsystemperm,
       "pfmSystemIpAddr": pfmSystemIpAddr,
       "pfmSystemIPNetMask": pfmSystemIPNetMask,
       "pfmSystemIPDefGway": pfmSystemIPDefGway,
       "pfmSystemFileServer": pfmSystemFileServer,
       "pfmSystemBootFile": pfmSystemBootFile,
       "pfmSystemReadCommunity": pfmSystemReadCommunity,
       "pfmSystemWriteCommunity": pfmSystemWriteCommunity,
       "pfmSystemSlipIpAddr": pfmSystemSlipIpAddr,
       "pfmSystemSlipIPNetMask": pfmSystemSlipIPNetMask,
       "pfmSystemSlipBaudRate": pfmSystemSlipBaudRate,
       "pfmSystemSlipParity": pfmSystemSlipParity,
       "pfmSystemSlipStopBits": pfmSystemSlipStopBits,
       "fmdiag": fmdiag,
       "fmDiagTrapInfo": fmDiagTrapInfo,
       "fmDiagFaultTable": fmDiagFaultTable,
       "fmDiagFaultEntry": fmDiagFaultEntry,
       "fmDiagFaultIndex": fmDiagFaultIndex,
       "fmDiagFaultReport": fmDiagFaultReport,
       "fmDiagDebug": fmDiagDebug,
       "fmDiagDeleteFaults": fmDiagDeleteFaults,
       "fmdebug": fmdebug,
       "fmDebugReadMem": fmDebugReadMem,
       "fmDebugReadEeprom": fmDebugReadEeprom}
)
