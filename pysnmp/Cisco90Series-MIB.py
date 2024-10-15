# SNMP MIB module (Cisco90Series-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Cisco90Series-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:46 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoTelesend_ObjectIdentity = ObjectIdentity
ciscoTelesend = _CiscoTelesend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1570)
)
_FrMux_ObjectIdentity = ObjectIdentity
frMux = _FrMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1570, 1)
)
_FrxSys_ObjectIdentity = ObjectIdentity
frxSys = _FrxSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1570, 1, 1)
)


class _FrxSysDescr_Type(DisplayString):
    """Custom type frxSysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FrxSysDescr_Type.__name__ = "DisplayString"
_FrxSysDescr_Object = MibScalar
frxSysDescr = _FrxSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 1, 1),
    _FrxSysDescr_Type()
)
frxSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxSysDescr.setStatus("mandatory")


class _FrxClockHour_Type(Integer32):
    """Custom type frxClockHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_FrxClockHour_Type.__name__ = "Integer32"
_FrxClockHour_Object = MibScalar
frxClockHour = _FrxClockHour_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 1, 2),
    _FrxClockHour_Type()
)
frxClockHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxClockHour.setStatus("mandatory")


class _FrxClockMin_Type(Integer32):
    """Custom type frxClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_FrxClockMin_Type.__name__ = "Integer32"
_FrxClockMin_Object = MibScalar
frxClockMin = _FrxClockMin_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 1, 3),
    _FrxClockMin_Type()
)
frxClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxClockMin.setStatus("mandatory")


class _FrxClockSec_Type(Integer32):
    """Custom type frxClockSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_FrxClockSec_Type.__name__ = "Integer32"
_FrxClockSec_Object = MibScalar
frxClockSec = _FrxClockSec_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 1, 4),
    _FrxClockSec_Type()
)
frxClockSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxClockSec.setStatus("mandatory")
_FrxUpTime_Type = TimeTicks
_FrxUpTime_Object = MibScalar
frxUpTime = _FrxUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 1, 5),
    _FrxUpTime_Type()
)
frxUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxUpTime.setStatus("mandatory")


class _FrxAdminContact_Type(DisplayString):
    """Custom type frxAdminContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FrxAdminContact_Type.__name__ = "DisplayString"
_FrxAdminContact_Object = MibScalar
frxAdminContact = _FrxAdminContact_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 1, 6),
    _FrxAdminContact_Type()
)
frxAdminContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxAdminContact.setStatus("mandatory")


class _FrxSysName_Type(DisplayString):
    """Custom type frxSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FrxSysName_Type.__name__ = "DisplayString"
_FrxSysName_Object = MibScalar
frxSysName = _FrxSysName_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 1, 7),
    _FrxSysName_Type()
)
frxSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxSysName.setStatus("mandatory")


class _FrxSysLoc_Type(DisplayString):
    """Custom type frxSysLoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FrxSysLoc_Type.__name__ = "DisplayString"
_FrxSysLoc_Object = MibScalar
frxSysLoc = _FrxSysLoc_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 1, 8),
    _FrxSysLoc_Type()
)
frxSysLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxSysLoc.setStatus("mandatory")


class _FrxSysVersion_Type(Integer32):
    """Custom type frxSysVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxSysVersion_Type.__name__ = "Integer32"
_FrxSysVersion_Object = MibScalar
frxSysVersion = _FrxSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 1, 9),
    _FrxSysVersion_Type()
)
frxSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxSysVersion.setStatus("mandatory")


class _FrxUPerfTrapEnable_Type(Integer32):
    """Custom type frxUPerfTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableUPerfTrap", 2),
          ("enableUPerfTrap", 1))
    )


_FrxUPerfTrapEnable_Type.__name__ = "Integer32"
_FrxUPerfTrapEnable_Object = MibScalar
frxUPerfTrapEnable = _FrxUPerfTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 1, 10),
    _FrxUPerfTrapEnable_Type()
)
frxUPerfTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxUPerfTrapEnable.setStatus("mandatory")
_FrxAgtLinkErrors_Type = Counter32
_FrxAgtLinkErrors_Object = MibScalar
frxAgtLinkErrors = _FrxAgtLinkErrors_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 1, 11),
    _FrxAgtLinkErrors_Type()
)
frxAgtLinkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxAgtLinkErrors.setStatus("mandatory")
_FrxAgtProtErrors_Type = Counter32
_FrxAgtProtErrors_Object = MibScalar
frxAgtProtErrors = _FrxAgtProtErrors_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 1, 12),
    _FrxAgtProtErrors_Type()
)
frxAgtProtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxAgtProtErrors.setStatus("mandatory")
_FrxAgtChInactive_Type = Counter32
_FrxAgtChInactive_Object = MibScalar
frxAgtChInactive = _FrxAgtChInactive_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 1, 13),
    _FrxAgtChInactive_Type()
)
frxAgtChInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxAgtChInactive.setStatus("mandatory")


class _FrxAgtChStatus_Type(Integer32):
    """Custom type frxAgtChStatus based on Integer32"""
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


_FrxAgtChStatus_Type.__name__ = "Integer32"
_FrxAgtChStatus_Object = MibScalar
frxAgtChStatus = _FrxAgtChStatus_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 1, 14),
    _FrxAgtChStatus_Type()
)
frxAgtChStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxAgtChStatus.setStatus("mandatory")
_FrxDefault_ObjectIdentity = ObjectIdentity
frxDefault = _FrxDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1570, 1, 2)
)


class _FrxDefaultEnable_Type(Integer32):
    """Custom type frxDefaultEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableAutoLoad", 2),
          ("enableAutoLoad", 1))
    )


_FrxDefaultEnable_Type.__name__ = "Integer32"
_FrxDefaultEnable_Object = MibScalar
frxDefaultEnable = _FrxDefaultEnable_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 2, 1),
    _FrxDefaultEnable_Type()
)
frxDefaultEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxDefaultEnable.setStatus("mandatory")


class _FrxDefaultTrap_Type(Integer32):
    """Custom type frxDefaultTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableConfigureTrap", 2),
          ("enableConfigureTrap", 1))
    )


_FrxDefaultTrap_Type.__name__ = "Integer32"
_FrxDefaultTrap_Object = MibScalar
frxDefaultTrap = _FrxDefaultTrap_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 2, 2),
    _FrxDefaultTrap_Type()
)
frxDefaultTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxDefaultTrap.setStatus("mandatory")


class _FrxDConfigSrc_Type(Integer32):
    """Custom type frxDConfigSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("annexD", 1),
          ("snmp", 2))
    )


_FrxDConfigSrc_Type.__name__ = "Integer32"
_FrxDConfigSrc_Object = MibScalar
frxDConfigSrc = _FrxDConfigSrc_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 2, 3),
    _FrxDConfigSrc_Type()
)
frxDConfigSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxDConfigSrc.setStatus("mandatory")


class _FrxDMgtT391_Type(Integer32):
    """Custom type frxDMgtT391 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrxDMgtT391_Type.__name__ = "Integer32"
_FrxDMgtT391_Object = MibScalar
frxDMgtT391 = _FrxDMgtT391_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 2, 4),
    _FrxDMgtT391_Type()
)
frxDMgtT391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxDMgtT391.setStatus("mandatory")


class _FrxDMgtT392_Type(Integer32):
    """Custom type frxDMgtT392 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrxDMgtT392_Type.__name__ = "Integer32"
_FrxDMgtT392_Object = MibScalar
frxDMgtT392 = _FrxDMgtT392_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 2, 5),
    _FrxDMgtT392_Type()
)
frxDMgtT392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxDMgtT392.setStatus("mandatory")


class _FrxDMgtN391_Type(Integer32):
    """Custom type frxDMgtN391 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrxDMgtN391_Type.__name__ = "Integer32"
_FrxDMgtN391_Object = MibScalar
frxDMgtN391 = _FrxDMgtN391_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 2, 6),
    _FrxDMgtN391_Type()
)
frxDMgtN391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxDMgtN391.setStatus("mandatory")


class _FrxDMgtN392_Type(Integer32):
    """Custom type frxDMgtN392 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrxDMgtN392_Type.__name__ = "Integer32"
_FrxDMgtN392_Object = MibScalar
frxDMgtN392 = _FrxDMgtN392_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 2, 7),
    _FrxDMgtN392_Type()
)
frxDMgtN392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxDMgtN392.setStatus("mandatory")


