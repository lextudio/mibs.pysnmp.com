# SNMP MIB module (Fx8210-private) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fx8210-private
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:28 2024
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
    (0, "Fx8210-private", "rTrapAddrAddr"),
)
if mibBuilder.loadTexts:
    rTrapAddrEntry.setStatus("mandatory")
_RTrapAddrAddr_Type = IpAddress
_RTrapAddrAddr_Object = MibTableColumn
rTrapAddrAddr = _RTrapAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 1),
    _RTrapAddrAddr_Type()
)
rTrapAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTrapAddrAddr.setStatus("mandatory")
_RTrapAddrComm_Type = OctetString
_RTrapAddrComm_Object = MibTableColumn
rTrapAddrComm = _RTrapAddrComm_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 2),
    _RTrapAddrComm_Type()
)
rTrapAddrComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTrapAddrComm.setStatus("mandatory")
_RTrapAddrVer_Type = Integer32
_RTrapAddrVer_Object = MibTableColumn
rTrapAddrVer = _RTrapAddrVer_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 3),
    _RTrapAddrVer_Type()
)
rTrapAddrVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTrapAddrVer.setStatus("mandatory")
_RTrapAddrType_Type = OctetString
_RTrapAddrType_Object = MibTableColumn
rTrapAddrType = _RTrapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 4),
    _RTrapAddrType_Type()
)
rTrapAddrType.setMaxAccess("read-only")
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
rTrapAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTrapAddrState.setStatus("mandatory")


class _RTrapAddrFlag_Type(Integer32):
    """Custom type rTrapAddrFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("removable", 1))
    )


_RTrapAddrFlag_Type.__name__ = "Integer32"
_RTrapAddrFlag_Object = MibTableColumn
rTrapAddrFlag = _RTrapAddrFlag_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 6),
    _RTrapAddrFlag_Type()
)
rTrapAddrFlag.setMaxAccess("read-only")
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
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
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
    (0, "Fx8210-private", "pTrapAddrAddr"),
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
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
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
_EventTrap_Type = OctetString
_EventTrap_Object = MibScalar
eventTrap = _EventTrap_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 3, 1),
    _EventTrap_Type()
)
eventTrap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTrap.setStatus("mandatory")
_Fxm8000_ObjectIdentity = ObjectIdentity
fxm8000 = _Fxm8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 10)
)
_Finexsystem_ObjectIdentity = ObjectIdentity
finexsystem = _Finexsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 10, 1)
)
_Fxmsystemrun_ObjectIdentity = ObjectIdentity
fxmsystemrun = _Fxmsystemrun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 1)
)
_FxmSystemIpAddr_Type = IpAddress
_FxmSystemIpAddr_Object = MibScalar
fxmSystemIpAddr = _FxmSystemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 1, 1),
    _FxmSystemIpAddr_Type()
)
fxmSystemIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxmSystemIpAddr.setStatus("mandatory")
_FxmSystemIPNetMask_Type = IpAddress
_FxmSystemIPNetMask_Object = MibScalar
fxmSystemIPNetMask = _FxmSystemIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 1, 2),
    _FxmSystemIPNetMask_Type()
)
fxmSystemIPNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxmSystemIPNetMask.setStatus("mandatory")
_FxmSystemIPDefGway_Type = IpAddress
_FxmSystemIPDefGway_Object = MibScalar
fxmSystemIPDefGway = _FxmSystemIPDefGway_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 1, 3),
    _FxmSystemIPDefGway_Type()
)
fxmSystemIPDefGway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxmSystemIPDefGway.setStatus("mandatory")
_FxmSystemBroadcastOpt_Type = IpAddress
_FxmSystemBroadcastOpt_Object = MibScalar
fxmSystemBroadcastOpt = _FxmSystemBroadcastOpt_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 1, 4),
    _FxmSystemBroadcastOpt_Type()
)
fxmSystemBroadcastOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxmSystemBroadcastOpt.setStatus("mandatory")
_FxmSystemBootServer_Type = IpAddress
_FxmSystemBootServer_Object = MibScalar
fxmSystemBootServer = _FxmSystemBootServer_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 1, 5),
    _FxmSystemBootServer_Type()
)
fxmSystemBootServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxmSystemBootServer.setStatus("mandatory")
_FxmSystemBootGenName_Type = OctetString
_FxmSystemBootGenName_Object = MibScalar
fxmSystemBootGenName = _FxmSystemBootGenName_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 1, 6),
    _FxmSystemBootGenName_Type()
)
fxmSystemBootGenName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxmSystemBootGenName.setStatus("mandatory")


class _FxmSystemBootMode_Type(Integer32):
    """Custom type fxmSystemBootMode based on Integer32"""
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


_FxmSystemBootMode_Type.__name__ = "Integer32"
_FxmSystemBootMode_Object = MibScalar
fxmSystemBootMode = _FxmSystemBootMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 1, 7),
    _FxmSystemBootMode_Type()
)
fxmSystemBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxmSystemBootMode.setStatus("mandatory")


class _FxmSystemSelfTestLevel_Type(Integer32):
    """Custom type fxmSystemSelfTestLevel based on Integer32"""
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
        *(("extended", 4),
          ("full", 2),
          ("none", 1),
          ("partial", 3))
    )


_FxmSystemSelfTestLevel_Type.__name__ = "Integer32"
_FxmSystemSelfTestLevel_Object = MibScalar
fxmSystemSelfTestLevel = _FxmSystemSelfTestLevel_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 1, 8),
    _FxmSystemSelfTestLevel_Type()
)
fxmSystemSelfTestLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxmSystemSelfTestLevel.setStatus("mandatory")


class _FxmSystemReset_Type(Integer32):
    """Custom type fxmSystemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cold-reset", 2),
          ("warm-reset", 1))
    )