class _FrxDMgtN393_Type(Integer32):
    """Custom type frxDMgtN393 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrxDMgtN393_Type.__name__ = "Integer32"
_FrxDMgtN393_Object = MibScalar
frxDMgtN393 = _FrxDMgtN393_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 2, 8),
    _FrxDMgtN393_Type()
)
frxDMgtN393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxDMgtN393.setStatus("mandatory")


class _FrxDPortSpeed_Type(Integer32):
    """Custom type frxDPortSpeed based on Integer32"""
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
        *(("use128kbps", 3),
          ("use144kbps", 4),
          ("use56kbps", 1),
          ("use64kbps", 2))
    )


_FrxDPortSpeed_Type.__name__ = "Integer32"
_FrxDPortSpeed_Object = MibScalar
frxDPortSpeed = _FrxDPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 2, 9),
    _FrxDPortSpeed_Type()
)
frxDPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxDPortSpeed.setStatus("mandatory")


class _FrxDPortProtocol_Type(Integer32):
    """Custom type frxDPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameRelay", 1),
          ("ppp", 2))
    )


_FrxDPortProtocol_Type.__name__ = "Integer32"
_FrxDPortProtocol_Object = MibScalar
frxDPortProtocol = _FrxDPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 2, 10),
    _FrxDPortProtocol_Type()
)
frxDPortProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxDPortProtocol.setStatus("mandatory")


class _FrxDCktCIR_Type(Integer32):
    """Custom type frxDCktCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1544000),
    )


_FrxDCktCIR_Type.__name__ = "Integer32"
_FrxDCktCIR_Object = MibScalar
frxDCktCIR = _FrxDCktCIR_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 2, 11),
    _FrxDCktCIR_Type()
)
frxDCktCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxDCktCIR.setStatus("mandatory")


class _FrxDCktBc_Type(Integer32):
    """Custom type frxDCktBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FrxDCktBc_Type.__name__ = "Integer32"
_FrxDCktBc_Object = MibScalar
frxDCktBc = _FrxDCktBc_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 2, 12),
    _FrxDCktBc_Type()
)
frxDCktBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxDCktBc.setStatus("mandatory")


class _FrxDCktBe_Type(Integer32):
    """Custom type frxDCktBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777212),
    )


_FrxDCktBe_Type.__name__ = "Integer32"
_FrxDCktBe_Object = MibScalar
frxDCktBe = _FrxDCktBe_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 2, 13),
    _FrxDCktBe_Type()
)
frxDCktBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxDCktBe.setStatus("mandatory")
_FrxBank_ObjectIdentity = ObjectIdentity
frxBank = _FrxBank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1570, 1, 3)
)
_FrxBankTable_Object = MibTable
frxBankTable = _FrxBankTable_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 3, 1)
)
if mibBuilder.loadTexts:
    frxBankTable.setStatus("mandatory")
_FrxBankEntry_Object = MibTableRow
frxBankEntry = _FrxBankEntry_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 3, 1, 1)
)
frxBankEntry.setIndexNames(
    (0, "Cisco90Series-MIB", "frxBankIndex"),
)
if mibBuilder.loadTexts:
    frxBankEntry.setStatus("mandatory")


class _FrxBankIndex_Type(Integer32):
    """Custom type frxBankIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_FrxBankIndex_Type.__name__ = "Integer32"
_FrxBankIndex_Object = MibTableColumn
frxBankIndex = _FrxBankIndex_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 3, 1, 1, 1),
    _FrxBankIndex_Type()
)
frxBankIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxBankIndex.setStatus("mandatory")


class _FrxBankType_Type(Integer32):
    """Custom type frxBankType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("d4", 1)
    )


_FrxBankType_Type.__name__ = "Integer32"
_FrxBankType_Object = MibTableColumn
frxBankType = _FrxBankType_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 3, 1, 1, 2),
    _FrxBankType_Type()
)
frxBankType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxBankType.setStatus("mandatory")
_FrxChUnit_ObjectIdentity = ObjectIdentity
frxChUnit = _FrxChUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4)
)
_FrxChUTable_Object = MibTable
frxChUTable = _FrxChUTable_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1)
)
if mibBuilder.loadTexts:
    frxChUTable.setStatus("mandatory")
_FrxChUEntry_Object = MibTableRow
frxChUEntry = _FrxChUEntry_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1)
)
frxChUEntry.setIndexNames(
    (0, "Cisco90Series-MIB", "frxBankIndex"),
    (0, "Cisco90Series-MIB", "frxChUIndex"),
)
if mibBuilder.loadTexts:
    frxChUEntry.setStatus("mandatory")


class _FrxChUIndex_Type(Integer32):
    """Custom type frxChUIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_FrxChUIndex_Type.__name__ = "Integer32"
_FrxChUIndex_Object = MibTableColumn
frxChUIndex = _FrxChUIndex_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 1),
    _FrxChUIndex_Type()
)
frxChUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxChUIndex.setStatus("mandatory")


class _FrxChUType_Type(Integer32):
    """Custom type frxChUType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            100
        )
    )
    namedValues = NamedValues(
        ("cisco90i", 100)
    )


_FrxChUType_Type.__name__ = "Integer32"
_FrxChUType_Object = MibTableColumn
frxChUType = _FrxChUType_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 2),
    _FrxChUType_Type()
)
frxChUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxChUType.setStatus("mandatory")


class _FrxChUVersion_Type(Integer32):
    """Custom type frxChUVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxChUVersion_Type.__name__ = "Integer32"
_FrxChUVersion_Object = MibTableColumn
frxChUVersion = _FrxChUVersion_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 3),
    _FrxChUVersion_Type()
)
frxChUVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxChUVersion.setStatus("mandatory")


class _FrxSigProtocol_Type(Integer32):
    """Custom type frxSigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("annexD", 1)
    )


_FrxSigProtocol_Type.__name__ = "Integer32"
_FrxSigProtocol_Object = MibTableColumn
frxSigProtocol = _FrxSigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 4),
    _FrxSigProtocol_Type()
)
frxSigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxSigProtocol.setStatus("mandatory")


class _FrxConfigSrc_Type(Integer32):
    """Custom type frxConfigSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("annexD", 1),
          ("snmp", 2))
    )


_FrxConfigSrc_Type.__name__ = "Integer32"
_FrxConfigSrc_Object = MibTableColumn
frxConfigSrc = _FrxConfigSrc_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 5),
    _FrxConfigSrc_Type()
)
frxConfigSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxConfigSrc.setStatus("mandatory")


class _FrxDLCIAdLen_Type(Integer32):
    """Custom type frxDLCIAdLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("twoOctetDlci", 1)
    )


_FrxDLCIAdLen_Type.__name__ = "Integer32"
_FrxDLCIAdLen_Object = MibTableColumn
frxDLCIAdLen = _FrxDLCIAdLen_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 6),
    _FrxDLCIAdLen_Type()
)
frxDLCIAdLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxDLCIAdLen.setStatus("mandatory")
_FrxNetInOctets_Type = Counter32
_FrxNetInOctets_Object = MibTableColumn
frxNetInOctets = _FrxNetInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 7),
    _FrxNetInOctets_Type()
)
frxNetInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxNetInOctets.setStatus("mandatory")
_FrxNetOutOctets_Type = Counter32
_FrxNetOutOctets_Object = MibTableColumn
frxNetOutOctets = _FrxNetOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 8),
    _FrxNetOutOctets_Type()
)
frxNetOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxNetOutOctets.setStatus("mandatory")
_FrxNetBadFrames_Type = Counter32
_FrxNetBadFrames_Object = MibTableColumn
frxNetBadFrames = _FrxNetBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 9),
    _FrxNetBadFrames_Type()
)
frxNetBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxNetBadFrames.setStatus("mandatory")
_FrxNetHDLCEs_Type = Counter32
_FrxNetHDLCEs_Object = MibTableColumn
frxNetHDLCEs = _FrxNetHDLCEs_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 10),
    _FrxNetHDLCEs_Type()
)
frxNetHDLCEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxNetHDLCEs.setStatus("mandatory")
_FrxNetCRCEs_Type = Counter32
_FrxNetCRCEs_Object = MibTableColumn
frxNetCRCEs = _FrxNetCRCEs_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 11),
    _FrxNetCRCEs_Type()
)
frxNetCRCEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxNetCRCEs.setStatus("mandatory")
_FrxNetLinkEs_Type = Counter32
_FrxNetLinkEs_Object = MibTableColumn
frxNetLinkEs = _FrxNetLinkEs_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 12),
    _FrxNetLinkEs_Type()
)
frxNetLinkEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxNetLinkEs.setStatus("mandatory")
_FrxNetFrShEs_Type = Counter32
_FrxNetFrShEs_Object = MibTableColumn
frxNetFrShEs = _FrxNetFrShEs_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 13),
    _FrxNetFrShEs_Type()
)
frxNetFrShEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxNetFrShEs.setStatus("mandatory")
_FrxNetFrLgEs_Type = Counter32
_FrxNetFrLgEs_Object = MibTableColumn
frxNetFrLgEs = _FrxNetFrLgEs_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 14),
    _FrxNetFrLgEs_Type()
)
frxNetFrLgEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxNetFrLgEs.setStatus("mandatory")
_FrxNetPPPEs_Type = Counter32
_FrxNetPPPEs_Object = MibTableColumn
frxNetPPPEs = _FrxNetPPPEs_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 15),
    _FrxNetPPPEs_Type()
)
frxNetPPPEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxNetPPPEs.setStatus("mandatory")
_FrxNetBufEs_Type = Counter32
_FrxNetBufEs_Object = MibTableColumn
frxNetBufEs = _FrxNetBufEs_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 4, 1, 1, 16),
    _FrxNetBufEs_Type()
)
frxNetBufEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxNetBufEs.setStatus("mandatory")
_FrxMgt_ObjectIdentity = ObjectIdentity
frxMgt = _FrxMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5)
)
_FrxMgtTable_Object = MibTable
frxMgtTable = _FrxMgtTable_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 1)
)
if mibBuilder.loadTexts:
    frxMgtTable.setStatus("mandatory")
_FrxMgtEntry_Object = MibTableRow
frxMgtEntry = _FrxMgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 1, 1)
)
frxMgtEntry.setIndexNames(
    (0, "Cisco90Series-MIB", "frxBankIndex"),
    (0, "Cisco90Series-MIB", "frxChUIndex"),
)
if mibBuilder.loadTexts:
    frxMgtEntry.setStatus("mandatory")


class _FrxPortsInSvc_Type(Integer32):
    """Custom type frxPortsInSvc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_FrxPortsInSvc_Type.__name__ = "Integer32"
_FrxPortsInSvc_Object = MibTableColumn
frxPortsInSvc = _FrxPortsInSvc_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 1, 1, 1),
    _FrxPortsInSvc_Type()
)
frxPortsInSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPortsInSvc.setStatus("mandatory")


class _FrxMgtT391_Type(Integer32):
    """Custom type frxMgtT391 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrxMgtT391_Type.__name__ = "Integer32"
_FrxMgtT391_Object = MibTableColumn
frxMgtT391 = _FrxMgtT391_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 1, 1, 2),
    _FrxMgtT391_Type()
)
frxMgtT391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxMgtT391.setStatus("mandatory")


class _FrxMgtT392_Type(Integer32):
    """Custom type frxMgtT392 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrxMgtT392_Type.__name__ = "Integer32"
_FrxMgtT392_Object = MibTableColumn
frxMgtT392 = _FrxMgtT392_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 1, 1, 3),
    _FrxMgtT392_Type()
)
frxMgtT392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxMgtT392.setStatus("mandatory")


class _FrxMgtN391_Type(Integer32):
    """Custom type frxMgtN391 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrxMgtN391_Type.__name__ = "Integer32"
_FrxMgtN391_Object = MibTableColumn
frxMgtN391 = _FrxMgtN391_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 1, 1, 4),
    _FrxMgtN391_Type()
)
frxMgtN391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxMgtN391.setStatus("mandatory")


class _FrxMgtN392_Type(Integer32):
    """Custom type frxMgtN392 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrxMgtN392_Type.__name__ = "Integer32"
_FrxMgtN392_Object = MibTableColumn
frxMgtN392 = _FrxMgtN392_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 1, 1, 5),
    _FrxMgtN392_Type()
)
frxMgtN392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxMgtN392.setStatus("mandatory")


class _FrxMgtN393_Type(Integer32):
    """Custom type frxMgtN393 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrxMgtN393_Type.__name__ = "Integer32"
_FrxMgtN393_Object = MibTableColumn
frxMgtN393 = _FrxMgtN393_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 1, 1, 6),
    _FrxMgtN393_Type()
)
frxMgtN393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxMgtN393.setStatus("mandatory")
_FrxNetLinkErrors_Type = Counter32
_FrxNetLinkErrors_Object = MibTableColumn
frxNetLinkErrors = _FrxNetLinkErrors_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 1, 1, 7),
    _FrxNetLinkErrors_Type()
)
frxNetLinkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxNetLinkErrors.setStatus("mandatory")
_FrxNetProtErrors_Type = Counter32
_FrxNetProtErrors_Object = MibTableColumn
frxNetProtErrors = _FrxNetProtErrors_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 1, 1, 8),
    _FrxNetProtErrors_Type()
)
frxNetProtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxNetProtErrors.setStatus("mandatory")
_FrxNetChInactive_Type = Counter32
_FrxNetChInactive_Object = MibTableColumn
frxNetChInactive = _FrxNetChInactive_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 1, 1, 9),
    _FrxNetChInactive_Type()
)
frxNetChInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxNetChInactive.setStatus("mandatory")


class _FrxNetChStatus_Type(Integer32):
    """Custom type frxNetChStatus based on Integer32"""
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


_FrxNetChStatus_Type.__name__ = "Integer32"
_FrxNetChStatus_Object = MibTableColumn
frxNetChStatus = _FrxNetChStatus_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 1, 1, 10),
    _FrxNetChStatus_Type()
)
frxNetChStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxNetChStatus.setStatus("mandatory")
_FrxMgtPortTable_Object = MibTable
frxMgtPortTable = _FrxMgtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 2)
)
if mibBuilder.loadTexts:
    frxMgtPortTable.setStatus("mandatory")
_FrxMgtPortEntry_Object = MibTableRow
frxMgtPortEntry = _FrxMgtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 2, 1)
)
frxMgtPortEntry.setIndexNames(
    (0, "Cisco90Series-MIB", "frxBankIndex"),
    (0, "Cisco90Series-MIB", "frxChUIndex"),
    (0, "Cisco90Series-MIB", "frxPortIndex"),
)
if mibBuilder.loadTexts:
    frxMgtPortEntry.setStatus("mandatory")


class _FrxPortIndex_Type(Integer32):
    """Custom type frxPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FrxPortIndex_Type.__name__ = "Integer32"
_FrxPortIndex_Object = MibTableColumn
frxPortIndex = _FrxPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 2, 1, 1),
    _FrxPortIndex_Type()
)
frxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPortIndex.setStatus("mandatory")
_FrxPortLinkErrors_Type = Counter32
_FrxPortLinkErrors_Object = MibTableColumn
frxPortLinkErrors = _FrxPortLinkErrors_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 2, 1, 2),
    _FrxPortLinkErrors_Type()
)
frxPortLinkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPortLinkErrors.setStatus("mandatory")
_FrxPortProtErrors_Type = Counter32
_FrxPortProtErrors_Object = MibTableColumn
frxPortProtErrors = _FrxPortProtErrors_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 2, 1, 3),
    _FrxPortProtErrors_Type()
)
frxPortProtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPortProtErrors.setStatus("mandatory")
_FrxPortChInactive_Type = Counter32
_FrxPortChInactive_Object = MibTableColumn
frxPortChInactive = _FrxPortChInactive_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 5, 2, 1, 4),
    _FrxPortChInactive_Type()
)
frxPortChInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPortChInactive.setStatus("mandatory")
_FrxPort_ObjectIdentity = ObjectIdentity
frxPort = _FrxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6)
)
_FrxPortTable_Object = MibTable
frxPortTable = _FrxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1)
)
if mibBuilder.loadTexts:
    frxPortTable.setStatus("mandatory")
_FrxPortEntry_Object = MibTableRow
frxPortEntry = _FrxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1)
)
frxPortEntry.setIndexNames(
    (0, "Cisco90Series-MIB", "frxBankIndex"),
    (0, "Cisco90Series-MIB", "frxChUIndex"),
    (0, "Cisco90Series-MIB", "frxPortIndex"),
)
if mibBuilder.loadTexts:
    frxPortEntry.setStatus("mandatory")


class _FrxPortSpeed_Type(Integer32):
    """Custom type frxPortSpeed based on Integer32"""
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
        *(("use128kbps", 3),
          ("use144kbps", 4),
          ("use56kbps", 1),
          ("use64kbps", 2))
    )


_FrxPortSpeed_Type.__name__ = "Integer32"
_FrxPortSpeed_Object = MibTableColumn
frxPortSpeed = _FrxPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 1),
    _FrxPortSpeed_Type()
)
frxPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxPortSpeed.setStatus("mandatory")