_FxmSystemReset_Type.__name__ = "Integer32"
_FxmSystemReset_Object = MibScalar
fxmSystemReset = _FxmSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 1, 9),
    _FxmSystemReset_Type()
)
fxmSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxmSystemReset.setStatus("mandatory")
_Fxmsystemperm_ObjectIdentity = ObjectIdentity
fxmsystemperm = _Fxmsystemperm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2)
)
_PfxmSystemIpAddr_Type = IpAddress
_PfxmSystemIpAddr_Object = MibScalar
pfxmSystemIpAddr = _PfxmSystemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 1),
    _PfxmSystemIpAddr_Type()
)
pfxmSystemIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfxmSystemIpAddr.setStatus("mandatory")
_PfxmSystemIPNetMask_Type = IpAddress
_PfxmSystemIPNetMask_Object = MibScalar
pfxmSystemIPNetMask = _PfxmSystemIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 2),
    _PfxmSystemIPNetMask_Type()
)
pfxmSystemIPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfxmSystemIPNetMask.setStatus("mandatory")
_PfxmSystemIPDefGway_Type = IpAddress
_PfxmSystemIPDefGway_Object = MibScalar
pfxmSystemIPDefGway = _PfxmSystemIPDefGway_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 3),
    _PfxmSystemIPDefGway_Type()
)
pfxmSystemIPDefGway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfxmSystemIPDefGway.setStatus("mandatory")
_PfxmSystemBroadcastOpt_Type = IpAddress
_PfxmSystemBroadcastOpt_Object = MibScalar
pfxmSystemBroadcastOpt = _PfxmSystemBroadcastOpt_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 4),
    _PfxmSystemBroadcastOpt_Type()
)
pfxmSystemBroadcastOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfxmSystemBroadcastOpt.setStatus("mandatory")
_PfxmSystemBootServer_Type = IpAddress
_PfxmSystemBootServer_Object = MibScalar
pfxmSystemBootServer = _PfxmSystemBootServer_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 5),
    _PfxmSystemBootServer_Type()
)
pfxmSystemBootServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfxmSystemBootServer.setStatus("mandatory")
_PfxmSystemBootGenName_Type = OctetString
_PfxmSystemBootGenName_Object = MibScalar
pfxmSystemBootGenName = _PfxmSystemBootGenName_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 6),
    _PfxmSystemBootGenName_Type()
)
pfxmSystemBootGenName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfxmSystemBootGenName.setStatus("mandatory")


class _PfxmSystemBootMode_Type(Integer32):
    """Custom type pfxmSystemBootMode based on Integer32"""
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


_PfxmSystemBootMode_Type.__name__ = "Integer32"
_PfxmSystemBootMode_Object = MibScalar
pfxmSystemBootMode = _PfxmSystemBootMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 7),
    _PfxmSystemBootMode_Type()
)
pfxmSystemBootMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfxmSystemBootMode.setStatus("mandatory")


class _PfxmSystemSelfTestLevel_Type(Integer32):
    """Custom type pfxmSystemSelfTestLevel based on Integer32"""
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
        *(("extended", 4),
          ("full", 2),
          ("none", 1),
          ("partial", 3))
    )


_PfxmSystemSelfTestLevel_Type.__name__ = "Integer32"
_PfxmSystemSelfTestLevel_Object = MibScalar
pfxmSystemSelfTestLevel = _PfxmSystemSelfTestLevel_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 8),
    _PfxmSystemSelfTestLevel_Type()
)
pfxmSystemSelfTestLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfxmSystemSelfTestLevel.setStatus("mandatory")


class _PfxmSpanMode_Type(Integer32):
    """Custom type pfxmSpanMode based on Integer32"""
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