class _FrxPortProtocol_Type(Integer32):
    """Custom type frxPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameRelay", 1),
          ("ppp", 2))
    )


_FrxPortProtocol_Type.__name__ = "Integer32"
_FrxPortProtocol_Object = MibTableColumn
frxPortProtocol = _FrxPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 2),
    _FrxPortProtocol_Type()
)
frxPortProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxPortProtocol.setStatus("mandatory")


class _FrxDSLStatus_Type(Integer32):
    """Custom type frxDSLStatus based on Integer32"""
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
        *(("dslSyncOnly", 2),
          ("loopDown", 1),
          ("loopUp", 4),
          ("loopUpInactive", 3))
    )


_FrxDSLStatus_Type.__name__ = "Integer32"
_FrxDSLStatus_Object = MibTableColumn
frxDSLStatus = _FrxDSLStatus_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 3),
    _FrxDSLStatus_Type()
)
frxDSLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxDSLStatus.setStatus("mandatory")


class _FrxPVCAssigned_Type(Integer32):
    """Custom type frxPVCAssigned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_FrxPVCAssigned_Type.__name__ = "Integer32"
_FrxPVCAssigned_Object = MibTableColumn
frxPVCAssigned = _FrxPVCAssigned_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 4),
    _FrxPVCAssigned_Type()
)
frxPVCAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPVCAssigned.setStatus("mandatory")
_FrxLastChange_Type = TimeTicks
_FrxLastChange_Object = MibTableColumn
frxLastChange = _FrxLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 5),
    _FrxLastChange_Type()
)
frxLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxLastChange.setStatus("mandatory")


class _FrxBrite_Type(Integer32):
    """Custom type frxBrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_FrxBrite_Type.__name__ = "Integer32"
_FrxBrite_Object = MibTableColumn
frxBrite = _FrxBrite_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 6),
    _FrxBrite_Type()
)
frxBrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxBrite.setStatus("mandatory")
_FrxDSLInOctets_Type = Counter32
_FrxDSLInOctets_Object = MibTableColumn
frxDSLInOctets = _FrxDSLInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 7),
    _FrxDSLInOctets_Type()
)
frxDSLInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxDSLInOctets.setStatus("mandatory")
_FrxDSLOutOctets_Type = Counter32
_FrxDSLOutOctets_Object = MibTableColumn
frxDSLOutOctets = _FrxDSLOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 8),
    _FrxDSLOutOctets_Type()
)
frxDSLOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxDSLOutOctets.setStatus("mandatory")
_FrxT1InOctets_Type = Counter32
_FrxT1InOctets_Object = MibTableColumn
frxT1InOctets = _FrxT1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 9),
    _FrxT1InOctets_Type()
)
frxT1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxT1InOctets.setStatus("mandatory")
_FrxT1OutOctets_Type = Counter32
_FrxT1OutOctets_Object = MibTableColumn
frxT1OutOctets = _FrxT1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 10),
    _FrxT1OutOctets_Type()
)
frxT1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxT1OutOctets.setStatus("mandatory")
_FrxDSLBadFrames_Type = Counter32
_FrxDSLBadFrames_Object = MibTableColumn
frxDSLBadFrames = _FrxDSLBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 11),
    _FrxDSLBadFrames_Type()
)
frxDSLBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxDSLBadFrames.setStatus("mandatory")
_FrxDSLHDLCEs_Type = Counter32
_FrxDSLHDLCEs_Object = MibTableColumn
frxDSLHDLCEs = _FrxDSLHDLCEs_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 12),
    _FrxDSLHDLCEs_Type()
)
frxDSLHDLCEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxDSLHDLCEs.setStatus("mandatory")
_FrxDSLCRCEs_Type = Counter32
_FrxDSLCRCEs_Object = MibTableColumn
frxDSLCRCEs = _FrxDSLCRCEs_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 13),
    _FrxDSLCRCEs_Type()
)
frxDSLCRCEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxDSLCRCEs.setStatus("mandatory")
_FrxDSLLinkEs_Type = Counter32
_FrxDSLLinkEs_Object = MibTableColumn
frxDSLLinkEs = _FrxDSLLinkEs_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 14),
    _FrxDSLLinkEs_Type()
)
frxDSLLinkEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxDSLLinkEs.setStatus("mandatory")
_FrxDSLFrShEs_Type = Counter32
_FrxDSLFrShEs_Object = MibTableColumn
frxDSLFrShEs = _FrxDSLFrShEs_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 15),
    _FrxDSLFrShEs_Type()
)
frxDSLFrShEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxDSLFrShEs.setStatus("mandatory")
_FrxDSLFrLgEs_Type = Counter32
_FrxDSLFrLgEs_Object = MibTableColumn
frxDSLFrLgEs = _FrxDSLFrLgEs_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 16),
    _FrxDSLFrLgEs_Type()
)
frxDSLFrLgEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxDSLFrLgEs.setStatus("mandatory")
_FrxDSLDLCIEs_Type = Counter32
_FrxDSLDLCIEs_Object = MibTableColumn
frxDSLDLCIEs = _FrxDSLDLCIEs_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 17),
    _FrxDSLDLCIEs_Type()
)
frxDSLDLCIEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxDSLDLCIEs.setStatus("mandatory")


class _FrxTxBuf_Type(Integer32):
    """Custom type frxTxBuf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxTxBuf_Type.__name__ = "Integer32"
_FrxTxBuf_Object = MibTableColumn
frxTxBuf = _FrxTxBuf_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 18),
    _FrxTxBuf_Type()
)
frxTxBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxTxBuf.setStatus("mandatory")


class _FrxRxBuf_Type(Integer32):
    """Custom type frxRxBuf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxRxBuf_Type.__name__ = "Integer32"
_FrxRxBuf_Object = MibTableColumn
frxRxBuf = _FrxRxBuf_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 19),
    _FrxRxBuf_Type()
)
frxRxBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxRxBuf.setStatus("mandatory")
_FrxPortNetEs_Type = Counter32
_FrxPortNetEs_Object = MibTableColumn
frxPortNetEs = _FrxPortNetEs_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 1, 1, 20),
    _FrxPortNetEs_Type()
)
frxPortNetEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPortNetEs.setStatus("mandatory")
_FrxCircuitTable_Object = MibTable
frxCircuitTable = _FrxCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 2)
)
if mibBuilder.loadTexts:
    frxCircuitTable.setStatus("mandatory")
_FrxCircuitEntry_Object = MibTableRow
frxCircuitEntry = _FrxCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 2, 1)
)
frxCircuitEntry.setIndexNames(
    (0, "Cisco90Series-MIB", "frxBankIndex"),
    (0, "Cisco90Series-MIB", "frxChUIndex"),
    (0, "Cisco90Series-MIB", "frxPortIndex"),
    (0, "Cisco90Series-MIB", "frxPvcIndex"),
)
if mibBuilder.loadTexts:
    frxCircuitEntry.setStatus("mandatory")


class _FrxPvcIndex_Type(Integer32):
    """Custom type frxPvcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 23),
    )


_FrxPvcIndex_Type.__name__ = "Integer32"
_FrxPvcIndex_Object = MibTableColumn
frxPvcIndex = _FrxPvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 2, 1, 1),
    _FrxPvcIndex_Type()
)
frxPvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPvcIndex.setStatus("mandatory")


class _FrxCktCIR_Type(Integer32):
    """Custom type frxCktCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1544000),
    )


_FrxCktCIR_Type.__name__ = "Integer32"
_FrxCktCIR_Object = MibTableColumn
frxCktCIR = _FrxCktCIR_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 2, 1, 2),
    _FrxCktCIR_Type()
)
frxCktCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxCktCIR.setStatus("mandatory")


class _FrxCktBc_Type(Integer32):
    """Custom type frxCktBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FrxCktBc_Type.__name__ = "Integer32"
_FrxCktBc_Object = MibTableColumn
frxCktBc = _FrxCktBc_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 2, 1, 3),
    _FrxCktBc_Type()
)
frxCktBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxCktBc.setStatus("mandatory")


class _FrxCktBe_Type(Integer32):
    """Custom type frxCktBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FrxCktBe_Type.__name__ = "Integer32"
_FrxCktBe_Object = MibTableColumn
frxCktBe = _FrxCktBe_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 2, 1, 4),
    _FrxCktBe_Type()
)
frxCktBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxCktBe.setStatus("mandatory")


class _FrxFarEndOpStat_Type(Integer32):
    """Custom type frxFarEndOpStat based on Integer32"""
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


_FrxFarEndOpStat_Type.__name__ = "Integer32"
_FrxFarEndOpStat_Object = MibTableColumn
frxFarEndOpStat = _FrxFarEndOpStat_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 2, 1, 5),
    _FrxFarEndOpStat_Type()
)
frxFarEndOpStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxFarEndOpStat.setStatus("mandatory")
_FrxCktInOctets_Type = Counter32
_FrxCktInOctets_Object = MibTableColumn
frxCktInOctets = _FrxCktInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 2, 1, 6),
    _FrxCktInOctets_Type()
)
frxCktInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxCktInOctets.setStatus("mandatory")
_FrxCktOutOctets_Type = Counter32
_FrxCktOutOctets_Object = MibTableColumn
frxCktOutOctets = _FrxCktOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 2, 1, 7),
    _FrxCktOutOctets_Type()
)
frxCktOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxCktOutOctets.setStatus("mandatory")
_FrxCktInFrames_Type = Counter32
_FrxCktInFrames_Object = MibTableColumn
frxCktInFrames = _FrxCktInFrames_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 2, 1, 8),
    _FrxCktInFrames_Type()
)
frxCktInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxCktInFrames.setStatus("mandatory")
_FrxCktOutFrames_Type = Counter32
_FrxCktOutFrames_Object = MibTableColumn
frxCktOutFrames = _FrxCktOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 2, 1, 9),
    _FrxCktOutFrames_Type()
)
frxCktOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxCktOutFrames.setStatus("mandatory")
_FrxCktDiscards_Type = Counter32
_FrxCktDiscards_Object = MibTableColumn
frxCktDiscards = _FrxCktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 2, 1, 10),
    _FrxCktDiscards_Type()
)
frxCktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxCktDiscards.setStatus("mandatory")
_FrxUEocTable_Object = MibTable
frxUEocTable = _FrxUEocTable_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 3)
)
if mibBuilder.loadTexts:
    frxUEocTable.setStatus("mandatory")
_FrxUEocEntry_Object = MibTableRow
frxUEocEntry = _FrxUEocEntry_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 3, 1)
)
frxUEocEntry.setIndexNames(
    (0, "Cisco90Series-MIB", "frxBankIndex"),
    (0, "Cisco90Series-MIB", "frxChUIndex"),
)
if mibBuilder.loadTexts:
    frxUEocEntry.setStatus("mandatory")


class _FrxTestPort_Type(Integer32):
    """Custom type frxTestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FrxTestPort_Type.__name__ = "Integer32"
_FrxTestPort_Object = MibTableColumn
frxTestPort = _FrxTestPort_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 3, 1, 1),
    _FrxTestPort_Type()
)
frxTestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxTestPort.setStatus("mandatory")


class _FrxTestType_Type(Integer32):
    """Custom type frxTestType based on Integer32"""
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
        *(("bertOnly", 2),
          ("localLoopAllPorts", 5),
          ("loopbackAndBert", 1),
          ("loopbackOnly", 4),
          ("sendCorruptCRC", 3))
    )


_FrxTestType_Type.__name__ = "Integer32"
_FrxTestType_Object = MibTableColumn
frxTestType = _FrxTestType_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 3, 1, 2),
    _FrxTestType_Type()
)
frxTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxTestType.setStatus("mandatory")


class _FrxLoopLoc_Type(Integer32):
    """Custom type frxLoopLoc based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("briteCard1", 1),
          ("briteCard2", 2),
          ("briteCard3", 3),
          ("briteCard4", 4),
          ("briteCard5", 5),
          ("briteCard6", 6),
          ("localFrx", 7),
          ("nt1", 8))
    )


_FrxLoopLoc_Type.__name__ = "Integer32"
_FrxLoopLoc_Object = MibTableColumn
frxLoopLoc = _FrxLoopLoc_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 3, 1, 3),
    _FrxLoopLoc_Type()
)
frxLoopLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxLoopLoc.setStatus("mandatory")


class _FrxLoopCh_Type(Integer32):
    """Custom type frxLoopCh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("b1only", 1),
          ("b2only", 2))
    )


_FrxLoopCh_Type.__name__ = "Integer32"
_FrxLoopCh_Object = MibTableColumn
frxLoopCh = _FrxLoopCh_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 3, 1, 4),
    _FrxLoopCh_Type()
)
frxLoopCh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxLoopCh.setStatus("mandatory")


class _FrxStartTest_Type(Integer32):
    """Custom type frxStartTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("startTest", 2),
          ("stopTest", 1))
    )


_FrxStartTest_Type.__name__ = "Integer32"
_FrxStartTest_Object = MibTableColumn
frxStartTest = _FrxStartTest_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 3, 1, 5),
    _FrxStartTest_Type()
)
frxStartTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxStartTest.setStatus("mandatory")


class _FrxBertRst_Type(Integer32):
    """Custom type frxBertRst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("resetBert", 2))
    )


_FrxBertRst_Type.__name__ = "Integer32"
_FrxBertRst_Object = MibTableColumn
frxBertRst = _FrxBertRst_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 3, 1, 6),
    _FrxBertRst_Type()
)
frxBertRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxBertRst.setStatus("mandatory")
_FrxBertBE_Type = Counter32
_FrxBertBE_Object = MibTableColumn
frxBertBE = _FrxBertBE_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 3, 1, 7),
    _FrxBertBE_Type()
)
frxBertBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxBertBE.setStatus("mandatory")
_FrxBertTestTime_Type = TimeTicks
_FrxBertTestTime_Object = MibTableColumn
frxBertTestTime = _FrxBertTestTime_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 3, 1, 8),
    _FrxBertTestTime_Type()
)
frxBertTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxBertTestTime.setStatus("mandatory")


class _FrxTestInProg_Type(Integer32):
    """Custom type frxTestInProg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalOperation", 2),
          ("testInProgress", 1))
    )


_FrxTestInProg_Type.__name__ = "Integer32"
_FrxTestInProg_Object = MibTableColumn
frxTestInProg = _FrxTestInProg_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 3, 1, 9),
    _FrxTestInProg_Type()
)
frxTestInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxTestInProg.setStatus("mandatory")
_FrxUThrTable_Object = MibTable
frxUThrTable = _FrxUThrTable_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 4)
)
if mibBuilder.loadTexts:
    frxUThrTable.setStatus("mandatory")
_FrxUThrEntry_Object = MibTableRow
frxUThrEntry = _FrxUThrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 4, 1)
)
frxUThrEntry.setIndexNames(
    (0, "Cisco90Series-MIB", "frxBankIndex"),
    (0, "Cisco90Series-MIB", "frxChUIndex"),
    (0, "Cisco90Series-MIB", "frxPortIndex"),
    (0, "Cisco90Series-MIB", "frxPAddrIndex"),
)
if mibBuilder.loadTexts:
    frxUThrEntry.setStatus("mandatory")


class _FrxPAddrIndex_Type(Integer32):
    """Custom type frxPAddrIndex based on Integer32"""
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
        *(("briteCard1", 1),
          ("briteCard2", 2),
          ("briteCard3", 3),
          ("briteCard4", 4),
          ("briteCard5", 5),
          ("briteCard6", 6),
          ("localFrx", 7))
    )


_FrxPAddrIndex_Type.__name__ = "Integer32"
_FrxPAddrIndex_Object = MibTableColumn
frxPAddrIndex = _FrxPAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 4, 1, 1),
    _FrxPAddrIndex_Type()
)
frxPAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPAddrIndex.setStatus("mandatory")


class _FrxChEsTh_Type(Integer32):
    """Custom type frxChEsTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_FrxChEsTh_Type.__name__ = "Integer32"
_FrxChEsTh_Object = MibTableColumn
frxChEsTh = _FrxChEsTh_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 4, 1, 2),
    _FrxChEsTh_Type()
)
frxChEsTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxChEsTh.setStatus("mandatory")


class _FrxCdEsTh_Type(Integer32):
    """Custom type frxCdEsTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrxCdEsTh_Type.__name__ = "Integer32"
_FrxCdEsTh_Object = MibTableColumn
frxCdEsTh = _FrxCdEsTh_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 4, 1, 3),
    _FrxCdEsTh_Type()
)
frxCdEsTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxCdEsTh.setStatus("mandatory")


class _FrxChSesTh_Type(Integer32):
    """Custom type frxChSesTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_FrxChSesTh_Type.__name__ = "Integer32"