_PfxmSpanMode_Type.__name__ = "Integer32"
_PfxmSpanMode_Object = MibScalar
pfxmSpanMode = _PfxmSpanMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 9),
    _PfxmSpanMode_Type()
)
pfxmSpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pfxmSpanMode.setStatus("mandatory")
_PfxmSystemCommunity1_Type = OctetString
_PfxmSystemCommunity1_Object = MibScalar
pfxmSystemCommunity1 = _PfxmSystemCommunity1_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 10),
    _PfxmSystemCommunity1_Type()
)
pfxmSystemCommunity1.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pfxmSystemCommunity1.setStatus("mandatory")
_PfxmSystemCommunity2_Type = OctetString
_PfxmSystemCommunity2_Object = MibScalar
pfxmSystemCommunity2 = _PfxmSystemCommunity2_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 11),
    _PfxmSystemCommunity2_Type()
)
pfxmSystemCommunity2.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pfxmSystemCommunity2.setStatus("mandatory")
_PfxmSystemCommunity3_Type = OctetString
_PfxmSystemCommunity3_Object = MibScalar
pfxmSystemCommunity3 = _PfxmSystemCommunity3_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 12),
    _PfxmSystemCommunity3_Type()
)
pfxmSystemCommunity3.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pfxmSystemCommunity3.setStatus("mandatory")
_PfxmSystemCommunity4_Type = OctetString
_PfxmSystemCommunity4_Object = MibScalar
pfxmSystemCommunity4 = _PfxmSystemCommunity4_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 13),
    _PfxmSystemCommunity4_Type()
)
pfxmSystemCommunity4.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pfxmSystemCommunity4.setStatus("mandatory")
_PfxmSystemCommunity5_Type = OctetString
_PfxmSystemCommunity5_Object = MibScalar
pfxmSystemCommunity5 = _PfxmSystemCommunity5_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 14),
    _PfxmSystemCommunity5_Type()
)
pfxmSystemCommunity5.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pfxmSystemCommunity5.setStatus("mandatory")
_PfxmSystemCommunity6_Type = OctetString
_PfxmSystemCommunity6_Object = MibScalar
pfxmSystemCommunity6 = _PfxmSystemCommunity6_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 15),
    _PfxmSystemCommunity6_Type()
)
pfxmSystemCommunity6.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pfxmSystemCommunity6.setStatus("mandatory")
_PfxmSystemCommunity7_Type = OctetString
_PfxmSystemCommunity7_Object = MibScalar
pfxmSystemCommunity7 = _PfxmSystemCommunity7_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 16),
    _PfxmSystemCommunity7_Type()
)
pfxmSystemCommunity7.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pfxmSystemCommunity7.setStatus("mandatory")
_PfxmSystemCommunity8_Type = OctetString
_PfxmSystemCommunity8_Object = MibScalar
pfxmSystemCommunity8 = _PfxmSystemCommunity8_Object(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 2, 17),
    _PfxmSystemCommunity8_Type()
)
pfxmSystemCommunity8.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pfxmSystemCommunity8.setStatus("mandatory")

# Managed Objects groups


# Notification objects

sendGenericEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 22, 10, 1, 0, 1)
)
sendGenericEvent.setObjects(
    ("Fx8210-private", "eventTrap")
)
if mibBuilder.loadTexts:
    sendGenericEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fx8210-private",
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
       "eventTrap": eventTrap,
       "fxm8000": fxm8000,
       "finexsystem": finexsystem,
       "sendGenericEvent": sendGenericEvent,
       "fxmsystemrun": fxmsystemrun,
       "fxmSystemIpAddr": fxmSystemIpAddr,
       "fxmSystemIPNetMask": fxmSystemIPNetMask,
       "fxmSystemIPDefGway": fxmSystemIPDefGway,
       "fxmSystemBroadcastOpt": fxmSystemBroadcastOpt,
       "fxmSystemBootServer": fxmSystemBootServer,
       "fxmSystemBootGenName": fxmSystemBootGenName,
       "fxmSystemBootMode": fxmSystemBootMode,
       "fxmSystemSelfTestLevel": fxmSystemSelfTestLevel,
       "fxmSystemReset": fxmSystemReset,
       "fxmsystemperm": fxmsystemperm,
       "pfxmSystemIpAddr": pfxmSystemIpAddr,
       "pfxmSystemIPNetMask": pfxmSystemIPNetMask,
       "pfxmSystemIPDefGway": pfxmSystemIPDefGway,
       "pfxmSystemBroadcastOpt": pfxmSystemBroadcastOpt,
       "pfxmSystemBootServer": pfxmSystemBootServer,
       "pfxmSystemBootGenName": pfxmSystemBootGenName,
       "pfxmSystemBootMode": pfxmSystemBootMode,
       "pfxmSystemSelfTestLevel": pfxmSystemSelfTestLevel,
       "pfxmSpanMode": pfxmSpanMode,
       "pfxmSystemCommunity1": pfxmSystemCommunity1,
       "pfxmSystemCommunity2": pfxmSystemCommunity2,
       "pfxmSystemCommunity3": pfxmSystemCommunity3,
       "pfxmSystemCommunity4": pfxmSystemCommunity4,
       "pfxmSystemCommunity5": pfxmSystemCommunity5,
       "pfxmSystemCommunity6": pfxmSystemCommunity6,
       "pfxmSystemCommunity7": pfxmSystemCommunity7,
       "pfxmSystemCommunity8": pfxmSystemCommunity8}
)