_FrxChSesTh_Object = MibTableColumn
frxChSesTh = _FrxChSesTh_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 4, 1, 4),
    _FrxChSesTh_Type()
)
frxChSesTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxChSesTh.setStatus("mandatory")


class _FrxCdSesTh_Type(Integer32):
    """Custom type frxCdSesTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrxCdSesTh_Type.__name__ = "Integer32"
_FrxCdSesTh_Object = MibTableColumn
frxCdSesTh = _FrxCdSesTh_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 4, 1, 5),
    _FrxCdSesTh_Type()
)
frxCdSesTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxCdSesTh.setStatus("mandatory")


class _FrxAlertMask_Type(Integer32):
    """Custom type frxAlertMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrxAlertMask_Type.__name__ = "Integer32"
_FrxAlertMask_Object = MibTableColumn
frxAlertMask = _FrxAlertMask_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 4, 1, 6),
    _FrxAlertMask_Type()
)
frxAlertMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxAlertMask.setStatus("mandatory")


class _FrxThCond_Type(Integer32):
    """Custom type frxThCond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrxThCond_Type.__name__ = "Integer32"
_FrxThCond_Object = MibTableColumn
frxThCond = _FrxThCond_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 4, 1, 7),
    _FrxThCond_Type()
)
frxThCond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxThCond.setStatus("mandatory")
_FrxUPerfTable_Object = MibTable
frxUPerfTable = _FrxUPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5)
)
if mibBuilder.loadTexts:
    frxUPerfTable.setStatus("mandatory")
_FrxUPerfEntry_Object = MibTableRow
frxUPerfEntry = _FrxUPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1)
)
frxUPerfEntry.setIndexNames(
    (0, "Cisco90Series-MIB", "frxBankIndex"),
    (0, "Cisco90Series-MIB", "frxChUIndex"),
    (0, "Cisco90Series-MIB", "frxPortIndex"),
    (0, "Cisco90Series-MIB", "frxPAddrIndex"),
)
if mibBuilder.loadTexts:
    frxUPerfEntry.setStatus("mandatory")


class _FrxResetPM_Type(Integer32):
    """Custom type frxResetPM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("resetPM", 2))
    )


_FrxResetPM_Type.__name__ = "Integer32"
_FrxResetPM_Object = MibTableColumn
frxResetPM = _FrxResetPM_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 1),
    _FrxResetPM_Type()
)
frxResetPM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frxResetPM.setStatus("mandatory")


class _FrxPMtype_Type(Integer32):
    """Custom type frxPMtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pathPM", 2),
          ("segmentedPM", 1))
    )


_FrxPMtype_Type.__name__ = "Integer32"
_FrxPMtype_Object = MibTableColumn
frxPMtype = _FrxPMtype_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 2),
    _FrxPMtype_Type()
)
frxPMtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPMtype.setStatus("mandatory")


class _FrxChEsTx_Type(Integer32):
    """Custom type frxChEsTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxChEsTx_Type.__name__ = "Integer32"
_FrxChEsTx_Object = MibTableColumn
frxChEsTx = _FrxChEsTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 3),
    _FrxChEsTx_Type()
)
frxChEsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxChEsTx.setStatus("mandatory")


class _FrxChEsRx_Type(Integer32):
    """Custom type frxChEsRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxChEsRx_Type.__name__ = "Integer32"
_FrxChEsRx_Object = MibTableColumn
frxChEsRx = _FrxChEsRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 4),
    _FrxChEsRx_Type()
)
frxChEsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxChEsRx.setStatus("mandatory")


class _FrxPhEsTx_Type(Integer32):
    """Custom type frxPhEsTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxPhEsTx_Type.__name__ = "Integer32"
_FrxPhEsTx_Object = MibTableColumn
frxPhEsTx = _FrxPhEsTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 5),
    _FrxPhEsTx_Type()
)
frxPhEsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPhEsTx.setStatus("mandatory")


class _FrxPhEsRx_Type(Integer32):
    """Custom type frxPhEsRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxPhEsRx_Type.__name__ = "Integer32"
_FrxPhEsRx_Object = MibTableColumn
frxPhEsRx = _FrxPhEsRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 6),
    _FrxPhEsRx_Type()
)
frxPhEsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPhEsRx.setStatus("mandatory")


class _FrxH2EsTx_Type(Integer32):
    """Custom type frxH2EsTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxH2EsTx_Type.__name__ = "Integer32"
_FrxH2EsTx_Object = MibTableColumn
frxH2EsTx = _FrxH2EsTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 7),
    _FrxH2EsTx_Type()
)
frxH2EsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxH2EsTx.setStatus("mandatory")


class _FrxH2EsRx_Type(Integer32):
    """Custom type frxH2EsRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxH2EsRx_Type.__name__ = "Integer32"
_FrxH2EsRx_Object = MibTableColumn
frxH2EsRx = _FrxH2EsRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 8),
    _FrxH2EsRx_Type()
)
frxH2EsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxH2EsRx.setStatus("mandatory")


class _FrxH3EsTx_Type(Integer32):
    """Custom type frxH3EsTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxH3EsTx_Type.__name__ = "Integer32"
_FrxH3EsTx_Object = MibTableColumn
frxH3EsTx = _FrxH3EsTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 9),
    _FrxH3EsTx_Type()
)
frxH3EsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxH3EsTx.setStatus("mandatory")


class _FrxH3EsRx_Type(Integer32):
    """Custom type frxH3EsRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxH3EsRx_Type.__name__ = "Integer32"
_FrxH3EsRx_Object = MibTableColumn
frxH3EsRx = _FrxH3EsRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 10),
    _FrxH3EsRx_Type()
)
frxH3EsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxH3EsRx.setStatus("mandatory")


class _FrxH4EsTx_Type(Integer32):
    """Custom type frxH4EsTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxH4EsTx_Type.__name__ = "Integer32"
_FrxH4EsTx_Object = MibTableColumn
frxH4EsTx = _FrxH4EsTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 11),
    _FrxH4EsTx_Type()
)
frxH4EsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxH4EsTx.setStatus("mandatory")


class _FrxH4EsRx_Type(Integer32):
    """Custom type frxH4EsRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxH4EsRx_Type.__name__ = "Integer32"
_FrxH4EsRx_Object = MibTableColumn
frxH4EsRx = _FrxH4EsRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 12),
    _FrxH4EsRx_Type()
)
frxH4EsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxH4EsRx.setStatus("mandatory")


class _FrxH5EsTx_Type(Integer32):
    """Custom type frxH5EsTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxH5EsTx_Type.__name__ = "Integer32"
_FrxH5EsTx_Object = MibTableColumn
frxH5EsTx = _FrxH5EsTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 13),
    _FrxH5EsTx_Type()
)
frxH5EsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxH5EsTx.setStatus("mandatory")


class _FrxH5EsRx_Type(Integer32):
    """Custom type frxH5EsRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxH5EsRx_Type.__name__ = "Integer32"
_FrxH5EsRx_Object = MibTableColumn
frxH5EsRx = _FrxH5EsRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 14),
    _FrxH5EsRx_Type()
)
frxH5EsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxH5EsRx.setStatus("mandatory")


class _FrxH6EsTx_Type(Integer32):
    """Custom type frxH6EsTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxH6EsTx_Type.__name__ = "Integer32"
_FrxH6EsTx_Object = MibTableColumn
frxH6EsTx = _FrxH6EsTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 15),
    _FrxH6EsTx_Type()
)
frxH6EsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxH6EsTx.setStatus("mandatory")


class _FrxH6EsRx_Type(Integer32):
    """Custom type frxH6EsRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxH6EsRx_Type.__name__ = "Integer32"
_FrxH6EsRx_Object = MibTableColumn
frxH6EsRx = _FrxH6EsRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 16),
    _FrxH6EsRx_Type()
)
frxH6EsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxH6EsRx.setStatus("mandatory")


class _FrxH7EsTx_Type(Integer32):
    """Custom type frxH7EsTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxH7EsTx_Type.__name__ = "Integer32"
_FrxH7EsTx_Object = MibTableColumn
frxH7EsTx = _FrxH7EsTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 17),
    _FrxH7EsTx_Type()
)
frxH7EsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxH7EsTx.setStatus("mandatory")


class _FrxH7EsRx_Type(Integer32):
    """Custom type frxH7EsRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxH7EsRx_Type.__name__ = "Integer32"
_FrxH7EsRx_Object = MibTableColumn
frxH7EsRx = _FrxH7EsRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 18),
    _FrxH7EsRx_Type()
)
frxH7EsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxH7EsRx.setStatus("mandatory")


class _FrxH8EsTx_Type(Integer32):
    """Custom type frxH8EsTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxH8EsTx_Type.__name__ = "Integer32"
_FrxH8EsTx_Object = MibTableColumn
frxH8EsTx = _FrxH8EsTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 19),
    _FrxH8EsTx_Type()
)
frxH8EsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxH8EsTx.setStatus("mandatory")


class _FrxH8EsRx_Type(Integer32):
    """Custom type frxH8EsRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxH8EsRx_Type.__name__ = "Integer32"
_FrxH8EsRx_Object = MibTableColumn
frxH8EsRx = _FrxH8EsRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 20),
    _FrxH8EsRx_Type()
)
frxH8EsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxH8EsRx.setStatus("mandatory")


class _FrxCdEsTx_Type(Integer32):
    """Custom type frxCdEsTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxCdEsTx_Type.__name__ = "Integer32"
_FrxCdEsTx_Object = MibTableColumn
frxCdEsTx = _FrxCdEsTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 21),
    _FrxCdEsTx_Type()
)
frxCdEsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxCdEsTx.setStatus("mandatory")


class _FrxCdEsRx_Type(Integer32):
    """Custom type frxCdEsRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxCdEsRx_Type.__name__ = "Integer32"
_FrxCdEsRx_Object = MibTableColumn
frxCdEsRx = _FrxCdEsRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 22),
    _FrxCdEsRx_Type()
)
frxCdEsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxCdEsRx.setStatus("mandatory")


class _FrxPdEsTx_Type(Integer32):
    """Custom type frxPdEsTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxPdEsTx_Type.__name__ = "Integer32"
_FrxPdEsTx_Object = MibTableColumn
frxPdEsTx = _FrxPdEsTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 23),
    _FrxPdEsTx_Type()
)
frxPdEsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPdEsTx.setStatus("mandatory")


class _FrxPdEsRx_Type(Integer32):
    """Custom type frxPdEsRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxPdEsRx_Type.__name__ = "Integer32"
_FrxPdEsRx_Object = MibTableColumn
frxPdEsRx = _FrxPdEsRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 24),
    _FrxPdEsRx_Type()
)
frxPdEsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPdEsRx.setStatus("mandatory")


class _FrxChSesTx_Type(Integer32):
    """Custom type frxChSesTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxChSesTx_Type.__name__ = "Integer32"
_FrxChSesTx_Object = MibTableColumn
frxChSesTx = _FrxChSesTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 25),
    _FrxChSesTx_Type()
)
frxChSesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxChSesTx.setStatus("mandatory")


class _FrxChSesRx_Type(Integer32):
    """Custom type frxChSesRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxChSesRx_Type.__name__ = "Integer32"
_FrxChSesRx_Object = MibTableColumn
frxChSesRx = _FrxChSesRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 26),
    _FrxChSesRx_Type()
)
frxChSesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxChSesRx.setStatus("mandatory")


class _FrxPhSesTx_Type(Integer32):
    """Custom type frxPhSesTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxPhSesTx_Type.__name__ = "Integer32"
_FrxPhSesTx_Object = MibTableColumn
frxPhSesTx = _FrxPhSesTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 27),
    _FrxPhSesTx_Type()
)
frxPhSesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPhSesTx.setStatus("mandatory")


class _FrxPhSesRx_Type(Integer32):
    """Custom type frxPhSesRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FrxPhSesRx_Type.__name__ = "Integer32"
_FrxPhSesRx_Object = MibTableColumn
frxPhSesRx = _FrxPhSesRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 28),
    _FrxPhSesRx_Type()
)
frxPhSesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPhSesRx.setStatus("mandatory")


class _FrxCdSesTx_Type(Integer32):
    """Custom type frxCdSesTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxCdSesTx_Type.__name__ = "Integer32"
_FrxCdSesTx_Object = MibTableColumn
frxCdSesTx = _FrxCdSesTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 29),
    _FrxCdSesTx_Type()
)
frxCdSesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxCdSesTx.setStatus("mandatory")


class _FrxCdSesRx_Type(Integer32):
    """Custom type frxCdSesRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxCdSesRx_Type.__name__ = "Integer32"
_FrxCdSesRx_Object = MibTableColumn
frxCdSesRx = _FrxCdSesRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 30),
    _FrxCdSesRx_Type()
)
frxCdSesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxCdSesRx.setStatus("mandatory")


class _FrxPdSesTx_Type(Integer32):
    """Custom type frxPdSesTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxPdSesTx_Type.__name__ = "Integer32"
_FrxPdSesTx_Object = MibTableColumn
frxPdSesTx = _FrxPdSesTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 31),
    _FrxPdSesTx_Type()
)
frxPdSesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPdSesTx.setStatus("mandatory")


class _FrxPdSesRx_Type(Integer32):
    """Custom type frxPdSesRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxPdSesRx_Type.__name__ = "Integer32"
_FrxPdSesRx_Object = MibTableColumn
frxPdSesRx = _FrxPdSesRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 32),
    _FrxPdSesRx_Type()
)
frxPdSesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPdSesRx.setStatus("mandatory")


class _FrxChBeTx_Type(Integer32):
    """Custom type frxChBeTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxChBeTx_Type.__name__ = "Integer32"
_FrxChBeTx_Object = MibTableColumn
frxChBeTx = _FrxChBeTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 33),
    _FrxChBeTx_Type()
)
frxChBeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxChBeTx.setStatus("mandatory")


class _FrxChBeRx_Type(Integer32):
    """Custom type frxChBeRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxChBeRx_Type.__name__ = "Integer32"
_FrxChBeRx_Object = MibTableColumn
frxChBeRx = _FrxChBeRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 34),
    _FrxChBeRx_Type()
)
frxChBeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxChBeRx.setStatus("mandatory")


class _FrxPhBeTx_Type(Integer32):
    """Custom type frxPhBeTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxPhBeTx_Type.__name__ = "Integer32"
_FrxPhBeTx_Object = MibTableColumn
frxPhBeTx = _FrxPhBeTx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 35),
    _FrxPhBeTx_Type()
)
frxPhBeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPhBeTx.setStatus("mandatory")


class _FrxPhBeRx_Type(Integer32):
    """Custom type frxPhBeRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrxPhBeRx_Type.__name__ = "Integer32"
_FrxPhBeRx_Object = MibTableColumn
frxPhBeRx = _FrxPhBeRx_Object(
    (1, 3, 6, 1, 4, 1, 1570, 1, 6, 5, 1, 36),
    _FrxPhBeRx_Type()
)
frxPhBeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frxPhBeRx.setStatus("mandatory")

# Managed Objects groups


# Notification objects

frxDownloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1570, 1, 0, 1)
)
frxDownloadTrap.setObjects(
      *(("Cisco90Series-MIB", "frxBankIndex"),
        ("Cisco90Series-MIB", "frxChUIndex"))
)
if mibBuilder.loadTexts:
    frxDownloadTrap.setStatus(
        ""
    )

frxUPerfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1570, 1, 0, 2)
)
frxUPerfTrap.setObjects(
      *(("Cisco90Series-MIB", "frxBankIndex"),
        ("Cisco90Series-MIB", "frxChUIndex"))
)
if mibBuilder.loadTexts:
    frxUPerfTrap.setStatus(
        ""
    )

frxInsertChUTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1570, 1, 0, 3)
)
frxInsertChUTrap.setObjects(
      *(("Cisco90Series-MIB", "frxBankIndex"),
        ("Cisco90Series-MIB", "frxChUIndex"))
)
if mibBuilder.loadTexts:
    frxInsertChUTrap.setStatus(
        ""
    )

frxRemoveChUTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1570, 1, 0, 4)
)
frxRemoveChUTrap.setObjects(
      *(("Cisco90Series-MIB", "frxBankIndex"),
        ("Cisco90Series-MIB", "frxChUIndex"))
)
if mibBuilder.loadTexts:
    frxRemoveChUTrap.setStatus(
        ""
    )

frxDConfigFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1570, 1, 0, 5)
)
frxDConfigFailed.setObjects(
      *(("Cisco90Series-MIB", "frxBankIndex"),
        ("Cisco90Series-MIB", "frxChUIndex"))
)
if mibBuilder.loadTexts:
    frxDConfigFailed.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Cisco90Series-MIB",
    **{"DisplayString": DisplayString,
       "ciscoTelesend": ciscoTelesend,
       "frMux": frMux,
       "frxDownloadTrap": frxDownloadTrap,
       "frxUPerfTrap": frxUPerfTrap,
       "frxInsertChUTrap": frxInsertChUTrap,
       "frxRemoveChUTrap": frxRemoveChUTrap,
       "frxDConfigFailed": frxDConfigFailed,
       "frxSys": frxSys,
       "frxSysDescr": frxSysDescr,
       "frxClockHour": frxClockHour,
       "frxClockMin": frxClockMin,
       "frxClockSec": frxClockSec,
       "frxUpTime": frxUpTime,
       "frxAdminContact": frxAdminContact,
       "frxSysName": frxSysName,
       "frxSysLoc": frxSysLoc,
       "frxSysVersion": frxSysVersion,
       "frxUPerfTrapEnable": frxUPerfTrapEnable,
       "frxAgtLinkErrors": frxAgtLinkErrors,
       "frxAgtProtErrors": frxAgtProtErrors,
       "frxAgtChInactive": frxAgtChInactive,
       "frxAgtChStatus": frxAgtChStatus,
       "frxDefault": frxDefault,
       "frxDefaultEnable": frxDefaultEnable,
       "frxDefaultTrap": frxDefaultTrap,
       "frxDConfigSrc": frxDConfigSrc,
       "frxDMgtT391": frxDMgtT391,
       "frxDMgtT392": frxDMgtT392,
       "frxDMgtN391": frxDMgtN391,
       "frxDMgtN392": frxDMgtN392,
       "frxDMgtN393": frxDMgtN393,
       "frxDPortSpeed": frxDPortSpeed,
       "frxDPortProtocol": frxDPortProtocol,
       "frxDCktCIR": frxDCktCIR,
       "frxDCktBc": frxDCktBc,
       "frxDCktBe": frxDCktBe,
       "frxBank": frxBank,
       "frxBankTable": frxBankTable,
       "frxBankEntry": frxBankEntry,
       "frxBankIndex": frxBankIndex,
       "frxBankType": frxBankType,
       "frxChUnit": frxChUnit,
       "frxChUTable": frxChUTable,
       "frxChUEntry": frxChUEntry,
       "frxChUIndex": frxChUIndex,
       "frxChUType": frxChUType,
       "frxChUVersion": frxChUVersion,
       "frxSigProtocol": frxSigProtocol,
       "frxConfigSrc": frxConfigSrc,
       "frxDLCIAdLen": frxDLCIAdLen,
       "frxNetInOctets": frxNetInOctets,
       "frxNetOutOctets": frxNetOutOctets,
       "frxNetBadFrames": frxNetBadFrames,
       "frxNetHDLCEs": frxNetHDLCEs,
       "frxNetCRCEs": frxNetCRCEs,
       "frxNetLinkEs": frxNetLinkEs,
       "frxNetFrShEs": frxNetFrShEs,
       "frxNetFrLgEs": frxNetFrLgEs,
       "frxNetPPPEs": frxNetPPPEs,
       "frxNetBufEs": frxNetBufEs,
       "frxMgt": frxMgt,
       "frxMgtTable": frxMgtTable,
       "frxMgtEntry": frxMgtEntry,
       "frxPortsInSvc": frxPortsInSvc,
       "frxMgtT391": frxMgtT391,
       "frxMgtT392": frxMgtT392,
       "frxMgtN391": frxMgtN391,
       "frxMgtN392": frxMgtN392,
       "frxMgtN393": frxMgtN393,
       "frxNetLinkErrors": frxNetLinkErrors,
       "frxNetProtErrors": frxNetProtErrors,
       "frxNetChInactive": frxNetChInactive,
       "frxNetChStatus": frxNetChStatus,
       "frxMgtPortTable": frxMgtPortTable,
       "frxMgtPortEntry": frxMgtPortEntry,
       "frxPortIndex": frxPortIndex,
       "frxPortLinkErrors": frxPortLinkErrors,
       "frxPortProtErrors": frxPortProtErrors,
       "frxPortChInactive": frxPortChInactive,
       "frxPort": frxPort,
       "frxPortTable": frxPortTable,
       "frxPortEntry": frxPortEntry,
       "frxPortSpeed": frxPortSpeed,
       "frxPortProtocol": frxPortProtocol,
       "frxDSLStatus": frxDSLStatus,
       "frxPVCAssigned": frxPVCAssigned,
       "frxLastChange": frxLastChange,
       "frxBrite": frxBrite,
       "frxDSLInOctets": frxDSLInOctets,
       "frxDSLOutOctets": frxDSLOutOctets,
       "frxT1InOctets": frxT1InOctets,
       "frxT1OutOctets": frxT1OutOctets,
       "frxDSLBadFrames": frxDSLBadFrames,
       "frxDSLHDLCEs": frxDSLHDLCEs,
       "frxDSLCRCEs": frxDSLCRCEs,
       "frxDSLLinkEs": frxDSLLinkEs,
       "frxDSLFrShEs": frxDSLFrShEs,
       "frxDSLFrLgEs": frxDSLFrLgEs,
       "frxDSLDLCIEs": frxDSLDLCIEs,
       "frxTxBuf": frxTxBuf,
       "frxRxBuf": frxRxBuf,
       "frxPortNetEs": frxPortNetEs,
       "frxCircuitTable": frxCircuitTable,
       "frxCircuitEntry": frxCircuitEntry,
       "frxPvcIndex": frxPvcIndex,
       "frxCktCIR": frxCktCIR,
       "frxCktBc": frxCktBc,
       "frxCktBe": frxCktBe,
       "frxFarEndOpStat": frxFarEndOpStat,
       "frxCktInOctets": frxCktInOctets,
       "frxCktOutOctets": frxCktOutOctets,
       "frxCktInFrames": frxCktInFrames,
       "frxCktOutFrames": frxCktOutFrames,
       "frxCktDiscards": frxCktDiscards,
       "frxUEocTable": frxUEocTable,
       "frxUEocEntry": frxUEocEntry,
       "frxTestPort": frxTestPort,
       "frxTestType": frxTestType,
       "frxLoopLoc": frxLoopLoc,
       "frxLoopCh": frxLoopCh,
       "frxStartTest": frxStartTest,
       "frxBertRst": frxBertRst,
       "frxBertBE": frxBertBE,
       "frxBertTestTime": frxBertTestTime,
       "frxTestInProg": frxTestInProg,
       "frxUThrTable": frxUThrTable,
       "frxUThrEntry": frxUThrEntry,
       "frxPAddrIndex": frxPAddrIndex,
       "frxChEsTh": frxChEsTh,
       "frxCdEsTh": frxCdEsTh,
       "frxChSesTh": frxChSesTh,
       "frxCdSesTh": frxCdSesTh,
       "frxAlertMask": frxAlertMask,
       "frxThCond": frxThCond,
       "frxUPerfTable": frxUPerfTable,
       "frxUPerfEntry": frxUPerfEntry,
       "frxResetPM": frxResetPM,
       "frxPMtype": frxPMtype,
       "frxChEsTx": frxChEsTx,
       "frxChEsRx": frxChEsRx,
       "frxPhEsTx": frxPhEsTx,
       "frxPhEsRx": frxPhEsRx,
       "frxH2EsTx": frxH2EsTx,
       "frxH2EsRx": frxH2EsRx,
       "frxH3EsTx": frxH3EsTx,
       "frxH3EsRx": frxH3EsRx,
       "frxH4EsTx": frxH4EsTx,
       "frxH4EsRx": frxH4EsRx,
       "frxH5EsTx": frxH5EsTx,
       "frxH5EsRx": frxH5EsRx,
       "frxH6EsTx": frxH6EsTx,
       "frxH6EsRx": frxH6EsRx,
       "frxH7EsTx": frxH7EsTx,
       "frxH7EsRx": frxH7EsRx,
       "frxH8EsTx": frxH8EsTx,
       "frxH8EsRx": frxH8EsRx,
       "frxCdEsTx": frxCdEsTx,
       "frxCdEsRx": frxCdEsRx,
       "frxPdEsTx": frxPdEsTx,
       "frxPdEsRx": frxPdEsRx,
       "frxChSesTx": frxChSesTx,
       "frxChSesRx": frxChSesRx,
       "frxPhSesTx": frxPhSesTx,
       "frxPhSesRx": frxPhSesRx,
       "frxCdSesTx": frxCdSesTx,
       "frxCdSesRx": frxCdSesRx,
       "frxPdSesTx": frxPdSesTx,
       "frxPdSesRx": frxPdSesRx,
       "frxChBeTx": frxChBeTx,
       "frxChBeRx": frxChBeRx,
       "frxPhBeTx": frxPhBeTx,
       "frxPhBeRx": frxPhBeRx}
)
