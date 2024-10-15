# SNMP MIB module (CXMCVOX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXMCVOX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:40 2024
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

(cxModuleHwPhysSlot,) = mibBuilder.importSymbols(
    "CXModuleHardware-MIB",
    "cxModuleHwPhysSlot")

(cxMc600,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxMc600")

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

_CxMcVox_ObjectIdentity = ObjectIdentity
cxMcVox = _CxMcVox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2)
)
_CxMcVoxGlobal_ObjectIdentity = ObjectIdentity
cxMcVoxGlobal = _CxMcVoxGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1)
)


class _CxMcVoxGlobalAdmPathLng_Type(Integer32):
    """Custom type cxMcVoxGlobalAdmPathLng based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_CxMcVoxGlobalAdmPathLng_Type.__name__ = "Integer32"
_CxMcVoxGlobalAdmPathLng_Object = MibScalar
cxMcVoxGlobalAdmPathLng = _CxMcVoxGlobalAdmPathLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 1),
    _CxMcVoxGlobalAdmPathLng_Type()
)
cxMcVoxGlobalAdmPathLng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalAdmPathLng.setStatus("obsolete")


class _CxMcVoxGlobalReinitPath_Type(Integer32):
    """Custom type cxMcVoxGlobalReinitPath based on Integer32"""
    defaultValue = 1

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


_CxMcVoxGlobalReinitPath_Type.__name__ = "Integer32"
_CxMcVoxGlobalReinitPath_Object = MibScalar
cxMcVoxGlobalReinitPath = _CxMcVoxGlobalReinitPath_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 2),
    _CxMcVoxGlobalReinitPath_Type()
)
cxMcVoxGlobalReinitPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalReinitPath.setStatus("obsolete")


class _CxMcVoxGlobalClearPath_Type(Integer32):
    """Custom type cxMcVoxGlobalClearPath based on Integer32"""
    defaultValue = 1

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


_CxMcVoxGlobalClearPath_Type.__name__ = "Integer32"
_CxMcVoxGlobalClearPath_Object = MibScalar
cxMcVoxGlobalClearPath = _CxMcVoxGlobalClearPath_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 3),
    _CxMcVoxGlobalClearPath_Type()
)
cxMcVoxGlobalClearPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalClearPath.setStatus("deprecated")


class _CxMcVoxGlobalReinitNet_Type(Integer32):
    """Custom type cxMcVoxGlobalReinitNet based on Integer32"""
    defaultValue = 1

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


_CxMcVoxGlobalReinitNet_Type.__name__ = "Integer32"
_CxMcVoxGlobalReinitNet_Object = MibScalar
cxMcVoxGlobalReinitNet = _CxMcVoxGlobalReinitNet_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 4),
    _CxMcVoxGlobalReinitNet_Type()
)
cxMcVoxGlobalReinitNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalReinitNet.setStatus("obsolete")


class _CxMcVoxGlobalClearNet_Type(Integer32):
    """Custom type cxMcVoxGlobalClearNet based on Integer32"""
    defaultValue = 1

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


_CxMcVoxGlobalClearNet_Type.__name__ = "Integer32"
_CxMcVoxGlobalClearNet_Object = MibScalar
cxMcVoxGlobalClearNet = _CxMcVoxGlobalClearNet_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 5),
    _CxMcVoxGlobalClearNet_Type()
)
cxMcVoxGlobalClearNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalClearNet.setStatus("deprecated")


class _CxMcVoxGlobalAdmLocalId_Type(DisplayString):
    """Custom type cxMcVoxGlobalAdmLocalId based on DisplayString"""
    defaultValue = OctetString("          ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CxMcVoxGlobalAdmLocalId_Type.__name__ = "DisplayString"
_CxMcVoxGlobalAdmLocalId_Object = MibScalar
cxMcVoxGlobalAdmLocalId = _CxMcVoxGlobalAdmLocalId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 6),
    _CxMcVoxGlobalAdmLocalId_Type()
)
cxMcVoxGlobalAdmLocalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalAdmLocalId.setStatus("optional")


class _CxMcVoxGlobalOpeLocalId_Type(DisplayString):
    """Custom type cxMcVoxGlobalOpeLocalId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CxMcVoxGlobalOpeLocalId_Type.__name__ = "DisplayString"
_CxMcVoxGlobalOpeLocalId_Object = MibScalar
cxMcVoxGlobalOpeLocalId = _CxMcVoxGlobalOpeLocalId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 7),
    _CxMcVoxGlobalOpeLocalId_Type()
)
cxMcVoxGlobalOpeLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGlobalOpeLocalId.setStatus("optional")


class _CxMcVoxGlobalTensionRing_Type(Integer32):
    """Custom type cxMcVoxGlobalTensionRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_CxMcVoxGlobalTensionRing_Type.__name__ = "Integer32"
_CxMcVoxGlobalTensionRing_Object = MibScalar
cxMcVoxGlobalTensionRing = _CxMcVoxGlobalTensionRing_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 8),
    _CxMcVoxGlobalTensionRing_Type()
)
cxMcVoxGlobalTensionRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGlobalTensionRing.setStatus("mandatory")


class _CxMcVoxGlobalTensionDc_Type(Integer32):
    """Custom type cxMcVoxGlobalTensionDc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_CxMcVoxGlobalTensionDc_Type.__name__ = "Integer32"
_CxMcVoxGlobalTensionDc_Object = MibScalar
cxMcVoxGlobalTensionDc = _CxMcVoxGlobalTensionDc_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 9),
    _CxMcVoxGlobalTensionDc_Type()
)
cxMcVoxGlobalTensionDc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGlobalTensionDc.setStatus("mandatory")


class _CxMcVoxGlobalTrapRing_Type(Integer32):
    """Custom type cxMcVoxGlobalTrapRing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxGlobalTrapRing_Type.__name__ = "Integer32"
_CxMcVoxGlobalTrapRing_Object = MibScalar
cxMcVoxGlobalTrapRing = _CxMcVoxGlobalTrapRing_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 10),
    _CxMcVoxGlobalTrapRing_Type()
)
cxMcVoxGlobalTrapRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalTrapRing.setStatus("mandatory")


class _CxMcVoxGlobalTrapDc_Type(Integer32):
    """Custom type cxMcVoxGlobalTrapDc based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxGlobalTrapDc_Type.__name__ = "Integer32"
_CxMcVoxGlobalTrapDc_Object = MibScalar
cxMcVoxGlobalTrapDc = _CxMcVoxGlobalTrapDc_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 11),
    _CxMcVoxGlobalTrapDc_Type()
)
cxMcVoxGlobalTrapDc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalTrapDc.setStatus("mandatory")


class _CxMcVoxGlobalAdmGrpNbPoll_Type(Integer32):
    """Custom type cxMcVoxGlobalAdmGrpNbPoll based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CxMcVoxGlobalAdmGrpNbPoll_Type.__name__ = "Integer32"
_CxMcVoxGlobalAdmGrpNbPoll_Object = MibScalar
cxMcVoxGlobalAdmGrpNbPoll = _CxMcVoxGlobalAdmGrpNbPoll_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 12),
    _CxMcVoxGlobalAdmGrpNbPoll_Type()
)
cxMcVoxGlobalAdmGrpNbPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalAdmGrpNbPoll.setStatus("deprecated")


class _CxMcVoxGlobalOpeGrpNbPoll_Type(Integer32):
    """Custom type cxMcVoxGlobalOpeGrpNbPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CxMcVoxGlobalOpeGrpNbPoll_Type.__name__ = "Integer32"
_CxMcVoxGlobalOpeGrpNbPoll_Object = MibScalar
cxMcVoxGlobalOpeGrpNbPoll = _CxMcVoxGlobalOpeGrpNbPoll_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 13),
    _CxMcVoxGlobalOpeGrpNbPoll_Type()
)
cxMcVoxGlobalOpeGrpNbPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGlobalOpeGrpNbPoll.setStatus("deprecated")


class _CxMcVoxGlobalClearGrp_Type(Integer32):
    """Custom type cxMcVoxGlobalClearGrp based on Integer32"""
    defaultValue = 1

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


_CxMcVoxGlobalClearGrp_Type.__name__ = "Integer32"
_CxMcVoxGlobalClearGrp_Object = MibScalar
cxMcVoxGlobalClearGrp = _CxMcVoxGlobalClearGrp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 14),
    _CxMcVoxGlobalClearGrp_Type()
)
cxMcVoxGlobalClearGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalClearGrp.setStatus("optional")


class _CxMcVoxGlobalOpePathLng_Type(Integer32):
    """Custom type cxMcVoxGlobalOpePathLng based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_CxMcVoxGlobalOpePathLng_Type.__name__ = "Integer32"
_CxMcVoxGlobalOpePathLng_Object = MibScalar
cxMcVoxGlobalOpePathLng = _CxMcVoxGlobalOpePathLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 15),
    _CxMcVoxGlobalOpePathLng_Type()
)
cxMcVoxGlobalOpePathLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGlobalOpePathLng.setStatus("obsolete")


class _CxMcVoxGlobalReinitRouting_Type(Integer32):
    """Custom type cxMcVoxGlobalReinitRouting based on Integer32"""
    defaultValue = 1

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


_CxMcVoxGlobalReinitRouting_Type.__name__ = "Integer32"
_CxMcVoxGlobalReinitRouting_Object = MibScalar
cxMcVoxGlobalReinitRouting = _CxMcVoxGlobalReinitRouting_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 16),
    _CxMcVoxGlobalReinitRouting_Type()
)
cxMcVoxGlobalReinitRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalReinitRouting.setStatus("optional")


class _CxMcVoxGlobalForceDefConfig_Type(Integer32):
    """Custom type cxMcVoxGlobalForceDefConfig based on Integer32"""
    defaultValue = 1

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


_CxMcVoxGlobalForceDefConfig_Type.__name__ = "Integer32"
_CxMcVoxGlobalForceDefConfig_Object = MibScalar
cxMcVoxGlobalForceDefConfig = _CxMcVoxGlobalForceDefConfig_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 17),
    _CxMcVoxGlobalForceDefConfig_Type()
)
cxMcVoxGlobalForceDefConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalForceDefConfig.setStatus("optional")


class _CxMcVoxGlobalReinitPinTable_Type(Integer32):
    """Custom type cxMcVoxGlobalReinitPinTable based on Integer32"""
    defaultValue = 1

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


_CxMcVoxGlobalReinitPinTable_Type.__name__ = "Integer32"
_CxMcVoxGlobalReinitPinTable_Object = MibScalar
cxMcVoxGlobalReinitPinTable = _CxMcVoxGlobalReinitPinTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 18),
    _CxMcVoxGlobalReinitPinTable_Type()
)
cxMcVoxGlobalReinitPinTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalReinitPinTable.setStatus("optional")


class _CxMcVoxGlobalAdmEnablePinTable_Type(Integer32):
    """Custom type cxMcVoxGlobalAdmEnablePinTable based on Integer32"""
    defaultValue = 1

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


_CxMcVoxGlobalAdmEnablePinTable_Type.__name__ = "Integer32"
_CxMcVoxGlobalAdmEnablePinTable_Object = MibScalar
cxMcVoxGlobalAdmEnablePinTable = _CxMcVoxGlobalAdmEnablePinTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 19),
    _CxMcVoxGlobalAdmEnablePinTable_Type()
)
cxMcVoxGlobalAdmEnablePinTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalAdmEnablePinTable.setStatus("optional")


class _CxMcVoxGlobalOpeEnablePinTable_Type(Integer32):
    """Custom type cxMcVoxGlobalOpeEnablePinTable based on Integer32"""
    defaultValue = 1

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


_CxMcVoxGlobalOpeEnablePinTable_Type.__name__ = "Integer32"
_CxMcVoxGlobalOpeEnablePinTable_Object = MibScalar
cxMcVoxGlobalOpeEnablePinTable = _CxMcVoxGlobalOpeEnablePinTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 20),
    _CxMcVoxGlobalOpeEnablePinTable_Type()
)
cxMcVoxGlobalOpeEnablePinTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGlobalOpeEnablePinTable.setStatus("optional")


class _CxMcVoxGlobalReinitCodesTable_Type(Integer32):
    """Custom type cxMcVoxGlobalReinitCodesTable based on Integer32"""
    defaultValue = 1

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


_CxMcVoxGlobalReinitCodesTable_Type.__name__ = "Integer32"
_CxMcVoxGlobalReinitCodesTable_Object = MibScalar
cxMcVoxGlobalReinitCodesTable = _CxMcVoxGlobalReinitCodesTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 21),
    _CxMcVoxGlobalReinitCodesTable_Type()
)
cxMcVoxGlobalReinitCodesTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalReinitCodesTable.setStatus("optional")


class _CxMcVoxGlobalAdmEnableCodesTable_Type(Integer32):
    """Custom type cxMcVoxGlobalAdmEnableCodesTable based on Integer32"""
    defaultValue = 1

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


_CxMcVoxGlobalAdmEnableCodesTable_Type.__name__ = "Integer32"
_CxMcVoxGlobalAdmEnableCodesTable_Object = MibScalar
cxMcVoxGlobalAdmEnableCodesTable = _CxMcVoxGlobalAdmEnableCodesTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 22),
    _CxMcVoxGlobalAdmEnableCodesTable_Type()
)
cxMcVoxGlobalAdmEnableCodesTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalAdmEnableCodesTable.setStatus("optional")


class _CxMcVoxGlobalOpeEnableCodesTable_Type(Integer32):
    """Custom type cxMcVoxGlobalOpeEnableCodesTable based on Integer32"""
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


_CxMcVoxGlobalOpeEnableCodesTable_Type.__name__ = "Integer32"
_CxMcVoxGlobalOpeEnableCodesTable_Object = MibScalar
cxMcVoxGlobalOpeEnableCodesTable = _CxMcVoxGlobalOpeEnableCodesTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 23),
    _CxMcVoxGlobalOpeEnableCodesTable_Type()
)
cxMcVoxGlobalOpeEnableCodesTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGlobalOpeEnableCodesTable.setStatus("optional")


class _CxMcVoxGlobalSoftRev_Type(DisplayString):
    """Custom type cxMcVoxGlobalSoftRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CxMcVoxGlobalSoftRev_Type.__name__ = "DisplayString"
_CxMcVoxGlobalSoftRev_Object = MibScalar
cxMcVoxGlobalSoftRev = _CxMcVoxGlobalSoftRev_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 24),
    _CxMcVoxGlobalSoftRev_Type()
)
cxMcVoxGlobalSoftRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGlobalSoftRev.setStatus("optional")


class _CxMcVoxGlobalGlmInBetwReqTime_Type(Integer32):
    """Custom type cxMcVoxGlobalGlmInBetwReqTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_CxMcVoxGlobalGlmInBetwReqTime_Type.__name__ = "Integer32"
_CxMcVoxGlobalGlmInBetwReqTime_Object = MibScalar
cxMcVoxGlobalGlmInBetwReqTime = _CxMcVoxGlobalGlmInBetwReqTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 100),
    _CxMcVoxGlobalGlmInBetwReqTime_Type()
)
cxMcVoxGlobalGlmInBetwReqTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalGlmInBetwReqTime.setStatus("mandatory")


class _CxMcVoxGlobalGlmMaxTimeToTxReq_Type(Integer32):
    """Custom type cxMcVoxGlobalGlmMaxTimeToTxReq based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 20000),
    )


_CxMcVoxGlobalGlmMaxTimeToTxReq_Type.__name__ = "Integer32"
_CxMcVoxGlobalGlmMaxTimeToTxReq_Object = MibScalar
cxMcVoxGlobalGlmMaxTimeToTxReq = _CxMcVoxGlobalGlmMaxTimeToTxReq_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 101),
    _CxMcVoxGlobalGlmMaxTimeToTxReq_Type()
)
cxMcVoxGlobalGlmMaxTimeToTxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalGlmMaxTimeToTxReq.setStatus("mandatory")


class _CxMcVoxGlobalGlmInBetwRespTime_Type(Integer32):
    """Custom type cxMcVoxGlobalGlmInBetwRespTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_CxMcVoxGlobalGlmInBetwRespTime_Type.__name__ = "Integer32"
_CxMcVoxGlobalGlmInBetwRespTime_Object = MibScalar
cxMcVoxGlobalGlmInBetwRespTime = _CxMcVoxGlobalGlmInBetwRespTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 102),
    _CxMcVoxGlobalGlmInBetwRespTime_Type()
)
cxMcVoxGlobalGlmInBetwRespTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalGlmInBetwRespTime.setStatus("mandatory")


class _CxMcVoxGlobalGlmMaxTimeToTxResp_Type(Integer32):
    """Custom type cxMcVoxGlobalGlmMaxTimeToTxResp based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 20000),
    )


_CxMcVoxGlobalGlmMaxTimeToTxResp_Type.__name__ = "Integer32"
_CxMcVoxGlobalGlmMaxTimeToTxResp_Object = MibScalar
cxMcVoxGlobalGlmMaxTimeToTxResp = _CxMcVoxGlobalGlmMaxTimeToTxResp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 103),
    _CxMcVoxGlobalGlmMaxTimeToTxResp_Type()
)
cxMcVoxGlobalGlmMaxTimeToTxResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalGlmMaxTimeToTxResp.setStatus("mandatory")


class _CxMcVoxGlobalGlmVoiceSilenceTime_Type(Integer32):
    """Custom type cxMcVoxGlobalGlmVoiceSilenceTime based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_CxMcVoxGlobalGlmVoiceSilenceTime_Type.__name__ = "Integer32"
_CxMcVoxGlobalGlmVoiceSilenceTime_Object = MibScalar
cxMcVoxGlobalGlmVoiceSilenceTime = _CxMcVoxGlobalGlmVoiceSilenceTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 104),
    _CxMcVoxGlobalGlmVoiceSilenceTime_Type()
)
cxMcVoxGlobalGlmVoiceSilenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalGlmVoiceSilenceTime.setStatus("mandatory")


class _CxMcVoxGlobalGlmSupervSilenceTime_Type(Integer32):
    """Custom type cxMcVoxGlobalGlmSupervSilenceTime based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 60000),
    )


_CxMcVoxGlobalGlmSupervSilenceTime_Type.__name__ = "Integer32"
_CxMcVoxGlobalGlmSupervSilenceTime_Object = MibScalar
cxMcVoxGlobalGlmSupervSilenceTime = _CxMcVoxGlobalGlmSupervSilenceTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 105),
    _CxMcVoxGlobalGlmSupervSilenceTime_Type()
)
cxMcVoxGlobalGlmSupervSilenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalGlmSupervSilenceTime.setStatus("mandatory")


class _CxMcVoxGlobalGsdAutoCnctDelay_Type(Integer32):
    """Custom type cxMcVoxGlobalGsdAutoCnctDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_CxMcVoxGlobalGsdAutoCnctDelay_Type.__name__ = "Integer32"
_CxMcVoxGlobalGsdAutoCnctDelay_Object = MibScalar
cxMcVoxGlobalGsdAutoCnctDelay = _CxMcVoxGlobalGsdAutoCnctDelay_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 106),
    _CxMcVoxGlobalGsdAutoCnctDelay_Type()
)
cxMcVoxGlobalGsdAutoCnctDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalGsdAutoCnctDelay.setStatus("mandatory")


class _CxMcVoxGlobalClearLclExt_Type(Integer32):
    """Custom type cxMcVoxGlobalClearLclExt based on Integer32"""
    defaultValue = 1

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


_CxMcVoxGlobalClearLclExt_Type.__name__ = "Integer32"
_CxMcVoxGlobalClearLclExt_Object = MibScalar
cxMcVoxGlobalClearLclExt = _CxMcVoxGlobalClearLclExt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 107),
    _CxMcVoxGlobalClearLclExt_Type()
)
cxMcVoxGlobalClearLclExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalClearLclExt.setStatus("optional")


class _CxMcVoxGlobalClearRmtExt_Type(Integer32):
    """Custom type cxMcVoxGlobalClearRmtExt based on Integer32"""
    defaultValue = 1

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


_CxMcVoxGlobalClearRmtExt_Type.__name__ = "Integer32"
_CxMcVoxGlobalClearRmtExt_Object = MibScalar
cxMcVoxGlobalClearRmtExt = _CxMcVoxGlobalClearRmtExt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 108),
    _CxMcVoxGlobalClearRmtExt_Type()
)
cxMcVoxGlobalClearRmtExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalClearRmtExt.setStatus("optional")


class _CxMcVoxGlobalWanSlot_Type(Integer32):
    """Custom type cxMcVoxGlobalWanSlot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CxMcVoxGlobalWanSlot_Type.__name__ = "Integer32"
_CxMcVoxGlobalWanSlot_Object = MibScalar
cxMcVoxGlobalWanSlot = _CxMcVoxGlobalWanSlot_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 109),
    _CxMcVoxGlobalWanSlot_Type()
)
cxMcVoxGlobalWanSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalWanSlot.setStatus("mandatory")


class _CxMcVoxGlobalNetNbDigits_Type(Integer32):
    """Custom type cxMcVoxGlobalNetNbDigits based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxGlobalNetNbDigits_Type.__name__ = "Integer32"
_CxMcVoxGlobalNetNbDigits_Object = MibScalar
cxMcVoxGlobalNetNbDigits = _CxMcVoxGlobalNetNbDigits_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 110),
    _CxMcVoxGlobalNetNbDigits_Type()
)
cxMcVoxGlobalNetNbDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalNetNbDigits.setStatus("mandatory")


class _CxMcVoxMibLevel_Type(Integer32):
    """Custom type cxMcVoxMibLevel based on Integer32"""
    defaultValue = 0


_CxMcVoxMibLevel_Object = MibScalar
cxMcVoxMibLevel = _CxMcVoxMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 111),
    _CxMcVoxMibLevel_Type()
)
cxMcVoxMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxMibLevel.setStatus("mandatory")


class _CxMcVoxGlobalRecogAcc_Type(Integer32):
    """Custom type cxMcVoxGlobalRecogAcc based on Integer32"""
    defaultValue = 1

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


_CxMcVoxGlobalRecogAcc_Type.__name__ = "Integer32"
_CxMcVoxGlobalRecogAcc_Object = MibScalar
cxMcVoxGlobalRecogAcc = _CxMcVoxGlobalRecogAcc_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 112),
    _CxMcVoxGlobalRecogAcc_Type()
)
cxMcVoxGlobalRecogAcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalRecogAcc.setStatus("mandatory")


class _CxMcVoxGlobalAccCode_Type(DisplayString):
    """Custom type cxMcVoxGlobalAccCode based on DisplayString"""
    defaultValue = OctetString("011")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CxMcVoxGlobalAccCode_Type.__name__ = "DisplayString"
_CxMcVoxGlobalAccCode_Object = MibScalar
cxMcVoxGlobalAccCode = _CxMcVoxGlobalAccCode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 113),
    _CxMcVoxGlobalAccCode_Type()
)
cxMcVoxGlobalAccCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalAccCode.setStatus("mandatory")


class _CxMcVoxGlobalAccCodeLng_Type(Integer32):
    """Custom type cxMcVoxGlobalAccCodeLng based on Integer32"""
    defaultValue = 3


_CxMcVoxGlobalAccCodeLng_Object = MibScalar
cxMcVoxGlobalAccCodeLng = _CxMcVoxGlobalAccCodeLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 114),
    _CxMcVoxGlobalAccCodeLng_Type()
)
cxMcVoxGlobalAccCodeLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGlobalAccCodeLng.setStatus("mandatory")


class _CxMcVoxGlobalAdmPinCodeLng_Type(Integer32):
    """Custom type cxMcVoxGlobalAdmPinCodeLng based on Integer32"""
    defaultValue = 4


_CxMcVoxGlobalAdmPinCodeLng_Object = MibScalar
cxMcVoxGlobalAdmPinCodeLng = _CxMcVoxGlobalAdmPinCodeLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 115),
    _CxMcVoxGlobalAdmPinCodeLng_Type()
)
cxMcVoxGlobalAdmPinCodeLng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalAdmPinCodeLng.setStatus("mandatory")


class _CxMcVoxGlobalOpePinCodeLng_Type(Integer32):
    """Custom type cxMcVoxGlobalOpePinCodeLng based on Integer32"""
    defaultValue = 4


_CxMcVoxGlobalOpePinCodeLng_Object = MibScalar
cxMcVoxGlobalOpePinCodeLng = _CxMcVoxGlobalOpePinCodeLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 116),
    _CxMcVoxGlobalOpePinCodeLng_Type()
)
cxMcVoxGlobalOpePinCodeLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGlobalOpePinCodeLng.setStatus("mandatory")


class _CxMcVoxGlobalClearHistoryTable_Type(Integer32):
    """Custom type cxMcVoxGlobalClearHistoryTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxGlobalClearHistoryTable_Type.__name__ = "Integer32"
_CxMcVoxGlobalClearHistoryTable_Object = MibScalar
cxMcVoxGlobalClearHistoryTable = _CxMcVoxGlobalClearHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 117),
    _CxMcVoxGlobalClearHistoryTable_Type()
)
cxMcVoxGlobalClearHistoryTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalClearHistoryTable.setStatus("mandatory")


class _CxMcVoxGlobalHistoryMaxNumberOfEntries_Type(Integer32):
    """Custom type cxMcVoxGlobalHistoryMaxNumberOfEntries based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 256),
    )


_CxMcVoxGlobalHistoryMaxNumberOfEntries_Type.__name__ = "Integer32"
_CxMcVoxGlobalHistoryMaxNumberOfEntries_Object = MibScalar
cxMcVoxGlobalHistoryMaxNumberOfEntries = _CxMcVoxGlobalHistoryMaxNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 118),
    _CxMcVoxGlobalHistoryMaxNumberOfEntries_Type()
)
cxMcVoxGlobalHistoryMaxNumberOfEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalHistoryMaxNumberOfEntries.setStatus("mandatory")


class _CxMcVoxGlobalHistoryPercentageFull_Type(Integer32):
    """Custom type cxMcVoxGlobalHistoryPercentageFull based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 95),
    )


_CxMcVoxGlobalHistoryPercentageFull_Type.__name__ = "Integer32"
_CxMcVoxGlobalHistoryPercentageFull_Object = MibScalar
cxMcVoxGlobalHistoryPercentageFull = _CxMcVoxGlobalHistoryPercentageFull_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 119),
    _CxMcVoxGlobalHistoryPercentageFull_Type()
)
cxMcVoxGlobalHistoryPercentageFull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalHistoryPercentageFull.setStatus("mandatory")


class _CxMcVoxGlobalTrapHistory_Type(Integer32):
    """Custom type cxMcVoxGlobalTrapHistory based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxGlobalTrapHistory_Type.__name__ = "Integer32"
_CxMcVoxGlobalTrapHistory_Object = MibScalar
cxMcVoxGlobalTrapHistory = _CxMcVoxGlobalTrapHistory_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 120),
    _CxMcVoxGlobalTrapHistory_Type()
)
cxMcVoxGlobalTrapHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalTrapHistory.setStatus("mandatory")


class _CxMcVoxGlobalLseTimerT2_Type(Integer32):
    """Custom type cxMcVoxGlobalLseTimerT2 based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CxMcVoxGlobalLseTimerT2_Type.__name__ = "Integer32"
_CxMcVoxGlobalLseTimerT2_Object = MibScalar
cxMcVoxGlobalLseTimerT2 = _CxMcVoxGlobalLseTimerT2_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 121),
    _CxMcVoxGlobalLseTimerT2_Type()
)
cxMcVoxGlobalLseTimerT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalLseTimerT2.setStatus("mandatory")


class _CxMcVoxGlobalLseTimerT3_Type(Integer32):
    """Custom type cxMcVoxGlobalLseTimerT3 based on Integer32"""
    defaultValue = 550

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CxMcVoxGlobalLseTimerT3_Type.__name__ = "Integer32"
_CxMcVoxGlobalLseTimerT3_Object = MibScalar
cxMcVoxGlobalLseTimerT3 = _CxMcVoxGlobalLseTimerT3_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 122),
    _CxMcVoxGlobalLseTimerT3_Type()
)
cxMcVoxGlobalLseTimerT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalLseTimerT3.setStatus("mandatory")


class _CxMcVoxGlobalExtBitMask_Type(Integer32):
    """Custom type cxMcVoxGlobalExtBitMask based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxMcVoxGlobalExtBitMask_Type.__name__ = "Integer32"
_CxMcVoxGlobalExtBitMask_Object = MibScalar
cxMcVoxGlobalExtBitMask = _CxMcVoxGlobalExtBitMask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 1, 123),
    _CxMcVoxGlobalExtBitMask_Type()
)
cxMcVoxGlobalExtBitMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGlobalExtBitMask.setStatus("mandatory")
_CxMcVoxCfgTable_Object = MibTable
cxMcVoxCfgTable = _CxMcVoxCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cxMcVoxCfgTable.setStatus("mandatory")
_CxMcVoxCfgEntry_Object = MibTableRow
cxMcVoxCfgEntry = _CxMcVoxCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1)
)
cxMcVoxCfgEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxCfgCardIndex"),
    (0, "CXMCVOX-MIB", "cxMcVoxCfgPortIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxCfgEntry.setStatus("mandatory")


class _CxMcVoxCfgCardIndex_Type(Integer32):
    """Custom type cxMcVoxCfgCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CxMcVoxCfgCardIndex_Type.__name__ = "Integer32"
_CxMcVoxCfgCardIndex_Object = MibTableColumn
cxMcVoxCfgCardIndex = _CxMcVoxCfgCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 1),
    _CxMcVoxCfgCardIndex_Type()
)
cxMcVoxCfgCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxCfgCardIndex.setStatus("mandatory")


class _CxMcVoxCfgPortIndex_Type(Integer32):
    """Custom type cxMcVoxCfgPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CxMcVoxCfgPortIndex_Type.__name__ = "Integer32"
_CxMcVoxCfgPortIndex_Object = MibTableColumn
cxMcVoxCfgPortIndex = _CxMcVoxCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 2),
    _CxMcVoxCfgPortIndex_Type()
)
cxMcVoxCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxCfgPortIndex.setStatus("mandatory")


class _CxMcVoxCfgDriverAdmUsed_Type(Integer32):
    """Custom type cxMcVoxCfgDriverAdmUsed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("em", 1),
          ("fxo", 3),
          ("fxs", 2))
    )


_CxMcVoxCfgDriverAdmUsed_Type.__name__ = "Integer32"
_CxMcVoxCfgDriverAdmUsed_Object = MibTableColumn
cxMcVoxCfgDriverAdmUsed = _CxMcVoxCfgDriverAdmUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 3),
    _CxMcVoxCfgDriverAdmUsed_Type()
)
cxMcVoxCfgDriverAdmUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxCfgDriverAdmUsed.setStatus("mandatory")


class _CxMcVoxCfgDriverOpeUsed_Type(Integer32):
    """Custom type cxMcVoxCfgDriverOpeUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("em", 1),
          ("fxo", 3),
          ("fxs", 2))
    )


_CxMcVoxCfgDriverOpeUsed_Type.__name__ = "Integer32"
_CxMcVoxCfgDriverOpeUsed_Object = MibTableColumn
cxMcVoxCfgDriverOpeUsed = _CxMcVoxCfgDriverOpeUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 4),
    _CxMcVoxCfgDriverOpeUsed_Type()
)
cxMcVoxCfgDriverOpeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxCfgDriverOpeUsed.setStatus("mandatory")


class _CxMcVoxCfgTrapOnLine_Type(Integer32):
    """Custom type cxMcVoxCfgTrapOnLine based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxCfgTrapOnLine_Type.__name__ = "Integer32"
_CxMcVoxCfgTrapOnLine_Object = MibTableColumn
cxMcVoxCfgTrapOnLine = _CxMcVoxCfgTrapOnLine_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 5),
    _CxMcVoxCfgTrapOnLine_Type()
)
cxMcVoxCfgTrapOnLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxCfgTrapOnLine.setStatus("deprecated")


class _CxMcVoxCfgTrapOffLine_Type(Integer32):
    """Custom type cxMcVoxCfgTrapOffLine based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxCfgTrapOffLine_Type.__name__ = "Integer32"
_CxMcVoxCfgTrapOffLine_Object = MibTableColumn
cxMcVoxCfgTrapOffLine = _CxMcVoxCfgTrapOffLine_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 6),
    _CxMcVoxCfgTrapOffLine_Type()
)
cxMcVoxCfgTrapOffLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxCfgTrapOffLine.setStatus("deprecated")


class _CxMcVoxCfgTrapStatus_Type(Integer32):
    """Custom type cxMcVoxCfgTrapStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxCfgTrapStatus_Type.__name__ = "Integer32"
_CxMcVoxCfgTrapStatus_Object = MibTableColumn
cxMcVoxCfgTrapStatus = _CxMcVoxCfgTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 7),
    _CxMcVoxCfgTrapStatus_Type()
)
cxMcVoxCfgTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxCfgTrapStatus.setStatus("mandatory")


class _CxMcVoxCfgTrapState_Type(Integer32):
    """Custom type cxMcVoxCfgTrapState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxCfgTrapState_Type.__name__ = "Integer32"
_CxMcVoxCfgTrapState_Object = MibTableColumn
cxMcVoxCfgTrapState = _CxMcVoxCfgTrapState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 8),
    _CxMcVoxCfgTrapState_Type()
)
cxMcVoxCfgTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxCfgTrapState.setStatus("deprecated")


class _CxMcVoxCfgTestPort_Type(Integer32):
    """Custom type cxMcVoxCfgTestPort based on Integer32"""
    defaultValue = 1

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


_CxMcVoxCfgTestPort_Type.__name__ = "Integer32"
_CxMcVoxCfgTestPort_Object = MibTableColumn
cxMcVoxCfgTestPort = _CxMcVoxCfgTestPort_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 9),
    _CxMcVoxCfgTestPort_Type()
)
cxMcVoxCfgTestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxCfgTestPort.setStatus("optional")


class _CxMcVoxCfgToneTest_Type(Integer32):
    """Custom type cxMcVoxCfgToneTest based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxCfgToneTest_Type.__name__ = "Integer32"
_CxMcVoxCfgToneTest_Object = MibTableColumn
cxMcVoxCfgToneTest = _CxMcVoxCfgToneTest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 10),
    _CxMcVoxCfgToneTest_Type()
)
cxMcVoxCfgToneTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxCfgToneTest.setStatus("mandatory")


class _CxMcVoxCfgReinitPort_Type(Integer32):
    """Custom type cxMcVoxCfgReinitPort based on Integer32"""
    defaultValue = 1

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


_CxMcVoxCfgReinitPort_Type.__name__ = "Integer32"
_CxMcVoxCfgReinitPort_Object = MibTableColumn
cxMcVoxCfgReinitPort = _CxMcVoxCfgReinitPort_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 11),
    _CxMcVoxCfgReinitPort_Type()
)
cxMcVoxCfgReinitPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxCfgReinitPort.setStatus("optional")


class _CxMcVoxCfgClearPort_Type(Integer32):
    """Custom type cxMcVoxCfgClearPort based on Integer32"""
    defaultValue = 1

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


_CxMcVoxCfgClearPort_Type.__name__ = "Integer32"
_CxMcVoxCfgClearPort_Object = MibTableColumn
cxMcVoxCfgClearPort = _CxMcVoxCfgClearPort_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 12),
    _CxMcVoxCfgClearPort_Type()
)
cxMcVoxCfgClearPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxCfgClearPort.setStatus("optional")


class _CxMcVoxCfgOpeAcelpRev_Type(DisplayString):
    """Custom type cxMcVoxCfgOpeAcelpRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_CxMcVoxCfgOpeAcelpRev_Type.__name__ = "DisplayString"
_CxMcVoxCfgOpeAcelpRev_Object = MibTableColumn
cxMcVoxCfgOpeAcelpRev = _CxMcVoxCfgOpeAcelpRev_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 14),
    _CxMcVoxCfgOpeAcelpRev_Type()
)
cxMcVoxCfgOpeAcelpRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxCfgOpeAcelpRev.setStatus("optional")


class _CxMcVoxCfgCmdImmTest_Type(Integer32):
    """Custom type cxMcVoxCfgCmdImmTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CxMcVoxCfgCmdImmTest_Type.__name__ = "Integer32"
_CxMcVoxCfgCmdImmTest_Object = MibTableColumn
cxMcVoxCfgCmdImmTest = _CxMcVoxCfgCmdImmTest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 15),
    _CxMcVoxCfgCmdImmTest_Type()
)
cxMcVoxCfgCmdImmTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxCfgCmdImmTest.setStatus("mandatory")


class _CxMcVoxCfgCmdTest_Type(Integer32):
    """Custom type cxMcVoxCfgCmdTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CxMcVoxCfgCmdTest_Type.__name__ = "Integer32"
_CxMcVoxCfgCmdTest_Object = MibTableColumn
cxMcVoxCfgCmdTest = _CxMcVoxCfgCmdTest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 16),
    _CxMcVoxCfgCmdTest_Type()
)
cxMcVoxCfgCmdTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxCfgCmdTest.setStatus("mandatory")


class _CxMcVoxCfgMaxPktFrame_Type(Integer32):
    """Custom type cxMcVoxCfgMaxPktFrame based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CxMcVoxCfgMaxPktFrame_Type.__name__ = "Integer32"
_CxMcVoxCfgMaxPktFrame_Object = MibTableColumn
cxMcVoxCfgMaxPktFrame = _CxMcVoxCfgMaxPktFrame_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 17),
    _CxMcVoxCfgMaxPktFrame_Type()
)
cxMcVoxCfgMaxPktFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxCfgMaxPktFrame.setStatus("mandatory")


class _CxMcVoxCfgMaxSkew_Type(Integer32):
    """Custom type cxMcVoxCfgMaxSkew based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 125),
    )


_CxMcVoxCfgMaxSkew_Type.__name__ = "Integer32"
_CxMcVoxCfgMaxSkew_Object = MibTableColumn
cxMcVoxCfgMaxSkew = _CxMcVoxCfgMaxSkew_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 2, 1, 18),
    _CxMcVoxCfgMaxSkew_Type()
)
cxMcVoxCfgMaxSkew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxCfgMaxSkew.setStatus("mandatory")
_CxMcVoxStatAndLog_ObjectIdentity = ObjectIdentity
cxMcVoxStatAndLog = _CxMcVoxStatAndLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3)
)
_CxMcVoxStatusTable_Object = MibTable
cxMcVoxStatusTable = _CxMcVoxStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cxMcVoxStatusTable.setStatus("mandatory")
_CxMcVoxStatusEntry_Object = MibTableRow
cxMcVoxStatusEntry = _CxMcVoxStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1)
)
cxMcVoxStatusEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxStatusCardNumber"),
    (0, "CXMCVOX-MIB", "cxMcVoxStatusPortNumber"),
)
if mibBuilder.loadTexts:
    cxMcVoxStatusEntry.setStatus("mandatory")


class _CxMcVoxStatusCardNumber_Type(Integer32):
    """Custom type cxMcVoxStatusCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CxMcVoxStatusCardNumber_Type.__name__ = "Integer32"
_CxMcVoxStatusCardNumber_Object = MibTableColumn
cxMcVoxStatusCardNumber = _CxMcVoxStatusCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 1),
    _CxMcVoxStatusCardNumber_Type()
)
cxMcVoxStatusCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusCardNumber.setStatus("mandatory")


class _CxMcVoxStatusPortNumber_Type(Integer32):
    """Custom type cxMcVoxStatusPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CxMcVoxStatusPortNumber_Type.__name__ = "Integer32"
_CxMcVoxStatusPortNumber_Object = MibTableColumn
cxMcVoxStatusPortNumber = _CxMcVoxStatusPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 2),
    _CxMcVoxStatusPortNumber_Type()
)
cxMcVoxStatusPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusPortNumber.setStatus("mandatory")


class _CxMcVoxStatusPortStatus_Type(Integer32):
    """Custom type cxMcVoxStatusPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              31,
              32,
              33,
              34,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("appl-err-1", 41),
          ("appl-err-2", 42),
          ("appl-err-3", 43),
          ("appl-err-4", 44),
          ("boot-err-1", 31),
          ("boot-err-2", 32),
          ("boot-err-3", 33),
          ("boot-err-4", 34),
          ("disable", 1),
          ("enable", 2),
          ("no-voice-io", 3))
    )


_CxMcVoxStatusPortStatus_Type.__name__ = "Integer32"
_CxMcVoxStatusPortStatus_Object = MibTableColumn
cxMcVoxStatusPortStatus = _CxMcVoxStatusPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 3),
    _CxMcVoxStatusPortStatus_Type()
)
cxMcVoxStatusPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusPortStatus.setStatus("mandatory")


class _CxMcVoxStatusHookLocal_Type(Integer32):
    """Custom type cxMcVoxStatusHookLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("unknown", 3))
    )


_CxMcVoxStatusHookLocal_Type.__name__ = "Integer32"
_CxMcVoxStatusHookLocal_Object = MibTableColumn
cxMcVoxStatusHookLocal = _CxMcVoxStatusHookLocal_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 4),
    _CxMcVoxStatusHookLocal_Type()
)
cxMcVoxStatusHookLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusHookLocal.setStatus("mandatory")


class _CxMcVoxStatusHookRem_Type(Integer32):
    """Custom type cxMcVoxStatusHookRem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("unknown", 3))
    )


_CxMcVoxStatusHookRem_Type.__name__ = "Integer32"
_CxMcVoxStatusHookRem_Object = MibTableColumn
cxMcVoxStatusHookRem = _CxMcVoxStatusHookRem_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 5),
    _CxMcVoxStatusHookRem_Type()
)
cxMcVoxStatusHookRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusHookRem.setStatus("mandatory")


class _CxMcVoxStatusIoAccess_Type(Integer32):
    """Custom type cxMcVoxStatusIoAccess based on Integer32"""
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
        *(("fault", 1),
          ("inapplicable", 3),
          ("passed", 2),
          ("running", 4))
    )


_CxMcVoxStatusIoAccess_Type.__name__ = "Integer32"
_CxMcVoxStatusIoAccess_Object = MibTableColumn
cxMcVoxStatusIoAccess = _CxMcVoxStatusIoAccess_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 6),
    _CxMcVoxStatusIoAccess_Type()
)
cxMcVoxStatusIoAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusIoAccess.setStatus("mandatory")


class _CxMcVoxStatusChannelAccess_Type(Integer32):
    """Custom type cxMcVoxStatusChannelAccess based on Integer32"""
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
        *(("fault", 1),
          ("inapplicable", 3),
          ("passed", 2),
          ("running", 4))
    )


_CxMcVoxStatusChannelAccess_Type.__name__ = "Integer32"
_CxMcVoxStatusChannelAccess_Object = MibTableColumn
cxMcVoxStatusChannelAccess = _CxMcVoxStatusChannelAccess_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 7),
    _CxMcVoxStatusChannelAccess_Type()
)
cxMcVoxStatusChannelAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusChannelAccess.setStatus("mandatory")


class _CxMcVoxStatusDspRam_Type(Integer32):
    """Custom type cxMcVoxStatusDspRam based on Integer32"""
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
        *(("fault", 1),
          ("inapplicable", 3),
          ("passed", 2),
          ("running", 4))
    )


_CxMcVoxStatusDspRam_Type.__name__ = "Integer32"
_CxMcVoxStatusDspRam_Object = MibTableColumn
cxMcVoxStatusDspRam = _CxMcVoxStatusDspRam_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 8),
    _CxMcVoxStatusDspRam_Type()
)
cxMcVoxStatusDspRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusDspRam.setStatus("mandatory")


class _CxMcVoxStatusDspDpram_Type(Integer32):
    """Custom type cxMcVoxStatusDspDpram based on Integer32"""
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
        *(("fault", 1),
          ("inapplicable", 3),
          ("passed", 2),
          ("running", 4))
    )


_CxMcVoxStatusDspDpram_Type.__name__ = "Integer32"
_CxMcVoxStatusDspDpram_Object = MibTableColumn
cxMcVoxStatusDspDpram = _CxMcVoxStatusDspDpram_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 9),
    _CxMcVoxStatusDspDpram_Type()
)
cxMcVoxStatusDspDpram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusDspDpram.setStatus("mandatory")


class _CxMcVoxStatusSamplingTime_Type(Integer32):
    """Custom type cxMcVoxStatusSamplingTime based on Integer32"""
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
        *(("fault", 1),
          ("inapplicable", 3),
          ("passed", 2),
          ("running", 4))
    )


_CxMcVoxStatusSamplingTime_Type.__name__ = "Integer32"
_CxMcVoxStatusSamplingTime_Object = MibTableColumn
cxMcVoxStatusSamplingTime = _CxMcVoxStatusSamplingTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 10),
    _CxMcVoxStatusSamplingTime_Type()
)
cxMcVoxStatusSamplingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusSamplingTime.setStatus("mandatory")


class _CxMcVoxStatusWatchdog_Type(Integer32):
    """Custom type cxMcVoxStatusWatchdog based on Integer32"""
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
        *(("fault", 1),
          ("inapplicable", 3),
          ("passed", 2),
          ("running", 4))
    )


_CxMcVoxStatusWatchdog_Type.__name__ = "Integer32"
_CxMcVoxStatusWatchdog_Object = MibTableColumn
cxMcVoxStatusWatchdog = _CxMcVoxStatusWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 11),
    _CxMcVoxStatusWatchdog_Type()
)
cxMcVoxStatusWatchdog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusWatchdog.setStatus("mandatory")


class _CxMcVoxStatusRemPortStatus_Type(Integer32):
    """Custom type cxMcVoxStatusRemPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CxMcVoxStatusRemPortStatus_Type.__name__ = "Integer32"
_CxMcVoxStatusRemPortStatus_Object = MibTableColumn
cxMcVoxStatusRemPortStatus = _CxMcVoxStatusRemPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 12),
    _CxMcVoxStatusRemPortStatus_Type()
)
cxMcVoxStatusRemPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusRemPortStatus.setStatus("mandatory")


class _CxMcVoxStatusInputDbmLevel_Type(Integer32):
    """Custom type cxMcVoxStatusInputDbmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(700, 1050),
    )


_CxMcVoxStatusInputDbmLevel_Type.__name__ = "Integer32"
_CxMcVoxStatusInputDbmLevel_Object = MibTableColumn
cxMcVoxStatusInputDbmLevel = _CxMcVoxStatusInputDbmLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 13),
    _CxMcVoxStatusInputDbmLevel_Type()
)
cxMcVoxStatusInputDbmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusInputDbmLevel.setStatus("mandatory")


class _CxMcVoxStatusPhyIfType_Type(Integer32):
    """Custom type cxMcVoxStatusPhyIfType based on Integer32"""
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
        *(("if-absent", 4),
          ("if-em", 1),
          ("if-fxo", 3),
          ("if-fxs", 2),
          ("if-unknown", 5))
    )


_CxMcVoxStatusPhyIfType_Type.__name__ = "Integer32"
_CxMcVoxStatusPhyIfType_Object = MibTableColumn
cxMcVoxStatusPhyIfType = _CxMcVoxStatusPhyIfType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 14),
    _CxMcVoxStatusPhyIfType_Type()
)
cxMcVoxStatusPhyIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusPhyIfType.setStatus("mandatory")


class _CxMcVoxStatusDspUtilization_Type(Integer32):
    """Custom type cxMcVoxStatusDspUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CxMcVoxStatusDspUtilization_Type.__name__ = "Integer32"
_CxMcVoxStatusDspUtilization_Object = MibTableColumn
cxMcVoxStatusDspUtilization = _CxMcVoxStatusDspUtilization_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 100),
    _CxMcVoxStatusDspUtilization_Type()
)
cxMcVoxStatusDspUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusDspUtilization.setStatus("mandatory")


class _CxMcVoxStatusIOResetState_Type(Integer32):
    """Custom type cxMcVoxStatusIOResetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in-reset", 1),
          ("normal", 2),
          ("unknown", 3))
    )


_CxMcVoxStatusIOResetState_Type.__name__ = "Integer32"
_CxMcVoxStatusIOResetState_Object = MibTableColumn
cxMcVoxStatusIOResetState = _CxMcVoxStatusIOResetState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 1, 1, 101),
    _CxMcVoxStatusIOResetState_Type()
)
cxMcVoxStatusIOResetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatusIOResetState.setStatus("mandatory")
_CxMcVoxEventTable_Object = MibTable
cxMcVoxEventTable = _CxMcVoxEventTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cxMcVoxEventTable.setStatus("deprecated")
_CxMcVoxEventEntry_Object = MibTableRow
cxMcVoxEventEntry = _CxMcVoxEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 2, 1)
)
cxMcVoxEventEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxEventCardNumber"),
    (0, "CXMCVOX-MIB", "cxMcVoxEventPortNumber"),
    (0, "CXMCVOX-MIB", "cxMcVoxEventLogIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxEventEntry.setStatus("deprecated")


class _CxMcVoxEventCardNumber_Type(Integer32):
    """Custom type cxMcVoxEventCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxEventCardNumber_Type.__name__ = "Integer32"
_CxMcVoxEventCardNumber_Object = MibTableColumn
cxMcVoxEventCardNumber = _CxMcVoxEventCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 2, 1, 1),
    _CxMcVoxEventCardNumber_Type()
)
cxMcVoxEventCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEventCardNumber.setStatus("deprecated")


class _CxMcVoxEventPortNumber_Type(Integer32):
    """Custom type cxMcVoxEventPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CxMcVoxEventPortNumber_Type.__name__ = "Integer32"
_CxMcVoxEventPortNumber_Object = MibTableColumn
cxMcVoxEventPortNumber = _CxMcVoxEventPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 2, 1, 2),
    _CxMcVoxEventPortNumber_Type()
)
cxMcVoxEventPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEventPortNumber.setStatus("deprecated")


class _CxMcVoxEventLogIndex_Type(Integer32):
    """Custom type cxMcVoxEventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CxMcVoxEventLogIndex_Type.__name__ = "Integer32"
_CxMcVoxEventLogIndex_Object = MibTableColumn
cxMcVoxEventLogIndex = _CxMcVoxEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 2, 1, 3),
    _CxMcVoxEventLogIndex_Type()
)
cxMcVoxEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEventLogIndex.setStatus("deprecated")


class _CxMcVoxEventDateAndTimeOnLine_Type(DisplayString):
    """Custom type cxMcVoxEventDateAndTimeOnLine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_CxMcVoxEventDateAndTimeOnLine_Type.__name__ = "DisplayString"
_CxMcVoxEventDateAndTimeOnLine_Object = MibTableColumn
cxMcVoxEventDateAndTimeOnLine = _CxMcVoxEventDateAndTimeOnLine_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 2, 1, 4),
    _CxMcVoxEventDateAndTimeOnLine_Type()
)
cxMcVoxEventDateAndTimeOnLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEventDateAndTimeOnLine.setStatus("deprecated")


class _CxMcVoxEventDateAndTimeOffLine_Type(DisplayString):
    """Custom type cxMcVoxEventDateAndTimeOffLine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_CxMcVoxEventDateAndTimeOffLine_Type.__name__ = "DisplayString"
_CxMcVoxEventDateAndTimeOffLine_Object = MibTableColumn
cxMcVoxEventDateAndTimeOffLine = _CxMcVoxEventDateAndTimeOffLine_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 2, 1, 5),
    _CxMcVoxEventDateAndTimeOffLine_Type()
)
cxMcVoxEventDateAndTimeOffLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEventDateAndTimeOffLine.setStatus("deprecated")


class _CxMcVoxEventPhoneNumber_Type(DisplayString):
    """Custom type cxMcVoxEventPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CxMcVoxEventPhoneNumber_Type.__name__ = "DisplayString"
_CxMcVoxEventPhoneNumber_Object = MibTableColumn
cxMcVoxEventPhoneNumber = _CxMcVoxEventPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 2, 1, 6),
    _CxMcVoxEventPhoneNumber_Type()
)
cxMcVoxEventPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEventPhoneNumber.setStatus("deprecated")


class _CxMcVoxEventLnkState_Type(Integer32):
    """Custom type cxMcVoxEventLnkState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("busy", 3),
          ("errActiveChn", 5),
          ("errLnk", 7),
          ("errPath", 6),
          ("fixedLnkDown", 8),
          ("fixedLnkUp", 9),
          ("open", 4),
          ("remError", 2),
          ("remUnavailable", 1))
    )


_CxMcVoxEventLnkState_Type.__name__ = "Integer32"
_CxMcVoxEventLnkState_Object = MibTableColumn
cxMcVoxEventLnkState = _CxMcVoxEventLnkState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 2, 1, 7),
    _CxMcVoxEventLnkState_Type()
)
cxMcVoxEventLnkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEventLnkState.setStatus("deprecated")


class _CxMcVoxEventPin_Type(DisplayString):
    """Custom type cxMcVoxEventPin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 8),
    )


_CxMcVoxEventPin_Type.__name__ = "DisplayString"
_CxMcVoxEventPin_Object = MibTableColumn
cxMcVoxEventPin = _CxMcVoxEventPin_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 2, 1, 8),
    _CxMcVoxEventPin_Type()
)
cxMcVoxEventPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEventPin.setStatus("deprecated")


class _CxMcVoxEventClrEvts_Type(Integer32):
    """Custom type cxMcVoxEventClrEvts based on Integer32"""
    defaultValue = 1

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


_CxMcVoxEventClrEvts_Type.__name__ = "Integer32"
_CxMcVoxEventClrEvts_Object = MibTableColumn
cxMcVoxEventClrEvts = _CxMcVoxEventClrEvts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 2, 1, 9),
    _CxMcVoxEventClrEvts_Type()
)
cxMcVoxEventClrEvts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEventClrEvts.setStatus("deprecated")
_CxMcVoxStateTable_Object = MibTable
cxMcVoxStateTable = _CxMcVoxStateTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    cxMcVoxStateTable.setStatus("deprecated")
_CxMcVoxStateEntry_Object = MibTableRow
cxMcVoxStateEntry = _CxMcVoxStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 3, 1)
)
cxMcVoxStateEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxStateCardNumber"),
    (0, "CXMCVOX-MIB", "cxMcVoxStatePortNumber"),
    (0, "CXMCVOX-MIB", "cxMcVoxStateLogIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxStateEntry.setStatus("deprecated")


class _CxMcVoxStateCardNumber_Type(Integer32):
    """Custom type cxMcVoxStateCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxStateCardNumber_Type.__name__ = "Integer32"
_CxMcVoxStateCardNumber_Object = MibTableColumn
cxMcVoxStateCardNumber = _CxMcVoxStateCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 3, 1, 1),
    _CxMcVoxStateCardNumber_Type()
)
cxMcVoxStateCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStateCardNumber.setStatus("deprecated")


class _CxMcVoxStatePortNumber_Type(Integer32):
    """Custom type cxMcVoxStatePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CxMcVoxStatePortNumber_Type.__name__ = "Integer32"
_CxMcVoxStatePortNumber_Object = MibTableColumn
cxMcVoxStatePortNumber = _CxMcVoxStatePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 3, 1, 2),
    _CxMcVoxStatePortNumber_Type()
)
cxMcVoxStatePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatePortNumber.setStatus("deprecated")


class _CxMcVoxStateLogIndex_Type(Integer32):
    """Custom type cxMcVoxStateLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CxMcVoxStateLogIndex_Type.__name__ = "Integer32"
_CxMcVoxStateLogIndex_Object = MibTableColumn
cxMcVoxStateLogIndex = _CxMcVoxStateLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 3, 1, 3),
    _CxMcVoxStateLogIndex_Type()
)
cxMcVoxStateLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStateLogIndex.setStatus("deprecated")


class _CxMcVoxStatePathId_Type(DisplayString):
    """Custom type cxMcVoxStatePathId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxStatePathId_Type.__name__ = "DisplayString"
_CxMcVoxStatePathId_Object = MibTableColumn
cxMcVoxStatePathId = _CxMcVoxStatePathId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 3, 1, 4),
    _CxMcVoxStatePathId_Type()
)
cxMcVoxStatePathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStatePathId.setStatus("deprecated")


class _CxMcVoxStateDateAndTime_Type(DisplayString):
    """Custom type cxMcVoxStateDateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_CxMcVoxStateDateAndTime_Type.__name__ = "DisplayString"
_CxMcVoxStateDateAndTime_Object = MibTableColumn
cxMcVoxStateDateAndTime = _CxMcVoxStateDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 3, 1, 5),
    _CxMcVoxStateDateAndTime_Type()
)
cxMcVoxStateDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStateDateAndTime.setStatus("deprecated")


class _CxMcVoxStateLnkState_Type(Integer32):
    """Custom type cxMcVoxStateLnkState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("busy", 3),
          ("errActiveChn", 5),
          ("errLnk", 7),
          ("errPath", 6),
          ("fixedLnkDown", 8),
          ("fixedLnkUp", 9),
          ("open", 4),
          ("remError", 2),
          ("remUnavailable", 1))
    )


_CxMcVoxStateLnkState_Type.__name__ = "Integer32"
_CxMcVoxStateLnkState_Object = MibTableColumn
cxMcVoxStateLnkState = _CxMcVoxStateLnkState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 3, 1, 6),
    _CxMcVoxStateLnkState_Type()
)
cxMcVoxStateLnkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStateLnkState.setStatus("deprecated")


class _CxMcVoxStateRmtExt_Type(DisplayString):
    """Custom type cxMcVoxStateRmtExt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CxMcVoxStateRmtExt_Type.__name__ = "DisplayString"
_CxMcVoxStateRmtExt_Object = MibTableColumn
cxMcVoxStateRmtExt = _CxMcVoxStateRmtExt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 3, 3, 1, 7),
    _CxMcVoxStateRmtExt_Type()
)
cxMcVoxStateRmtExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxStateRmtExt.setStatus("deprecated")
_CxMcVoxPathAdmTable_Object = MibTable
cxMcVoxPathAdmTable = _CxMcVoxPathAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cxMcVoxPathAdmTable.setStatus("deprecated")
_CxMcVoxPathAdmEntry_Object = MibTableRow
cxMcVoxPathAdmEntry = _CxMcVoxPathAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 4, 1)
)
cxMcVoxPathAdmEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxPathAdmIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxPathAdmEntry.setStatus("deprecated")


class _CxMcVoxPathAdmIndex_Type(Integer32):
    """Custom type cxMcVoxPathAdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CxMcVoxPathAdmIndex_Type.__name__ = "Integer32"
_CxMcVoxPathAdmIndex_Object = MibTableColumn
cxMcVoxPathAdmIndex = _CxMcVoxPathAdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 4, 1, 1),
    _CxMcVoxPathAdmIndex_Type()
)
cxMcVoxPathAdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxPathAdmIndex.setStatus("deprecated")


class _CxMcVoxPathAdmRowStatus_Type(Integer32):
    """Custom type cxMcVoxPathAdmRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxMcVoxPathAdmRowStatus_Type.__name__ = "Integer32"
_CxMcVoxPathAdmRowStatus_Object = MibTableColumn
cxMcVoxPathAdmRowStatus = _CxMcVoxPathAdmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 4, 1, 2),
    _CxMcVoxPathAdmRowStatus_Type()
)
cxMcVoxPathAdmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxPathAdmRowStatus.setStatus("deprecated")


class _CxMcVoxPathAdmPathId_Type(DisplayString):
    """Custom type cxMcVoxPathAdmPathId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxPathAdmPathId_Type.__name__ = "DisplayString"
_CxMcVoxPathAdmPathId_Object = MibTableColumn
cxMcVoxPathAdmPathId = _CxMcVoxPathAdmPathId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 4, 1, 3),
    _CxMcVoxPathAdmPathId_Type()
)
cxMcVoxPathAdmPathId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxPathAdmPathId.setStatus("deprecated")


class _CxMcVoxPathAdmRemStationId_Type(DisplayString):
    """Custom type cxMcVoxPathAdmRemStationId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_CxMcVoxPathAdmRemStationId_Type.__name__ = "DisplayString"
_CxMcVoxPathAdmRemStationId_Object = MibTableColumn
cxMcVoxPathAdmRemStationId = _CxMcVoxPathAdmRemStationId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 4, 1, 4),
    _CxMcVoxPathAdmRemStationId_Type()
)
cxMcVoxPathAdmRemStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxPathAdmRemStationId.setStatus("deprecated")


class _CxMcVoxPathAdmHunt_Type(Integer32):
    """Custom type cxMcVoxPathAdmHunt based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CxMcVoxPathAdmHunt_Type.__name__ = "Integer32"
_CxMcVoxPathAdmHunt_Object = MibTableColumn
cxMcVoxPathAdmHunt = _CxMcVoxPathAdmHunt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 4, 1, 5),
    _CxMcVoxPathAdmHunt_Type()
)
cxMcVoxPathAdmHunt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxPathAdmHunt.setStatus("deprecated")


class _CxMcVoxPathAdmLng_Type(Integer32):
    """Custom type cxMcVoxPathAdmLng based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxPathAdmLng_Type.__name__ = "Integer32"
_CxMcVoxPathAdmLng_Object = MibTableColumn
cxMcVoxPathAdmLng = _CxMcVoxPathAdmLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 4, 1, 6),
    _CxMcVoxPathAdmLng_Type()
)
cxMcVoxPathAdmLng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxPathAdmLng.setStatus("deprecated")
_CxMcVoxPathOpeTable_Object = MibTable
cxMcVoxPathOpeTable = _CxMcVoxPathOpeTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cxMcVoxPathOpeTable.setStatus("deprecated")
_CxMcVoxPathOpeEntry_Object = MibTableRow
cxMcVoxPathOpeEntry = _CxMcVoxPathOpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 5, 1)
)
cxMcVoxPathOpeEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxPathOpeIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxPathOpeEntry.setStatus("deprecated")


class _CxMcVoxPathOpeIndex_Type(Integer32):
    """Custom type cxMcVoxPathOpeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CxMcVoxPathOpeIndex_Type.__name__ = "Integer32"
_CxMcVoxPathOpeIndex_Object = MibTableColumn
cxMcVoxPathOpeIndex = _CxMcVoxPathOpeIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 5, 1, 1),
    _CxMcVoxPathOpeIndex_Type()
)
cxMcVoxPathOpeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxPathOpeIndex.setStatus("deprecated")


class _CxMcVoxPathOpePathId_Type(DisplayString):
    """Custom type cxMcVoxPathOpePathId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxPathOpePathId_Type.__name__ = "DisplayString"
_CxMcVoxPathOpePathId_Object = MibTableColumn
cxMcVoxPathOpePathId = _CxMcVoxPathOpePathId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 5, 1, 2),
    _CxMcVoxPathOpePathId_Type()
)
cxMcVoxPathOpePathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxPathOpePathId.setStatus("deprecated")


class _CxMcVoxPathOpeRemStationId_Type(DisplayString):
    """Custom type cxMcVoxPathOpeRemStationId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_CxMcVoxPathOpeRemStationId_Type.__name__ = "DisplayString"
_CxMcVoxPathOpeRemStationId_Object = MibTableColumn
cxMcVoxPathOpeRemStationId = _CxMcVoxPathOpeRemStationId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 5, 1, 3),
    _CxMcVoxPathOpeRemStationId_Type()
)
cxMcVoxPathOpeRemStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxPathOpeRemStationId.setStatus("deprecated")


class _CxMcVoxPathOpeHunt_Type(Integer32):
    """Custom type cxMcVoxPathOpeHunt based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CxMcVoxPathOpeHunt_Type.__name__ = "Integer32"
_CxMcVoxPathOpeHunt_Object = MibTableColumn
cxMcVoxPathOpeHunt = _CxMcVoxPathOpeHunt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 5, 1, 4),
    _CxMcVoxPathOpeHunt_Type()
)
cxMcVoxPathOpeHunt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxPathOpeHunt.setStatus("deprecated")


class _CxMcVoxPathOpeLng_Type(Integer32):
    """Custom type cxMcVoxPathOpeLng based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxPathOpeLng_Type.__name__ = "Integer32"
_CxMcVoxPathOpeLng_Object = MibTableColumn
cxMcVoxPathOpeLng = _CxMcVoxPathOpeLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 5, 1, 5),
    _CxMcVoxPathOpeLng_Type()
)
cxMcVoxPathOpeLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxPathOpeLng.setStatus("deprecated")
_CxMcVoxNetAdmTable_Object = MibTable
cxMcVoxNetAdmTable = _CxMcVoxNetAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cxMcVoxNetAdmTable.setStatus("deprecated")
_CxMcVoxNetAdmEntry_Object = MibTableRow
cxMcVoxNetAdmEntry = _CxMcVoxNetAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 6, 1)
)
cxMcVoxNetAdmEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxNetAdmIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxNetAdmEntry.setStatus("deprecated")


class _CxMcVoxNetAdmIndex_Type(Integer32):
    """Custom type cxMcVoxNetAdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CxMcVoxNetAdmIndex_Type.__name__ = "Integer32"
_CxMcVoxNetAdmIndex_Object = MibTableColumn
cxMcVoxNetAdmIndex = _CxMcVoxNetAdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 6, 1, 1),
    _CxMcVoxNetAdmIndex_Type()
)
cxMcVoxNetAdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxNetAdmIndex.setStatus("deprecated")


class _CxMcVoxNetAdmRowStatus_Type(Integer32):
    """Custom type cxMcVoxNetAdmRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxMcVoxNetAdmRowStatus_Type.__name__ = "Integer32"
_CxMcVoxNetAdmRowStatus_Object = MibTableColumn
cxMcVoxNetAdmRowStatus = _CxMcVoxNetAdmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 6, 1, 2),
    _CxMcVoxNetAdmRowStatus_Type()
)
cxMcVoxNetAdmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxNetAdmRowStatus.setStatus("deprecated")


class _CxMcVoxNetAdmRemStationId_Type(DisplayString):
    """Custom type cxMcVoxNetAdmRemStationId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_CxMcVoxNetAdmRemStationId_Type.__name__ = "DisplayString"
_CxMcVoxNetAdmRemStationId_Object = MibTableColumn
cxMcVoxNetAdmRemStationId = _CxMcVoxNetAdmRemStationId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 6, 1, 3),
    _CxMcVoxNetAdmRemStationId_Type()
)
cxMcVoxNetAdmRemStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxNetAdmRemStationId.setStatus("deprecated")


class _CxMcVoxNetAdmLocalLnkStation_Type(Integer32):
    """Custom type cxMcVoxNetAdmLocalLnkStation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CxMcVoxNetAdmLocalLnkStation_Type.__name__ = "Integer32"
_CxMcVoxNetAdmLocalLnkStation_Object = MibTableColumn
cxMcVoxNetAdmLocalLnkStation = _CxMcVoxNetAdmLocalLnkStation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 6, 1, 4),
    _CxMcVoxNetAdmLocalLnkStation_Type()
)
cxMcVoxNetAdmLocalLnkStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxNetAdmLocalLnkStation.setStatus("deprecated")


class _CxMcVoxNetAdmRoute_Type(Integer32):
    """Custom type cxMcVoxNetAdmRoute based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CxMcVoxNetAdmRoute_Type.__name__ = "Integer32"
_CxMcVoxNetAdmRoute_Object = MibTableColumn
cxMcVoxNetAdmRoute = _CxMcVoxNetAdmRoute_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 6, 1, 5),
    _CxMcVoxNetAdmRoute_Type()
)
cxMcVoxNetAdmRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxNetAdmRoute.setStatus("deprecated")


class _CxMcVoxNetAdmRemVoxStation_Type(Integer32):
    """Custom type cxMcVoxNetAdmRemVoxStation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CxMcVoxNetAdmRemVoxStation_Type.__name__ = "Integer32"
_CxMcVoxNetAdmRemVoxStation_Object = MibTableColumn
cxMcVoxNetAdmRemVoxStation = _CxMcVoxNetAdmRemVoxStation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 6, 1, 6),
    _CxMcVoxNetAdmRemVoxStation_Type()
)
cxMcVoxNetAdmRemVoxStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxNetAdmRemVoxStation.setStatus("deprecated")
_CxMcVoxNetOpeTable_Object = MibTable
cxMcVoxNetOpeTable = _CxMcVoxNetOpeTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cxMcVoxNetOpeTable.setStatus("deprecated")
_CxMcVoxNetOpeEntry_Object = MibTableRow
cxMcVoxNetOpeEntry = _CxMcVoxNetOpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 7, 1)
)
cxMcVoxNetOpeEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxNetOpeIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxNetOpeEntry.setStatus("deprecated")


class _CxMcVoxNetOpeIndex_Type(Integer32):
    """Custom type cxMcVoxNetOpeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CxMcVoxNetOpeIndex_Type.__name__ = "Integer32"
_CxMcVoxNetOpeIndex_Object = MibTableColumn
cxMcVoxNetOpeIndex = _CxMcVoxNetOpeIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 7, 1, 1),
    _CxMcVoxNetOpeIndex_Type()
)
cxMcVoxNetOpeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxNetOpeIndex.setStatus("deprecated")


class _CxMcVoxNetOpeRemStationId_Type(DisplayString):
    """Custom type cxMcVoxNetOpeRemStationId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_CxMcVoxNetOpeRemStationId_Type.__name__ = "DisplayString"
_CxMcVoxNetOpeRemStationId_Object = MibTableColumn
cxMcVoxNetOpeRemStationId = _CxMcVoxNetOpeRemStationId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 7, 1, 2),
    _CxMcVoxNetOpeRemStationId_Type()
)
cxMcVoxNetOpeRemStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxNetOpeRemStationId.setStatus("deprecated")


class _CxMcVoxNetOpeLocalLnkStation_Type(Integer32):
    """Custom type cxMcVoxNetOpeLocalLnkStation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CxMcVoxNetOpeLocalLnkStation_Type.__name__ = "Integer32"
_CxMcVoxNetOpeLocalLnkStation_Object = MibTableColumn
cxMcVoxNetOpeLocalLnkStation = _CxMcVoxNetOpeLocalLnkStation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 7, 1, 3),
    _CxMcVoxNetOpeLocalLnkStation_Type()
)
cxMcVoxNetOpeLocalLnkStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxNetOpeLocalLnkStation.setStatus("deprecated")


class _CxMcVoxNetOpeRoute_Type(Integer32):
    """Custom type cxMcVoxNetOpeRoute based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CxMcVoxNetOpeRoute_Type.__name__ = "Integer32"
_CxMcVoxNetOpeRoute_Object = MibTableColumn
cxMcVoxNetOpeRoute = _CxMcVoxNetOpeRoute_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 7, 1, 4),
    _CxMcVoxNetOpeRoute_Type()
)
cxMcVoxNetOpeRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxNetOpeRoute.setStatus("deprecated")


class _CxMcVoxNetOpeRemVoxStation_Type(Integer32):
    """Custom type cxMcVoxNetOpeRemVoxStation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CxMcVoxNetOpeRemVoxStation_Type.__name__ = "Integer32"
_CxMcVoxNetOpeRemVoxStation_Object = MibTableColumn
cxMcVoxNetOpeRemVoxStation = _CxMcVoxNetOpeRemVoxStation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 7, 1, 5),
    _CxMcVoxNetOpeRemVoxStation_Type()
)
cxMcVoxNetOpeRemVoxStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxNetOpeRemVoxStation.setStatus("deprecated")
_CxMcVoxDriverAdm_ObjectIdentity = ObjectIdentity
cxMcVoxDriverAdm = _CxMcVoxDriverAdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8)
)
_CxMcVoxEmAdmTable_Object = MibTable
cxMcVoxEmAdmTable = _CxMcVoxEmAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    cxMcVoxEmAdmTable.setStatus("mandatory")
_CxMcVoxEmAdmEntry_Object = MibTableRow
cxMcVoxEmAdmEntry = _CxMcVoxEmAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1)
)
cxMcVoxEmAdmEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxEmAdmCardUsed"),
    (0, "CXMCVOX-MIB", "cxMcVoxEmAdmPortUsed"),
)
if mibBuilder.loadTexts:
    cxMcVoxEmAdmEntry.setStatus("mandatory")


class _CxMcVoxEmAdmCardUsed_Type(Integer32):
    """Custom type cxMcVoxEmAdmCardUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CxMcVoxEmAdmCardUsed_Type.__name__ = "Integer32"
_CxMcVoxEmAdmCardUsed_Object = MibTableColumn
cxMcVoxEmAdmCardUsed = _CxMcVoxEmAdmCardUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 1),
    _CxMcVoxEmAdmCardUsed_Type()
)
cxMcVoxEmAdmCardUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmCardUsed.setStatus("mandatory")


class _CxMcVoxEmAdmPortUsed_Type(Integer32):
    """Custom type cxMcVoxEmAdmPortUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CxMcVoxEmAdmPortUsed_Type.__name__ = "Integer32"
_CxMcVoxEmAdmPortUsed_Object = MibTableColumn
cxMcVoxEmAdmPortUsed = _CxMcVoxEmAdmPortUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 2),
    _CxMcVoxEmAdmPortUsed_Type()
)
cxMcVoxEmAdmPortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmPortUsed.setStatus("mandatory")


class _CxMcVoxEmAdmPortStatus_Type(Integer32):
    """Custom type cxMcVoxEmAdmPortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxEmAdmPortStatus_Type.__name__ = "Integer32"
_CxMcVoxEmAdmPortStatus_Object = MibTableColumn
cxMcVoxEmAdmPortStatus = _CxMcVoxEmAdmPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 3),
    _CxMcVoxEmAdmPortStatus_Type()
)
cxMcVoxEmAdmPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmPortStatus.setStatus("mandatory")


class _CxMcVoxEmAdmVocoder_Type(Integer32):
    """Custom type cxMcVoxEmAdmVocoder based on Integer32"""
    defaultValue = 2

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
        *(("bps5800", 1),
          ("bps8000", 2),
          ("kbps16", 6),
          ("kbps24", 5),
          ("kbps32", 4),
          ("kbps40", 3),
          ("opt7", 7),
          ("opt8", 8))
    )


_CxMcVoxEmAdmVocoder_Type.__name__ = "Integer32"
_CxMcVoxEmAdmVocoder_Object = MibTableColumn
cxMcVoxEmAdmVocoder = _CxMcVoxEmAdmVocoder_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 4),
    _CxMcVoxEmAdmVocoder_Type()
)
cxMcVoxEmAdmVocoder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmVocoder.setStatus("mandatory")


class _CxMcVoxEmAdmFaxBw_Type(Integer32):
    """Custom type cxMcVoxEmAdmFaxBw based on Integer32"""
    defaultValue = 3

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
        *(("bps2400", 1),
          ("bps4800", 2),
          ("bps7200", 3),
          ("bps9600", 4))
    )


_CxMcVoxEmAdmFaxBw_Type.__name__ = "Integer32"
_CxMcVoxEmAdmFaxBw_Object = MibTableColumn
cxMcVoxEmAdmFaxBw = _CxMcVoxEmAdmFaxBw_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 5),
    _CxMcVoxEmAdmFaxBw_Type()
)
cxMcVoxEmAdmFaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmFaxBw.setStatus("mandatory")


class _CxMcVoxEmAdmAutoCnx_Type(Integer32):
    """Custom type cxMcVoxEmAdmAutoCnx based on Integer32"""
    defaultValue = 1

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


_CxMcVoxEmAdmAutoCnx_Type.__name__ = "Integer32"
_CxMcVoxEmAdmAutoCnx_Object = MibTableColumn
cxMcVoxEmAdmAutoCnx = _CxMcVoxEmAdmAutoCnx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 6),
    _CxMcVoxEmAdmAutoCnx_Type()
)
cxMcVoxEmAdmAutoCnx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmAutoCnx.setStatus("obsolete")


class _CxMcVoxEmAdmPathId_Type(DisplayString):
    """Custom type cxMcVoxEmAdmPathId based on DisplayString"""
    defaultValue = OctetString("000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxEmAdmPathId_Type.__name__ = "DisplayString"
_CxMcVoxEmAdmPathId_Object = MibTableColumn
cxMcVoxEmAdmPathId = _CxMcVoxEmAdmPathId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 7),
    _CxMcVoxEmAdmPathId_Type()
)
cxMcVoxEmAdmPathId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmPathId.setStatus("deprecated")


class _CxMcVoxEmAdmTxGain_Type(Integer32):
    """Custom type cxMcVoxEmAdmTxGain based on Integer32"""
    defaultValue = 960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxEmAdmTxGain_Type.__name__ = "Integer32"
_CxMcVoxEmAdmTxGain_Object = MibTableColumn
cxMcVoxEmAdmTxGain = _CxMcVoxEmAdmTxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 8),
    _CxMcVoxEmAdmTxGain_Type()
)
cxMcVoxEmAdmTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmTxGain.setStatus("mandatory")


class _CxMcVoxEmAdmRxGain_Type(Integer32):
    """Custom type cxMcVoxEmAdmRxGain based on Integer32"""
    defaultValue = 960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxEmAdmRxGain_Type.__name__ = "Integer32"
_CxMcVoxEmAdmRxGain_Object = MibTableColumn
cxMcVoxEmAdmRxGain = _CxMcVoxEmAdmRxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 9),
    _CxMcVoxEmAdmRxGain_Type()
)
cxMcVoxEmAdmRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmRxGain.setStatus("mandatory")


class _CxMcVoxEmAdmEchoCancel_Type(Integer32):
    """Custom type cxMcVoxEmAdmEchoCancel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxEmAdmEchoCancel_Type.__name__ = "Integer32"
_CxMcVoxEmAdmEchoCancel_Object = MibTableColumn
cxMcVoxEmAdmEchoCancel = _CxMcVoxEmAdmEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 10),
    _CxMcVoxEmAdmEchoCancel_Type()
)
cxMcVoxEmAdmEchoCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmEchoCancel.setStatus("mandatory")


class _CxMcVoxEmAdmType_Type(Integer32):
    """Custom type cxMcVoxEmAdmType based on Integer32"""
    defaultValue = 2

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
        *(("type-1", 1),
          ("type-2", 2),
          ("type-3", 3),
          ("type-4", 4),
          ("type-5", 5))
    )


_CxMcVoxEmAdmType_Type.__name__ = "Integer32"
_CxMcVoxEmAdmType_Object = MibTableColumn
cxMcVoxEmAdmType = _CxMcVoxEmAdmType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 11),
    _CxMcVoxEmAdmType_Type()
)
cxMcVoxEmAdmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmType.setStatus("mandatory")


class _CxMcVoxEmAdmMode_Type(Integer32):
    """Custom type cxMcVoxEmAdmMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reverse", 2))
    )


_CxMcVoxEmAdmMode_Type.__name__ = "Integer32"
_CxMcVoxEmAdmMode_Object = MibTableColumn
cxMcVoxEmAdmMode = _CxMcVoxEmAdmMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 12),
    _CxMcVoxEmAdmMode_Type()
)
cxMcVoxEmAdmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmMode.setStatus("mandatory")


class _CxMcVoxEmAdmDialType_Type(Integer32):
    """Custom type cxMcVoxEmAdmDialType based on Integer32"""
    defaultValue = 1

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
        *(("dtmf", 1),
          ("mfR1", 3),
          ("mfR2", 4),
          ("pulse", 2))
    )


_CxMcVoxEmAdmDialType_Type.__name__ = "Integer32"
_CxMcVoxEmAdmDialType_Object = MibTableColumn
cxMcVoxEmAdmDialType = _CxMcVoxEmAdmDialType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 13),
    _CxMcVoxEmAdmDialType_Type()
)
cxMcVoxEmAdmDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmDialType.setStatus("mandatory")


class _CxMcVoxEmAdmSignalType_Type(Integer32):
    """Custom type cxMcVoxEmAdmSignalType based on Integer32"""
    defaultValue = 1

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
        *(("ac15", 4),
          ("delay", 2),
          ("isdn", 8),
          ("mfcr2", 7),
          ("normal", 1),
          ("openchn", 5),
          ("r2", 6),
          ("wink", 3))
    )


_CxMcVoxEmAdmSignalType_Type.__name__ = "Integer32"
_CxMcVoxEmAdmSignalType_Object = MibTableColumn
cxMcVoxEmAdmSignalType = _CxMcVoxEmAdmSignalType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 14),
    _CxMcVoxEmAdmSignalType_Type()
)
cxMcVoxEmAdmSignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmSignalType.setStatus("mandatory")


class _CxMcVoxEmAdmAc15Type_Type(Integer32):
    """Custom type cxMcVoxEmAdmAc15Type based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delay", 2),
          ("normal", 1))
    )


_CxMcVoxEmAdmAc15Type_Type.__name__ = "Integer32"
_CxMcVoxEmAdmAc15Type_Object = MibTableColumn
cxMcVoxEmAdmAc15Type = _CxMcVoxEmAdmAc15Type_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 15),
    _CxMcVoxEmAdmAc15Type_Type()
)
cxMcVoxEmAdmAc15Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmAc15Type.setStatus("mandatory")


class _CxMcVoxEmAdmAc15TimeOn_Type(Integer32):
    """Custom type cxMcVoxEmAdmAc15TimeOn based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxEmAdmAc15TimeOn_Type.__name__ = "Integer32"
_CxMcVoxEmAdmAc15TimeOn_Object = MibTableColumn
cxMcVoxEmAdmAc15TimeOn = _CxMcVoxEmAdmAc15TimeOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 16),
    _CxMcVoxEmAdmAc15TimeOn_Type()
)
cxMcVoxEmAdmAc15TimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmAc15TimeOn.setStatus("mandatory")


class _CxMcVoxEmAdmAc15TimeOff_Type(Integer32):
    """Custom type cxMcVoxEmAdmAc15TimeOff based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxEmAdmAc15TimeOff_Type.__name__ = "Integer32"
_CxMcVoxEmAdmAc15TimeOff_Object = MibTableColumn
cxMcVoxEmAdmAc15TimeOff = _CxMcVoxEmAdmAc15TimeOff_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 17),
    _CxMcVoxEmAdmAc15TimeOff_Type()
)
cxMcVoxEmAdmAc15TimeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmAc15TimeOff.setStatus("mandatory")


class _CxMcVoxEmAdmCnctType_Type(Integer32):
    """Custom type cxMcVoxEmAdmCnctType based on Integer32"""
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
        *(("auto-connect", 2),
          ("fixed", 3),
          ("switched", 1))
    )


_CxMcVoxEmAdmCnctType_Type.__name__ = "Integer32"
_CxMcVoxEmAdmCnctType_Object = MibTableColumn
cxMcVoxEmAdmCnctType = _CxMcVoxEmAdmCnctType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 18),
    _CxMcVoxEmAdmCnctType_Type()
)
cxMcVoxEmAdmCnctType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmCnctType.setStatus("mandatory")


class _CxMcVoxEmAdmRingType_Type(Integer32):
    """Custom type cxMcVoxEmAdmRingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("international", 2),
          ("north-american", 1))
    )


_CxMcVoxEmAdmRingType_Type.__name__ = "Integer32"
_CxMcVoxEmAdmRingType_Object = MibTableColumn
cxMcVoxEmAdmRingType = _CxMcVoxEmAdmRingType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 19),
    _CxMcVoxEmAdmRingType_Type()
)
cxMcVoxEmAdmRingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmRingType.setStatus("mandatory")


class _CxMcVoxEmAdmRmtExt_Type(DisplayString):
    """Custom type cxMcVoxEmAdmRmtExt based on DisplayString"""
    defaultValue = OctetString("000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CxMcVoxEmAdmRmtExt_Type.__name__ = "DisplayString"
_CxMcVoxEmAdmRmtExt_Object = MibTableColumn
cxMcVoxEmAdmRmtExt = _CxMcVoxEmAdmRmtExt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 20),
    _CxMcVoxEmAdmRmtExt_Type()
)
cxMcVoxEmAdmRmtExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmRmtExt.setStatus("mandatory")


class _CxMcVoxEmAdmRmtId_Type(DisplayString):
    """Custom type cxMcVoxEmAdmRmtId based on DisplayString"""
    defaultValue = OctetString("          ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CxMcVoxEmAdmRmtId_Type.__name__ = "DisplayString"
_CxMcVoxEmAdmRmtId_Object = MibTableColumn
cxMcVoxEmAdmRmtId = _CxMcVoxEmAdmRmtId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 21),
    _CxMcVoxEmAdmRmtId_Type()
)
cxMcVoxEmAdmRmtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmRmtId.setStatus("optional")


class _CxMcVoxEmAdmTranspMode_Type(Integer32):
    """Custom type cxMcVoxEmAdmTranspMode based on Integer32"""
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
        *(("emulate", 1),
          ("local", 3),
          ("transparent", 2))
    )


_CxMcVoxEmAdmTranspMode_Type.__name__ = "Integer32"
_CxMcVoxEmAdmTranspMode_Object = MibTableColumn
cxMcVoxEmAdmTranspMode = _CxMcVoxEmAdmTranspMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 22),
    _CxMcVoxEmAdmTranspMode_Type()
)
cxMcVoxEmAdmTranspMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmTranspMode.setStatus("mandatory")


class _CxMcVoxEmAdmFaxEnable_Type(Integer32):
    """Custom type cxMcVoxEmAdmFaxEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxEmAdmFaxEnable_Type.__name__ = "Integer32"
_CxMcVoxEmAdmFaxEnable_Object = MibTableColumn
cxMcVoxEmAdmFaxEnable = _CxMcVoxEmAdmFaxEnable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 23),
    _CxMcVoxEmAdmFaxEnable_Type()
)
cxMcVoxEmAdmFaxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmFaxEnable.setStatus("mandatory")


class _CxMcVoxEmAdmBroadcast_Type(Integer32):
    """Custom type cxMcVoxEmAdmBroadcast based on Integer32"""
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
        *(("master", 2),
          ("none", 1),
          ("slave", 3))
    )


_CxMcVoxEmAdmBroadcast_Type.__name__ = "Integer32"
_CxMcVoxEmAdmBroadcast_Object = MibTableColumn
cxMcVoxEmAdmBroadcast = _CxMcVoxEmAdmBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 24),
    _CxMcVoxEmAdmBroadcast_Type()
)
cxMcVoxEmAdmBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmBroadcast.setStatus("mandatory")


class _CxMcVoxEmAdmImpedance_Type(Integer32):
    """Custom type cxMcVoxEmAdmImpedance based on Integer32"""
    defaultValue = 1

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
        *(("att", 3),
          ("aus", 4),
          ("i600-ohms", 1),
          ("i900-ohms", 2))
    )


_CxMcVoxEmAdmImpedance_Type.__name__ = "Integer32"
_CxMcVoxEmAdmImpedance_Object = MibTableColumn
cxMcVoxEmAdmImpedance = _CxMcVoxEmAdmImpedance_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 25),
    _CxMcVoxEmAdmImpedance_Type()
)
cxMcVoxEmAdmImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmImpedance.setStatus("mandatory")


class _CxMcVoxEmAdmVoiceConnection_Type(Integer32):
    """Custom type cxMcVoxEmAdmVoiceConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("four-wires", 2),
          ("two-wires", 1))
    )


_CxMcVoxEmAdmVoiceConnection_Type.__name__ = "Integer32"
_CxMcVoxEmAdmVoiceConnection_Object = MibTableColumn
cxMcVoxEmAdmVoiceConnection = _CxMcVoxEmAdmVoiceConnection_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 1, 1, 26),
    _CxMcVoxEmAdmVoiceConnection_Type()
)
cxMcVoxEmAdmVoiceConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmAdmVoiceConnection.setStatus("mandatory")
_CxMcVoxFxsAdmTable_Object = MibTable
cxMcVoxFxsAdmTable = _CxMcVoxFxsAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmTable.setStatus("mandatory")
_CxMcVoxFxsAdmEntry_Object = MibTableRow
cxMcVoxFxsAdmEntry = _CxMcVoxFxsAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1)
)
cxMcVoxFxsAdmEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxFxsAdmCardUsed"),
    (0, "CXMCVOX-MIB", "cxMcVoxFxsAdmPortUsed"),
)
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmEntry.setStatus("mandatory")


class _CxMcVoxFxsAdmCardUsed_Type(Integer32):
    """Custom type cxMcVoxFxsAdmCardUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CxMcVoxFxsAdmCardUsed_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmCardUsed_Object = MibTableColumn
cxMcVoxFxsAdmCardUsed = _CxMcVoxFxsAdmCardUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 1),
    _CxMcVoxFxsAdmCardUsed_Type()
)
cxMcVoxFxsAdmCardUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmCardUsed.setStatus("mandatory")


class _CxMcVoxFxsAdmPortUsed_Type(Integer32):
    """Custom type cxMcVoxFxsAdmPortUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CxMcVoxFxsAdmPortUsed_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmPortUsed_Object = MibTableColumn
cxMcVoxFxsAdmPortUsed = _CxMcVoxFxsAdmPortUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 2),
    _CxMcVoxFxsAdmPortUsed_Type()
)
cxMcVoxFxsAdmPortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmPortUsed.setStatus("mandatory")


class _CxMcVoxFxsAdmPortStatus_Type(Integer32):
    """Custom type cxMcVoxFxsAdmPortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxFxsAdmPortStatus_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmPortStatus_Object = MibTableColumn
cxMcVoxFxsAdmPortStatus = _CxMcVoxFxsAdmPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 3),
    _CxMcVoxFxsAdmPortStatus_Type()
)
cxMcVoxFxsAdmPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmPortStatus.setStatus("mandatory")


class _CxMcVoxFxsAdmVocoder_Type(Integer32):
    """Custom type cxMcVoxFxsAdmVocoder based on Integer32"""
    defaultValue = 2

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
        *(("bps5800", 1),
          ("bps8000", 2),
          ("kbps16", 6),
          ("kbps24", 5),
          ("kbps32", 4),
          ("kbps40", 3),
          ("opt7", 7),
          ("opt8", 8))
    )


_CxMcVoxFxsAdmVocoder_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmVocoder_Object = MibTableColumn
cxMcVoxFxsAdmVocoder = _CxMcVoxFxsAdmVocoder_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 4),
    _CxMcVoxFxsAdmVocoder_Type()
)
cxMcVoxFxsAdmVocoder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmVocoder.setStatus("mandatory")


class _CxMcVoxFxsAdmFaxBw_Type(Integer32):
    """Custom type cxMcVoxFxsAdmFaxBw based on Integer32"""
    defaultValue = 3

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
        *(("bps2400", 1),
          ("bps4800", 2),
          ("bps7200", 3),
          ("bps9600", 4))
    )


_CxMcVoxFxsAdmFaxBw_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmFaxBw_Object = MibTableColumn
cxMcVoxFxsAdmFaxBw = _CxMcVoxFxsAdmFaxBw_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 5),
    _CxMcVoxFxsAdmFaxBw_Type()
)
cxMcVoxFxsAdmFaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmFaxBw.setStatus("mandatory")


class _CxMcVoxFxsAdmAutoCnx_Type(Integer32):
    """Custom type cxMcVoxFxsAdmAutoCnx based on Integer32"""
    defaultValue = 1

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


_CxMcVoxFxsAdmAutoCnx_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmAutoCnx_Object = MibTableColumn
cxMcVoxFxsAdmAutoCnx = _CxMcVoxFxsAdmAutoCnx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 6),
    _CxMcVoxFxsAdmAutoCnx_Type()
)
cxMcVoxFxsAdmAutoCnx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmAutoCnx.setStatus("obsolete")


class _CxMcVoxFxsAdmPathId_Type(DisplayString):
    """Custom type cxMcVoxFxsAdmPathId based on DisplayString"""
    defaultValue = OctetString("000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxFxsAdmPathId_Type.__name__ = "DisplayString"
_CxMcVoxFxsAdmPathId_Object = MibTableColumn
cxMcVoxFxsAdmPathId = _CxMcVoxFxsAdmPathId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 7),
    _CxMcVoxFxsAdmPathId_Type()
)
cxMcVoxFxsAdmPathId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmPathId.setStatus("deprecated")


class _CxMcVoxFxsAdmTxGain_Type(Integer32):
    """Custom type cxMcVoxFxsAdmTxGain based on Integer32"""
    defaultValue = 960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxFxsAdmTxGain_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmTxGain_Object = MibTableColumn
cxMcVoxFxsAdmTxGain = _CxMcVoxFxsAdmTxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 8),
    _CxMcVoxFxsAdmTxGain_Type()
)
cxMcVoxFxsAdmTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmTxGain.setStatus("mandatory")


class _CxMcVoxFxsAdmRxGain_Type(Integer32):
    """Custom type cxMcVoxFxsAdmRxGain based on Integer32"""
    defaultValue = 960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxFxsAdmRxGain_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmRxGain_Object = MibTableColumn
cxMcVoxFxsAdmRxGain = _CxMcVoxFxsAdmRxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 9),
    _CxMcVoxFxsAdmRxGain_Type()
)
cxMcVoxFxsAdmRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmRxGain.setStatus("mandatory")


class _CxMcVoxFxsAdmEchoCancel_Type(Integer32):
    """Custom type cxMcVoxFxsAdmEchoCancel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxFxsAdmEchoCancel_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmEchoCancel_Object = MibTableColumn
cxMcVoxFxsAdmEchoCancel = _CxMcVoxFxsAdmEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 10),
    _CxMcVoxFxsAdmEchoCancel_Type()
)
cxMcVoxFxsAdmEchoCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmEchoCancel.setStatus("mandatory")


class _CxMcVoxFxsAdmSignaling_Type(Integer32):
    """Custom type cxMcVoxFxsAdmSignaling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("did", 3),
          ("ground-start", 1),
          ("loop-start", 2))
    )


_CxMcVoxFxsAdmSignaling_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmSignaling_Object = MibTableColumn
cxMcVoxFxsAdmSignaling = _CxMcVoxFxsAdmSignaling_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 11),
    _CxMcVoxFxsAdmSignaling_Type()
)
cxMcVoxFxsAdmSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmSignaling.setStatus("mandatory")


class _CxMcVoxFxsAdmTimeOn_Type(Integer32):
    """Custom type cxMcVoxFxsAdmTimeOn based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CxMcVoxFxsAdmTimeOn_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmTimeOn_Object = MibTableColumn
cxMcVoxFxsAdmTimeOn = _CxMcVoxFxsAdmTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 12),
    _CxMcVoxFxsAdmTimeOn_Type()
)
cxMcVoxFxsAdmTimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmTimeOn.setStatus("obsolete")


class _CxMcVoxFxsAdmTimeOff_Type(Integer32):
    """Custom type cxMcVoxFxsAdmTimeOff based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CxMcVoxFxsAdmTimeOff_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmTimeOff_Object = MibTableColumn
cxMcVoxFxsAdmTimeOff = _CxMcVoxFxsAdmTimeOff_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 13),
    _CxMcVoxFxsAdmTimeOff_Type()
)
cxMcVoxFxsAdmTimeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmTimeOff.setStatus("obsolete")


class _CxMcVoxFxsAdmCnctType_Type(Integer32):
    """Custom type cxMcVoxFxsAdmCnctType based on Integer32"""
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
        *(("auto-connect", 2),
          ("fixed", 3),
          ("switched", 1))
    )


_CxMcVoxFxsAdmCnctType_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmCnctType_Object = MibTableColumn
cxMcVoxFxsAdmCnctType = _CxMcVoxFxsAdmCnctType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 14),
    _CxMcVoxFxsAdmCnctType_Type()
)
cxMcVoxFxsAdmCnctType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmCnctType.setStatus("mandatory")


class _CxMcVoxFxsAdmRingType_Type(Integer32):
    """Custom type cxMcVoxFxsAdmRingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("international", 2),
          ("north-american", 1))
    )


_CxMcVoxFxsAdmRingType_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmRingType_Object = MibTableColumn
cxMcVoxFxsAdmRingType = _CxMcVoxFxsAdmRingType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 15),
    _CxMcVoxFxsAdmRingType_Type()
)
cxMcVoxFxsAdmRingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmRingType.setStatus("mandatory")


class _CxMcVoxFxsAdmImpedance_Type(Integer32):
    """Custom type cxMcVoxFxsAdmImpedance based on Integer32"""
    defaultValue = 1

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
        *(("att", 3),
          ("aus", 4),
          ("i600-ohms", 1),
          ("i900-ohms", 2))
    )


_CxMcVoxFxsAdmImpedance_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmImpedance_Object = MibTableColumn
cxMcVoxFxsAdmImpedance = _CxMcVoxFxsAdmImpedance_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 16),
    _CxMcVoxFxsAdmImpedance_Type()
)
cxMcVoxFxsAdmImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmImpedance.setStatus("mandatory")


class _CxMcVoxFxsAdmDialType_Type(Integer32):
    """Custom type cxMcVoxFxsAdmDialType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("pulse", 2))
    )


_CxMcVoxFxsAdmDialType_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmDialType_Object = MibTableColumn
cxMcVoxFxsAdmDialType = _CxMcVoxFxsAdmDialType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 17),
    _CxMcVoxFxsAdmDialType_Type()
)
cxMcVoxFxsAdmDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmDialType.setStatus("mandatory")


class _CxMcVoxFxsAdmDidSignalType_Type(Integer32):
    """Custom type cxMcVoxFxsAdmDidSignalType based on Integer32"""
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
        *(("delay", 2),
          ("normal", 1),
          ("wink", 3))
    )


_CxMcVoxFxsAdmDidSignalType_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmDidSignalType_Object = MibTableColumn
cxMcVoxFxsAdmDidSignalType = _CxMcVoxFxsAdmDidSignalType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 18),
    _CxMcVoxFxsAdmDidSignalType_Type()
)
cxMcVoxFxsAdmDidSignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmDidSignalType.setStatus("mandatory")


class _CxMcVoxFxsAdmRmtExt_Type(DisplayString):
    """Custom type cxMcVoxFxsAdmRmtExt based on DisplayString"""
    defaultValue = OctetString("000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CxMcVoxFxsAdmRmtExt_Type.__name__ = "DisplayString"
_CxMcVoxFxsAdmRmtExt_Object = MibTableColumn
cxMcVoxFxsAdmRmtExt = _CxMcVoxFxsAdmRmtExt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 19),
    _CxMcVoxFxsAdmRmtExt_Type()
)
cxMcVoxFxsAdmRmtExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmRmtExt.setStatus("mandatory")


class _CxMcVoxFxsAdmRmtId_Type(DisplayString):
    """Custom type cxMcVoxFxsAdmRmtId based on DisplayString"""
    defaultValue = OctetString("          ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CxMcVoxFxsAdmRmtId_Type.__name__ = "DisplayString"
_CxMcVoxFxsAdmRmtId_Object = MibTableColumn
cxMcVoxFxsAdmRmtId = _CxMcVoxFxsAdmRmtId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 20),
    _CxMcVoxFxsAdmRmtId_Type()
)
cxMcVoxFxsAdmRmtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmRmtId.setStatus("optional")


class _CxMcVoxFxsAdmTranspMode_Type(Integer32):
    """Custom type cxMcVoxFxsAdmTranspMode based on Integer32"""
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
        *(("emulate", 1),
          ("local", 3),
          ("transparent", 2))
    )


_CxMcVoxFxsAdmTranspMode_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmTranspMode_Object = MibTableColumn
cxMcVoxFxsAdmTranspMode = _CxMcVoxFxsAdmTranspMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 21),
    _CxMcVoxFxsAdmTranspMode_Type()
)
cxMcVoxFxsAdmTranspMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmTranspMode.setStatus("mandatory")


class _CxMcVoxFxsAdmFaxEnable_Type(Integer32):
    """Custom type cxMcVoxFxsAdmFaxEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxFxsAdmFaxEnable_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmFaxEnable_Object = MibTableColumn
cxMcVoxFxsAdmFaxEnable = _CxMcVoxFxsAdmFaxEnable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 22),
    _CxMcVoxFxsAdmFaxEnable_Type()
)
cxMcVoxFxsAdmFaxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmFaxEnable.setStatus("mandatory")


class _CxMcVoxFxsAdmBroadcast_Type(Integer32):
    """Custom type cxMcVoxFxsAdmBroadcast based on Integer32"""
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
        *(("master", 2),
          ("none", 1),
          ("slave", 3))
    )


_CxMcVoxFxsAdmBroadcast_Type.__name__ = "Integer32"
_CxMcVoxFxsAdmBroadcast_Object = MibTableColumn
cxMcVoxFxsAdmBroadcast = _CxMcVoxFxsAdmBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 2, 1, 23),
    _CxMcVoxFxsAdmBroadcast_Type()
)
cxMcVoxFxsAdmBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsAdmBroadcast.setStatus("mandatory")
_CxMcVoxFxoAdmTable_Object = MibTable
cxMcVoxFxoAdmTable = _CxMcVoxFxoAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmTable.setStatus("mandatory")
_CxMcVoxFxoAdmEntry_Object = MibTableRow
cxMcVoxFxoAdmEntry = _CxMcVoxFxoAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1)
)
cxMcVoxFxoAdmEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxFxoAdmCardUsed"),
    (0, "CXMCVOX-MIB", "cxMcVoxFxoAdmPortUsed"),
)
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmEntry.setStatus("mandatory")


class _CxMcVoxFxoAdmCardUsed_Type(Integer32):
    """Custom type cxMcVoxFxoAdmCardUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CxMcVoxFxoAdmCardUsed_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmCardUsed_Object = MibTableColumn
cxMcVoxFxoAdmCardUsed = _CxMcVoxFxoAdmCardUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 1),
    _CxMcVoxFxoAdmCardUsed_Type()
)
cxMcVoxFxoAdmCardUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmCardUsed.setStatus("mandatory")


class _CxMcVoxFxoAdmPortUsed_Type(Integer32):
    """Custom type cxMcVoxFxoAdmPortUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CxMcVoxFxoAdmPortUsed_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmPortUsed_Object = MibTableColumn
cxMcVoxFxoAdmPortUsed = _CxMcVoxFxoAdmPortUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 2),
    _CxMcVoxFxoAdmPortUsed_Type()
)
cxMcVoxFxoAdmPortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmPortUsed.setStatus("mandatory")


class _CxMcVoxFxoAdmPortStatus_Type(Integer32):
    """Custom type cxMcVoxFxoAdmPortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxFxoAdmPortStatus_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmPortStatus_Object = MibTableColumn
cxMcVoxFxoAdmPortStatus = _CxMcVoxFxoAdmPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 3),
    _CxMcVoxFxoAdmPortStatus_Type()
)
cxMcVoxFxoAdmPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmPortStatus.setStatus("mandatory")


class _CxMcVoxFxoAdmVocoder_Type(Integer32):
    """Custom type cxMcVoxFxoAdmVocoder based on Integer32"""
    defaultValue = 2

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
        *(("bps5800", 1),
          ("bps8000", 2),
          ("kbps16", 6),
          ("kbps24", 5),
          ("kbps32", 4),
          ("kbps40", 3),
          ("opt7", 7),
          ("opt8", 8))
    )


_CxMcVoxFxoAdmVocoder_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmVocoder_Object = MibTableColumn
cxMcVoxFxoAdmVocoder = _CxMcVoxFxoAdmVocoder_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 4),
    _CxMcVoxFxoAdmVocoder_Type()
)
cxMcVoxFxoAdmVocoder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmVocoder.setStatus("mandatory")


class _CxMcVoxFxoAdmFaxBw_Type(Integer32):
    """Custom type cxMcVoxFxoAdmFaxBw based on Integer32"""
    defaultValue = 3

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
        *(("bps2400", 1),
          ("bps4800", 2),
          ("bps7200", 3),
          ("bps9600", 4))
    )


_CxMcVoxFxoAdmFaxBw_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmFaxBw_Object = MibTableColumn
cxMcVoxFxoAdmFaxBw = _CxMcVoxFxoAdmFaxBw_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 5),
    _CxMcVoxFxoAdmFaxBw_Type()
)
cxMcVoxFxoAdmFaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmFaxBw.setStatus("mandatory")


class _CxMcVoxFxoAdmAutoCnx_Type(Integer32):
    """Custom type cxMcVoxFxoAdmAutoCnx based on Integer32"""
    defaultValue = 1

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


_CxMcVoxFxoAdmAutoCnx_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmAutoCnx_Object = MibTableColumn
cxMcVoxFxoAdmAutoCnx = _CxMcVoxFxoAdmAutoCnx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 6),
    _CxMcVoxFxoAdmAutoCnx_Type()
)
cxMcVoxFxoAdmAutoCnx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmAutoCnx.setStatus("obsolete")


class _CxMcVoxFxoAdmPathId_Type(DisplayString):
    """Custom type cxMcVoxFxoAdmPathId based on DisplayString"""
    defaultValue = OctetString("000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxFxoAdmPathId_Type.__name__ = "DisplayString"
_CxMcVoxFxoAdmPathId_Object = MibTableColumn
cxMcVoxFxoAdmPathId = _CxMcVoxFxoAdmPathId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 7),
    _CxMcVoxFxoAdmPathId_Type()
)
cxMcVoxFxoAdmPathId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmPathId.setStatus("deprecated")


class _CxMcVoxFxoAdmTxGain_Type(Integer32):
    """Custom type cxMcVoxFxoAdmTxGain based on Integer32"""
    defaultValue = 960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxFxoAdmTxGain_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmTxGain_Object = MibTableColumn
cxMcVoxFxoAdmTxGain = _CxMcVoxFxoAdmTxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 8),
    _CxMcVoxFxoAdmTxGain_Type()
)
cxMcVoxFxoAdmTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmTxGain.setStatus("mandatory")


class _CxMcVoxFxoAdmRxGain_Type(Integer32):
    """Custom type cxMcVoxFxoAdmRxGain based on Integer32"""
    defaultValue = 960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxFxoAdmRxGain_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmRxGain_Object = MibTableColumn
cxMcVoxFxoAdmRxGain = _CxMcVoxFxoAdmRxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 9),
    _CxMcVoxFxoAdmRxGain_Type()
)
cxMcVoxFxoAdmRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmRxGain.setStatus("mandatory")


class _CxMcVoxFxoAdmEchoCancel_Type(Integer32):
    """Custom type cxMcVoxFxoAdmEchoCancel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxFxoAdmEchoCancel_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmEchoCancel_Object = MibTableColumn
cxMcVoxFxoAdmEchoCancel = _CxMcVoxFxoAdmEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 10),
    _CxMcVoxFxoAdmEchoCancel_Type()
)
cxMcVoxFxoAdmEchoCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmEchoCancel.setStatus("mandatory")


class _CxMcVoxFxoAdmSignaling_Type(Integer32):
    """Custom type cxMcVoxFxoAdmSignaling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("did", 3),
          ("ground-start", 1),
          ("loop-start", 2))
    )


_CxMcVoxFxoAdmSignaling_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmSignaling_Object = MibTableColumn
cxMcVoxFxoAdmSignaling = _CxMcVoxFxoAdmSignaling_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 11),
    _CxMcVoxFxoAdmSignaling_Type()
)
cxMcVoxFxoAdmSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmSignaling.setStatus("mandatory")


class _CxMcVoxFxoAdmCnctType_Type(Integer32):
    """Custom type cxMcVoxFxoAdmCnctType based on Integer32"""
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
        *(("auto-connect", 2),
          ("fixed", 3),
          ("switched", 1))
    )


_CxMcVoxFxoAdmCnctType_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmCnctType_Object = MibTableColumn
cxMcVoxFxoAdmCnctType = _CxMcVoxFxoAdmCnctType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 12),
    _CxMcVoxFxoAdmCnctType_Type()
)
cxMcVoxFxoAdmCnctType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmCnctType.setStatus("mandatory")


class _CxMcVoxFxoAdmRingType_Type(Integer32):
    """Custom type cxMcVoxFxoAdmRingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("international", 2),
          ("north-american", 1))
    )


_CxMcVoxFxoAdmRingType_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmRingType_Object = MibTableColumn
cxMcVoxFxoAdmRingType = _CxMcVoxFxoAdmRingType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 13),
    _CxMcVoxFxoAdmRingType_Type()
)
cxMcVoxFxoAdmRingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmRingType.setStatus("mandatory")


class _CxMcVoxFxoAdmImpedance_Type(Integer32):
    """Custom type cxMcVoxFxoAdmImpedance based on Integer32"""
    defaultValue = 1

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
        *(("att", 3),
          ("aus", 4),
          ("i600-ohms", 1),
          ("i900-ohms", 2))
    )


_CxMcVoxFxoAdmImpedance_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmImpedance_Object = MibTableColumn
cxMcVoxFxoAdmImpedance = _CxMcVoxFxoAdmImpedance_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 14),
    _CxMcVoxFxoAdmImpedance_Type()
)
cxMcVoxFxoAdmImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmImpedance.setStatus("mandatory")


class _CxMcVoxFxoAdmDialType_Type(Integer32):
    """Custom type cxMcVoxFxoAdmDialType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("pulse", 2))
    )


_CxMcVoxFxoAdmDialType_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmDialType_Object = MibTableColumn
cxMcVoxFxoAdmDialType = _CxMcVoxFxoAdmDialType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 15),
    _CxMcVoxFxoAdmDialType_Type()
)
cxMcVoxFxoAdmDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmDialType.setStatus("mandatory")


class _CxMcVoxFxoAdmDidSignalType_Type(Integer32):
    """Custom type cxMcVoxFxoAdmDidSignalType based on Integer32"""
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
        *(("delay", 2),
          ("normal", 1),
          ("wink", 3))
    )


_CxMcVoxFxoAdmDidSignalType_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmDidSignalType_Object = MibTableColumn
cxMcVoxFxoAdmDidSignalType = _CxMcVoxFxoAdmDidSignalType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 16),
    _CxMcVoxFxoAdmDidSignalType_Type()
)
cxMcVoxFxoAdmDidSignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmDidSignalType.setStatus("mandatory")


class _CxMcVoxFxoAdmRmtExt_Type(DisplayString):
    """Custom type cxMcVoxFxoAdmRmtExt based on DisplayString"""
    defaultValue = OctetString("000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CxMcVoxFxoAdmRmtExt_Type.__name__ = "DisplayString"
_CxMcVoxFxoAdmRmtExt_Object = MibTableColumn
cxMcVoxFxoAdmRmtExt = _CxMcVoxFxoAdmRmtExt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 17),
    _CxMcVoxFxoAdmRmtExt_Type()
)
cxMcVoxFxoAdmRmtExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmRmtExt.setStatus("mandatory")


class _CxMcVoxFxoAdmRmtId_Type(DisplayString):
    """Custom type cxMcVoxFxoAdmRmtId based on DisplayString"""
    defaultValue = OctetString("          ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CxMcVoxFxoAdmRmtId_Type.__name__ = "DisplayString"
_CxMcVoxFxoAdmRmtId_Object = MibTableColumn
cxMcVoxFxoAdmRmtId = _CxMcVoxFxoAdmRmtId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 18),
    _CxMcVoxFxoAdmRmtId_Type()
)
cxMcVoxFxoAdmRmtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmRmtId.setStatus("optional")


class _CxMcVoxFxoAdmTranspMode_Type(Integer32):
    """Custom type cxMcVoxFxoAdmTranspMode based on Integer32"""
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
        *(("emulate", 1),
          ("local", 3),
          ("transparent", 2))
    )


_CxMcVoxFxoAdmTranspMode_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmTranspMode_Object = MibTableColumn
cxMcVoxFxoAdmTranspMode = _CxMcVoxFxoAdmTranspMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 19),
    _CxMcVoxFxoAdmTranspMode_Type()
)
cxMcVoxFxoAdmTranspMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmTranspMode.setStatus("mandatory")


class _CxMcVoxFxoAdmFaxEnable_Type(Integer32):
    """Custom type cxMcVoxFxoAdmFaxEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxFxoAdmFaxEnable_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmFaxEnable_Object = MibTableColumn
cxMcVoxFxoAdmFaxEnable = _CxMcVoxFxoAdmFaxEnable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 20),
    _CxMcVoxFxoAdmFaxEnable_Type()
)
cxMcVoxFxoAdmFaxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmFaxEnable.setStatus("mandatory")


class _CxMcVoxFxoAdmBroadcast_Type(Integer32):
    """Custom type cxMcVoxFxoAdmBroadcast based on Integer32"""
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
        *(("master", 2),
          ("none", 1),
          ("slave", 3))
    )


_CxMcVoxFxoAdmBroadcast_Type.__name__ = "Integer32"
_CxMcVoxFxoAdmBroadcast_Object = MibTableColumn
cxMcVoxFxoAdmBroadcast = _CxMcVoxFxoAdmBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 8, 3, 1, 21),
    _CxMcVoxFxoAdmBroadcast_Type()
)
cxMcVoxFxoAdmBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoAdmBroadcast.setStatus("mandatory")
_CxMcVoxDriverOpe_ObjectIdentity = ObjectIdentity
cxMcVoxDriverOpe = _CxMcVoxDriverOpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9)
)
_CxMcVoxEmOpeTable_Object = MibTable
cxMcVoxEmOpeTable = _CxMcVoxEmOpeTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    cxMcVoxEmOpeTable.setStatus("mandatory")
_CxMcVoxEmOpeEntry_Object = MibTableRow
cxMcVoxEmOpeEntry = _CxMcVoxEmOpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1)
)
cxMcVoxEmOpeEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxEmOpeCardUsed"),
    (0, "CXMCVOX-MIB", "cxMcVoxEmOpePortUsed"),
)
if mibBuilder.loadTexts:
    cxMcVoxEmOpeEntry.setStatus("mandatory")


class _CxMcVoxEmOpeCardUsed_Type(Integer32):
    """Custom type cxMcVoxEmOpeCardUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CxMcVoxEmOpeCardUsed_Type.__name__ = "Integer32"
_CxMcVoxEmOpeCardUsed_Object = MibTableColumn
cxMcVoxEmOpeCardUsed = _CxMcVoxEmOpeCardUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 1),
    _CxMcVoxEmOpeCardUsed_Type()
)
cxMcVoxEmOpeCardUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeCardUsed.setStatus("mandatory")


class _CxMcVoxEmOpePortUsed_Type(Integer32):
    """Custom type cxMcVoxEmOpePortUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CxMcVoxEmOpePortUsed_Type.__name__ = "Integer32"
_CxMcVoxEmOpePortUsed_Object = MibTableColumn
cxMcVoxEmOpePortUsed = _CxMcVoxEmOpePortUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 2),
    _CxMcVoxEmOpePortUsed_Type()
)
cxMcVoxEmOpePortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpePortUsed.setStatus("mandatory")


class _CxMcVoxEmOpePortStatus_Type(Integer32):
    """Custom type cxMcVoxEmOpePortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              31,
              32,
              33,
              34,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("appl-err-1", 41),
          ("appl-err-2", 42),
          ("appl-err-3", 43),
          ("appl-err-4", 44),
          ("boot-err-1", 31),
          ("boot-err-2", 32),
          ("boot-err-3", 33),
          ("boot-err-4", 34),
          ("disable", 1),
          ("enable", 2),
          ("no-voice-io", 3))
    )


_CxMcVoxEmOpePortStatus_Type.__name__ = "Integer32"
_CxMcVoxEmOpePortStatus_Object = MibTableColumn
cxMcVoxEmOpePortStatus = _CxMcVoxEmOpePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 3),
    _CxMcVoxEmOpePortStatus_Type()
)
cxMcVoxEmOpePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpePortStatus.setStatus("mandatory")


class _CxMcVoxEmOpeVocoder_Type(Integer32):
    """Custom type cxMcVoxEmOpeVocoder based on Integer32"""
    defaultValue = 2

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
        *(("bps5800", 1),
          ("bps8000", 2),
          ("kbps16", 6),
          ("kbps24", 5),
          ("kbps32", 4),
          ("kbps40", 3),
          ("opt7", 7),
          ("opt8", 8))
    )


_CxMcVoxEmOpeVocoder_Type.__name__ = "Integer32"
_CxMcVoxEmOpeVocoder_Object = MibTableColumn
cxMcVoxEmOpeVocoder = _CxMcVoxEmOpeVocoder_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 4),
    _CxMcVoxEmOpeVocoder_Type()
)
cxMcVoxEmOpeVocoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeVocoder.setStatus("mandatory")


class _CxMcVoxEmOpeFaxBw_Type(Integer32):
    """Custom type cxMcVoxEmOpeFaxBw based on Integer32"""
    defaultValue = 3

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
        *(("bps2400", 1),
          ("bps4800", 2),
          ("bps7200", 3),
          ("bps9600", 4))
    )


_CxMcVoxEmOpeFaxBw_Type.__name__ = "Integer32"
_CxMcVoxEmOpeFaxBw_Object = MibTableColumn
cxMcVoxEmOpeFaxBw = _CxMcVoxEmOpeFaxBw_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 5),
    _CxMcVoxEmOpeFaxBw_Type()
)
cxMcVoxEmOpeFaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeFaxBw.setStatus("mandatory")


class _CxMcVoxEmOpeAutoCnx_Type(Integer32):
    """Custom type cxMcVoxEmOpeAutoCnx based on Integer32"""
    defaultValue = 1

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


_CxMcVoxEmOpeAutoCnx_Type.__name__ = "Integer32"
_CxMcVoxEmOpeAutoCnx_Object = MibTableColumn
cxMcVoxEmOpeAutoCnx = _CxMcVoxEmOpeAutoCnx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 6),
    _CxMcVoxEmOpeAutoCnx_Type()
)
cxMcVoxEmOpeAutoCnx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeAutoCnx.setStatus("obsolete")


class _CxMcVoxEmOpePathId_Type(DisplayString):
    """Custom type cxMcVoxEmOpePathId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxEmOpePathId_Type.__name__ = "DisplayString"
_CxMcVoxEmOpePathId_Object = MibTableColumn
cxMcVoxEmOpePathId = _CxMcVoxEmOpePathId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 7),
    _CxMcVoxEmOpePathId_Type()
)
cxMcVoxEmOpePathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpePathId.setStatus("deprecated")


class _CxMcVoxEmOpeTxGain_Type(Integer32):
    """Custom type cxMcVoxEmOpeTxGain based on Integer32"""
    defaultValue = 960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxEmOpeTxGain_Type.__name__ = "Integer32"
_CxMcVoxEmOpeTxGain_Object = MibTableColumn
cxMcVoxEmOpeTxGain = _CxMcVoxEmOpeTxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 8),
    _CxMcVoxEmOpeTxGain_Type()
)
cxMcVoxEmOpeTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeTxGain.setStatus("mandatory")


class _CxMcVoxEmOpeRxGain_Type(Integer32):
    """Custom type cxMcVoxEmOpeRxGain based on Integer32"""
    defaultValue = 960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxEmOpeRxGain_Type.__name__ = "Integer32"
_CxMcVoxEmOpeRxGain_Object = MibTableColumn
cxMcVoxEmOpeRxGain = _CxMcVoxEmOpeRxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 9),
    _CxMcVoxEmOpeRxGain_Type()
)
cxMcVoxEmOpeRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeRxGain.setStatus("mandatory")


class _CxMcVoxEmOpeEchoCancel_Type(Integer32):
    """Custom type cxMcVoxEmOpeEchoCancel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxEmOpeEchoCancel_Type.__name__ = "Integer32"
_CxMcVoxEmOpeEchoCancel_Object = MibTableColumn
cxMcVoxEmOpeEchoCancel = _CxMcVoxEmOpeEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 10),
    _CxMcVoxEmOpeEchoCancel_Type()
)
cxMcVoxEmOpeEchoCancel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeEchoCancel.setStatus("mandatory")


class _CxMcVoxEmOpeType_Type(Integer32):
    """Custom type cxMcVoxEmOpeType based on Integer32"""
    defaultValue = 2

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
        *(("type-1", 1),
          ("type-2", 2),
          ("type-3", 3),
          ("type-4", 4),
          ("type-5", 5))
    )


_CxMcVoxEmOpeType_Type.__name__ = "Integer32"
_CxMcVoxEmOpeType_Object = MibTableColumn
cxMcVoxEmOpeType = _CxMcVoxEmOpeType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 11),
    _CxMcVoxEmOpeType_Type()
)
cxMcVoxEmOpeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeType.setStatus("mandatory")


class _CxMcVoxEmOpeMode_Type(Integer32):
    """Custom type cxMcVoxEmOpeMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reverse", 2))
    )


_CxMcVoxEmOpeMode_Type.__name__ = "Integer32"
_CxMcVoxEmOpeMode_Object = MibTableColumn
cxMcVoxEmOpeMode = _CxMcVoxEmOpeMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 12),
    _CxMcVoxEmOpeMode_Type()
)
cxMcVoxEmOpeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeMode.setStatus("mandatory")


class _CxMcVoxEmOpeDialType_Type(Integer32):
    """Custom type cxMcVoxEmOpeDialType based on Integer32"""
    defaultValue = 1

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
        *(("dtmf", 1),
          ("mfR1", 3),
          ("mfR2", 4),
          ("pulse", 2))
    )


_CxMcVoxEmOpeDialType_Type.__name__ = "Integer32"
_CxMcVoxEmOpeDialType_Object = MibTableColumn
cxMcVoxEmOpeDialType = _CxMcVoxEmOpeDialType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 13),
    _CxMcVoxEmOpeDialType_Type()
)
cxMcVoxEmOpeDialType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeDialType.setStatus("mandatory")


class _CxMcVoxEmOpeSignalType_Type(Integer32):
    """Custom type cxMcVoxEmOpeSignalType based on Integer32"""
    defaultValue = 1

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
        *(("ac15", 4),
          ("delay", 2),
          ("isdn", 8),
          ("mfcr2", 7),
          ("normal", 1),
          ("openchn", 5),
          ("r2", 6),
          ("wink", 3))
    )


_CxMcVoxEmOpeSignalType_Type.__name__ = "Integer32"
_CxMcVoxEmOpeSignalType_Object = MibTableColumn
cxMcVoxEmOpeSignalType = _CxMcVoxEmOpeSignalType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 14),
    _CxMcVoxEmOpeSignalType_Type()
)
cxMcVoxEmOpeSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeSignalType.setStatus("mandatory")


class _CxMcVoxEmOpeAc15Type_Type(Integer32):
    """Custom type cxMcVoxEmOpeAc15Type based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delay", 2),
          ("normal", 1))
    )


_CxMcVoxEmOpeAc15Type_Type.__name__ = "Integer32"
_CxMcVoxEmOpeAc15Type_Object = MibTableColumn
cxMcVoxEmOpeAc15Type = _CxMcVoxEmOpeAc15Type_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 15),
    _CxMcVoxEmOpeAc15Type_Type()
)
cxMcVoxEmOpeAc15Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeAc15Type.setStatus("mandatory")


class _CxMcVoxEmOpeAc15TimeOn_Type(Integer32):
    """Custom type cxMcVoxEmOpeAc15TimeOn based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxEmOpeAc15TimeOn_Type.__name__ = "Integer32"
_CxMcVoxEmOpeAc15TimeOn_Object = MibTableColumn
cxMcVoxEmOpeAc15TimeOn = _CxMcVoxEmOpeAc15TimeOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 16),
    _CxMcVoxEmOpeAc15TimeOn_Type()
)
cxMcVoxEmOpeAc15TimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeAc15TimeOn.setStatus("mandatory")


class _CxMcVoxEmOpeAc15TimeOff_Type(Integer32):
    """Custom type cxMcVoxEmOpeAc15TimeOff based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxEmOpeAc15TimeOff_Type.__name__ = "Integer32"
_CxMcVoxEmOpeAc15TimeOff_Object = MibTableColumn
cxMcVoxEmOpeAc15TimeOff = _CxMcVoxEmOpeAc15TimeOff_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 17),
    _CxMcVoxEmOpeAc15TimeOff_Type()
)
cxMcVoxEmOpeAc15TimeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeAc15TimeOff.setStatus("mandatory")


class _CxMcVoxEmOpeCnctType_Type(Integer32):
    """Custom type cxMcVoxEmOpeCnctType based on Integer32"""
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
        *(("auto-connect", 2),
          ("fixed", 3),
          ("switched", 1))
    )


_CxMcVoxEmOpeCnctType_Type.__name__ = "Integer32"
_CxMcVoxEmOpeCnctType_Object = MibTableColumn
cxMcVoxEmOpeCnctType = _CxMcVoxEmOpeCnctType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 18),
    _CxMcVoxEmOpeCnctType_Type()
)
cxMcVoxEmOpeCnctType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeCnctType.setStatus("mandatory")


class _CxMcVoxEmOpeRingType_Type(Integer32):
    """Custom type cxMcVoxEmOpeRingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("international", 2),
          ("north-american", 1))
    )


_CxMcVoxEmOpeRingType_Type.__name__ = "Integer32"
_CxMcVoxEmOpeRingType_Object = MibTableColumn
cxMcVoxEmOpeRingType = _CxMcVoxEmOpeRingType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 19),
    _CxMcVoxEmOpeRingType_Type()
)
cxMcVoxEmOpeRingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeRingType.setStatus("mandatory")


class _CxMcVoxEmOpeRmtExt_Type(DisplayString):
    """Custom type cxMcVoxEmOpeRmtExt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CxMcVoxEmOpeRmtExt_Type.__name__ = "DisplayString"
_CxMcVoxEmOpeRmtExt_Object = MibTableColumn
cxMcVoxEmOpeRmtExt = _CxMcVoxEmOpeRmtExt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 20),
    _CxMcVoxEmOpeRmtExt_Type()
)
cxMcVoxEmOpeRmtExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeRmtExt.setStatus("mandatory")


class _CxMcVoxEmOpeRmtId_Type(DisplayString):
    """Custom type cxMcVoxEmOpeRmtId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CxMcVoxEmOpeRmtId_Type.__name__ = "DisplayString"
_CxMcVoxEmOpeRmtId_Object = MibTableColumn
cxMcVoxEmOpeRmtId = _CxMcVoxEmOpeRmtId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 21),
    _CxMcVoxEmOpeRmtId_Type()
)
cxMcVoxEmOpeRmtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeRmtId.setStatus("optional")


class _CxMcVoxEmOpeTranspMode_Type(Integer32):
    """Custom type cxMcVoxEmOpeTranspMode based on Integer32"""
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
        *(("emulate", 1),
          ("local", 3),
          ("transparent", 2))
    )


_CxMcVoxEmOpeTranspMode_Type.__name__ = "Integer32"
_CxMcVoxEmOpeTranspMode_Object = MibTableColumn
cxMcVoxEmOpeTranspMode = _CxMcVoxEmOpeTranspMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 22),
    _CxMcVoxEmOpeTranspMode_Type()
)
cxMcVoxEmOpeTranspMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeTranspMode.setStatus("mandatory")


class _CxMcVoxEmOpeFaxEnable_Type(Integer32):
    """Custom type cxMcVoxEmOpeFaxEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxEmOpeFaxEnable_Type.__name__ = "Integer32"
_CxMcVoxEmOpeFaxEnable_Object = MibTableColumn
cxMcVoxEmOpeFaxEnable = _CxMcVoxEmOpeFaxEnable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 23),
    _CxMcVoxEmOpeFaxEnable_Type()
)
cxMcVoxEmOpeFaxEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeFaxEnable.setStatus("mandatory")


class _CxMcVoxEmOpeBroadcast_Type(Integer32):
    """Custom type cxMcVoxEmOpeBroadcast based on Integer32"""
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
        *(("master", 2),
          ("none", 1),
          ("slave", 3))
    )


_CxMcVoxEmOpeBroadcast_Type.__name__ = "Integer32"
_CxMcVoxEmOpeBroadcast_Object = MibTableColumn
cxMcVoxEmOpeBroadcast = _CxMcVoxEmOpeBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 24),
    _CxMcVoxEmOpeBroadcast_Type()
)
cxMcVoxEmOpeBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeBroadcast.setStatus("mandatory")


class _CxMcVoxEmOpeImpedance_Type(Integer32):
    """Custom type cxMcVoxEmOpeImpedance based on Integer32"""
    defaultValue = 1

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
        *(("att", 3),
          ("aus", 4),
          ("i600-ohms", 1),
          ("i900-ohms", 2))
    )


_CxMcVoxEmOpeImpedance_Type.__name__ = "Integer32"
_CxMcVoxEmOpeImpedance_Object = MibTableColumn
cxMcVoxEmOpeImpedance = _CxMcVoxEmOpeImpedance_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 25),
    _CxMcVoxEmOpeImpedance_Type()
)
cxMcVoxEmOpeImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeImpedance.setStatus("mandatory")


class _CxMcVoxEmOpeVoiceConnection_Type(Integer32):
    """Custom type cxMcVoxEmOpeVoiceConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("four-wires", 2),
          ("two-wires", 1))
    )


_CxMcVoxEmOpeVoiceConnection_Type.__name__ = "Integer32"
_CxMcVoxEmOpeVoiceConnection_Object = MibTableColumn
cxMcVoxEmOpeVoiceConnection = _CxMcVoxEmOpeVoiceConnection_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 1, 1, 26),
    _CxMcVoxEmOpeVoiceConnection_Type()
)
cxMcVoxEmOpeVoiceConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxEmOpeVoiceConnection.setStatus("mandatory")
_CxMcVoxFxsOpeTable_Object = MibTable
cxMcVoxFxsOpeTable = _CxMcVoxFxsOpeTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeTable.setStatus("mandatory")
_CxMcVoxFxsOpeEntry_Object = MibTableRow
cxMcVoxFxsOpeEntry = _CxMcVoxFxsOpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1)
)
cxMcVoxFxsOpeEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxFxsOpeCardUsed"),
    (0, "CXMCVOX-MIB", "cxMcVoxFxsOpePortUsed"),
)
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeEntry.setStatus("mandatory")


class _CxMcVoxFxsOpeCardUsed_Type(Integer32):
    """Custom type cxMcVoxFxsOpeCardUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CxMcVoxFxsOpeCardUsed_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeCardUsed_Object = MibTableColumn
cxMcVoxFxsOpeCardUsed = _CxMcVoxFxsOpeCardUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 1),
    _CxMcVoxFxsOpeCardUsed_Type()
)
cxMcVoxFxsOpeCardUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeCardUsed.setStatus("mandatory")


class _CxMcVoxFxsOpePortUsed_Type(Integer32):
    """Custom type cxMcVoxFxsOpePortUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CxMcVoxFxsOpePortUsed_Type.__name__ = "Integer32"
_CxMcVoxFxsOpePortUsed_Object = MibTableColumn
cxMcVoxFxsOpePortUsed = _CxMcVoxFxsOpePortUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 2),
    _CxMcVoxFxsOpePortUsed_Type()
)
cxMcVoxFxsOpePortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpePortUsed.setStatus("mandatory")


class _CxMcVoxFxsOpePortStatus_Type(Integer32):
    """Custom type cxMcVoxFxsOpePortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              31,
              32,
              33,
              34,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("appl-err-1", 41),
          ("appl-err-2", 42),
          ("appl-err-3", 43),
          ("appl-err-4", 44),
          ("boot-err-1", 31),
          ("boot-err-2", 32),
          ("boot-err-3", 33),
          ("boot-err-4", 34),
          ("disable", 1),
          ("enable", 2),
          ("no-voice-io", 3))
    )


_CxMcVoxFxsOpePortStatus_Type.__name__ = "Integer32"
_CxMcVoxFxsOpePortStatus_Object = MibTableColumn
cxMcVoxFxsOpePortStatus = _CxMcVoxFxsOpePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 3),
    _CxMcVoxFxsOpePortStatus_Type()
)
cxMcVoxFxsOpePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpePortStatus.setStatus("mandatory")


class _CxMcVoxFxsOpeVocoder_Type(Integer32):
    """Custom type cxMcVoxFxsOpeVocoder based on Integer32"""
    defaultValue = 2

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
        *(("bps5800", 1),
          ("bps8000", 2),
          ("kbps16", 6),
          ("kbps24", 5),
          ("kbps32", 4),
          ("kbps40", 3),
          ("opt7", 7),
          ("opt8", 8))
    )


_CxMcVoxFxsOpeVocoder_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeVocoder_Object = MibTableColumn
cxMcVoxFxsOpeVocoder = _CxMcVoxFxsOpeVocoder_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 4),
    _CxMcVoxFxsOpeVocoder_Type()
)
cxMcVoxFxsOpeVocoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeVocoder.setStatus("mandatory")


class _CxMcVoxFxsOpeFaxBw_Type(Integer32):
    """Custom type cxMcVoxFxsOpeFaxBw based on Integer32"""
    defaultValue = 3

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
        *(("bps2400", 1),
          ("bps4800", 2),
          ("bps7200", 3),
          ("bps9600", 4))
    )


_CxMcVoxFxsOpeFaxBw_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeFaxBw_Object = MibTableColumn
cxMcVoxFxsOpeFaxBw = _CxMcVoxFxsOpeFaxBw_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 5),
    _CxMcVoxFxsOpeFaxBw_Type()
)
cxMcVoxFxsOpeFaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeFaxBw.setStatus("mandatory")


class _CxMcVoxFxsOpeAutoCnx_Type(Integer32):
    """Custom type cxMcVoxFxsOpeAutoCnx based on Integer32"""
    defaultValue = 1

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


_CxMcVoxFxsOpeAutoCnx_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeAutoCnx_Object = MibTableColumn
cxMcVoxFxsOpeAutoCnx = _CxMcVoxFxsOpeAutoCnx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 6),
    _CxMcVoxFxsOpeAutoCnx_Type()
)
cxMcVoxFxsOpeAutoCnx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeAutoCnx.setStatus("obsolete")


class _CxMcVoxFxsOpePathId_Type(DisplayString):
    """Custom type cxMcVoxFxsOpePathId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxFxsOpePathId_Type.__name__ = "DisplayString"
_CxMcVoxFxsOpePathId_Object = MibTableColumn
cxMcVoxFxsOpePathId = _CxMcVoxFxsOpePathId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 7),
    _CxMcVoxFxsOpePathId_Type()
)
cxMcVoxFxsOpePathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpePathId.setStatus("deprecated")


class _CxMcVoxFxsOpeTxGain_Type(Integer32):
    """Custom type cxMcVoxFxsOpeTxGain based on Integer32"""
    defaultValue = 960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxFxsOpeTxGain_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeTxGain_Object = MibTableColumn
cxMcVoxFxsOpeTxGain = _CxMcVoxFxsOpeTxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 8),
    _CxMcVoxFxsOpeTxGain_Type()
)
cxMcVoxFxsOpeTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeTxGain.setStatus("mandatory")


class _CxMcVoxFxsOpeRxGain_Type(Integer32):
    """Custom type cxMcVoxFxsOpeRxGain based on Integer32"""
    defaultValue = 960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxFxsOpeRxGain_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeRxGain_Object = MibTableColumn
cxMcVoxFxsOpeRxGain = _CxMcVoxFxsOpeRxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 9),
    _CxMcVoxFxsOpeRxGain_Type()
)
cxMcVoxFxsOpeRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeRxGain.setStatus("mandatory")


class _CxMcVoxFxsOpeEchoCancel_Type(Integer32):
    """Custom type cxMcVoxFxsOpeEchoCancel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxFxsOpeEchoCancel_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeEchoCancel_Object = MibTableColumn
cxMcVoxFxsOpeEchoCancel = _CxMcVoxFxsOpeEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 10),
    _CxMcVoxFxsOpeEchoCancel_Type()
)
cxMcVoxFxsOpeEchoCancel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeEchoCancel.setStatus("mandatory")


class _CxMcVoxFxsOpeSignaling_Type(Integer32):
    """Custom type cxMcVoxFxsOpeSignaling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("did", 3),
          ("ground-start", 1),
          ("loop-start", 2))
    )


_CxMcVoxFxsOpeSignaling_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeSignaling_Object = MibTableColumn
cxMcVoxFxsOpeSignaling = _CxMcVoxFxsOpeSignaling_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 11),
    _CxMcVoxFxsOpeSignaling_Type()
)
cxMcVoxFxsOpeSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeSignaling.setStatus("mandatory")


class _CxMcVoxFxsOpeTimeOn_Type(Integer32):
    """Custom type cxMcVoxFxsOpeTimeOn based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CxMcVoxFxsOpeTimeOn_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeTimeOn_Object = MibTableColumn
cxMcVoxFxsOpeTimeOn = _CxMcVoxFxsOpeTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 12),
    _CxMcVoxFxsOpeTimeOn_Type()
)
cxMcVoxFxsOpeTimeOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeTimeOn.setStatus("obsolete")


class _CxMcVoxFxsOpeTimeOff_Type(Integer32):
    """Custom type cxMcVoxFxsOpeTimeOff based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CxMcVoxFxsOpeTimeOff_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeTimeOff_Object = MibTableColumn
cxMcVoxFxsOpeTimeOff = _CxMcVoxFxsOpeTimeOff_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 13),
    _CxMcVoxFxsOpeTimeOff_Type()
)
cxMcVoxFxsOpeTimeOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeTimeOff.setStatus("obsolete")


class _CxMcVoxFxsOpeCnctType_Type(Integer32):
    """Custom type cxMcVoxFxsOpeCnctType based on Integer32"""
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
        *(("auto-connect", 2),
          ("fixed", 3),
          ("switched", 1))
    )


_CxMcVoxFxsOpeCnctType_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeCnctType_Object = MibTableColumn
cxMcVoxFxsOpeCnctType = _CxMcVoxFxsOpeCnctType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 14),
    _CxMcVoxFxsOpeCnctType_Type()
)
cxMcVoxFxsOpeCnctType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeCnctType.setStatus("mandatory")


class _CxMcVoxFxsOpeRingType_Type(Integer32):
    """Custom type cxMcVoxFxsOpeRingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("international", 2),
          ("north-american", 1))
    )


_CxMcVoxFxsOpeRingType_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeRingType_Object = MibTableColumn
cxMcVoxFxsOpeRingType = _CxMcVoxFxsOpeRingType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 15),
    _CxMcVoxFxsOpeRingType_Type()
)
cxMcVoxFxsOpeRingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeRingType.setStatus("mandatory")


class _CxMcVoxFxsOpeImpedance_Type(Integer32):
    """Custom type cxMcVoxFxsOpeImpedance based on Integer32"""
    defaultValue = 1

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
        *(("att", 3),
          ("aus", 4),
          ("i600-ohms", 1),
          ("i900-ohms", 2))
    )


_CxMcVoxFxsOpeImpedance_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeImpedance_Object = MibTableColumn
cxMcVoxFxsOpeImpedance = _CxMcVoxFxsOpeImpedance_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 16),
    _CxMcVoxFxsOpeImpedance_Type()
)
cxMcVoxFxsOpeImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeImpedance.setStatus("mandatory")


class _CxMcVoxFxsOpeDialType_Type(Integer32):
    """Custom type cxMcVoxFxsOpeDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("pulse", 2))
    )


_CxMcVoxFxsOpeDialType_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeDialType_Object = MibTableColumn
cxMcVoxFxsOpeDialType = _CxMcVoxFxsOpeDialType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 17),
    _CxMcVoxFxsOpeDialType_Type()
)
cxMcVoxFxsOpeDialType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeDialType.setStatus("mandatory")


class _CxMcVoxFxsOpeDidSignalType_Type(Integer32):
    """Custom type cxMcVoxFxsOpeDidSignalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delay", 2),
          ("normal", 1),
          ("wink", 3))
    )


_CxMcVoxFxsOpeDidSignalType_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeDidSignalType_Object = MibTableColumn
cxMcVoxFxsOpeDidSignalType = _CxMcVoxFxsOpeDidSignalType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 18),
    _CxMcVoxFxsOpeDidSignalType_Type()
)
cxMcVoxFxsOpeDidSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeDidSignalType.setStatus("mandatory")


class _CxMcVoxFxsOpeRmtExt_Type(DisplayString):
    """Custom type cxMcVoxFxsOpeRmtExt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CxMcVoxFxsOpeRmtExt_Type.__name__ = "DisplayString"
_CxMcVoxFxsOpeRmtExt_Object = MibTableColumn
cxMcVoxFxsOpeRmtExt = _CxMcVoxFxsOpeRmtExt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 19),
    _CxMcVoxFxsOpeRmtExt_Type()
)
cxMcVoxFxsOpeRmtExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeRmtExt.setStatus("mandatory")


class _CxMcVoxFxsOpeRmtId_Type(DisplayString):
    """Custom type cxMcVoxFxsOpeRmtId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CxMcVoxFxsOpeRmtId_Type.__name__ = "DisplayString"
_CxMcVoxFxsOpeRmtId_Object = MibTableColumn
cxMcVoxFxsOpeRmtId = _CxMcVoxFxsOpeRmtId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 20),
    _CxMcVoxFxsOpeRmtId_Type()
)
cxMcVoxFxsOpeRmtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeRmtId.setStatus("optional")


class _CxMcVoxFxsOpeTranspMode_Type(Integer32):
    """Custom type cxMcVoxFxsOpeTranspMode based on Integer32"""
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
        *(("emulate", 1),
          ("local", 3),
          ("transparent", 2))
    )


_CxMcVoxFxsOpeTranspMode_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeTranspMode_Object = MibTableColumn
cxMcVoxFxsOpeTranspMode = _CxMcVoxFxsOpeTranspMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 21),
    _CxMcVoxFxsOpeTranspMode_Type()
)
cxMcVoxFxsOpeTranspMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeTranspMode.setStatus("mandatory")


class _CxMcVoxFxsOpeFaxEnable_Type(Integer32):
    """Custom type cxMcVoxFxsOpeFaxEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxFxsOpeFaxEnable_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeFaxEnable_Object = MibTableColumn
cxMcVoxFxsOpeFaxEnable = _CxMcVoxFxsOpeFaxEnable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 22),
    _CxMcVoxFxsOpeFaxEnable_Type()
)
cxMcVoxFxsOpeFaxEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeFaxEnable.setStatus("mandatory")


class _CxMcVoxFxsOpeBroadcast_Type(Integer32):
    """Custom type cxMcVoxFxsOpeBroadcast based on Integer32"""
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
        *(("master", 2),
          ("none", 1),
          ("slave", 3))
    )


_CxMcVoxFxsOpeBroadcast_Type.__name__ = "Integer32"
_CxMcVoxFxsOpeBroadcast_Object = MibTableColumn
cxMcVoxFxsOpeBroadcast = _CxMcVoxFxsOpeBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 2, 1, 23),
    _CxMcVoxFxsOpeBroadcast_Type()
)
cxMcVoxFxsOpeBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxsOpeBroadcast.setStatus("mandatory")
_CxMcVoxFxoOpeTable_Object = MibTable
cxMcVoxFxoOpeTable = _CxMcVoxFxoOpeTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3)
)
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeTable.setStatus("mandatory")
_CxMcVoxFxoOpeEntry_Object = MibTableRow
cxMcVoxFxoOpeEntry = _CxMcVoxFxoOpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1)
)
cxMcVoxFxoOpeEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxFxoOpeCardUsed"),
    (0, "CXMCVOX-MIB", "cxMcVoxFxoOpePortUsed"),
)
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeEntry.setStatus("mandatory")


class _CxMcVoxFxoOpeCardUsed_Type(Integer32):
    """Custom type cxMcVoxFxoOpeCardUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CxMcVoxFxoOpeCardUsed_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeCardUsed_Object = MibTableColumn
cxMcVoxFxoOpeCardUsed = _CxMcVoxFxoOpeCardUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 1),
    _CxMcVoxFxoOpeCardUsed_Type()
)
cxMcVoxFxoOpeCardUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeCardUsed.setStatus("mandatory")


class _CxMcVoxFxoOpePortUsed_Type(Integer32):
    """Custom type cxMcVoxFxoOpePortUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CxMcVoxFxoOpePortUsed_Type.__name__ = "Integer32"
_CxMcVoxFxoOpePortUsed_Object = MibTableColumn
cxMcVoxFxoOpePortUsed = _CxMcVoxFxoOpePortUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 2),
    _CxMcVoxFxoOpePortUsed_Type()
)
cxMcVoxFxoOpePortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpePortUsed.setStatus("mandatory")


class _CxMcVoxFxoOpePortStatus_Type(Integer32):
    """Custom type cxMcVoxFxoOpePortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              31,
              32,
              33,
              34,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("appl-err-1", 41),
          ("appl-err-2", 42),
          ("appl-err-3", 43),
          ("appl-err-4", 44),
          ("boot-err-1", 31),
          ("boot-err-2", 32),
          ("boot-err-3", 33),
          ("boot-err-4", 34),
          ("disable", 1),
          ("enable", 2),
          ("no-voice-io", 3))
    )


_CxMcVoxFxoOpePortStatus_Type.__name__ = "Integer32"
_CxMcVoxFxoOpePortStatus_Object = MibTableColumn
cxMcVoxFxoOpePortStatus = _CxMcVoxFxoOpePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 3),
    _CxMcVoxFxoOpePortStatus_Type()
)
cxMcVoxFxoOpePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpePortStatus.setStatus("mandatory")


class _CxMcVoxFxoOpeVocoder_Type(Integer32):
    """Custom type cxMcVoxFxoOpeVocoder based on Integer32"""
    defaultValue = 2

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
        *(("bps5800", 1),
          ("bps8000", 2),
          ("kbps16", 6),
          ("kbps24", 5),
          ("kbps32", 4),
          ("kbps40", 3),
          ("opt7", 7),
          ("opt8", 8))
    )


_CxMcVoxFxoOpeVocoder_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeVocoder_Object = MibTableColumn
cxMcVoxFxoOpeVocoder = _CxMcVoxFxoOpeVocoder_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 4),
    _CxMcVoxFxoOpeVocoder_Type()
)
cxMcVoxFxoOpeVocoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeVocoder.setStatus("mandatory")


class _CxMcVoxFxoOpeFaxBw_Type(Integer32):
    """Custom type cxMcVoxFxoOpeFaxBw based on Integer32"""
    defaultValue = 3

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
        *(("bps2400", 1),
          ("bps4800", 2),
          ("bps7200", 3),
          ("bps9600", 4))
    )


_CxMcVoxFxoOpeFaxBw_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeFaxBw_Object = MibTableColumn
cxMcVoxFxoOpeFaxBw = _CxMcVoxFxoOpeFaxBw_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 5),
    _CxMcVoxFxoOpeFaxBw_Type()
)
cxMcVoxFxoOpeFaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeFaxBw.setStatus("mandatory")


class _CxMcVoxFxoOpeAutoCnx_Type(Integer32):
    """Custom type cxMcVoxFxoOpeAutoCnx based on Integer32"""
    defaultValue = 1

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


_CxMcVoxFxoOpeAutoCnx_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeAutoCnx_Object = MibTableColumn
cxMcVoxFxoOpeAutoCnx = _CxMcVoxFxoOpeAutoCnx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 6),
    _CxMcVoxFxoOpeAutoCnx_Type()
)
cxMcVoxFxoOpeAutoCnx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeAutoCnx.setStatus("obsolete")


class _CxMcVoxFxoOpePathId_Type(DisplayString):
    """Custom type cxMcVoxFxoOpePathId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxFxoOpePathId_Type.__name__ = "DisplayString"
_CxMcVoxFxoOpePathId_Object = MibTableColumn
cxMcVoxFxoOpePathId = _CxMcVoxFxoOpePathId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 7),
    _CxMcVoxFxoOpePathId_Type()
)
cxMcVoxFxoOpePathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpePathId.setStatus("deprecated")


class _CxMcVoxFxoOpeTxGain_Type(Integer32):
    """Custom type cxMcVoxFxoOpeTxGain based on Integer32"""
    defaultValue = 960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxFxoOpeTxGain_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeTxGain_Object = MibTableColumn
cxMcVoxFxoOpeTxGain = _CxMcVoxFxoOpeTxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 8),
    _CxMcVoxFxoOpeTxGain_Type()
)
cxMcVoxFxoOpeTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeTxGain.setStatus("mandatory")


class _CxMcVoxFxoOpeRxGain_Type(Integer32):
    """Custom type cxMcVoxFxoOpeRxGain based on Integer32"""
    defaultValue = 960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxFxoOpeRxGain_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeRxGain_Object = MibTableColumn
cxMcVoxFxoOpeRxGain = _CxMcVoxFxoOpeRxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 9),
    _CxMcVoxFxoOpeRxGain_Type()
)
cxMcVoxFxoOpeRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeRxGain.setStatus("mandatory")


class _CxMcVoxFxoOpeEchoCancel_Type(Integer32):
    """Custom type cxMcVoxFxoOpeEchoCancel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxFxoOpeEchoCancel_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeEchoCancel_Object = MibTableColumn
cxMcVoxFxoOpeEchoCancel = _CxMcVoxFxoOpeEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 10),
    _CxMcVoxFxoOpeEchoCancel_Type()
)
cxMcVoxFxoOpeEchoCancel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeEchoCancel.setStatus("mandatory")


class _CxMcVoxFxoOpeSignaling_Type(Integer32):
    """Custom type cxMcVoxFxoOpeSignaling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("did", 3),
          ("ground-start", 1),
          ("loop-start", 2))
    )


_CxMcVoxFxoOpeSignaling_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeSignaling_Object = MibTableColumn
cxMcVoxFxoOpeSignaling = _CxMcVoxFxoOpeSignaling_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 11),
    _CxMcVoxFxoOpeSignaling_Type()
)
cxMcVoxFxoOpeSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeSignaling.setStatus("mandatory")


class _CxMcVoxFxoOpeCnctType_Type(Integer32):
    """Custom type cxMcVoxFxoOpeCnctType based on Integer32"""
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
        *(("auto-connect", 2),
          ("fixed", 3),
          ("switched", 1))
    )


_CxMcVoxFxoOpeCnctType_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeCnctType_Object = MibTableColumn
cxMcVoxFxoOpeCnctType = _CxMcVoxFxoOpeCnctType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 12),
    _CxMcVoxFxoOpeCnctType_Type()
)
cxMcVoxFxoOpeCnctType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeCnctType.setStatus("mandatory")


class _CxMcVoxFxoOpeRingType_Type(Integer32):
    """Custom type cxMcVoxFxoOpeRingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("international", 2),
          ("north-american", 1))
    )


_CxMcVoxFxoOpeRingType_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeRingType_Object = MibTableColumn
cxMcVoxFxoOpeRingType = _CxMcVoxFxoOpeRingType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 13),
    _CxMcVoxFxoOpeRingType_Type()
)
cxMcVoxFxoOpeRingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeRingType.setStatus("mandatory")


class _CxMcVoxFxoOpeImpedance_Type(Integer32):
    """Custom type cxMcVoxFxoOpeImpedance based on Integer32"""
    defaultValue = 1

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
        *(("att", 3),
          ("aus", 4),
          ("i600-ohms", 1),
          ("i900-ohms", 2))
    )


_CxMcVoxFxoOpeImpedance_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeImpedance_Object = MibTableColumn
cxMcVoxFxoOpeImpedance = _CxMcVoxFxoOpeImpedance_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 14),
    _CxMcVoxFxoOpeImpedance_Type()
)
cxMcVoxFxoOpeImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeImpedance.setStatus("mandatory")


class _CxMcVoxFxoOpeDialType_Type(Integer32):
    """Custom type cxMcVoxFxoOpeDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("pulse", 2))
    )


_CxMcVoxFxoOpeDialType_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeDialType_Object = MibTableColumn
cxMcVoxFxoOpeDialType = _CxMcVoxFxoOpeDialType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 15),
    _CxMcVoxFxoOpeDialType_Type()
)
cxMcVoxFxoOpeDialType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeDialType.setStatus("mandatory")


class _CxMcVoxFxoOpeDidSignalType_Type(Integer32):
    """Custom type cxMcVoxFxoOpeDidSignalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delay", 2),
          ("normal", 1),
          ("wink", 3))
    )


_CxMcVoxFxoOpeDidSignalType_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeDidSignalType_Object = MibTableColumn
cxMcVoxFxoOpeDidSignalType = _CxMcVoxFxoOpeDidSignalType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 16),
    _CxMcVoxFxoOpeDidSignalType_Type()
)
cxMcVoxFxoOpeDidSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeDidSignalType.setStatus("mandatory")


class _CxMcVoxFxoOpeRmtExt_Type(DisplayString):
    """Custom type cxMcVoxFxoOpeRmtExt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CxMcVoxFxoOpeRmtExt_Type.__name__ = "DisplayString"
_CxMcVoxFxoOpeRmtExt_Object = MibTableColumn
cxMcVoxFxoOpeRmtExt = _CxMcVoxFxoOpeRmtExt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 17),
    _CxMcVoxFxoOpeRmtExt_Type()
)
cxMcVoxFxoOpeRmtExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeRmtExt.setStatus("mandatory")


class _CxMcVoxFxoOpeRmtId_Type(DisplayString):
    """Custom type cxMcVoxFxoOpeRmtId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CxMcVoxFxoOpeRmtId_Type.__name__ = "DisplayString"
_CxMcVoxFxoOpeRmtId_Object = MibTableColumn
cxMcVoxFxoOpeRmtId = _CxMcVoxFxoOpeRmtId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 18),
    _CxMcVoxFxoOpeRmtId_Type()
)
cxMcVoxFxoOpeRmtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeRmtId.setStatus("optional")


class _CxMcVoxFxoOpeTranspMode_Type(Integer32):
    """Custom type cxMcVoxFxoOpeTranspMode based on Integer32"""
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
        *(("emulate", 1),
          ("local", 3),
          ("transparent", 2))
    )


_CxMcVoxFxoOpeTranspMode_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeTranspMode_Object = MibTableColumn
cxMcVoxFxoOpeTranspMode = _CxMcVoxFxoOpeTranspMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 19),
    _CxMcVoxFxoOpeTranspMode_Type()
)
cxMcVoxFxoOpeTranspMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeTranspMode.setStatus("mandatory")


class _CxMcVoxFxoOpeFaxEnable_Type(Integer32):
    """Custom type cxMcVoxFxoOpeFaxEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcVoxFxoOpeFaxEnable_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeFaxEnable_Object = MibTableColumn
cxMcVoxFxoOpeFaxEnable = _CxMcVoxFxoOpeFaxEnable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 20),
    _CxMcVoxFxoOpeFaxEnable_Type()
)
cxMcVoxFxoOpeFaxEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeFaxEnable.setStatus("mandatory")


class _CxMcVoxFxoOpeBroadcast_Type(Integer32):
    """Custom type cxMcVoxFxoOpeBroadcast based on Integer32"""
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
        *(("master", 2),
          ("none", 1),
          ("slave", 3))
    )


_CxMcVoxFxoOpeBroadcast_Type.__name__ = "Integer32"
_CxMcVoxFxoOpeBroadcast_Object = MibTableColumn
cxMcVoxFxoOpeBroadcast = _CxMcVoxFxoOpeBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 9, 3, 1, 21),
    _CxMcVoxFxoOpeBroadcast_Type()
)
cxMcVoxFxoOpeBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxFxoOpeBroadcast.setStatus("mandatory")
_CxMcVoxGrpIdAdmTable_Object = MibTable
cxMcVoxGrpIdAdmTable = _CxMcVoxGrpIdAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cxMcVoxGrpIdAdmTable.setStatus("mandatory")
_CxMcVoxGrpIdAdmEntry_Object = MibTableRow
cxMcVoxGrpIdAdmEntry = _CxMcVoxGrpIdAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 10, 1)
)
cxMcVoxGrpIdAdmEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxGrpIdAdmIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxGrpIdAdmEntry.setStatus("mandatory")


class _CxMcVoxGrpIdAdmIndex_Type(Integer32):
    """Custom type cxMcVoxGrpIdAdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CxMcVoxGrpIdAdmIndex_Type.__name__ = "Integer32"
_CxMcVoxGrpIdAdmIndex_Object = MibTableColumn
cxMcVoxGrpIdAdmIndex = _CxMcVoxGrpIdAdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 10, 1, 1),
    _CxMcVoxGrpIdAdmIndex_Type()
)
cxMcVoxGrpIdAdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGrpIdAdmIndex.setStatus("mandatory")


class _CxMcVoxGrpIdAdm_Type(DisplayString):
    """Custom type cxMcVoxGrpIdAdm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxGrpIdAdm_Type.__name__ = "DisplayString"
_CxMcVoxGrpIdAdm_Object = MibTableColumn
cxMcVoxGrpIdAdm = _CxMcVoxGrpIdAdm_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 10, 1, 2),
    _CxMcVoxGrpIdAdm_Type()
)
cxMcVoxGrpIdAdm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGrpIdAdm.setStatus("mandatory")


class _CxMcVoxGrpIdLenAdm_Type(Integer32):
    """Custom type cxMcVoxGrpIdLenAdm based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxGrpIdLenAdm_Type.__name__ = "Integer32"
_CxMcVoxGrpIdLenAdm_Object = MibTableColumn
cxMcVoxGrpIdLenAdm = _CxMcVoxGrpIdLenAdm_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 10, 1, 3),
    _CxMcVoxGrpIdLenAdm_Type()
)
cxMcVoxGrpIdLenAdm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGrpIdLenAdm.setStatus("mandatory")


class _CxMcVoxGrpIdAdmRowStatus_Type(Integer32):
    """Custom type cxMcVoxGrpIdAdmRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxMcVoxGrpIdAdmRowStatus_Type.__name__ = "Integer32"
_CxMcVoxGrpIdAdmRowStatus_Object = MibTableColumn
cxMcVoxGrpIdAdmRowStatus = _CxMcVoxGrpIdAdmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 10, 1, 4),
    _CxMcVoxGrpIdAdmRowStatus_Type()
)
cxMcVoxGrpIdAdmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGrpIdAdmRowStatus.setStatus("mandatory")


class _CxMcVoxGrpIdAdmNbPoll_Type(Integer32):
    """Custom type cxMcVoxGrpIdAdmNbPoll based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CxMcVoxGrpIdAdmNbPoll_Type.__name__ = "Integer32"
_CxMcVoxGrpIdAdmNbPoll_Object = MibTableColumn
cxMcVoxGrpIdAdmNbPoll = _CxMcVoxGrpIdAdmNbPoll_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 10, 1, 5),
    _CxMcVoxGrpIdAdmNbPoll_Type()
)
cxMcVoxGrpIdAdmNbPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGrpIdAdmNbPoll.setStatus("optional")
_CxMcVoxGrpIdOpeTable_Object = MibTable
cxMcVoxGrpIdOpeTable = _CxMcVoxGrpIdOpeTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cxMcVoxGrpIdOpeTable.setStatus("mandatory")
_CxMcVoxGrpIdOpeEntry_Object = MibTableRow
cxMcVoxGrpIdOpeEntry = _CxMcVoxGrpIdOpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 11, 1)
)
cxMcVoxGrpIdOpeEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxGrpIdOpeIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxGrpIdOpeEntry.setStatus("mandatory")


class _CxMcVoxGrpIdOpeIndex_Type(Integer32):
    """Custom type cxMcVoxGrpIdOpeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CxMcVoxGrpIdOpeIndex_Type.__name__ = "Integer32"
_CxMcVoxGrpIdOpeIndex_Object = MibTableColumn
cxMcVoxGrpIdOpeIndex = _CxMcVoxGrpIdOpeIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 11, 1, 1),
    _CxMcVoxGrpIdOpeIndex_Type()
)
cxMcVoxGrpIdOpeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGrpIdOpeIndex.setStatus("mandatory")


class _CxMcVoxGrpIdOpe_Type(DisplayString):
    """Custom type cxMcVoxGrpIdOpe based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxGrpIdOpe_Type.__name__ = "DisplayString"
_CxMcVoxGrpIdOpe_Object = MibTableColumn
cxMcVoxGrpIdOpe = _CxMcVoxGrpIdOpe_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 11, 1, 2),
    _CxMcVoxGrpIdOpe_Type()
)
cxMcVoxGrpIdOpe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGrpIdOpe.setStatus("mandatory")


class _CxMcVoxGrpIdLenOpe_Type(Integer32):
    """Custom type cxMcVoxGrpIdLenOpe based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxGrpIdLenOpe_Type.__name__ = "Integer32"
_CxMcVoxGrpIdLenOpe_Object = MibTableColumn
cxMcVoxGrpIdLenOpe = _CxMcVoxGrpIdLenOpe_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 11, 1, 3),
    _CxMcVoxGrpIdLenOpe_Type()
)
cxMcVoxGrpIdLenOpe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGrpIdLenOpe.setStatus("mandatory")


class _CxMcVoxGrpIdOpeNbPoll_Type(Integer32):
    """Custom type cxMcVoxGrpIdOpeNbPoll based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CxMcVoxGrpIdOpeNbPoll_Type.__name__ = "Integer32"
_CxMcVoxGrpIdOpeNbPoll_Object = MibTableColumn
cxMcVoxGrpIdOpeNbPoll = _CxMcVoxGrpIdOpeNbPoll_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 11, 1, 4),
    _CxMcVoxGrpIdOpeNbPoll_Type()
)
cxMcVoxGrpIdOpeNbPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGrpIdOpeNbPoll.setStatus("optional")
_CxMcVoxGrpDefAdmTable_Object = MibTable
cxMcVoxGrpDefAdmTable = _CxMcVoxGrpDefAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 12)
)
if mibBuilder.loadTexts:
    cxMcVoxGrpDefAdmTable.setStatus("mandatory")
_CxMcVoxGrpDefAdmEntry_Object = MibTableRow
cxMcVoxGrpDefAdmEntry = _CxMcVoxGrpDefAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 12, 1)
)
cxMcVoxGrpDefAdmEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxGrpDefAdmIndex"),
    (0, "CXMCVOX-MIB", "cxMcVoxGrpDefAdmPriority"),
)
if mibBuilder.loadTexts:
    cxMcVoxGrpDefAdmEntry.setStatus("mandatory")


class _CxMcVoxGrpDefAdmIndex_Type(Integer32):
    """Custom type cxMcVoxGrpDefAdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CxMcVoxGrpDefAdmIndex_Type.__name__ = "Integer32"
_CxMcVoxGrpDefAdmIndex_Object = MibTableColumn
cxMcVoxGrpDefAdmIndex = _CxMcVoxGrpDefAdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 12, 1, 1),
    _CxMcVoxGrpDefAdmIndex_Type()
)
cxMcVoxGrpDefAdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGrpDefAdmIndex.setStatus("mandatory")


class _CxMcVoxGrpDefAdmPriority_Type(Integer32):
    """Custom type cxMcVoxGrpDefAdmPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_CxMcVoxGrpDefAdmPriority_Type.__name__ = "Integer32"
_CxMcVoxGrpDefAdmPriority_Object = MibTableColumn
cxMcVoxGrpDefAdmPriority = _CxMcVoxGrpDefAdmPriority_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 12, 1, 2),
    _CxMcVoxGrpDefAdmPriority_Type()
)
cxMcVoxGrpDefAdmPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGrpDefAdmPriority.setStatus("mandatory")


class _CxMcVoxGrpDefAdmRowStatus_Type(Integer32):
    """Custom type cxMcVoxGrpDefAdmRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxMcVoxGrpDefAdmRowStatus_Type.__name__ = "Integer32"
_CxMcVoxGrpDefAdmRowStatus_Object = MibTableColumn
cxMcVoxGrpDefAdmRowStatus = _CxMcVoxGrpDefAdmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 12, 1, 3),
    _CxMcVoxGrpDefAdmRowStatus_Type()
)
cxMcVoxGrpDefAdmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGrpDefAdmRowStatus.setStatus("mandatory")


class _CxMcVoxGrpDefAdmPathId_Type(DisplayString):
    """Custom type cxMcVoxGrpDefAdmPathId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxGrpDefAdmPathId_Type.__name__ = "DisplayString"
_CxMcVoxGrpDefAdmPathId_Object = MibTableColumn
cxMcVoxGrpDefAdmPathId = _CxMcVoxGrpDefAdmPathId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 12, 1, 4),
    _CxMcVoxGrpDefAdmPathId_Type()
)
cxMcVoxGrpDefAdmPathId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGrpDefAdmPathId.setStatus("deprecated")


class _CxMcVoxGrpDefAdmRmtExt_Type(DisplayString):
    """Custom type cxMcVoxGrpDefAdmRmtExt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CxMcVoxGrpDefAdmRmtExt_Type.__name__ = "DisplayString"
_CxMcVoxGrpDefAdmRmtExt_Object = MibTableColumn
cxMcVoxGrpDefAdmRmtExt = _CxMcVoxGrpDefAdmRmtExt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 12, 1, 5),
    _CxMcVoxGrpDefAdmRmtExt_Type()
)
cxMcVoxGrpDefAdmRmtExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxGrpDefAdmRmtExt.setStatus("mandatory")
_CxMcVoxGrpDefOpeTable_Object = MibTable
cxMcVoxGrpDefOpeTable = _CxMcVoxGrpDefOpeTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 13)
)
if mibBuilder.loadTexts:
    cxMcVoxGrpDefOpeTable.setStatus("mandatory")
_CxMcVoxGrpDefOpeEntry_Object = MibTableRow
cxMcVoxGrpDefOpeEntry = _CxMcVoxGrpDefOpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 13, 1)
)
cxMcVoxGrpDefOpeEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxGrpDefOpeIndex"),
    (0, "CXMCVOX-MIB", "cxMcVoxGrpDefOpePriority"),
)
if mibBuilder.loadTexts:
    cxMcVoxGrpDefOpeEntry.setStatus("mandatory")


class _CxMcVoxGrpDefOpeIndex_Type(Integer32):
    """Custom type cxMcVoxGrpDefOpeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CxMcVoxGrpDefOpeIndex_Type.__name__ = "Integer32"
_CxMcVoxGrpDefOpeIndex_Object = MibTableColumn
cxMcVoxGrpDefOpeIndex = _CxMcVoxGrpDefOpeIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 13, 1, 1),
    _CxMcVoxGrpDefOpeIndex_Type()
)
cxMcVoxGrpDefOpeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGrpDefOpeIndex.setStatus("mandatory")


class _CxMcVoxGrpDefOpePriority_Type(Integer32):
    """Custom type cxMcVoxGrpDefOpePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_CxMcVoxGrpDefOpePriority_Type.__name__ = "Integer32"
_CxMcVoxGrpDefOpePriority_Object = MibTableColumn
cxMcVoxGrpDefOpePriority = _CxMcVoxGrpDefOpePriority_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 13, 1, 2),
    _CxMcVoxGrpDefOpePriority_Type()
)
cxMcVoxGrpDefOpePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGrpDefOpePriority.setStatus("mandatory")


class _CxMcVoxGrpDefOpePathId_Type(DisplayString):
    """Custom type cxMcVoxGrpDefOpePathId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxGrpDefOpePathId_Type.__name__ = "DisplayString"
_CxMcVoxGrpDefOpePathId_Object = MibTableColumn
cxMcVoxGrpDefOpePathId = _CxMcVoxGrpDefOpePathId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 13, 1, 3),
    _CxMcVoxGrpDefOpePathId_Type()
)
cxMcVoxGrpDefOpePathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGrpDefOpePathId.setStatus("deprecated")


class _CxMcVoxGrpDefOpeRmtExt_Type(DisplayString):
    """Custom type cxMcVoxGrpDefOpeRmtExt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CxMcVoxGrpDefOpeRmtExt_Type.__name__ = "DisplayString"
_CxMcVoxGrpDefOpeRmtExt_Object = MibTableColumn
cxMcVoxGrpDefOpeRmtExt = _CxMcVoxGrpDefOpeRmtExt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 13, 1, 4),
    _CxMcVoxGrpDefOpeRmtExt_Type()
)
cxMcVoxGrpDefOpeRmtExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxGrpDefOpeRmtExt.setStatus("mandatory")
_CxMcVoxAdmPinTable_Object = MibTable
cxMcVoxAdmPinTable = _CxMcVoxAdmPinTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 14)
)
if mibBuilder.loadTexts:
    cxMcVoxAdmPinTable.setStatus("mandatory")
_CxMcVoxAdmPinEntry_Object = MibTableRow
cxMcVoxAdmPinEntry = _CxMcVoxAdmPinEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 14, 1)
)
cxMcVoxAdmPinEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxAdmPinIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxAdmPinEntry.setStatus("mandatory")


class _CxMcVoxAdmPinIndex_Type(Integer32):
    """Custom type cxMcVoxAdmPinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CxMcVoxAdmPinIndex_Type.__name__ = "Integer32"
_CxMcVoxAdmPinIndex_Object = MibTableColumn
cxMcVoxAdmPinIndex = _CxMcVoxAdmPinIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 14, 1, 1),
    _CxMcVoxAdmPinIndex_Type()
)
cxMcVoxAdmPinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxAdmPinIndex.setStatus("mandatory")


class _CxMcVoxAdmPinCode_Type(DisplayString):
    """Custom type cxMcVoxAdmPinCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 8),
    )


_CxMcVoxAdmPinCode_Type.__name__ = "DisplayString"
_CxMcVoxAdmPinCode_Object = MibTableColumn
cxMcVoxAdmPinCode = _CxMcVoxAdmPinCode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 14, 1, 2),
    _CxMcVoxAdmPinCode_Type()
)
cxMcVoxAdmPinCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmPinCode.setStatus("mandatory")


class _CxMcVoxAdmPinRowStatus_Type(Integer32):
    """Custom type cxMcVoxAdmPinRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxMcVoxAdmPinRowStatus_Type.__name__ = "Integer32"
_CxMcVoxAdmPinRowStatus_Object = MibTableColumn
cxMcVoxAdmPinRowStatus = _CxMcVoxAdmPinRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 14, 1, 3),
    _CxMcVoxAdmPinRowStatus_Type()
)
cxMcVoxAdmPinRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmPinRowStatus.setStatus("mandatory")
_CxMcVoxOpePinTable_Object = MibTable
cxMcVoxOpePinTable = _CxMcVoxOpePinTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 15)
)
if mibBuilder.loadTexts:
    cxMcVoxOpePinTable.setStatus("mandatory")
_CxMcVoxOpePinEntry_Object = MibTableRow
cxMcVoxOpePinEntry = _CxMcVoxOpePinEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 15, 1)
)
cxMcVoxOpePinEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxOpePinIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxOpePinEntry.setStatus("mandatory")


class _CxMcVoxOpePinIndex_Type(Integer32):
    """Custom type cxMcVoxOpePinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CxMcVoxOpePinIndex_Type.__name__ = "Integer32"
_CxMcVoxOpePinIndex_Object = MibTableColumn
cxMcVoxOpePinIndex = _CxMcVoxOpePinIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 15, 1, 1),
    _CxMcVoxOpePinIndex_Type()
)
cxMcVoxOpePinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpePinIndex.setStatus("mandatory")


class _CxMcVoxOpePinCode_Type(DisplayString):
    """Custom type cxMcVoxOpePinCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 8),
    )


_CxMcVoxOpePinCode_Type.__name__ = "DisplayString"
_CxMcVoxOpePinCode_Object = MibTableColumn
cxMcVoxOpePinCode = _CxMcVoxOpePinCode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 15, 1, 2),
    _CxMcVoxOpePinCode_Type()
)
cxMcVoxOpePinCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpePinCode.setStatus("mandatory")
_CxMcVoxAdmLclZoneTable_Object = MibTable
cxMcVoxAdmLclZoneTable = _CxMcVoxAdmLclZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 16)
)
if mibBuilder.loadTexts:
    cxMcVoxAdmLclZoneTable.setStatus("mandatory")
_CxMcVoxAdmLclZoneEntry_Object = MibTableRow
cxMcVoxAdmLclZoneEntry = _CxMcVoxAdmLclZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 16, 1)
)
cxMcVoxAdmLclZoneEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxAdmLclZoneIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxAdmLclZoneEntry.setStatus("mandatory")


class _CxMcVoxAdmLclZoneIndex_Type(Integer32):
    """Custom type cxMcVoxAdmLclZoneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CxMcVoxAdmLclZoneIndex_Type.__name__ = "Integer32"
_CxMcVoxAdmLclZoneIndex_Object = MibTableColumn
cxMcVoxAdmLclZoneIndex = _CxMcVoxAdmLclZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 16, 1, 1),
    _CxMcVoxAdmLclZoneIndex_Type()
)
cxMcVoxAdmLclZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxAdmLclZoneIndex.setStatus("mandatory")


class _CxMcVoxAdmLclZoneCode_Type(DisplayString):
    """Custom type cxMcVoxAdmLclZoneCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxAdmLclZoneCode_Type.__name__ = "DisplayString"
_CxMcVoxAdmLclZoneCode_Object = MibTableColumn
cxMcVoxAdmLclZoneCode = _CxMcVoxAdmLclZoneCode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 16, 1, 2),
    _CxMcVoxAdmLclZoneCode_Type()
)
cxMcVoxAdmLclZoneCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmLclZoneCode.setStatus("mandatory")


class _CxMcVoxAdmLclZoneLng_Type(Integer32):
    """Custom type cxMcVoxAdmLclZoneLng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxAdmLclZoneLng_Type.__name__ = "Integer32"
_CxMcVoxAdmLclZoneLng_Object = MibTableColumn
cxMcVoxAdmLclZoneLng = _CxMcVoxAdmLclZoneLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 16, 1, 3),
    _CxMcVoxAdmLclZoneLng_Type()
)
cxMcVoxAdmLclZoneLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxAdmLclZoneLng.setStatus("mandatory")


class _CxMcVoxAdmLclZoneRowStatus_Type(Integer32):
    """Custom type cxMcVoxAdmLclZoneRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxMcVoxAdmLclZoneRowStatus_Type.__name__ = "Integer32"
_CxMcVoxAdmLclZoneRowStatus_Object = MibTableColumn
cxMcVoxAdmLclZoneRowStatus = _CxMcVoxAdmLclZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 16, 1, 4),
    _CxMcVoxAdmLclZoneRowStatus_Type()
)
cxMcVoxAdmLclZoneRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmLclZoneRowStatus.setStatus("mandatory")
_CxMcVoxOpeLclZoneTable_Object = MibTable
cxMcVoxOpeLclZoneTable = _CxMcVoxOpeLclZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 17)
)
if mibBuilder.loadTexts:
    cxMcVoxOpeLclZoneTable.setStatus("mandatory")
_CxMcVoxOpeLclZoneEntry_Object = MibTableRow
cxMcVoxOpeLclZoneEntry = _CxMcVoxOpeLclZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 17, 1)
)
cxMcVoxOpeLclZoneEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxOpeLclZoneIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxOpeLclZoneEntry.setStatus("mandatory")


class _CxMcVoxOpeLclZoneIndex_Type(Integer32):
    """Custom type cxMcVoxOpeLclZoneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CxMcVoxOpeLclZoneIndex_Type.__name__ = "Integer32"
_CxMcVoxOpeLclZoneIndex_Object = MibTableColumn
cxMcVoxOpeLclZoneIndex = _CxMcVoxOpeLclZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 17, 1, 1),
    _CxMcVoxOpeLclZoneIndex_Type()
)
cxMcVoxOpeLclZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeLclZoneIndex.setStatus("mandatory")


class _CxMcVoxOpeLclZoneCode_Type(DisplayString):
    """Custom type cxMcVoxOpeLclZoneCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxOpeLclZoneCode_Type.__name__ = "DisplayString"
_CxMcVoxOpeLclZoneCode_Object = MibTableColumn
cxMcVoxOpeLclZoneCode = _CxMcVoxOpeLclZoneCode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 17, 1, 2),
    _CxMcVoxOpeLclZoneCode_Type()
)
cxMcVoxOpeLclZoneCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeLclZoneCode.setStatus("mandatory")


class _CxMcVoxOpeLclZoneLng_Type(Integer32):
    """Custom type cxMcVoxOpeLclZoneLng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxOpeLclZoneLng_Type.__name__ = "Integer32"
_CxMcVoxOpeLclZoneLng_Object = MibTableColumn
cxMcVoxOpeLclZoneLng = _CxMcVoxOpeLclZoneLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 17, 1, 3),
    _CxMcVoxOpeLclZoneLng_Type()
)
cxMcVoxOpeLclZoneLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeLclZoneLng.setStatus("mandatory")
_CxMcVoxAdmRTC_ObjectIdentity = ObjectIdentity
cxMcVoxAdmRTC = _CxMcVoxAdmRTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 18)
)


class _CxMcVoxAdmRTCCountry_Type(DisplayString):
    """Custom type cxMcVoxAdmRTCCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxAdmRTCCountry_Type.__name__ = "DisplayString"
_CxMcVoxAdmRTCCountry_Object = MibScalar
cxMcVoxAdmRTCCountry = _CxMcVoxAdmRTCCountry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 18, 1),
    _CxMcVoxAdmRTCCountry_Type()
)
cxMcVoxAdmRTCCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmRTCCountry.setStatus("deprecated")


class _CxMcVoxAdmRTCCountryLng_Type(Integer32):
    """Custom type cxMcVoxAdmRTCCountryLng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxAdmRTCCountryLng_Type.__name__ = "Integer32"
_CxMcVoxAdmRTCCountryLng_Object = MibScalar
cxMcVoxAdmRTCCountryLng = _CxMcVoxAdmRTCCountryLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 18, 2),
    _CxMcVoxAdmRTCCountryLng_Type()
)
cxMcVoxAdmRTCCountryLng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmRTCCountryLng.setStatus("deprecated")


class _CxMcVoxAdmRTCNonLclCountry_Type(DisplayString):
    """Custom type cxMcVoxAdmRTCNonLclCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxAdmRTCNonLclCountry_Type.__name__ = "DisplayString"
_CxMcVoxAdmRTCNonLclCountry_Object = MibScalar
cxMcVoxAdmRTCNonLclCountry = _CxMcVoxAdmRTCNonLclCountry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 18, 3),
    _CxMcVoxAdmRTCNonLclCountry_Type()
)
cxMcVoxAdmRTCNonLclCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmRTCNonLclCountry.setStatus("deprecated")


class _CxMcVoxAdmRTCNonLclCountryLng_Type(Integer32):
    """Custom type cxMcVoxAdmRTCNonLclCountryLng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxAdmRTCNonLclCountryLng_Type.__name__ = "Integer32"
_CxMcVoxAdmRTCNonLclCountryLng_Object = MibScalar
cxMcVoxAdmRTCNonLclCountryLng = _CxMcVoxAdmRTCNonLclCountryLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 18, 4),
    _CxMcVoxAdmRTCNonLclCountryLng_Type()
)
cxMcVoxAdmRTCNonLclCountryLng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmRTCNonLclCountryLng.setStatus("deprecated")


class _CxMcVoxAdmRTCArea_Type(DisplayString):
    """Custom type cxMcVoxAdmRTCArea based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxAdmRTCArea_Type.__name__ = "DisplayString"
_CxMcVoxAdmRTCArea_Object = MibScalar
cxMcVoxAdmRTCArea = _CxMcVoxAdmRTCArea_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 18, 5),
    _CxMcVoxAdmRTCArea_Type()
)
cxMcVoxAdmRTCArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmRTCArea.setStatus("deprecated")


class _CxMcVoxAdmRTCAreaLng_Type(Integer32):
    """Custom type cxMcVoxAdmRTCAreaLng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxAdmRTCAreaLng_Type.__name__ = "Integer32"
_CxMcVoxAdmRTCAreaLng_Object = MibScalar
cxMcVoxAdmRTCAreaLng = _CxMcVoxAdmRTCAreaLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 18, 6),
    _CxMcVoxAdmRTCAreaLng_Type()
)
cxMcVoxAdmRTCAreaLng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmRTCAreaLng.setStatus("deprecated")


class _CxMcVoxAdmRTCNonLclArea_Type(DisplayString):
    """Custom type cxMcVoxAdmRTCNonLclArea based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxAdmRTCNonLclArea_Type.__name__ = "DisplayString"
_CxMcVoxAdmRTCNonLclArea_Object = MibScalar
cxMcVoxAdmRTCNonLclArea = _CxMcVoxAdmRTCNonLclArea_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 18, 7),
    _CxMcVoxAdmRTCNonLclArea_Type()
)
cxMcVoxAdmRTCNonLclArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmRTCNonLclArea.setStatus("deprecated")


class _CxMcVoxAdmRTCNonLclAreaLng_Type(Integer32):
    """Custom type cxMcVoxAdmRTCNonLclAreaLng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxAdmRTCNonLclAreaLng_Type.__name__ = "Integer32"
_CxMcVoxAdmRTCNonLclAreaLng_Object = MibScalar
cxMcVoxAdmRTCNonLclAreaLng = _CxMcVoxAdmRTCNonLclAreaLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 18, 8),
    _CxMcVoxAdmRTCNonLclAreaLng_Type()
)
cxMcVoxAdmRTCNonLclAreaLng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmRTCNonLclAreaLng.setStatus("deprecated")


class _CxMcVoxAdmRTCNonLclZone_Type(DisplayString):
    """Custom type cxMcVoxAdmRTCNonLclZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxAdmRTCNonLclZone_Type.__name__ = "DisplayString"
_CxMcVoxAdmRTCNonLclZone_Object = MibScalar
cxMcVoxAdmRTCNonLclZone = _CxMcVoxAdmRTCNonLclZone_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 18, 9),
    _CxMcVoxAdmRTCNonLclZone_Type()
)
cxMcVoxAdmRTCNonLclZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmRTCNonLclZone.setStatus("deprecated")


class _CxMcVoxAdmRTCNonLclZoneLng_Type(Integer32):
    """Custom type cxMcVoxAdmRTCNonLclZoneLng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxAdmRTCNonLclZoneLng_Type.__name__ = "Integer32"
_CxMcVoxAdmRTCNonLclZoneLng_Object = MibScalar
cxMcVoxAdmRTCNonLclZoneLng = _CxMcVoxAdmRTCNonLclZoneLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 18, 10),
    _CxMcVoxAdmRTCNonLclZoneLng_Type()
)
cxMcVoxAdmRTCNonLclZoneLng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmRTCNonLclZoneLng.setStatus("deprecated")
_CxMcVoxOpeRTC_ObjectIdentity = ObjectIdentity
cxMcVoxOpeRTC = _CxMcVoxOpeRTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 19)
)


class _CxMcVoxOpeRTCCountry_Type(DisplayString):
    """Custom type cxMcVoxOpeRTCCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxOpeRTCCountry_Type.__name__ = "DisplayString"
_CxMcVoxOpeRTCCountry_Object = MibScalar
cxMcVoxOpeRTCCountry = _CxMcVoxOpeRTCCountry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 19, 1),
    _CxMcVoxOpeRTCCountry_Type()
)
cxMcVoxOpeRTCCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeRTCCountry.setStatus("deprecated")


class _CxMcVoxOpeRTCCountryLng_Type(Integer32):
    """Custom type cxMcVoxOpeRTCCountryLng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxOpeRTCCountryLng_Type.__name__ = "Integer32"
_CxMcVoxOpeRTCCountryLng_Object = MibScalar
cxMcVoxOpeRTCCountryLng = _CxMcVoxOpeRTCCountryLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 19, 2),
    _CxMcVoxOpeRTCCountryLng_Type()
)
cxMcVoxOpeRTCCountryLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeRTCCountryLng.setStatus("deprecated")


class _CxMcVoxOpeRTCNonLclCountry_Type(DisplayString):
    """Custom type cxMcVoxOpeRTCNonLclCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxOpeRTCNonLclCountry_Type.__name__ = "DisplayString"
_CxMcVoxOpeRTCNonLclCountry_Object = MibScalar
cxMcVoxOpeRTCNonLclCountry = _CxMcVoxOpeRTCNonLclCountry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 19, 3),
    _CxMcVoxOpeRTCNonLclCountry_Type()
)
cxMcVoxOpeRTCNonLclCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeRTCNonLclCountry.setStatus("deprecated")


class _CxMcVoxOpeRTCNonLclCountryLng_Type(Integer32):
    """Custom type cxMcVoxOpeRTCNonLclCountryLng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxOpeRTCNonLclCountryLng_Type.__name__ = "Integer32"
_CxMcVoxOpeRTCNonLclCountryLng_Object = MibScalar
cxMcVoxOpeRTCNonLclCountryLng = _CxMcVoxOpeRTCNonLclCountryLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 19, 4),
    _CxMcVoxOpeRTCNonLclCountryLng_Type()
)
cxMcVoxOpeRTCNonLclCountryLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeRTCNonLclCountryLng.setStatus("deprecated")


class _CxMcVoxOpeRTCArea_Type(DisplayString):
    """Custom type cxMcVoxOpeRTCArea based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxOpeRTCArea_Type.__name__ = "DisplayString"
_CxMcVoxOpeRTCArea_Object = MibScalar
cxMcVoxOpeRTCArea = _CxMcVoxOpeRTCArea_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 19, 5),
    _CxMcVoxOpeRTCArea_Type()
)
cxMcVoxOpeRTCArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeRTCArea.setStatus("deprecated")


class _CxMcVoxOpeRTCAreaLng_Type(Integer32):
    """Custom type cxMcVoxOpeRTCAreaLng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxOpeRTCAreaLng_Type.__name__ = "Integer32"
_CxMcVoxOpeRTCAreaLng_Object = MibScalar
cxMcVoxOpeRTCAreaLng = _CxMcVoxOpeRTCAreaLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 19, 6),
    _CxMcVoxOpeRTCAreaLng_Type()
)
cxMcVoxOpeRTCAreaLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeRTCAreaLng.setStatus("deprecated")


class _CxMcVoxOpeRTCNonLclArea_Type(DisplayString):
    """Custom type cxMcVoxOpeRTCNonLclArea based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxOpeRTCNonLclArea_Type.__name__ = "DisplayString"
_CxMcVoxOpeRTCNonLclArea_Object = MibScalar
cxMcVoxOpeRTCNonLclArea = _CxMcVoxOpeRTCNonLclArea_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 19, 7),
    _CxMcVoxOpeRTCNonLclArea_Type()
)
cxMcVoxOpeRTCNonLclArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeRTCNonLclArea.setStatus("deprecated")


class _CxMcVoxOpeRTCNonLclAreaLng_Type(Integer32):
    """Custom type cxMcVoxOpeRTCNonLclAreaLng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxOpeRTCNonLclAreaLng_Type.__name__ = "Integer32"
_CxMcVoxOpeRTCNonLclAreaLng_Object = MibScalar
cxMcVoxOpeRTCNonLclAreaLng = _CxMcVoxOpeRTCNonLclAreaLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 19, 8),
    _CxMcVoxOpeRTCNonLclAreaLng_Type()
)
cxMcVoxOpeRTCNonLclAreaLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeRTCNonLclAreaLng.setStatus("deprecated")


class _CxMcVoxOpeRTCNonLclZone_Type(DisplayString):
    """Custom type cxMcVoxOpeRTCNonLclZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxOpeRTCNonLclZone_Type.__name__ = "DisplayString"
_CxMcVoxOpeRTCNonLclZone_Object = MibScalar
cxMcVoxOpeRTCNonLclZone = _CxMcVoxOpeRTCNonLclZone_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 19, 9),
    _CxMcVoxOpeRTCNonLclZone_Type()
)
cxMcVoxOpeRTCNonLclZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeRTCNonLclZone.setStatus("deprecated")


class _CxMcVoxOpeRTCNonLclZoneLng_Type(Integer32):
    """Custom type cxMcVoxOpeRTCNonLclZoneLng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxOpeRTCNonLclZoneLng_Type.__name__ = "Integer32"
_CxMcVoxOpeRTCNonLclZoneLng_Object = MibScalar
cxMcVoxOpeRTCNonLclZoneLng = _CxMcVoxOpeRTCNonLclZoneLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 19, 10),
    _CxMcVoxOpeRTCNonLclZoneLng_Type()
)
cxMcVoxOpeRTCNonLclZoneLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeRTCNonLclZoneLng.setStatus("deprecated")
_CxMcVoxDriverAdmPriv_ObjectIdentity = ObjectIdentity
cxMcVoxDriverAdmPriv = _CxMcVoxDriverAdmPriv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20)
)
_CxMcVoxAdmPortPrivTable_Object = MibTable
cxMcVoxAdmPortPrivTable = _CxMcVoxAdmPortPrivTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1)
)
if mibBuilder.loadTexts:
    cxMcVoxAdmPortPrivTable.setStatus("mandatory")
_CxMcVoxAdmPortPrivEntry_Object = MibTableRow
cxMcVoxAdmPortPrivEntry = _CxMcVoxAdmPortPrivEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1)
)
cxMcVoxAdmPortPrivEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxAdmCardUsed"),
    (0, "CXMCVOX-MIB", "cxMcVoxAdmPortUsed"),
)
if mibBuilder.loadTexts:
    cxMcVoxAdmPortPrivEntry.setStatus("mandatory")


class _CxMcVoxAdmCardUsed_Type(Integer32):
    """Custom type cxMcVoxAdmCardUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CxMcVoxAdmCardUsed_Type.__name__ = "Integer32"
_CxMcVoxAdmCardUsed_Object = MibTableColumn
cxMcVoxAdmCardUsed = _CxMcVoxAdmCardUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 1),
    _CxMcVoxAdmCardUsed_Type()
)
cxMcVoxAdmCardUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxAdmCardUsed.setStatus("mandatory")


class _CxMcVoxAdmPortUsed_Type(Integer32):
    """Custom type cxMcVoxAdmPortUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CxMcVoxAdmPortUsed_Type.__name__ = "Integer32"
_CxMcVoxAdmPortUsed_Object = MibTableColumn
cxMcVoxAdmPortUsed = _CxMcVoxAdmPortUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 2),
    _CxMcVoxAdmPortUsed_Type()
)
cxMcVoxAdmPortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxAdmPortUsed.setStatus("mandatory")


class _CxMcVoxAdmRingTimeOn_Type(Integer32):
    """Custom type cxMcVoxAdmRingTimeOn based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CxMcVoxAdmRingTimeOn_Type.__name__ = "Integer32"
_CxMcVoxAdmRingTimeOn_Object = MibTableColumn
cxMcVoxAdmRingTimeOn = _CxMcVoxAdmRingTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 3),
    _CxMcVoxAdmRingTimeOn_Type()
)
cxMcVoxAdmRingTimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmRingTimeOn.setStatus("mandatory")


class _CxMcVoxAdmRingTimeOff1_Type(Integer32):
    """Custom type cxMcVoxAdmRingTimeOff1 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CxMcVoxAdmRingTimeOff1_Type.__name__ = "Integer32"
_CxMcVoxAdmRingTimeOff1_Object = MibTableColumn
cxMcVoxAdmRingTimeOff1 = _CxMcVoxAdmRingTimeOff1_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 4),
    _CxMcVoxAdmRingTimeOff1_Type()
)
cxMcVoxAdmRingTimeOff1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmRingTimeOff1.setStatus("mandatory")


class _CxMcVoxAdmRingTimeOff2_Type(Integer32):
    """Custom type cxMcVoxAdmRingTimeOff2 based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CxMcVoxAdmRingTimeOff2_Type.__name__ = "Integer32"
_CxMcVoxAdmRingTimeOff2_Object = MibTableColumn
cxMcVoxAdmRingTimeOff2 = _CxMcVoxAdmRingTimeOff2_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 5),
    _CxMcVoxAdmRingTimeOff2_Type()
)
cxMcVoxAdmRingTimeOff2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmRingTimeOff2.setStatus("mandatory")


class _CxMcVoxAdmEchoCancelLevel_Type(Integer32):
    """Custom type cxMcVoxAdmEchoCancelLevel based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CxMcVoxAdmEchoCancelLevel_Type.__name__ = "Integer32"
_CxMcVoxAdmEchoCancelLevel_Object = MibTableColumn
cxMcVoxAdmEchoCancelLevel = _CxMcVoxAdmEchoCancelLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 6),
    _CxMcVoxAdmEchoCancelLevel_Type()
)
cxMcVoxAdmEchoCancelLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmEchoCancelLevel.setStatus("mandatory")


class _CxMcVoxAdmToneDelayAfterCnct_Type(Integer32):
    """Custom type cxMcVoxAdmToneDelayAfterCnct based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_CxMcVoxAdmToneDelayAfterCnct_Type.__name__ = "Integer32"
_CxMcVoxAdmToneDelayAfterCnct_Object = MibTableColumn
cxMcVoxAdmToneDelayAfterCnct = _CxMcVoxAdmToneDelayAfterCnct_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 7),
    _CxMcVoxAdmToneDelayAfterCnct_Type()
)
cxMcVoxAdmToneDelayAfterCnct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmToneDelayAfterCnct.setStatus("mandatory")


class _CxMcVoxAdmToneDelayAfterFlash_Type(Integer32):
    """Custom type cxMcVoxAdmToneDelayAfterFlash based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_CxMcVoxAdmToneDelayAfterFlash_Type.__name__ = "Integer32"
_CxMcVoxAdmToneDelayAfterFlash_Object = MibTableColumn
cxMcVoxAdmToneDelayAfterFlash = _CxMcVoxAdmToneDelayAfterFlash_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 8),
    _CxMcVoxAdmToneDelayAfterFlash_Type()
)
cxMcVoxAdmToneDelayAfterFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmToneDelayAfterFlash.setStatus("mandatory")


class _CxMcVoxAdmToneOffsetTxGain_Type(Integer32):
    """Custom type cxMcVoxAdmToneOffsetTxGain based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxAdmToneOffsetTxGain_Type.__name__ = "Integer32"
_CxMcVoxAdmToneOffsetTxGain_Object = MibTableColumn
cxMcVoxAdmToneOffsetTxGain = _CxMcVoxAdmToneOffsetTxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 9),
    _CxMcVoxAdmToneOffsetTxGain_Type()
)
cxMcVoxAdmToneOffsetTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmToneOffsetTxGain.setStatus("mandatory")


class _CxMcVoxAdmVoiceOffsetTxGain_Type(Integer32):
    """Custom type cxMcVoxAdmVoiceOffsetTxGain based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxAdmVoiceOffsetTxGain_Type.__name__ = "Integer32"
_CxMcVoxAdmVoiceOffsetTxGain_Object = MibTableColumn
cxMcVoxAdmVoiceOffsetTxGain = _CxMcVoxAdmVoiceOffsetTxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 10),
    _CxMcVoxAdmVoiceOffsetTxGain_Type()
)
cxMcVoxAdmVoiceOffsetTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmVoiceOffsetTxGain.setStatus("mandatory")


class _CxMcVoxAdmAc15InterDigit_Type(Integer32):
    """Custom type cxMcVoxAdmAc15InterDigit based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxAdmAc15InterDigit_Type.__name__ = "Integer32"
_CxMcVoxAdmAc15InterDigit_Object = MibTableColumn
cxMcVoxAdmAc15InterDigit = _CxMcVoxAdmAc15InterDigit_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 11),
    _CxMcVoxAdmAc15InterDigit_Type()
)
cxMcVoxAdmAc15InterDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmAc15InterDigit.setStatus("mandatory")


class _CxMcVoxAdmMfToneThold_Type(Integer32):
    """Custom type cxMcVoxAdmMfToneThold based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxMcVoxAdmMfToneThold_Type.__name__ = "Integer32"
_CxMcVoxAdmMfToneThold_Object = MibTableColumn
cxMcVoxAdmMfToneThold = _CxMcVoxAdmMfToneThold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 12),
    _CxMcVoxAdmMfToneThold_Type()
)
cxMcVoxAdmMfToneThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmMfToneThold.setStatus("mandatory")


class _CxMcVoxAdmPulseTmin_Type(Integer32):
    """Custom type cxMcVoxAdmPulseTmin based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_CxMcVoxAdmPulseTmin_Type.__name__ = "Integer32"
_CxMcVoxAdmPulseTmin_Object = MibTableColumn
cxMcVoxAdmPulseTmin = _CxMcVoxAdmPulseTmin_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 13),
    _CxMcVoxAdmPulseTmin_Type()
)
cxMcVoxAdmPulseTmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmPulseTmin.setStatus("mandatory")


class _CxMcVoxAdmPulseTmax_Type(Integer32):
    """Custom type cxMcVoxAdmPulseTmax based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_CxMcVoxAdmPulseTmax_Type.__name__ = "Integer32"
_CxMcVoxAdmPulseTmax_Object = MibTableColumn
cxMcVoxAdmPulseTmax = _CxMcVoxAdmPulseTmax_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 14),
    _CxMcVoxAdmPulseTmax_Type()
)
cxMcVoxAdmPulseTmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmPulseTmax.setStatus("mandatory")


class _CxMcVoxAdmPulseInterDigit_Type(Integer32):
    """Custom type cxMcVoxAdmPulseInterDigit based on Integer32"""
    defaultValue = 275

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_CxMcVoxAdmPulseInterDigit_Type.__name__ = "Integer32"
_CxMcVoxAdmPulseInterDigit_Object = MibTableColumn
cxMcVoxAdmPulseInterDigit = _CxMcVoxAdmPulseInterDigit_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 15),
    _CxMcVoxAdmPulseInterDigit_Type()
)
cxMcVoxAdmPulseInterDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmPulseInterDigit.setStatus("mandatory")


class _CxMcVoxAdmDtmfGuard_Type(Integer32):
    """Custom type cxMcVoxAdmDtmfGuard based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxMcVoxAdmDtmfGuard_Type.__name__ = "Integer32"
_CxMcVoxAdmDtmfGuard_Object = MibTableColumn
cxMcVoxAdmDtmfGuard = _CxMcVoxAdmDtmfGuard_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 16),
    _CxMcVoxAdmDtmfGuard_Type()
)
cxMcVoxAdmDtmfGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmDtmfGuard.setStatus("mandatory")


class _CxMcVoxAdmDtmfOpeLevel_Type(Integer32):
    """Custom type cxMcVoxAdmDtmfOpeLevel based on Integer32"""
    defaultValue = 1

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
        *(("minus-25", 1),
          ("minus-28", 2),
          ("minus-31", 3),
          ("minus-34", 4))
    )


_CxMcVoxAdmDtmfOpeLevel_Type.__name__ = "Integer32"
_CxMcVoxAdmDtmfOpeLevel_Object = MibTableColumn
cxMcVoxAdmDtmfOpeLevel = _CxMcVoxAdmDtmfOpeLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 17),
    _CxMcVoxAdmDtmfOpeLevel_Type()
)
cxMcVoxAdmDtmfOpeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmDtmfOpeLevel.setStatus("mandatory")


class _CxMcVoxAdmDtmfTxTimeOn_Type(Integer32):
    """Custom type cxMcVoxAdmDtmfTxTimeOn based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CxMcVoxAdmDtmfTxTimeOn_Type.__name__ = "Integer32"
_CxMcVoxAdmDtmfTxTimeOn_Object = MibTableColumn
cxMcVoxAdmDtmfTxTimeOn = _CxMcVoxAdmDtmfTxTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 18),
    _CxMcVoxAdmDtmfTxTimeOn_Type()
)
cxMcVoxAdmDtmfTxTimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmDtmfTxTimeOn.setStatus("mandatory")


class _CxMcVoxAdmDtmfTxTimeOff_Type(Integer32):
    """Custom type cxMcVoxAdmDtmfTxTimeOff based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CxMcVoxAdmDtmfTxTimeOff_Type.__name__ = "Integer32"
_CxMcVoxAdmDtmfTxTimeOff_Object = MibTableColumn
cxMcVoxAdmDtmfTxTimeOff = _CxMcVoxAdmDtmfTxTimeOff_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 19),
    _CxMcVoxAdmDtmfTxTimeOff_Type()
)
cxMcVoxAdmDtmfTxTimeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmDtmfTxTimeOff.setStatus("mandatory")


class _CxMcVoxAdmFlashTmin_Type(Integer32):
    """Custom type cxMcVoxAdmFlashTmin based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_CxMcVoxAdmFlashTmin_Type.__name__ = "Integer32"
_CxMcVoxAdmFlashTmin_Object = MibTableColumn
cxMcVoxAdmFlashTmin = _CxMcVoxAdmFlashTmin_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 20),
    _CxMcVoxAdmFlashTmin_Type()
)
cxMcVoxAdmFlashTmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFlashTmin.setStatus("mandatory")


class _CxMcVoxAdmFlashTmax_Type(Integer32):
    """Custom type cxMcVoxAdmFlashTmax based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_CxMcVoxAdmFlashTmax_Type.__name__ = "Integer32"
_CxMcVoxAdmFlashTmax_Object = MibTableColumn
cxMcVoxAdmFlashTmax = _CxMcVoxAdmFlashTmax_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 21),
    _CxMcVoxAdmFlashTmax_Type()
)
cxMcVoxAdmFlashTmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFlashTmax.setStatus("mandatory")


class _CxMcVoxAdmFlashTgen_Type(Integer32):
    """Custom type cxMcVoxAdmFlashTgen based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_CxMcVoxAdmFlashTgen_Type.__name__ = "Integer32"
_CxMcVoxAdmFlashTgen_Object = MibTableColumn
cxMcVoxAdmFlashTgen = _CxMcVoxAdmFlashTgen_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 22),
    _CxMcVoxAdmFlashTgen_Type()
)
cxMcVoxAdmFlashTgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFlashTgen.setStatus("mandatory")


class _CxMcVoxAdmAfterToneSilences_Type(Integer32):
    """Custom type cxMcVoxAdmAfterToneSilences based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CxMcVoxAdmAfterToneSilences_Type.__name__ = "Integer32"
_CxMcVoxAdmAfterToneSilences_Object = MibTableColumn
cxMcVoxAdmAfterToneSilences = _CxMcVoxAdmAfterToneSilences_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 23),
    _CxMcVoxAdmAfterToneSilences_Type()
)
cxMcVoxAdmAfterToneSilences.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmAfterToneSilences.setStatus("mandatory")


class _CxMcVoxAdmFaxTxGain_Type(Integer32):
    """Custom type cxMcVoxAdmFaxTxGain based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxAdmFaxTxGain_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxTxGain_Object = MibTableColumn
cxMcVoxAdmFaxTxGain = _CxMcVoxAdmFaxTxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 24),
    _CxMcVoxAdmFaxTxGain_Type()
)
cxMcVoxAdmFaxTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxTxGain.setStatus("mandatory")


class _CxMcVoxAdmFaxRxGain_Type(Integer32):
    """Custom type cxMcVoxAdmFaxRxGain based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxAdmFaxRxGain_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxRxGain_Object = MibTableColumn
cxMcVoxAdmFaxRxGain = _CxMcVoxAdmFaxRxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 25),
    _CxMcVoxAdmFaxRxGain_Type()
)
cxMcVoxAdmFaxRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxRxGain.setStatus("mandatory")


class _CxMcVoxAdmFaxHdlcFlags_Type(Integer32):
    """Custom type cxMcVoxAdmFaxHdlcFlags based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CxMcVoxAdmFaxHdlcFlags_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxHdlcFlags_Object = MibTableColumn
cxMcVoxAdmFaxHdlcFlags = _CxMcVoxAdmFaxHdlcFlags_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 26),
    _CxMcVoxAdmFaxHdlcFlags_Type()
)
cxMcVoxAdmFaxHdlcFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxHdlcFlags.setStatus("mandatory")


class _CxMcVoxAdmFaxPreambleDuration_Type(Integer32):
    """Custom type cxMcVoxAdmFaxPreambleDuration based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxAdmFaxPreambleDuration_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxPreambleDuration_Object = MibTableColumn
cxMcVoxAdmFaxPreambleDuration = _CxMcVoxAdmFaxPreambleDuration_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 27),
    _CxMcVoxAdmFaxPreambleDuration_Type()
)
cxMcVoxAdmFaxPreambleDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxPreambleDuration.setStatus("deprecated")


class _CxMcVoxAdmFaxPreambleDelay_Type(Integer32):
    """Custom type cxMcVoxAdmFaxPreambleDelay based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxAdmFaxPreambleDelay_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxPreambleDelay_Object = MibTableColumn
cxMcVoxAdmFaxPreambleDelay = _CxMcVoxAdmFaxPreambleDelay_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 28),
    _CxMcVoxAdmFaxPreambleDelay_Type()
)
cxMcVoxAdmFaxPreambleDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxPreambleDelay.setStatus("deprecated")


class _CxMcVoxAdmFaxCedToneDuration_Type(Integer32):
    """Custom type cxMcVoxAdmFaxCedToneDuration based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxAdmFaxCedToneDuration_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxCedToneDuration_Object = MibTableColumn
cxMcVoxAdmFaxCedToneDuration = _CxMcVoxAdmFaxCedToneDuration_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 29),
    _CxMcVoxAdmFaxCedToneDuration_Type()
)
cxMcVoxAdmFaxCedToneDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxCedToneDuration.setStatus("deprecated")


class _CxMcVoxAdmFaxInterProtoGap_Type(Integer32):
    """Custom type cxMcVoxAdmFaxInterProtoGap based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxAdmFaxInterProtoGap_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxInterProtoGap_Object = MibTableColumn
cxMcVoxAdmFaxInterProtoGap = _CxMcVoxAdmFaxInterProtoGap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 30),
    _CxMcVoxAdmFaxInterProtoGap_Type()
)
cxMcVoxAdmFaxInterProtoGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxInterProtoGap.setStatus("mandatory")


class _CxMcVoxAdmFaxTimerDetectSync_Type(Integer32):
    """Custom type cxMcVoxAdmFaxTimerDetectSync based on Integer32"""
    defaultValue = 7500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_CxMcVoxAdmFaxTimerDetectSync_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxTimerDetectSync_Object = MibTableColumn
cxMcVoxAdmFaxTimerDetectSync = _CxMcVoxAdmFaxTimerDetectSync_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 31),
    _CxMcVoxAdmFaxTimerDetectSync_Type()
)
cxMcVoxAdmFaxTimerDetectSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxTimerDetectSync.setStatus("mandatory")


class _CxMcVoxAdmFaxTimerWaitId_Type(Integer32):
    """Custom type cxMcVoxAdmFaxTimerWaitId based on Integer32"""
    defaultValue = 40000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_CxMcVoxAdmFaxTimerWaitId_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxTimerWaitId_Object = MibTableColumn
cxMcVoxAdmFaxTimerWaitId = _CxMcVoxAdmFaxTimerWaitId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 32),
    _CxMcVoxAdmFaxTimerWaitId_Type()
)
cxMcVoxAdmFaxTimerWaitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxTimerWaitId.setStatus("mandatory")


class _CxMcVoxAdmFaxMinPreambleDur_Type(Integer32):
    """Custom type cxMcVoxAdmFaxMinPreambleDur based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxAdmFaxMinPreambleDur_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxMinPreambleDur_Object = MibTableColumn
cxMcVoxAdmFaxMinPreambleDur = _CxMcVoxAdmFaxMinPreambleDur_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 33),
    _CxMcVoxAdmFaxMinPreambleDur_Type()
)
cxMcVoxAdmFaxMinPreambleDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxMinPreambleDur.setStatus("mandatory")


class _CxMcVoxAdmFaxMaxPreambleDur_Type(Integer32):
    """Custom type cxMcVoxAdmFaxMaxPreambleDur based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxAdmFaxMaxPreambleDur_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxMaxPreambleDur_Object = MibTableColumn
cxMcVoxAdmFaxMaxPreambleDur = _CxMcVoxAdmFaxMaxPreambleDur_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 34),
    _CxMcVoxAdmFaxMaxPreambleDur_Type()
)
cxMcVoxAdmFaxMaxPreambleDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxMaxPreambleDur.setStatus("mandatory")


class _CxMcVoxAdmFaxMinPreambleDly_Type(Integer32):
    """Custom type cxMcVoxAdmFaxMinPreambleDly based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxAdmFaxMinPreambleDly_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxMinPreambleDly_Object = MibTableColumn
cxMcVoxAdmFaxMinPreambleDly = _CxMcVoxAdmFaxMinPreambleDly_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 35),
    _CxMcVoxAdmFaxMinPreambleDly_Type()
)
cxMcVoxAdmFaxMinPreambleDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxMinPreambleDly.setStatus("mandatory")


class _CxMcVoxAdmFaxMaxPreambleDly_Type(Integer32):
    """Custom type cxMcVoxAdmFaxMaxPreambleDly based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxAdmFaxMaxPreambleDly_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxMaxPreambleDly_Object = MibTableColumn
cxMcVoxAdmFaxMaxPreambleDly = _CxMcVoxAdmFaxMaxPreambleDly_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 36),
    _CxMcVoxAdmFaxMaxPreambleDly_Type()
)
cxMcVoxAdmFaxMaxPreambleDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxMaxPreambleDly.setStatus("mandatory")


class _CxMcVoxAdmFaxCedToneDetection_Type(Integer32):
    """Custom type cxMcVoxAdmFaxCedToneDetection based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxAdmFaxCedToneDetection_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxCedToneDetection_Object = MibTableColumn
cxMcVoxAdmFaxCedToneDetection = _CxMcVoxAdmFaxCedToneDetection_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 37),
    _CxMcVoxAdmFaxCedToneDetection_Type()
)
cxMcVoxAdmFaxCedToneDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxCedToneDetection.setStatus("mandatory")


class _CxMcVoxAdmFaxCedMinToneDur_Type(Integer32):
    """Custom type cxMcVoxAdmFaxCedMinToneDur based on Integer32"""
    defaultValue = 2600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxAdmFaxCedMinToneDur_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxCedMinToneDur_Object = MibTableColumn
cxMcVoxAdmFaxCedMinToneDur = _CxMcVoxAdmFaxCedMinToneDur_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 38),
    _CxMcVoxAdmFaxCedMinToneDur_Type()
)
cxMcVoxAdmFaxCedMinToneDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxCedMinToneDur.setStatus("mandatory")


class _CxMcVoxAdmFaxCedMaxToneDur_Type(Integer32):
    """Custom type cxMcVoxAdmFaxCedMaxToneDur based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxAdmFaxCedMaxToneDur_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxCedMaxToneDur_Object = MibTableColumn
cxMcVoxAdmFaxCedMaxToneDur = _CxMcVoxAdmFaxCedMaxToneDur_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 39),
    _CxMcVoxAdmFaxCedMaxToneDur_Type()
)
cxMcVoxAdmFaxCedMaxToneDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxCedMaxToneDur.setStatus("mandatory")


class _CxMcVoxAdmFaxMaxHdlcFlags_Type(Integer32):
    """Custom type cxMcVoxAdmFaxMaxHdlcFlags based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CxMcVoxAdmFaxMaxHdlcFlags_Type.__name__ = "Integer32"
_CxMcVoxAdmFaxMaxHdlcFlags_Object = MibTableColumn
cxMcVoxAdmFaxMaxHdlcFlags = _CxMcVoxAdmFaxMaxHdlcFlags_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 20, 1, 1, 40),
    _CxMcVoxAdmFaxMaxHdlcFlags_Type()
)
cxMcVoxAdmFaxMaxHdlcFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxAdmFaxMaxHdlcFlags.setStatus("mandatory")
_CxMcVoxDriverOpePriv_ObjectIdentity = ObjectIdentity
cxMcVoxDriverOpePriv = _CxMcVoxDriverOpePriv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21)
)
_CxMcVoxOpePortPrivTable_Object = MibTable
cxMcVoxOpePortPrivTable = _CxMcVoxOpePortPrivTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1)
)
if mibBuilder.loadTexts:
    cxMcVoxOpePortPrivTable.setStatus("mandatory")
_CxMcVoxOpePortPrivEntry_Object = MibTableRow
cxMcVoxOpePortPrivEntry = _CxMcVoxOpePortPrivEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1)
)
cxMcVoxOpePortPrivEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxOpeCardUsed"),
    (0, "CXMCVOX-MIB", "cxMcVoxOpePortUsed"),
)
if mibBuilder.loadTexts:
    cxMcVoxOpePortPrivEntry.setStatus("mandatory")


class _CxMcVoxOpeCardUsed_Type(Integer32):
    """Custom type cxMcVoxOpeCardUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CxMcVoxOpeCardUsed_Type.__name__ = "Integer32"
_CxMcVoxOpeCardUsed_Object = MibTableColumn
cxMcVoxOpeCardUsed = _CxMcVoxOpeCardUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 1),
    _CxMcVoxOpeCardUsed_Type()
)
cxMcVoxOpeCardUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeCardUsed.setStatus("mandatory")


class _CxMcVoxOpePortUsed_Type(Integer32):
    """Custom type cxMcVoxOpePortUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CxMcVoxOpePortUsed_Type.__name__ = "Integer32"
_CxMcVoxOpePortUsed_Object = MibTableColumn
cxMcVoxOpePortUsed = _CxMcVoxOpePortUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 2),
    _CxMcVoxOpePortUsed_Type()
)
cxMcVoxOpePortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpePortUsed.setStatus("mandatory")


class _CxMcVoxOpeRingTimeOn_Type(Integer32):
    """Custom type cxMcVoxOpeRingTimeOn based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CxMcVoxOpeRingTimeOn_Type.__name__ = "Integer32"
_CxMcVoxOpeRingTimeOn_Object = MibTableColumn
cxMcVoxOpeRingTimeOn = _CxMcVoxOpeRingTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 3),
    _CxMcVoxOpeRingTimeOn_Type()
)
cxMcVoxOpeRingTimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeRingTimeOn.setStatus("mandatory")


class _CxMcVoxOpeRingTimeOff1_Type(Integer32):
    """Custom type cxMcVoxOpeRingTimeOff1 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CxMcVoxOpeRingTimeOff1_Type.__name__ = "Integer32"
_CxMcVoxOpeRingTimeOff1_Object = MibTableColumn
cxMcVoxOpeRingTimeOff1 = _CxMcVoxOpeRingTimeOff1_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 4),
    _CxMcVoxOpeRingTimeOff1_Type()
)
cxMcVoxOpeRingTimeOff1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeRingTimeOff1.setStatus("mandatory")


class _CxMcVoxOpeRingTimeOff2_Type(Integer32):
    """Custom type cxMcVoxOpeRingTimeOff2 based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CxMcVoxOpeRingTimeOff2_Type.__name__ = "Integer32"
_CxMcVoxOpeRingTimeOff2_Object = MibTableColumn
cxMcVoxOpeRingTimeOff2 = _CxMcVoxOpeRingTimeOff2_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 5),
    _CxMcVoxOpeRingTimeOff2_Type()
)
cxMcVoxOpeRingTimeOff2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeRingTimeOff2.setStatus("mandatory")


class _CxMcVoxOpeEchoCancelLevel_Type(Integer32):
    """Custom type cxMcVoxOpeEchoCancelLevel based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CxMcVoxOpeEchoCancelLevel_Type.__name__ = "Integer32"
_CxMcVoxOpeEchoCancelLevel_Object = MibTableColumn
cxMcVoxOpeEchoCancelLevel = _CxMcVoxOpeEchoCancelLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 6),
    _CxMcVoxOpeEchoCancelLevel_Type()
)
cxMcVoxOpeEchoCancelLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeEchoCancelLevel.setStatus("mandatory")


class _CxMcVoxOpeToneDelayAfterCnct_Type(Integer32):
    """Custom type cxMcVoxOpeToneDelayAfterCnct based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_CxMcVoxOpeToneDelayAfterCnct_Type.__name__ = "Integer32"
_CxMcVoxOpeToneDelayAfterCnct_Object = MibTableColumn
cxMcVoxOpeToneDelayAfterCnct = _CxMcVoxOpeToneDelayAfterCnct_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 7),
    _CxMcVoxOpeToneDelayAfterCnct_Type()
)
cxMcVoxOpeToneDelayAfterCnct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeToneDelayAfterCnct.setStatus("mandatory")


class _CxMcVoxOpeToneDelayAfterFlash_Type(Integer32):
    """Custom type cxMcVoxOpeToneDelayAfterFlash based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_CxMcVoxOpeToneDelayAfterFlash_Type.__name__ = "Integer32"
_CxMcVoxOpeToneDelayAfterFlash_Object = MibTableColumn
cxMcVoxOpeToneDelayAfterFlash = _CxMcVoxOpeToneDelayAfterFlash_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 8),
    _CxMcVoxOpeToneDelayAfterFlash_Type()
)
cxMcVoxOpeToneDelayAfterFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeToneDelayAfterFlash.setStatus("mandatory")


class _CxMcVoxOpeToneOffsetTxGain_Type(Integer32):
    """Custom type cxMcVoxOpeToneOffsetTxGain based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxOpeToneOffsetTxGain_Type.__name__ = "Integer32"
_CxMcVoxOpeToneOffsetTxGain_Object = MibTableColumn
cxMcVoxOpeToneOffsetTxGain = _CxMcVoxOpeToneOffsetTxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 9),
    _CxMcVoxOpeToneOffsetTxGain_Type()
)
cxMcVoxOpeToneOffsetTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeToneOffsetTxGain.setStatus("mandatory")


class _CxMcVoxOpeVoiceOffsetTxGain_Type(Integer32):
    """Custom type cxMcVoxOpeVoiceOffsetTxGain based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxOpeVoiceOffsetTxGain_Type.__name__ = "Integer32"
_CxMcVoxOpeVoiceOffsetTxGain_Object = MibTableColumn
cxMcVoxOpeVoiceOffsetTxGain = _CxMcVoxOpeVoiceOffsetTxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 10),
    _CxMcVoxOpeVoiceOffsetTxGain_Type()
)
cxMcVoxOpeVoiceOffsetTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeVoiceOffsetTxGain.setStatus("mandatory")


class _CxMcVoxOpeAc15InterDigit_Type(Integer32):
    """Custom type cxMcVoxOpeAc15InterDigit based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeAc15InterDigit_Type.__name__ = "Integer32"
_CxMcVoxOpeAc15InterDigit_Object = MibTableColumn
cxMcVoxOpeAc15InterDigit = _CxMcVoxOpeAc15InterDigit_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 11),
    _CxMcVoxOpeAc15InterDigit_Type()
)
cxMcVoxOpeAc15InterDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeAc15InterDigit.setStatus("mandatory")


class _CxMcVoxOpeMfToneThold_Type(Integer32):
    """Custom type cxMcVoxOpeMfToneThold based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxMcVoxOpeMfToneThold_Type.__name__ = "Integer32"
_CxMcVoxOpeMfToneThold_Object = MibTableColumn
cxMcVoxOpeMfToneThold = _CxMcVoxOpeMfToneThold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 12),
    _CxMcVoxOpeMfToneThold_Type()
)
cxMcVoxOpeMfToneThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeMfToneThold.setStatus("mandatory")


class _CxMcVoxOpePulseTmin_Type(Integer32):
    """Custom type cxMcVoxOpePulseTmin based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_CxMcVoxOpePulseTmin_Type.__name__ = "Integer32"
_CxMcVoxOpePulseTmin_Object = MibTableColumn
cxMcVoxOpePulseTmin = _CxMcVoxOpePulseTmin_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 13),
    _CxMcVoxOpePulseTmin_Type()
)
cxMcVoxOpePulseTmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpePulseTmin.setStatus("mandatory")


class _CxMcVoxOpePulseTmax_Type(Integer32):
    """Custom type cxMcVoxOpePulseTmax based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_CxMcVoxOpePulseTmax_Type.__name__ = "Integer32"
_CxMcVoxOpePulseTmax_Object = MibTableColumn
cxMcVoxOpePulseTmax = _CxMcVoxOpePulseTmax_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 14),
    _CxMcVoxOpePulseTmax_Type()
)
cxMcVoxOpePulseTmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpePulseTmax.setStatus("mandatory")


class _CxMcVoxOpePulseInterDigit_Type(Integer32):
    """Custom type cxMcVoxOpePulseInterDigit based on Integer32"""
    defaultValue = 275

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_CxMcVoxOpePulseInterDigit_Type.__name__ = "Integer32"
_CxMcVoxOpePulseInterDigit_Object = MibTableColumn
cxMcVoxOpePulseInterDigit = _CxMcVoxOpePulseInterDigit_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 15),
    _CxMcVoxOpePulseInterDigit_Type()
)
cxMcVoxOpePulseInterDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpePulseInterDigit.setStatus("mandatory")


class _CxMcVoxOpeDtmfGuard_Type(Integer32):
    """Custom type cxMcVoxOpeDtmfGuard based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxMcVoxOpeDtmfGuard_Type.__name__ = "Integer32"
_CxMcVoxOpeDtmfGuard_Object = MibTableColumn
cxMcVoxOpeDtmfGuard = _CxMcVoxOpeDtmfGuard_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 16),
    _CxMcVoxOpeDtmfGuard_Type()
)
cxMcVoxOpeDtmfGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeDtmfGuard.setStatus("mandatory")


class _CxMcVoxOpeDtmfOpeLevel_Type(Integer32):
    """Custom type cxMcVoxOpeDtmfOpeLevel based on Integer32"""
    defaultValue = 1

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
        *(("minus-25", 1),
          ("minus-28", 2),
          ("minus-31", 3),
          ("minus-34", 4))
    )


_CxMcVoxOpeDtmfOpeLevel_Type.__name__ = "Integer32"
_CxMcVoxOpeDtmfOpeLevel_Object = MibTableColumn
cxMcVoxOpeDtmfOpeLevel = _CxMcVoxOpeDtmfOpeLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 17),
    _CxMcVoxOpeDtmfOpeLevel_Type()
)
cxMcVoxOpeDtmfOpeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeDtmfOpeLevel.setStatus("mandatory")


class _CxMcVoxOpeDtmfTxTimeOn_Type(Integer32):
    """Custom type cxMcVoxOpeDtmfTxTimeOn based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CxMcVoxOpeDtmfTxTimeOn_Type.__name__ = "Integer32"
_CxMcVoxOpeDtmfTxTimeOn_Object = MibTableColumn
cxMcVoxOpeDtmfTxTimeOn = _CxMcVoxOpeDtmfTxTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 18),
    _CxMcVoxOpeDtmfTxTimeOn_Type()
)
cxMcVoxOpeDtmfTxTimeOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeDtmfTxTimeOn.setStatus("mandatory")


class _CxMcVoxOpeDtmfTxTimeOff_Type(Integer32):
    """Custom type cxMcVoxOpeDtmfTxTimeOff based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CxMcVoxOpeDtmfTxTimeOff_Type.__name__ = "Integer32"
_CxMcVoxOpeDtmfTxTimeOff_Object = MibTableColumn
cxMcVoxOpeDtmfTxTimeOff = _CxMcVoxOpeDtmfTxTimeOff_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 19),
    _CxMcVoxOpeDtmfTxTimeOff_Type()
)
cxMcVoxOpeDtmfTxTimeOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeDtmfTxTimeOff.setStatus("mandatory")


class _CxMcVoxOpeFlashTmin_Type(Integer32):
    """Custom type cxMcVoxOpeFlashTmin based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_CxMcVoxOpeFlashTmin_Type.__name__ = "Integer32"
_CxMcVoxOpeFlashTmin_Object = MibTableColumn
cxMcVoxOpeFlashTmin = _CxMcVoxOpeFlashTmin_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 20),
    _CxMcVoxOpeFlashTmin_Type()
)
cxMcVoxOpeFlashTmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFlashTmin.setStatus("mandatory")


class _CxMcVoxOpeFlashTmax_Type(Integer32):
    """Custom type cxMcVoxOpeFlashTmax based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_CxMcVoxOpeFlashTmax_Type.__name__ = "Integer32"
_CxMcVoxOpeFlashTmax_Object = MibTableColumn
cxMcVoxOpeFlashTmax = _CxMcVoxOpeFlashTmax_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 21),
    _CxMcVoxOpeFlashTmax_Type()
)
cxMcVoxOpeFlashTmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFlashTmax.setStatus("mandatory")


class _CxMcVoxOpeFlashTgen_Type(Integer32):
    """Custom type cxMcVoxOpeFlashTgen based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_CxMcVoxOpeFlashTgen_Type.__name__ = "Integer32"
_CxMcVoxOpeFlashTgen_Object = MibTableColumn
cxMcVoxOpeFlashTgen = _CxMcVoxOpeFlashTgen_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 22),
    _CxMcVoxOpeFlashTgen_Type()
)
cxMcVoxOpeFlashTgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFlashTgen.setStatus("mandatory")


class _CxMcVoxOpeAfterToneSilences_Type(Integer32):
    """Custom type cxMcVoxOpeAfterToneSilences based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CxMcVoxOpeAfterToneSilences_Type.__name__ = "Integer32"
_CxMcVoxOpeAfterToneSilences_Object = MibTableColumn
cxMcVoxOpeAfterToneSilences = _CxMcVoxOpeAfterToneSilences_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 23),
    _CxMcVoxOpeAfterToneSilences_Type()
)
cxMcVoxOpeAfterToneSilences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeAfterToneSilences.setStatus("mandatory")


class _CxMcVoxOpeFaxTxGain_Type(Integer32):
    """Custom type cxMcVoxOpeFaxTxGain based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxOpeFaxTxGain_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxTxGain_Object = MibTableColumn
cxMcVoxOpeFaxTxGain = _CxMcVoxOpeFaxTxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 24),
    _CxMcVoxOpeFaxTxGain_Type()
)
cxMcVoxOpeFaxTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxTxGain.setStatus("mandatory")


class _CxMcVoxOpeFaxRxGain_Type(Integer32):
    """Custom type cxMcVoxOpeFaxRxGain based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(820, 1180),
    )


_CxMcVoxOpeFaxRxGain_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxRxGain_Object = MibTableColumn
cxMcVoxOpeFaxRxGain = _CxMcVoxOpeFaxRxGain_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 25),
    _CxMcVoxOpeFaxRxGain_Type()
)
cxMcVoxOpeFaxRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxRxGain.setStatus("mandatory")


class _CxMcVoxOpeFaxHdlcFlags_Type(Integer32):
    """Custom type cxMcVoxOpeFaxHdlcFlags based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CxMcVoxOpeFaxHdlcFlags_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxHdlcFlags_Object = MibTableColumn
cxMcVoxOpeFaxHdlcFlags = _CxMcVoxOpeFaxHdlcFlags_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 26),
    _CxMcVoxOpeFaxHdlcFlags_Type()
)
cxMcVoxOpeFaxHdlcFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxHdlcFlags.setStatus("mandatory")


class _CxMcVoxOpeFaxPreambleDuration_Type(Integer32):
    """Custom type cxMcVoxOpeFaxPreambleDuration based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeFaxPreambleDuration_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxPreambleDuration_Object = MibTableColumn
cxMcVoxOpeFaxPreambleDuration = _CxMcVoxOpeFaxPreambleDuration_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 27),
    _CxMcVoxOpeFaxPreambleDuration_Type()
)
cxMcVoxOpeFaxPreambleDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxPreambleDuration.setStatus("deprecated")


class _CxMcVoxOpeFaxPreambleDelay_Type(Integer32):
    """Custom type cxMcVoxOpeFaxPreambleDelay based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeFaxPreambleDelay_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxPreambleDelay_Object = MibTableColumn
cxMcVoxOpeFaxPreambleDelay = _CxMcVoxOpeFaxPreambleDelay_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 28),
    _CxMcVoxOpeFaxPreambleDelay_Type()
)
cxMcVoxOpeFaxPreambleDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxPreambleDelay.setStatus("deprecated")


class _CxMcVoxOpeFaxCedToneDuration_Type(Integer32):
    """Custom type cxMcVoxOpeFaxCedToneDuration based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeFaxCedToneDuration_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxCedToneDuration_Object = MibTableColumn
cxMcVoxOpeFaxCedToneDuration = _CxMcVoxOpeFaxCedToneDuration_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 29),
    _CxMcVoxOpeFaxCedToneDuration_Type()
)
cxMcVoxOpeFaxCedToneDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxCedToneDuration.setStatus("deprecated")


class _CxMcVoxOpeFaxInterProtoGap_Type(Integer32):
    """Custom type cxMcVoxOpeFaxInterProtoGap based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeFaxInterProtoGap_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxInterProtoGap_Object = MibTableColumn
cxMcVoxOpeFaxInterProtoGap = _CxMcVoxOpeFaxInterProtoGap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 30),
    _CxMcVoxOpeFaxInterProtoGap_Type()
)
cxMcVoxOpeFaxInterProtoGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxInterProtoGap.setStatus("mandatory")


class _CxMcVoxOpeFaxTimerDetectSync_Type(Integer32):
    """Custom type cxMcVoxOpeFaxTimerDetectSync based on Integer32"""
    defaultValue = 7500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_CxMcVoxOpeFaxTimerDetectSync_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxTimerDetectSync_Object = MibTableColumn
cxMcVoxOpeFaxTimerDetectSync = _CxMcVoxOpeFaxTimerDetectSync_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 31),
    _CxMcVoxOpeFaxTimerDetectSync_Type()
)
cxMcVoxOpeFaxTimerDetectSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxTimerDetectSync.setStatus("mandatory")


class _CxMcVoxOpeFaxTimerWaitId_Type(Integer32):
    """Custom type cxMcVoxOpeFaxTimerWaitId based on Integer32"""
    defaultValue = 40000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_CxMcVoxOpeFaxTimerWaitId_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxTimerWaitId_Object = MibTableColumn
cxMcVoxOpeFaxTimerWaitId = _CxMcVoxOpeFaxTimerWaitId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 32),
    _CxMcVoxOpeFaxTimerWaitId_Type()
)
cxMcVoxOpeFaxTimerWaitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxTimerWaitId.setStatus("mandatory")


class _CxMcVoxOpeFaxMinPreambleDur_Type(Integer32):
    """Custom type cxMcVoxOpeFaxMinPreambleDur based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeFaxMinPreambleDur_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxMinPreambleDur_Object = MibTableColumn
cxMcVoxOpeFaxMinPreambleDur = _CxMcVoxOpeFaxMinPreambleDur_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 33),
    _CxMcVoxOpeFaxMinPreambleDur_Type()
)
cxMcVoxOpeFaxMinPreambleDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxMinPreambleDur.setStatus("mandatory")


class _CxMcVoxOpeFaxMaxPreambleDur_Type(Integer32):
    """Custom type cxMcVoxOpeFaxMaxPreambleDur based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeFaxMaxPreambleDur_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxMaxPreambleDur_Object = MibTableColumn
cxMcVoxOpeFaxMaxPreambleDur = _CxMcVoxOpeFaxMaxPreambleDur_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 34),
    _CxMcVoxOpeFaxMaxPreambleDur_Type()
)
cxMcVoxOpeFaxMaxPreambleDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxMaxPreambleDur.setStatus("mandatory")


class _CxMcVoxOpeFaxMinPreambleDly_Type(Integer32):
    """Custom type cxMcVoxOpeFaxMinPreambleDly based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeFaxMinPreambleDly_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxMinPreambleDly_Object = MibTableColumn
cxMcVoxOpeFaxMinPreambleDly = _CxMcVoxOpeFaxMinPreambleDly_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 35),
    _CxMcVoxOpeFaxMinPreambleDly_Type()
)
cxMcVoxOpeFaxMinPreambleDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxMinPreambleDly.setStatus("mandatory")


class _CxMcVoxOpeFaxMaxPreambleDly_Type(Integer32):
    """Custom type cxMcVoxOpeFaxMaxPreambleDly based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeFaxMaxPreambleDly_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxMaxPreambleDly_Object = MibTableColumn
cxMcVoxOpeFaxMaxPreambleDly = _CxMcVoxOpeFaxMaxPreambleDly_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 36),
    _CxMcVoxOpeFaxMaxPreambleDly_Type()
)
cxMcVoxOpeFaxMaxPreambleDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxMaxPreambleDly.setStatus("mandatory")


class _CxMcVoxOpeFaxCedToneDetection_Type(Integer32):
    """Custom type cxMcVoxOpeFaxCedToneDetection based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeFaxCedToneDetection_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxCedToneDetection_Object = MibTableColumn
cxMcVoxOpeFaxCedToneDetection = _CxMcVoxOpeFaxCedToneDetection_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 37),
    _CxMcVoxOpeFaxCedToneDetection_Type()
)
cxMcVoxOpeFaxCedToneDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxCedToneDetection.setStatus("mandatory")


class _CxMcVoxOpeFaxCedMinToneDur_Type(Integer32):
    """Custom type cxMcVoxOpeFaxCedMinToneDur based on Integer32"""
    defaultValue = 2600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeFaxCedMinToneDur_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxCedMinToneDur_Object = MibTableColumn
cxMcVoxOpeFaxCedMinToneDur = _CxMcVoxOpeFaxCedMinToneDur_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 38),
    _CxMcVoxOpeFaxCedMinToneDur_Type()
)
cxMcVoxOpeFaxCedMinToneDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxCedMinToneDur.setStatus("mandatory")


class _CxMcVoxOpeFaxCedMaxToneDur_Type(Integer32):
    """Custom type cxMcVoxOpeFaxCedMaxToneDur based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeFaxCedMaxToneDur_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxCedMaxToneDur_Object = MibTableColumn
cxMcVoxOpeFaxCedMaxToneDur = _CxMcVoxOpeFaxCedMaxToneDur_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 39),
    _CxMcVoxOpeFaxCedMaxToneDur_Type()
)
cxMcVoxOpeFaxCedMaxToneDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxCedMaxToneDur.setStatus("mandatory")


class _CxMcVoxOpeFaxMaxHdlcFlags_Type(Integer32):
    """Custom type cxMcVoxOpeFaxMaxHdlcFlags based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CxMcVoxOpeFaxMaxHdlcFlags_Type.__name__ = "Integer32"
_CxMcVoxOpeFaxMaxHdlcFlags_Object = MibTableColumn
cxMcVoxOpeFaxMaxHdlcFlags = _CxMcVoxOpeFaxMaxHdlcFlags_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 21, 1, 1, 40),
    _CxMcVoxOpeFaxMaxHdlcFlags_Type()
)
cxMcVoxOpeFaxMaxHdlcFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeFaxMaxHdlcFlags.setStatus("mandatory")
_CxMcVoxTimerOpePriv_ObjectIdentity = ObjectIdentity
cxMcVoxTimerOpePriv = _CxMcVoxTimerOpePriv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23)
)
_CxMcVoxOpeTimerPrivTable_Object = MibTable
cxMcVoxOpeTimerPrivTable = _CxMcVoxOpeTimerPrivTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1)
)
if mibBuilder.loadTexts:
    cxMcVoxOpeTimerPrivTable.setStatus("mandatory")
_CxMcVoxOpeTimerPrivEntry_Object = MibTableRow
cxMcVoxOpeTimerPrivEntry = _CxMcVoxOpeTimerPrivEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1)
)
cxMcVoxOpeTimerPrivEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxOpeInterfaceType"),
)
if mibBuilder.loadTexts:
    cxMcVoxOpeTimerPrivEntry.setStatus("mandatory")


class _CxMcVoxOpeInterfaceType_Type(Integer32):
    """Custom type cxMcVoxOpeInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("em", 1),
          ("fxo", 3),
          ("fxs", 2))
    )


_CxMcVoxOpeInterfaceType_Type.__name__ = "Integer32"
_CxMcVoxOpeInterfaceType_Object = MibTableColumn
cxMcVoxOpeInterfaceType = _CxMcVoxOpeInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 1),
    _CxMcVoxOpeInterfaceType_Type()
)
cxMcVoxOpeInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxOpeInterfaceType.setStatus("mandatory")


class _CxMcVoxOpeTimeSeizeIn_Type(Integer32):
    """Custom type cxMcVoxOpeTimeSeizeIn based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeSeizeIn_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeSeizeIn_Object = MibTableColumn
cxMcVoxOpeTimeSeizeIn = _CxMcVoxOpeTimeSeizeIn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 2),
    _CxMcVoxOpeTimeSeizeIn_Type()
)
cxMcVoxOpeTimeSeizeIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeSeizeIn.setStatus("mandatory")


class _CxMcVoxOpeTimeWaitDialOut_Type(Integer32):
    """Custom type cxMcVoxOpeTimeWaitDialOut based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeWaitDialOut_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeWaitDialOut_Object = MibTableColumn
cxMcVoxOpeTimeWaitDialOut = _CxMcVoxOpeTimeWaitDialOut_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 3),
    _CxMcVoxOpeTimeWaitDialOut_Type()
)
cxMcVoxOpeTimeWaitDialOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeWaitDialOut.setStatus("mandatory")


class _CxMcVoxOpeTimeWaitDialIn_Type(Integer32):
    """Custom type cxMcVoxOpeTimeWaitDialIn based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeWaitDialIn_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeWaitDialIn_Object = MibTableColumn
cxMcVoxOpeTimeWaitDialIn = _CxMcVoxOpeTimeWaitDialIn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 4),
    _CxMcVoxOpeTimeWaitDialIn_Type()
)
cxMcVoxOpeTimeWaitDialIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeWaitDialIn.setStatus("mandatory")


class _CxMcVoxOpeTimeDialOut_Type(Integer32):
    """Custom type cxMcVoxOpeTimeDialOut based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeDialOut_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeDialOut_Object = MibTableColumn
cxMcVoxOpeTimeDialOut = _CxMcVoxOpeTimeDialOut_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 5),
    _CxMcVoxOpeTimeDialOut_Type()
)
cxMcVoxOpeTimeDialOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeDialOut.setStatus("mandatory")


class _CxMcVoxOpeTimeDialIn_Type(Integer32):
    """Custom type cxMcVoxOpeTimeDialIn based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeDialIn_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeDialIn_Object = MibTableColumn
cxMcVoxOpeTimeDialIn = _CxMcVoxOpeTimeDialIn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 6),
    _CxMcVoxOpeTimeDialIn_Type()
)
cxMcVoxOpeTimeDialIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeDialIn.setStatus("mandatory")


class _CxMcVoxOpeTimeSiOff_Type(Integer32):
    """Custom type cxMcVoxOpeTimeSiOff based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeSiOff_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeSiOff_Object = MibTableColumn
cxMcVoxOpeTimeSiOff = _CxMcVoxOpeTimeSiOff_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 7),
    _CxMcVoxOpeTimeSiOff_Type()
)
cxMcVoxOpeTimeSiOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeSiOff.setStatus("mandatory")


class _CxMcVoxOpeTimeProceed_Type(Integer32):
    """Custom type cxMcVoxOpeTimeProceed based on Integer32"""
    defaultValue = 30000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeProceed_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeProceed_Object = MibTableColumn
cxMcVoxOpeTimeProceed = _CxMcVoxOpeTimeProceed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 8),
    _CxMcVoxOpeTimeProceed_Type()
)
cxMcVoxOpeTimeProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeProceed.setStatus("mandatory")


class _CxMcVoxOpeTimeAnswer_Type(Integer32):
    """Custom type cxMcVoxOpeTimeAnswer based on Integer32"""
    defaultValue = 60000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeAnswer_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeAnswer_Object = MibTableColumn
cxMcVoxOpeTimeAnswer = _CxMcVoxOpeTimeAnswer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 9),
    _CxMcVoxOpeTimeAnswer_Type()
)
cxMcVoxOpeTimeAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeAnswer.setStatus("mandatory")


class _CxMcVoxOpeTimeBeforeToneOff_Type(Integer32):
    """Custom type cxMcVoxOpeTimeBeforeToneOff based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeBeforeToneOff_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeBeforeToneOff_Object = MibTableColumn
cxMcVoxOpeTimeBeforeToneOff = _CxMcVoxOpeTimeBeforeToneOff_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 10),
    _CxMcVoxOpeTimeBeforeToneOff_Type()
)
cxMcVoxOpeTimeBeforeToneOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeBeforeToneOff.setStatus("mandatory")


class _CxMcVoxOpeTimeWinkStartIn_Type(Integer32):
    """Custom type cxMcVoxOpeTimeWinkStartIn based on Integer32"""
    defaultValue = 220

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeWinkStartIn_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeWinkStartIn_Object = MibTableColumn
cxMcVoxOpeTimeWinkStartIn = _CxMcVoxOpeTimeWinkStartIn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 11),
    _CxMcVoxOpeTimeWinkStartIn_Type()
)
cxMcVoxOpeTimeWinkStartIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeWinkStartIn.setStatus("mandatory")


class _CxMcVoxOpeTimeWinkStartOut_Type(Integer32):
    """Custom type cxMcVoxOpeTimeWinkStartOut based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeWinkStartOut_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeWinkStartOut_Object = MibTableColumn
cxMcVoxOpeTimeWinkStartOut = _CxMcVoxOpeTimeWinkStartOut_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 12),
    _CxMcVoxOpeTimeWinkStartOut_Type()
)
cxMcVoxOpeTimeWinkStartOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeWinkStartOut.setStatus("mandatory")


class _CxMcVoxOpeTimeWinkMin_Type(Integer32):
    """Custom type cxMcVoxOpeTimeWinkMin based on Integer32"""
    defaultValue = 140

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeWinkMin_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeWinkMin_Object = MibTableColumn
cxMcVoxOpeTimeWinkMin = _CxMcVoxOpeTimeWinkMin_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 13),
    _CxMcVoxOpeTimeWinkMin_Type()
)
cxMcVoxOpeTimeWinkMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeWinkMin.setStatus("mandatory")


class _CxMcVoxOpeTimeWinkMax_Type(Integer32):
    """Custom type cxMcVoxOpeTimeWinkMax based on Integer32"""
    defaultValue = 290

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeWinkMax_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeWinkMax_Object = MibTableColumn
cxMcVoxOpeTimeWinkMax = _CxMcVoxOpeTimeWinkMax_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 14),
    _CxMcVoxOpeTimeWinkMax_Type()
)
cxMcVoxOpeTimeWinkMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeWinkMax.setStatus("mandatory")


class _CxMcVoxOpeTimeSeize_Type(Integer32):
    """Custom type cxMcVoxOpeTimeSeize based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeSeize_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeSeize_Object = MibTableColumn
cxMcVoxOpeTimeSeize = _CxMcVoxOpeTimeSeize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 15),
    _CxMcVoxOpeTimeSeize_Type()
)
cxMcVoxOpeTimeSeize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeSeize.setStatus("mandatory")


class _CxMcVoxOpeTimeDial_Type(Integer32):
    """Custom type cxMcVoxOpeTimeDial based on Integer32"""
    defaultValue = 210

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeDial_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeDial_Object = MibTableColumn
cxMcVoxOpeTimeDial = _CxMcVoxOpeTimeDial_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 16),
    _CxMcVoxOpeTimeDial_Type()
)
cxMcVoxOpeTimeDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeDial.setStatus("mandatory")


class _CxMcVoxOpeTimeOffIn_Type(Integer32):
    """Custom type cxMcVoxOpeTimeOffIn based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeOffIn_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeOffIn_Object = MibTableColumn
cxMcVoxOpeTimeOffIn = _CxMcVoxOpeTimeOffIn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 17),
    _CxMcVoxOpeTimeOffIn_Type()
)
cxMcVoxOpeTimeOffIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeOffIn.setStatus("mandatory")


class _CxMcVoxOpeTimeSiOn_Type(Integer32):
    """Custom type cxMcVoxOpeTimeSiOn based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeSiOn_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeSiOn_Object = MibTableColumn
cxMcVoxOpeTimeSiOn = _CxMcVoxOpeTimeSiOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 18),
    _CxMcVoxOpeTimeSiOn_Type()
)
cxMcVoxOpeTimeSiOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeSiOn.setStatus("mandatory")


class _CxMcVoxOpeTimeOffOut_Type(Integer32):
    """Custom type cxMcVoxOpeTimeOffOut based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeOffOut_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeOffOut_Object = MibTableColumn
cxMcVoxOpeTimeOffOut = _CxMcVoxOpeTimeOffOut_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 19),
    _CxMcVoxOpeTimeOffOut_Type()
)
cxMcVoxOpeTimeOffOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeOffOut.setStatus("mandatory")


class _CxMcVoxOpeTimeDiscIn_Type(Integer32):
    """Custom type cxMcVoxOpeTimeDiscIn based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeDiscIn_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeDiscIn_Object = MibTableColumn
cxMcVoxOpeTimeDiscIn = _CxMcVoxOpeTimeDiscIn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 20),
    _CxMcVoxOpeTimeDiscIn_Type()
)
cxMcVoxOpeTimeDiscIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeDiscIn.setStatus("mandatory")


class _CxMcVoxOpeTimeDiscOut_Type(Integer32):
    """Custom type cxMcVoxOpeTimeDiscOut based on Integer32"""
    defaultValue = 650

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeDiscOut_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeDiscOut_Object = MibTableColumn
cxMcVoxOpeTimeDiscOut = _CxMcVoxOpeTimeDiscOut_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 21),
    _CxMcVoxOpeTimeDiscOut_Type()
)
cxMcVoxOpeTimeDiscOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeDiscOut.setStatus("mandatory")


class _CxMcVoxOpeTimeToneOut_Type(Integer32):
    """Custom type cxMcVoxOpeTimeToneOut based on Integer32"""
    defaultValue = 15000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CxMcVoxOpeTimeToneOut_Type.__name__ = "Integer32"
_CxMcVoxOpeTimeToneOut_Object = MibTableColumn
cxMcVoxOpeTimeToneOut = _CxMcVoxOpeTimeToneOut_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 23, 1, 1, 22),
    _CxMcVoxOpeTimeToneOut_Type()
)
cxMcVoxOpeTimeToneOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxOpeTimeToneOut.setStatus("mandatory")
_CxMcVoxDiagTable_Object = MibTable
cxMcVoxDiagTable = _CxMcVoxDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24)
)
if mibBuilder.loadTexts:
    cxMcVoxDiagTable.setStatus("mandatory")
_CxMcVoxDiagEntry_Object = MibTableRow
cxMcVoxDiagEntry = _CxMcVoxDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1)
)
cxMcVoxDiagEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxDiagCardIndex"),
    (0, "CXMCVOX-MIB", "cxMcVoxDiagPortIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxDiagEntry.setStatus("mandatory")


class _CxMcVoxDiagCardIndex_Type(Integer32):
    """Custom type cxMcVoxDiagCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CxMcVoxDiagCardIndex_Type.__name__ = "Integer32"
_CxMcVoxDiagCardIndex_Object = MibTableColumn
cxMcVoxDiagCardIndex = _CxMcVoxDiagCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 1),
    _CxMcVoxDiagCardIndex_Type()
)
cxMcVoxDiagCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxDiagCardIndex.setStatus("mandatory")


class _CxMcVoxDiagPortIndex_Type(Integer32):
    """Custom type cxMcVoxDiagPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CxMcVoxDiagPortIndex_Type.__name__ = "Integer32"
_CxMcVoxDiagPortIndex_Object = MibTableColumn
cxMcVoxDiagPortIndex = _CxMcVoxDiagPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 2),
    _CxMcVoxDiagPortIndex_Type()
)
cxMcVoxDiagPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxDiagPortIndex.setStatus("mandatory")


class _CxMcVoxDiagScvEvents_Type(Integer32):
    """Custom type cxMcVoxDiagScvEvents based on Integer32"""
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
        *(("no-action", 1),
          ("reset", 3),
          ("trigger", 2))
    )


_CxMcVoxDiagScvEvents_Type.__name__ = "Integer32"
_CxMcVoxDiagScvEvents_Object = MibTableColumn
cxMcVoxDiagScvEvents = _CxMcVoxDiagScvEvents_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 3),
    _CxMcVoxDiagScvEvents_Type()
)
cxMcVoxDiagScvEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxDiagScvEvents.setStatus("mandatory")


class _CxMcVoxDiagGsdEvents_Type(Integer32):
    """Custom type cxMcVoxDiagGsdEvents based on Integer32"""
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
        *(("no-action", 1),
          ("reset", 3),
          ("trigger", 2))
    )


_CxMcVoxDiagGsdEvents_Type.__name__ = "Integer32"
_CxMcVoxDiagGsdEvents_Object = MibTableColumn
cxMcVoxDiagGsdEvents = _CxMcVoxDiagGsdEvents_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 4),
    _CxMcVoxDiagGsdEvents_Type()
)
cxMcVoxDiagGsdEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxDiagGsdEvents.setStatus("mandatory")


class _CxMcVoxDiagToneInEvents_Type(Integer32):
    """Custom type cxMcVoxDiagToneInEvents based on Integer32"""
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
        *(("no-action", 1),
          ("reset", 3),
          ("trigger", 2))
    )


_CxMcVoxDiagToneInEvents_Type.__name__ = "Integer32"
_CxMcVoxDiagToneInEvents_Object = MibTableColumn
cxMcVoxDiagToneInEvents = _CxMcVoxDiagToneInEvents_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 5),
    _CxMcVoxDiagToneInEvents_Type()
)
cxMcVoxDiagToneInEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxDiagToneInEvents.setStatus("mandatory")


class _CxMcVoxDiagToneOutEvents_Type(Integer32):
    """Custom type cxMcVoxDiagToneOutEvents based on Integer32"""
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
        *(("no-action", 1),
          ("reset", 3),
          ("trigger", 2))
    )


_CxMcVoxDiagToneOutEvents_Type.__name__ = "Integer32"
_CxMcVoxDiagToneOutEvents_Object = MibTableColumn
cxMcVoxDiagToneOutEvents = _CxMcVoxDiagToneOutEvents_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 6),
    _CxMcVoxDiagToneOutEvents_Type()
)
cxMcVoxDiagToneOutEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxDiagToneOutEvents.setStatus("mandatory")


class _CxMcVoxDiagFaxInEvents_Type(Integer32):
    """Custom type cxMcVoxDiagFaxInEvents based on Integer32"""
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
        *(("no-action", 1),
          ("reset", 3),
          ("trigger", 2))
    )


_CxMcVoxDiagFaxInEvents_Type.__name__ = "Integer32"
_CxMcVoxDiagFaxInEvents_Object = MibTableColumn
cxMcVoxDiagFaxInEvents = _CxMcVoxDiagFaxInEvents_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 7),
    _CxMcVoxDiagFaxInEvents_Type()
)
cxMcVoxDiagFaxInEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxDiagFaxInEvents.setStatus("mandatory")


class _CxMcVoxDiagFaxOutEvents_Type(Integer32):
    """Custom type cxMcVoxDiagFaxOutEvents based on Integer32"""
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
        *(("no-action", 1),
          ("reset", 3),
          ("trigger", 2))
    )


_CxMcVoxDiagFaxOutEvents_Type.__name__ = "Integer32"
_CxMcVoxDiagFaxOutEvents_Object = MibTableColumn
cxMcVoxDiagFaxOutEvents = _CxMcVoxDiagFaxOutEvents_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 8),
    _CxMcVoxDiagFaxOutEvents_Type()
)
cxMcVoxDiagFaxOutEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxDiagFaxOutEvents.setStatus("mandatory")


class _CxMcVoxDiagGlmEvents_Type(Integer32):
    """Custom type cxMcVoxDiagGlmEvents based on Integer32"""
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
        *(("no-action", 1),
          ("reset", 3),
          ("trigger", 2))
    )


_CxMcVoxDiagGlmEvents_Type.__name__ = "Integer32"
_CxMcVoxDiagGlmEvents_Object = MibTableColumn
cxMcVoxDiagGlmEvents = _CxMcVoxDiagGlmEvents_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 9),
    _CxMcVoxDiagGlmEvents_Type()
)
cxMcVoxDiagGlmEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxDiagGlmEvents.setStatus("mandatory")


class _CxMcVoxDiagIbvDiags_Type(Integer32):
    """Custom type cxMcVoxDiagIbvDiags based on Integer32"""
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
        *(("no-action", 1),
          ("reset", 3),
          ("trigger", 2))
    )


_CxMcVoxDiagIbvDiags_Type.__name__ = "Integer32"
_CxMcVoxDiagIbvDiags_Object = MibTableColumn
cxMcVoxDiagIbvDiags = _CxMcVoxDiagIbvDiags_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 10),
    _CxMcVoxDiagIbvDiags_Type()
)
cxMcVoxDiagIbvDiags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxDiagIbvDiags.setStatus("mandatory")


class _CxMcVoxDiagPcvDiags_Type(Integer32):
    """Custom type cxMcVoxDiagPcvDiags based on Integer32"""
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
        *(("no-action", 1),
          ("reset", 3),
          ("trigger", 2))
    )


_CxMcVoxDiagPcvDiags_Type.__name__ = "Integer32"
_CxMcVoxDiagPcvDiags_Object = MibTableColumn
cxMcVoxDiagPcvDiags = _CxMcVoxDiagPcvDiags_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 11),
    _CxMcVoxDiagPcvDiags_Type()
)
cxMcVoxDiagPcvDiags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxDiagPcvDiags.setStatus("mandatory")


class _CxMcVoxDiagGcvDiags_Type(Integer32):
    """Custom type cxMcVoxDiagGcvDiags based on Integer32"""
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
        *(("no-action", 1),
          ("reset", 3),
          ("trigger", 2))
    )


_CxMcVoxDiagGcvDiags_Type.__name__ = "Integer32"
_CxMcVoxDiagGcvDiags_Object = MibTableColumn
cxMcVoxDiagGcvDiags = _CxMcVoxDiagGcvDiags_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 12),
    _CxMcVoxDiagGcvDiags_Type()
)
cxMcVoxDiagGcvDiags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxDiagGcvDiags.setStatus("mandatory")


class _CxMcVoxDiagFaxDiags_Type(Integer32):
    """Custom type cxMcVoxDiagFaxDiags based on Integer32"""
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
        *(("no-action", 1),
          ("reset", 3),
          ("trigger", 2))
    )


_CxMcVoxDiagFaxDiags_Type.__name__ = "Integer32"
_CxMcVoxDiagFaxDiags_Object = MibTableColumn
cxMcVoxDiagFaxDiags = _CxMcVoxDiagFaxDiags_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 13),
    _CxMcVoxDiagFaxDiags_Type()
)
cxMcVoxDiagFaxDiags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxDiagFaxDiags.setStatus("mandatory")


class _CxMcVoxDiagLseDiags_Type(Integer32):
    """Custom type cxMcVoxDiagLseDiags based on Integer32"""
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
        *(("no-action", 1),
          ("reset", 3),
          ("trigger", 2))
    )


_CxMcVoxDiagLseDiags_Type.__name__ = "Integer32"
_CxMcVoxDiagLseDiags_Object = MibTableColumn
cxMcVoxDiagLseDiags = _CxMcVoxDiagLseDiags_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 14),
    _CxMcVoxDiagLseDiags_Type()
)
cxMcVoxDiagLseDiags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxDiagLseDiags.setStatus("mandatory")


class _CxMcVoxDiagScvDiags_Type(Integer32):
    """Custom type cxMcVoxDiagScvDiags based on Integer32"""
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
        *(("no-action", 1),
          ("reset", 3),
          ("trigger", 2))
    )


_CxMcVoxDiagScvDiags_Type.__name__ = "Integer32"
_CxMcVoxDiagScvDiags_Object = MibTableColumn
cxMcVoxDiagScvDiags = _CxMcVoxDiagScvDiags_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 15),
    _CxMcVoxDiagScvDiags_Type()
)
cxMcVoxDiagScvDiags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxDiagScvDiags.setStatus("mandatory")


class _CxMcVoxDiagGlmDiags_Type(Integer32):
    """Custom type cxMcVoxDiagGlmDiags based on Integer32"""
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
        *(("no-action", 1),
          ("reset", 3),
          ("trigger", 2))
    )


_CxMcVoxDiagGlmDiags_Type.__name__ = "Integer32"
_CxMcVoxDiagGlmDiags_Object = MibTableColumn
cxMcVoxDiagGlmDiags = _CxMcVoxDiagGlmDiags_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 24, 1, 16),
    _CxMcVoxDiagGlmDiags_Type()
)
cxMcVoxDiagGlmDiags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxDiagGlmDiags.setStatus("mandatory")
_CxMcVoxDownload_ObjectIdentity = ObjectIdentity
cxMcVoxDownload = _CxMcVoxDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 25)
)
_CxMcVoxLclExtAdmTable_Object = MibTable
cxMcVoxLclExtAdmTable = _CxMcVoxLclExtAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 26)
)
if mibBuilder.loadTexts:
    cxMcVoxLclExtAdmTable.setStatus("mandatory")
_CxMcVoxLclExtAdmEntry_Object = MibTableRow
cxMcVoxLclExtAdmEntry = _CxMcVoxLclExtAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 26, 1)
)
cxMcVoxLclExtAdmEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxLclExtAdmIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxLclExtAdmEntry.setStatus("mandatory")


class _CxMcVoxLclExtAdmIndex_Type(Integer32):
    """Custom type cxMcVoxLclExtAdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CxMcVoxLclExtAdmIndex_Type.__name__ = "Integer32"
_CxMcVoxLclExtAdmIndex_Object = MibTableColumn
cxMcVoxLclExtAdmIndex = _CxMcVoxLclExtAdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 26, 1, 1),
    _CxMcVoxLclExtAdmIndex_Type()
)
cxMcVoxLclExtAdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxLclExtAdmIndex.setStatus("mandatory")


class _CxMcVoxLclExtAdmRowStatus_Type(Integer32):
    """Custom type cxMcVoxLclExtAdmRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxMcVoxLclExtAdmRowStatus_Type.__name__ = "Integer32"
_CxMcVoxLclExtAdmRowStatus_Object = MibTableColumn
cxMcVoxLclExtAdmRowStatus = _CxMcVoxLclExtAdmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 26, 1, 2),
    _CxMcVoxLclExtAdmRowStatus_Type()
)
cxMcVoxLclExtAdmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxLclExtAdmRowStatus.setStatus("mandatory")


class _CxMcVoxLclExtAdmExt_Type(DisplayString):
    """Custom type cxMcVoxLclExtAdmExt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CxMcVoxLclExtAdmExt_Type.__name__ = "DisplayString"
_CxMcVoxLclExtAdmExt_Object = MibTableColumn
cxMcVoxLclExtAdmExt = _CxMcVoxLclExtAdmExt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 26, 1, 3),
    _CxMcVoxLclExtAdmExt_Type()
)
cxMcVoxLclExtAdmExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxLclExtAdmExt.setStatus("mandatory")


class _CxMcVoxLclExtAdmHuntChnl_Type(Integer32):
    """Custom type cxMcVoxLclExtAdmHuntChnl based on Integer32"""
    defaultValue = 1073741823

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1073741823),
    )


_CxMcVoxLclExtAdmHuntChnl_Type.__name__ = "Integer32"
_CxMcVoxLclExtAdmHuntChnl_Object = MibTableColumn
cxMcVoxLclExtAdmHuntChnl = _CxMcVoxLclExtAdmHuntChnl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 26, 1, 4),
    _CxMcVoxLclExtAdmHuntChnl_Type()
)
cxMcVoxLclExtAdmHuntChnl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxLclExtAdmHuntChnl.setStatus("mandatory")
_CxMcVoxLclExtOpeTable_Object = MibTable
cxMcVoxLclExtOpeTable = _CxMcVoxLclExtOpeTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 27)
)
if mibBuilder.loadTexts:
    cxMcVoxLclExtOpeTable.setStatus("mandatory")
_CxMcVoxLclExtOpeEntry_Object = MibTableRow
cxMcVoxLclExtOpeEntry = _CxMcVoxLclExtOpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 27, 1)
)
cxMcVoxLclExtOpeEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxLclExtOpeIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxLclExtOpeEntry.setStatus("mandatory")


class _CxMcVoxLclExtOpeIndex_Type(Integer32):
    """Custom type cxMcVoxLclExtOpeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CxMcVoxLclExtOpeIndex_Type.__name__ = "Integer32"
_CxMcVoxLclExtOpeIndex_Object = MibTableColumn
cxMcVoxLclExtOpeIndex = _CxMcVoxLclExtOpeIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 27, 1, 1),
    _CxMcVoxLclExtOpeIndex_Type()
)
cxMcVoxLclExtOpeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxLclExtOpeIndex.setStatus("mandatory")


class _CxMcVoxLclExtOpeExt_Type(DisplayString):
    """Custom type cxMcVoxLclExtOpeExt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CxMcVoxLclExtOpeExt_Type.__name__ = "DisplayString"
_CxMcVoxLclExtOpeExt_Object = MibTableColumn
cxMcVoxLclExtOpeExt = _CxMcVoxLclExtOpeExt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 27, 1, 2),
    _CxMcVoxLclExtOpeExt_Type()
)
cxMcVoxLclExtOpeExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxLclExtOpeExt.setStatus("mandatory")


class _CxMcVoxLclExtOpeHuntChnl_Type(Integer32):
    """Custom type cxMcVoxLclExtOpeHuntChnl based on Integer32"""
    defaultValue = 1073741823

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1073741823),
    )


_CxMcVoxLclExtOpeHuntChnl_Type.__name__ = "Integer32"
_CxMcVoxLclExtOpeHuntChnl_Object = MibTableColumn
cxMcVoxLclExtOpeHuntChnl = _CxMcVoxLclExtOpeHuntChnl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 27, 1, 3),
    _CxMcVoxLclExtOpeHuntChnl_Type()
)
cxMcVoxLclExtOpeHuntChnl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxLclExtOpeHuntChnl.setStatus("mandatory")
_CxMcVoxRegenOpe_ObjectIdentity = ObjectIdentity
cxMcVoxRegenOpe = _CxMcVoxRegenOpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 28)
)


class _CxMcVoxRegenOpeExt_Type(Integer32):
    """Custom type cxMcVoxRegenOpeExt based on Integer32"""
    defaultValue = 1

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


_CxMcVoxRegenOpeExt_Type.__name__ = "Integer32"
_CxMcVoxRegenOpeExt_Object = MibScalar
cxMcVoxRegenOpeExt = _CxMcVoxRegenOpeExt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 28, 1),
    _CxMcVoxRegenOpeExt_Type()
)
cxMcVoxRegenOpeExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxRegenOpeExt.setStatus("mandatory")


class _CxMcVoxRegenOpeGid_Type(Integer32):
    """Custom type cxMcVoxRegenOpeGid based on Integer32"""
    defaultValue = 1

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


_CxMcVoxRegenOpeGid_Type.__name__ = "Integer32"
_CxMcVoxRegenOpeGid_Object = MibScalar
cxMcVoxRegenOpeGid = _CxMcVoxRegenOpeGid_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 28, 2),
    _CxMcVoxRegenOpeGid_Type()
)
cxMcVoxRegenOpeGid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxRegenOpeGid.setStatus("mandatory")


class _CxMcVoxRegenOpeNbDigits_Type(Integer32):
    """Custom type cxMcVoxRegenOpeNbDigits based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CxMcVoxRegenOpeNbDigits_Type.__name__ = "Integer32"
_CxMcVoxRegenOpeNbDigits_Object = MibScalar
cxMcVoxRegenOpeNbDigits = _CxMcVoxRegenOpeNbDigits_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 28, 3),
    _CxMcVoxRegenOpeNbDigits_Type()
)
cxMcVoxRegenOpeNbDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxRegenOpeNbDigits.setStatus("mandatory")


class _CxMcVoxRegenOpeExtBitMask_Type(Integer32):
    """Custom type cxMcVoxRegenOpeExtBitMask based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxMcVoxRegenOpeExtBitMask_Type.__name__ = "Integer32"
_CxMcVoxRegenOpeExtBitMask_Object = MibScalar
cxMcVoxRegenOpeExtBitMask = _CxMcVoxRegenOpeExtBitMask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 28, 4),
    _CxMcVoxRegenOpeExtBitMask_Type()
)
cxMcVoxRegenOpeExtBitMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxRegenOpeExtBitMask.setStatus("mandatory")
_CxMcVoxTranslOpe_ObjectIdentity = ObjectIdentity
cxMcVoxTranslOpe = _CxMcVoxTranslOpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 29)
)


class _CxMcVoxTranslOpeCntryCodeEnable_Type(Integer32):
    """Custom type cxMcVoxTranslOpeCntryCodeEnable based on Integer32"""
    defaultValue = 1

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


_CxMcVoxTranslOpeCntryCodeEnable_Type.__name__ = "Integer32"
_CxMcVoxTranslOpeCntryCodeEnable_Object = MibScalar
cxMcVoxTranslOpeCntryCodeEnable = _CxMcVoxTranslOpeCntryCodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 29, 1),
    _CxMcVoxTranslOpeCntryCodeEnable_Type()
)
cxMcVoxTranslOpeCntryCodeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxTranslOpeCntryCodeEnable.setStatus("mandatory")


class _CxMcVoxTranslOpeCntryCode_Type(DisplayString):
    """Custom type cxMcVoxTranslOpeCntryCode based on DisplayString"""
    defaultValue = OctetString("1")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxTranslOpeCntryCode_Type.__name__ = "DisplayString"
_CxMcVoxTranslOpeCntryCode_Object = MibScalar
cxMcVoxTranslOpeCntryCode = _CxMcVoxTranslOpeCntryCode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 29, 2),
    _CxMcVoxTranslOpeCntryCode_Type()
)
cxMcVoxTranslOpeCntryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxTranslOpeCntryCode.setStatus("mandatory")


class _CxMcVoxTranslOpeCntryCodeLng_Type(Integer32):
    """Custom type cxMcVoxTranslOpeCntryCodeLng based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxTranslOpeCntryCodeLng_Type.__name__ = "Integer32"
_CxMcVoxTranslOpeCntryCodeLng_Object = MibScalar
cxMcVoxTranslOpeCntryCodeLng = _CxMcVoxTranslOpeCntryCodeLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 29, 3),
    _CxMcVoxTranslOpeCntryCodeLng_Type()
)
cxMcVoxTranslOpeCntryCodeLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxTranslOpeCntryCodeLng.setStatus("mandatory")


class _CxMcVoxTranslOpeCCPrefix_Type(DisplayString):
    """Custom type cxMcVoxTranslOpeCCPrefix based on DisplayString"""
    defaultValue = OctetString("2")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxTranslOpeCCPrefix_Type.__name__ = "DisplayString"
_CxMcVoxTranslOpeCCPrefix_Object = MibScalar
cxMcVoxTranslOpeCCPrefix = _CxMcVoxTranslOpeCCPrefix_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 29, 4),
    _CxMcVoxTranslOpeCCPrefix_Type()
)
cxMcVoxTranslOpeCCPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxTranslOpeCCPrefix.setStatus("mandatory")


class _CxMcVoxTranslOpeCCPrefixLng_Type(Integer32):
    """Custom type cxMcVoxTranslOpeCCPrefixLng based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxTranslOpeCCPrefixLng_Type.__name__ = "Integer32"
_CxMcVoxTranslOpeCCPrefixLng_Object = MibScalar
cxMcVoxTranslOpeCCPrefixLng = _CxMcVoxTranslOpeCCPrefixLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 29, 5),
    _CxMcVoxTranslOpeCCPrefixLng_Type()
)
cxMcVoxTranslOpeCCPrefixLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxTranslOpeCCPrefixLng.setStatus("mandatory")


class _CxMcVoxTranslOpeAreaCodeEnable_Type(Integer32):
    """Custom type cxMcVoxTranslOpeAreaCodeEnable based on Integer32"""
    defaultValue = 1

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


_CxMcVoxTranslOpeAreaCodeEnable_Type.__name__ = "Integer32"
_CxMcVoxTranslOpeAreaCodeEnable_Object = MibScalar
cxMcVoxTranslOpeAreaCodeEnable = _CxMcVoxTranslOpeAreaCodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 29, 6),
    _CxMcVoxTranslOpeAreaCodeEnable_Type()
)
cxMcVoxTranslOpeAreaCodeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxTranslOpeAreaCodeEnable.setStatus("mandatory")


class _CxMcVoxTranslOpeAreaCode_Type(DisplayString):
    """Custom type cxMcVoxTranslOpeAreaCode based on DisplayString"""
    defaultValue = OctetString("514")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxTranslOpeAreaCode_Type.__name__ = "DisplayString"
_CxMcVoxTranslOpeAreaCode_Object = MibScalar
cxMcVoxTranslOpeAreaCode = _CxMcVoxTranslOpeAreaCode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 29, 7),
    _CxMcVoxTranslOpeAreaCode_Type()
)
cxMcVoxTranslOpeAreaCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxTranslOpeAreaCode.setStatus("mandatory")


class _CxMcVoxTranslOpeAreaCodeLng_Type(Integer32):
    """Custom type cxMcVoxTranslOpeAreaCodeLng based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxTranslOpeAreaCodeLng_Type.__name__ = "Integer32"
_CxMcVoxTranslOpeAreaCodeLng_Object = MibScalar
cxMcVoxTranslOpeAreaCodeLng = _CxMcVoxTranslOpeAreaCodeLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 29, 8),
    _CxMcVoxTranslOpeAreaCodeLng_Type()
)
cxMcVoxTranslOpeAreaCodeLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxTranslOpeAreaCodeLng.setStatus("mandatory")


class _CxMcVoxTranslOpeACPrefix_Type(DisplayString):
    """Custom type cxMcVoxTranslOpeACPrefix based on DisplayString"""
    defaultValue = OctetString("1")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxTranslOpeACPrefix_Type.__name__ = "DisplayString"
_CxMcVoxTranslOpeACPrefix_Object = MibScalar
cxMcVoxTranslOpeACPrefix = _CxMcVoxTranslOpeACPrefix_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 29, 9),
    _CxMcVoxTranslOpeACPrefix_Type()
)
cxMcVoxTranslOpeACPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxTranslOpeACPrefix.setStatus("mandatory")


class _CxMcVoxTranslOpeACPrefixLng_Type(Integer32):
    """Custom type cxMcVoxTranslOpeACPrefixLng based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxTranslOpeACPrefixLng_Type.__name__ = "Integer32"
_CxMcVoxTranslOpeACPrefixLng_Object = MibScalar
cxMcVoxTranslOpeACPrefixLng = _CxMcVoxTranslOpeACPrefixLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 29, 10),
    _CxMcVoxTranslOpeACPrefixLng_Type()
)
cxMcVoxTranslOpeACPrefixLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxTranslOpeACPrefixLng.setStatus("mandatory")


class _CxMcVoxTranslOpeZoneCodeEnable_Type(Integer32):
    """Custom type cxMcVoxTranslOpeZoneCodeEnable based on Integer32"""
    defaultValue = 1

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


_CxMcVoxTranslOpeZoneCodeEnable_Type.__name__ = "Integer32"
_CxMcVoxTranslOpeZoneCodeEnable_Object = MibScalar
cxMcVoxTranslOpeZoneCodeEnable = _CxMcVoxTranslOpeZoneCodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 29, 11),
    _CxMcVoxTranslOpeZoneCodeEnable_Type()
)
cxMcVoxTranslOpeZoneCodeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxTranslOpeZoneCodeEnable.setStatus("mandatory")


class _CxMcVoxTranslOpeZCPrefix_Type(DisplayString):
    """Custom type cxMcVoxTranslOpeZCPrefix based on DisplayString"""
    defaultValue = OctetString("7")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxTranslOpeZCPrefix_Type.__name__ = "DisplayString"
_CxMcVoxTranslOpeZCPrefix_Object = MibScalar
cxMcVoxTranslOpeZCPrefix = _CxMcVoxTranslOpeZCPrefix_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 29, 12),
    _CxMcVoxTranslOpeZCPrefix_Type()
)
cxMcVoxTranslOpeZCPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcVoxTranslOpeZCPrefix.setStatus("mandatory")


class _CxMcVoxTranslOpeZCPrefixLng_Type(Integer32):
    """Custom type cxMcVoxTranslOpeZCPrefixLng based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxTranslOpeZCPrefixLng_Type.__name__ = "Integer32"
_CxMcVoxTranslOpeZCPrefixLng_Object = MibScalar
cxMcVoxTranslOpeZCPrefixLng = _CxMcVoxTranslOpeZCPrefixLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 29, 13),
    _CxMcVoxTranslOpeZCPrefixLng_Type()
)
cxMcVoxTranslOpeZCPrefixLng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxTranslOpeZCPrefixLng.setStatus("mandatory")
_CxMcVoxHistoryTable_Object = MibTable
cxMcVoxHistoryTable = _CxMcVoxHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 30)
)
if mibBuilder.loadTexts:
    cxMcVoxHistoryTable.setStatus("mandatory")
_CxMcVoxHistoryEntry_Object = MibTableRow
cxMcVoxHistoryEntry = _CxMcVoxHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 30, 1)
)
cxMcVoxHistoryEntry.setIndexNames(
    (0, "CXMCVOX-MIB", "cxMcVoxHistoryIndex"),
)
if mibBuilder.loadTexts:
    cxMcVoxHistoryEntry.setStatus("mandatory")


class _CxMcVoxHistoryIndex_Type(Integer32):
    """Custom type cxMcVoxHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CxMcVoxHistoryIndex_Type.__name__ = "Integer32"
_CxMcVoxHistoryIndex_Object = MibTableColumn
cxMcVoxHistoryIndex = _CxMcVoxHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 30, 1, 1),
    _CxMcVoxHistoryIndex_Type()
)
cxMcVoxHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxHistoryIndex.setStatus("mandatory")


class _CxMcVoxHistoryLclCardNumber_Type(Integer32):
    """Custom type cxMcVoxHistoryLclCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxHistoryLclCardNumber_Type.__name__ = "Integer32"
_CxMcVoxHistoryLclCardNumber_Object = MibTableColumn
cxMcVoxHistoryLclCardNumber = _CxMcVoxHistoryLclCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 30, 1, 2),
    _CxMcVoxHistoryLclCardNumber_Type()
)
cxMcVoxHistoryLclCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxHistoryLclCardNumber.setStatus("mandatory")


class _CxMcVoxHistoryLclPortNumber_Type(Integer32):
    """Custom type cxMcVoxHistoryLclPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CxMcVoxHistoryLclPortNumber_Type.__name__ = "Integer32"
_CxMcVoxHistoryLclPortNumber_Object = MibTableColumn
cxMcVoxHistoryLclPortNumber = _CxMcVoxHistoryLclPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 30, 1, 3),
    _CxMcVoxHistoryLclPortNumber_Type()
)
cxMcVoxHistoryLclPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxHistoryLclPortNumber.setStatus("mandatory")


class _CxMcVoxHistoryRmtCardNumber_Type(Integer32):
    """Custom type cxMcVoxHistoryRmtCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcVoxHistoryRmtCardNumber_Type.__name__ = "Integer32"
_CxMcVoxHistoryRmtCardNumber_Object = MibTableColumn
cxMcVoxHistoryRmtCardNumber = _CxMcVoxHistoryRmtCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 30, 1, 4),
    _CxMcVoxHistoryRmtCardNumber_Type()
)
cxMcVoxHistoryRmtCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxHistoryRmtCardNumber.setStatus("mandatory")


class _CxMcVoxHistoryRmtPortNumber_Type(Integer32):
    """Custom type cxMcVoxHistoryRmtPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CxMcVoxHistoryRmtPortNumber_Type.__name__ = "Integer32"
_CxMcVoxHistoryRmtPortNumber_Object = MibTableColumn
cxMcVoxHistoryRmtPortNumber = _CxMcVoxHistoryRmtPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 30, 1, 5),
    _CxMcVoxHistoryRmtPortNumber_Type()
)
cxMcVoxHistoryRmtPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxHistoryRmtPortNumber.setStatus("mandatory")


class _CxMcVoxHistoryTimeStampOnLine_Type(Integer32):
    """Custom type cxMcVoxHistoryTimeStampOnLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CxMcVoxHistoryTimeStampOnLine_Type.__name__ = "Integer32"
_CxMcVoxHistoryTimeStampOnLine_Object = MibTableColumn
cxMcVoxHistoryTimeStampOnLine = _CxMcVoxHistoryTimeStampOnLine_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 30, 1, 6),
    _CxMcVoxHistoryTimeStampOnLine_Type()
)
cxMcVoxHistoryTimeStampOnLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxHistoryTimeStampOnLine.setStatus("mandatory")


class _CxMcVoxHistoryTimeStampOffLine_Type(Integer32):
    """Custom type cxMcVoxHistoryTimeStampOffLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CxMcVoxHistoryTimeStampOffLine_Type.__name__ = "Integer32"
_CxMcVoxHistoryTimeStampOffLine_Object = MibTableColumn
cxMcVoxHistoryTimeStampOffLine = _CxMcVoxHistoryTimeStampOffLine_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 30, 1, 7),
    _CxMcVoxHistoryTimeStampOffLine_Type()
)
cxMcVoxHistoryTimeStampOffLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxHistoryTimeStampOffLine.setStatus("mandatory")


class _CxMcVoxHistoryLnkState_Type(DisplayString):
    """Custom type cxMcVoxHistoryLnkState based on DisplayString"""
    defaultValue = OctetString("CallAborted")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CxMcVoxHistoryLnkState_Type.__name__ = "DisplayString"
_CxMcVoxHistoryLnkState_Object = MibTableColumn
cxMcVoxHistoryLnkState = _CxMcVoxHistoryLnkState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 30, 1, 8),
    _CxMcVoxHistoryLnkState_Type()
)
cxMcVoxHistoryLnkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxHistoryLnkState.setStatus("mandatory")


class _CxMcVoxHistoryPin_Type(DisplayString):
    """Custom type cxMcVoxHistoryPin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 8),
    )


_CxMcVoxHistoryPin_Type.__name__ = "DisplayString"
_CxMcVoxHistoryPin_Object = MibTableColumn
cxMcVoxHistoryPin = _CxMcVoxHistoryPin_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 30, 1, 9),
    _CxMcVoxHistoryPin_Type()
)
cxMcVoxHistoryPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxHistoryPin.setStatus("mandatory")


class _CxMcVoxHistoryExtensionOrGrpId_Type(DisplayString):
    """Custom type cxMcVoxHistoryExtensionOrGrpId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CxMcVoxHistoryExtensionOrGrpId_Type.__name__ = "DisplayString"
_CxMcVoxHistoryExtensionOrGrpId_Object = MibTableColumn
cxMcVoxHistoryExtensionOrGrpId = _CxMcVoxHistoryExtensionOrGrpId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 30, 1, 10),
    _CxMcVoxHistoryExtensionOrGrpId_Type()
)
cxMcVoxHistoryExtensionOrGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxHistoryExtensionOrGrpId.setStatus("mandatory")


class _CxMcVoxHistoryPhoneNumber_Type(DisplayString):
    """Custom type cxMcVoxHistoryPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_CxMcVoxHistoryPhoneNumber_Type.__name__ = "DisplayString"
_CxMcVoxHistoryPhoneNumber_Object = MibTableColumn
cxMcVoxHistoryPhoneNumber = _CxMcVoxHistoryPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 30, 1, 11),
    _CxMcVoxHistoryPhoneNumber_Type()
)
cxMcVoxHistoryPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcVoxHistoryPhoneNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cxMcVoxTrapStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 0, 1)
)
cxMcVoxTrapStatus.setObjects(
      *(("CXModuleHardware-MIB", "cxModuleHwPhysSlot"),
        ("CXMCVOX-MIB", "cxMcVoxStatusCardNumber"),
        ("CXMCVOX-MIB", "cxMcVoxStatusPortNumber"),
        ("CXMCVOX-MIB", "cxMcVoxStatusPortStatus"))
)
if mibBuilder.loadTexts:
    cxMcVoxTrapStatus.setStatus(
        ""
    )

cxMcVoxTrapRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 0, 2)
)
cxMcVoxTrapRing.setObjects(
      *(("CXModuleHardware-MIB", "cxModuleHwPhysSlot"),
        ("CXMCVOX-MIB", "cxMcVoxGlobalTensionRing"))
)
if mibBuilder.loadTexts:
    cxMcVoxTrapRing.setStatus(
        ""
    )

cxMcVoxTrapDc = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 0, 3)
)
cxMcVoxTrapDc.setObjects(
      *(("CXModuleHardware-MIB", "cxModuleHwPhysSlot"),
        ("CXMCVOX-MIB", "cxMcVoxGlobalTensionDc"))
)
if mibBuilder.loadTexts:
    cxMcVoxTrapDc.setStatus(
        ""
    )

cxMcVoxHistoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 2, 0, 4)
)
cxMcVoxHistoryTrap.setObjects(
      *(("CXModuleHardware-MIB", "cxModuleHwPhysSlot"),
        ("CXMCVOX-MIB", "cxMcVoxHistoryIndex"),
        ("CXMCVOX-MIB", "cxMcVoxGlobalHistoryMaxNumberOfEntries"))
)
if mibBuilder.loadTexts:
    cxMcVoxHistoryTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXMCVOX-MIB",
    **{"cxMcVox": cxMcVox,
       "cxMcVoxTrapStatus": cxMcVoxTrapStatus,
       "cxMcVoxTrapRing": cxMcVoxTrapRing,
       "cxMcVoxTrapDc": cxMcVoxTrapDc,
       "cxMcVoxHistoryTrap": cxMcVoxHistoryTrap,
       "cxMcVoxGlobal": cxMcVoxGlobal,
       "cxMcVoxGlobalAdmPathLng": cxMcVoxGlobalAdmPathLng,
       "cxMcVoxGlobalReinitPath": cxMcVoxGlobalReinitPath,
       "cxMcVoxGlobalClearPath": cxMcVoxGlobalClearPath,
       "cxMcVoxGlobalReinitNet": cxMcVoxGlobalReinitNet,
       "cxMcVoxGlobalClearNet": cxMcVoxGlobalClearNet,
       "cxMcVoxGlobalAdmLocalId": cxMcVoxGlobalAdmLocalId,
       "cxMcVoxGlobalOpeLocalId": cxMcVoxGlobalOpeLocalId,
       "cxMcVoxGlobalTensionRing": cxMcVoxGlobalTensionRing,
       "cxMcVoxGlobalTensionDc": cxMcVoxGlobalTensionDc,
       "cxMcVoxGlobalTrapRing": cxMcVoxGlobalTrapRing,
       "cxMcVoxGlobalTrapDc": cxMcVoxGlobalTrapDc,
       "cxMcVoxGlobalAdmGrpNbPoll": cxMcVoxGlobalAdmGrpNbPoll,
       "cxMcVoxGlobalOpeGrpNbPoll": cxMcVoxGlobalOpeGrpNbPoll,
       "cxMcVoxGlobalClearGrp": cxMcVoxGlobalClearGrp,
       "cxMcVoxGlobalOpePathLng": cxMcVoxGlobalOpePathLng,
       "cxMcVoxGlobalReinitRouting": cxMcVoxGlobalReinitRouting,
       "cxMcVoxGlobalForceDefConfig": cxMcVoxGlobalForceDefConfig,
       "cxMcVoxGlobalReinitPinTable": cxMcVoxGlobalReinitPinTable,
       "cxMcVoxGlobalAdmEnablePinTable": cxMcVoxGlobalAdmEnablePinTable,
       "cxMcVoxGlobalOpeEnablePinTable": cxMcVoxGlobalOpeEnablePinTable,
       "cxMcVoxGlobalReinitCodesTable": cxMcVoxGlobalReinitCodesTable,
       "cxMcVoxGlobalAdmEnableCodesTable": cxMcVoxGlobalAdmEnableCodesTable,
       "cxMcVoxGlobalOpeEnableCodesTable": cxMcVoxGlobalOpeEnableCodesTable,
       "cxMcVoxGlobalSoftRev": cxMcVoxGlobalSoftRev,
       "cxMcVoxGlobalGlmInBetwReqTime": cxMcVoxGlobalGlmInBetwReqTime,
       "cxMcVoxGlobalGlmMaxTimeToTxReq": cxMcVoxGlobalGlmMaxTimeToTxReq,
       "cxMcVoxGlobalGlmInBetwRespTime": cxMcVoxGlobalGlmInBetwRespTime,
       "cxMcVoxGlobalGlmMaxTimeToTxResp": cxMcVoxGlobalGlmMaxTimeToTxResp,
       "cxMcVoxGlobalGlmVoiceSilenceTime": cxMcVoxGlobalGlmVoiceSilenceTime,
       "cxMcVoxGlobalGlmSupervSilenceTime": cxMcVoxGlobalGlmSupervSilenceTime,
       "cxMcVoxGlobalGsdAutoCnctDelay": cxMcVoxGlobalGsdAutoCnctDelay,
       "cxMcVoxGlobalClearLclExt": cxMcVoxGlobalClearLclExt,
       "cxMcVoxGlobalClearRmtExt": cxMcVoxGlobalClearRmtExt,
       "cxMcVoxGlobalWanSlot": cxMcVoxGlobalWanSlot,
       "cxMcVoxGlobalNetNbDigits": cxMcVoxGlobalNetNbDigits,
       "cxMcVoxMibLevel": cxMcVoxMibLevel,
       "cxMcVoxGlobalRecogAcc": cxMcVoxGlobalRecogAcc,
       "cxMcVoxGlobalAccCode": cxMcVoxGlobalAccCode,
       "cxMcVoxGlobalAccCodeLng": cxMcVoxGlobalAccCodeLng,
       "cxMcVoxGlobalAdmPinCodeLng": cxMcVoxGlobalAdmPinCodeLng,
       "cxMcVoxGlobalOpePinCodeLng": cxMcVoxGlobalOpePinCodeLng,
       "cxMcVoxGlobalClearHistoryTable": cxMcVoxGlobalClearHistoryTable,
       "cxMcVoxGlobalHistoryMaxNumberOfEntries": cxMcVoxGlobalHistoryMaxNumberOfEntries,
       "cxMcVoxGlobalHistoryPercentageFull": cxMcVoxGlobalHistoryPercentageFull,
       "cxMcVoxGlobalTrapHistory": cxMcVoxGlobalTrapHistory,
       "cxMcVoxGlobalLseTimerT2": cxMcVoxGlobalLseTimerT2,
       "cxMcVoxGlobalLseTimerT3": cxMcVoxGlobalLseTimerT3,
       "cxMcVoxGlobalExtBitMask": cxMcVoxGlobalExtBitMask,
       "cxMcVoxCfgTable": cxMcVoxCfgTable,
       "cxMcVoxCfgEntry": cxMcVoxCfgEntry,
       "cxMcVoxCfgCardIndex": cxMcVoxCfgCardIndex,
       "cxMcVoxCfgPortIndex": cxMcVoxCfgPortIndex,
       "cxMcVoxCfgDriverAdmUsed": cxMcVoxCfgDriverAdmUsed,
       "cxMcVoxCfgDriverOpeUsed": cxMcVoxCfgDriverOpeUsed,
       "cxMcVoxCfgTrapOnLine": cxMcVoxCfgTrapOnLine,
       "cxMcVoxCfgTrapOffLine": cxMcVoxCfgTrapOffLine,
       "cxMcVoxCfgTrapStatus": cxMcVoxCfgTrapStatus,
       "cxMcVoxCfgTrapState": cxMcVoxCfgTrapState,
       "cxMcVoxCfgTestPort": cxMcVoxCfgTestPort,
       "cxMcVoxCfgToneTest": cxMcVoxCfgToneTest,
       "cxMcVoxCfgReinitPort": cxMcVoxCfgReinitPort,
       "cxMcVoxCfgClearPort": cxMcVoxCfgClearPort,
       "cxMcVoxCfgOpeAcelpRev": cxMcVoxCfgOpeAcelpRev,
       "cxMcVoxCfgCmdImmTest": cxMcVoxCfgCmdImmTest,
       "cxMcVoxCfgCmdTest": cxMcVoxCfgCmdTest,
       "cxMcVoxCfgMaxPktFrame": cxMcVoxCfgMaxPktFrame,
       "cxMcVoxCfgMaxSkew": cxMcVoxCfgMaxSkew,
       "cxMcVoxStatAndLog": cxMcVoxStatAndLog,
       "cxMcVoxStatusTable": cxMcVoxStatusTable,
       "cxMcVoxStatusEntry": cxMcVoxStatusEntry,
       "cxMcVoxStatusCardNumber": cxMcVoxStatusCardNumber,
       "cxMcVoxStatusPortNumber": cxMcVoxStatusPortNumber,
       "cxMcVoxStatusPortStatus": cxMcVoxStatusPortStatus,
       "cxMcVoxStatusHookLocal": cxMcVoxStatusHookLocal,
       "cxMcVoxStatusHookRem": cxMcVoxStatusHookRem,
       "cxMcVoxStatusIoAccess": cxMcVoxStatusIoAccess,
       "cxMcVoxStatusChannelAccess": cxMcVoxStatusChannelAccess,
       "cxMcVoxStatusDspRam": cxMcVoxStatusDspRam,
       "cxMcVoxStatusDspDpram": cxMcVoxStatusDspDpram,
       "cxMcVoxStatusSamplingTime": cxMcVoxStatusSamplingTime,
       "cxMcVoxStatusWatchdog": cxMcVoxStatusWatchdog,
       "cxMcVoxStatusRemPortStatus": cxMcVoxStatusRemPortStatus,
       "cxMcVoxStatusInputDbmLevel": cxMcVoxStatusInputDbmLevel,
       "cxMcVoxStatusPhyIfType": cxMcVoxStatusPhyIfType,
       "cxMcVoxStatusDspUtilization": cxMcVoxStatusDspUtilization,
       "cxMcVoxStatusIOResetState": cxMcVoxStatusIOResetState,
       "cxMcVoxEventTable": cxMcVoxEventTable,
       "cxMcVoxEventEntry": cxMcVoxEventEntry,
       "cxMcVoxEventCardNumber": cxMcVoxEventCardNumber,
       "cxMcVoxEventPortNumber": cxMcVoxEventPortNumber,
       "cxMcVoxEventLogIndex": cxMcVoxEventLogIndex,
       "cxMcVoxEventDateAndTimeOnLine": cxMcVoxEventDateAndTimeOnLine,
       "cxMcVoxEventDateAndTimeOffLine": cxMcVoxEventDateAndTimeOffLine,
       "cxMcVoxEventPhoneNumber": cxMcVoxEventPhoneNumber,
       "cxMcVoxEventLnkState": cxMcVoxEventLnkState,
       "cxMcVoxEventPin": cxMcVoxEventPin,
       "cxMcVoxEventClrEvts": cxMcVoxEventClrEvts,
       "cxMcVoxStateTable": cxMcVoxStateTable,
       "cxMcVoxStateEntry": cxMcVoxStateEntry,
       "cxMcVoxStateCardNumber": cxMcVoxStateCardNumber,
       "cxMcVoxStatePortNumber": cxMcVoxStatePortNumber,
       "cxMcVoxStateLogIndex": cxMcVoxStateLogIndex,
       "cxMcVoxStatePathId": cxMcVoxStatePathId,
       "cxMcVoxStateDateAndTime": cxMcVoxStateDateAndTime,
       "cxMcVoxStateLnkState": cxMcVoxStateLnkState,
       "cxMcVoxStateRmtExt": cxMcVoxStateRmtExt,
       "cxMcVoxPathAdmTable": cxMcVoxPathAdmTable,
       "cxMcVoxPathAdmEntry": cxMcVoxPathAdmEntry,
       "cxMcVoxPathAdmIndex": cxMcVoxPathAdmIndex,
       "cxMcVoxPathAdmRowStatus": cxMcVoxPathAdmRowStatus,
       "cxMcVoxPathAdmPathId": cxMcVoxPathAdmPathId,
       "cxMcVoxPathAdmRemStationId": cxMcVoxPathAdmRemStationId,
       "cxMcVoxPathAdmHunt": cxMcVoxPathAdmHunt,
       "cxMcVoxPathAdmLng": cxMcVoxPathAdmLng,
       "cxMcVoxPathOpeTable": cxMcVoxPathOpeTable,
       "cxMcVoxPathOpeEntry": cxMcVoxPathOpeEntry,
       "cxMcVoxPathOpeIndex": cxMcVoxPathOpeIndex,
       "cxMcVoxPathOpePathId": cxMcVoxPathOpePathId,
       "cxMcVoxPathOpeRemStationId": cxMcVoxPathOpeRemStationId,
       "cxMcVoxPathOpeHunt": cxMcVoxPathOpeHunt,
       "cxMcVoxPathOpeLng": cxMcVoxPathOpeLng,
       "cxMcVoxNetAdmTable": cxMcVoxNetAdmTable,
       "cxMcVoxNetAdmEntry": cxMcVoxNetAdmEntry,
       "cxMcVoxNetAdmIndex": cxMcVoxNetAdmIndex,
       "cxMcVoxNetAdmRowStatus": cxMcVoxNetAdmRowStatus,
       "cxMcVoxNetAdmRemStationId": cxMcVoxNetAdmRemStationId,
       "cxMcVoxNetAdmLocalLnkStation": cxMcVoxNetAdmLocalLnkStation,
       "cxMcVoxNetAdmRoute": cxMcVoxNetAdmRoute,
       "cxMcVoxNetAdmRemVoxStation": cxMcVoxNetAdmRemVoxStation,
       "cxMcVoxNetOpeTable": cxMcVoxNetOpeTable,
       "cxMcVoxNetOpeEntry": cxMcVoxNetOpeEntry,
       "cxMcVoxNetOpeIndex": cxMcVoxNetOpeIndex,
       "cxMcVoxNetOpeRemStationId": cxMcVoxNetOpeRemStationId,
       "cxMcVoxNetOpeLocalLnkStation": cxMcVoxNetOpeLocalLnkStation,
       "cxMcVoxNetOpeRoute": cxMcVoxNetOpeRoute,
       "cxMcVoxNetOpeRemVoxStation": cxMcVoxNetOpeRemVoxStation,
       "cxMcVoxDriverAdm": cxMcVoxDriverAdm,
       "cxMcVoxEmAdmTable": cxMcVoxEmAdmTable,
       "cxMcVoxEmAdmEntry": cxMcVoxEmAdmEntry,
       "cxMcVoxEmAdmCardUsed": cxMcVoxEmAdmCardUsed,
       "cxMcVoxEmAdmPortUsed": cxMcVoxEmAdmPortUsed,
       "cxMcVoxEmAdmPortStatus": cxMcVoxEmAdmPortStatus,
       "cxMcVoxEmAdmVocoder": cxMcVoxEmAdmVocoder,
       "cxMcVoxEmAdmFaxBw": cxMcVoxEmAdmFaxBw,
       "cxMcVoxEmAdmAutoCnx": cxMcVoxEmAdmAutoCnx,
       "cxMcVoxEmAdmPathId": cxMcVoxEmAdmPathId,
       "cxMcVoxEmAdmTxGain": cxMcVoxEmAdmTxGain,
       "cxMcVoxEmAdmRxGain": cxMcVoxEmAdmRxGain,
       "cxMcVoxEmAdmEchoCancel": cxMcVoxEmAdmEchoCancel,
       "cxMcVoxEmAdmType": cxMcVoxEmAdmType,
       "cxMcVoxEmAdmMode": cxMcVoxEmAdmMode,
       "cxMcVoxEmAdmDialType": cxMcVoxEmAdmDialType,
       "cxMcVoxEmAdmSignalType": cxMcVoxEmAdmSignalType,
       "cxMcVoxEmAdmAc15Type": cxMcVoxEmAdmAc15Type,
       "cxMcVoxEmAdmAc15TimeOn": cxMcVoxEmAdmAc15TimeOn,
       "cxMcVoxEmAdmAc15TimeOff": cxMcVoxEmAdmAc15TimeOff,
       "cxMcVoxEmAdmCnctType": cxMcVoxEmAdmCnctType,
       "cxMcVoxEmAdmRingType": cxMcVoxEmAdmRingType,
       "cxMcVoxEmAdmRmtExt": cxMcVoxEmAdmRmtExt,
       "cxMcVoxEmAdmRmtId": cxMcVoxEmAdmRmtId,
       "cxMcVoxEmAdmTranspMode": cxMcVoxEmAdmTranspMode,
       "cxMcVoxEmAdmFaxEnable": cxMcVoxEmAdmFaxEnable,
       "cxMcVoxEmAdmBroadcast": cxMcVoxEmAdmBroadcast,
       "cxMcVoxEmAdmImpedance": cxMcVoxEmAdmImpedance,
       "cxMcVoxEmAdmVoiceConnection": cxMcVoxEmAdmVoiceConnection,
       "cxMcVoxFxsAdmTable": cxMcVoxFxsAdmTable,
       "cxMcVoxFxsAdmEntry": cxMcVoxFxsAdmEntry,
       "cxMcVoxFxsAdmCardUsed": cxMcVoxFxsAdmCardUsed,
       "cxMcVoxFxsAdmPortUsed": cxMcVoxFxsAdmPortUsed,
       "cxMcVoxFxsAdmPortStatus": cxMcVoxFxsAdmPortStatus,
       "cxMcVoxFxsAdmVocoder": cxMcVoxFxsAdmVocoder,
       "cxMcVoxFxsAdmFaxBw": cxMcVoxFxsAdmFaxBw,
       "cxMcVoxFxsAdmAutoCnx": cxMcVoxFxsAdmAutoCnx,
       "cxMcVoxFxsAdmPathId": cxMcVoxFxsAdmPathId,
       "cxMcVoxFxsAdmTxGain": cxMcVoxFxsAdmTxGain,
       "cxMcVoxFxsAdmRxGain": cxMcVoxFxsAdmRxGain,
       "cxMcVoxFxsAdmEchoCancel": cxMcVoxFxsAdmEchoCancel,
       "cxMcVoxFxsAdmSignaling": cxMcVoxFxsAdmSignaling,
       "cxMcVoxFxsAdmTimeOn": cxMcVoxFxsAdmTimeOn,
       "cxMcVoxFxsAdmTimeOff": cxMcVoxFxsAdmTimeOff,
       "cxMcVoxFxsAdmCnctType": cxMcVoxFxsAdmCnctType,
       "cxMcVoxFxsAdmRingType": cxMcVoxFxsAdmRingType,
       "cxMcVoxFxsAdmImpedance": cxMcVoxFxsAdmImpedance,
       "cxMcVoxFxsAdmDialType": cxMcVoxFxsAdmDialType,
       "cxMcVoxFxsAdmDidSignalType": cxMcVoxFxsAdmDidSignalType,
       "cxMcVoxFxsAdmRmtExt": cxMcVoxFxsAdmRmtExt,
       "cxMcVoxFxsAdmRmtId": cxMcVoxFxsAdmRmtId,
       "cxMcVoxFxsAdmTranspMode": cxMcVoxFxsAdmTranspMode,
       "cxMcVoxFxsAdmFaxEnable": cxMcVoxFxsAdmFaxEnable,
       "cxMcVoxFxsAdmBroadcast": cxMcVoxFxsAdmBroadcast,
       "cxMcVoxFxoAdmTable": cxMcVoxFxoAdmTable,
       "cxMcVoxFxoAdmEntry": cxMcVoxFxoAdmEntry,
       "cxMcVoxFxoAdmCardUsed": cxMcVoxFxoAdmCardUsed,
       "cxMcVoxFxoAdmPortUsed": cxMcVoxFxoAdmPortUsed,
       "cxMcVoxFxoAdmPortStatus": cxMcVoxFxoAdmPortStatus,
       "cxMcVoxFxoAdmVocoder": cxMcVoxFxoAdmVocoder,
       "cxMcVoxFxoAdmFaxBw": cxMcVoxFxoAdmFaxBw,
       "cxMcVoxFxoAdmAutoCnx": cxMcVoxFxoAdmAutoCnx,
       "cxMcVoxFxoAdmPathId": cxMcVoxFxoAdmPathId,
       "cxMcVoxFxoAdmTxGain": cxMcVoxFxoAdmTxGain,
       "cxMcVoxFxoAdmRxGain": cxMcVoxFxoAdmRxGain,
       "cxMcVoxFxoAdmEchoCancel": cxMcVoxFxoAdmEchoCancel,
       "cxMcVoxFxoAdmSignaling": cxMcVoxFxoAdmSignaling,
       "cxMcVoxFxoAdmCnctType": cxMcVoxFxoAdmCnctType,
       "cxMcVoxFxoAdmRingType": cxMcVoxFxoAdmRingType,
       "cxMcVoxFxoAdmImpedance": cxMcVoxFxoAdmImpedance,
       "cxMcVoxFxoAdmDialType": cxMcVoxFxoAdmDialType,
       "cxMcVoxFxoAdmDidSignalType": cxMcVoxFxoAdmDidSignalType,
       "cxMcVoxFxoAdmRmtExt": cxMcVoxFxoAdmRmtExt,
       "cxMcVoxFxoAdmRmtId": cxMcVoxFxoAdmRmtId,
       "cxMcVoxFxoAdmTranspMode": cxMcVoxFxoAdmTranspMode,
       "cxMcVoxFxoAdmFaxEnable": cxMcVoxFxoAdmFaxEnable,
       "cxMcVoxFxoAdmBroadcast": cxMcVoxFxoAdmBroadcast,
       "cxMcVoxDriverOpe": cxMcVoxDriverOpe,
       "cxMcVoxEmOpeTable": cxMcVoxEmOpeTable,
       "cxMcVoxEmOpeEntry": cxMcVoxEmOpeEntry,
       "cxMcVoxEmOpeCardUsed": cxMcVoxEmOpeCardUsed,
       "cxMcVoxEmOpePortUsed": cxMcVoxEmOpePortUsed,
       "cxMcVoxEmOpePortStatus": cxMcVoxEmOpePortStatus,
       "cxMcVoxEmOpeVocoder": cxMcVoxEmOpeVocoder,
       "cxMcVoxEmOpeFaxBw": cxMcVoxEmOpeFaxBw,
       "cxMcVoxEmOpeAutoCnx": cxMcVoxEmOpeAutoCnx,
       "cxMcVoxEmOpePathId": cxMcVoxEmOpePathId,
       "cxMcVoxEmOpeTxGain": cxMcVoxEmOpeTxGain,
       "cxMcVoxEmOpeRxGain": cxMcVoxEmOpeRxGain,
       "cxMcVoxEmOpeEchoCancel": cxMcVoxEmOpeEchoCancel,
       "cxMcVoxEmOpeType": cxMcVoxEmOpeType,
       "cxMcVoxEmOpeMode": cxMcVoxEmOpeMode,
       "cxMcVoxEmOpeDialType": cxMcVoxEmOpeDialType,
       "cxMcVoxEmOpeSignalType": cxMcVoxEmOpeSignalType,
       "cxMcVoxEmOpeAc15Type": cxMcVoxEmOpeAc15Type,
       "cxMcVoxEmOpeAc15TimeOn": cxMcVoxEmOpeAc15TimeOn,
       "cxMcVoxEmOpeAc15TimeOff": cxMcVoxEmOpeAc15TimeOff,
       "cxMcVoxEmOpeCnctType": cxMcVoxEmOpeCnctType,
       "cxMcVoxEmOpeRingType": cxMcVoxEmOpeRingType,
       "cxMcVoxEmOpeRmtExt": cxMcVoxEmOpeRmtExt,
       "cxMcVoxEmOpeRmtId": cxMcVoxEmOpeRmtId,
       "cxMcVoxEmOpeTranspMode": cxMcVoxEmOpeTranspMode,
       "cxMcVoxEmOpeFaxEnable": cxMcVoxEmOpeFaxEnable,
       "cxMcVoxEmOpeBroadcast": cxMcVoxEmOpeBroadcast,
       "cxMcVoxEmOpeImpedance": cxMcVoxEmOpeImpedance,
       "cxMcVoxEmOpeVoiceConnection": cxMcVoxEmOpeVoiceConnection,
       "cxMcVoxFxsOpeTable": cxMcVoxFxsOpeTable,
       "cxMcVoxFxsOpeEntry": cxMcVoxFxsOpeEntry,
       "cxMcVoxFxsOpeCardUsed": cxMcVoxFxsOpeCardUsed,
       "cxMcVoxFxsOpePortUsed": cxMcVoxFxsOpePortUsed,
       "cxMcVoxFxsOpePortStatus": cxMcVoxFxsOpePortStatus,
       "cxMcVoxFxsOpeVocoder": cxMcVoxFxsOpeVocoder,
       "cxMcVoxFxsOpeFaxBw": cxMcVoxFxsOpeFaxBw,
       "cxMcVoxFxsOpeAutoCnx": cxMcVoxFxsOpeAutoCnx,
       "cxMcVoxFxsOpePathId": cxMcVoxFxsOpePathId,
       "cxMcVoxFxsOpeTxGain": cxMcVoxFxsOpeTxGain,
       "cxMcVoxFxsOpeRxGain": cxMcVoxFxsOpeRxGain,
       "cxMcVoxFxsOpeEchoCancel": cxMcVoxFxsOpeEchoCancel,
       "cxMcVoxFxsOpeSignaling": cxMcVoxFxsOpeSignaling,
       "cxMcVoxFxsOpeTimeOn": cxMcVoxFxsOpeTimeOn,
       "cxMcVoxFxsOpeTimeOff": cxMcVoxFxsOpeTimeOff,
       "cxMcVoxFxsOpeCnctType": cxMcVoxFxsOpeCnctType,
       "cxMcVoxFxsOpeRingType": cxMcVoxFxsOpeRingType,
       "cxMcVoxFxsOpeImpedance": cxMcVoxFxsOpeImpedance,
       "cxMcVoxFxsOpeDialType": cxMcVoxFxsOpeDialType,
       "cxMcVoxFxsOpeDidSignalType": cxMcVoxFxsOpeDidSignalType,
       "cxMcVoxFxsOpeRmtExt": cxMcVoxFxsOpeRmtExt,
       "cxMcVoxFxsOpeRmtId": cxMcVoxFxsOpeRmtId,
       "cxMcVoxFxsOpeTranspMode": cxMcVoxFxsOpeTranspMode,
       "cxMcVoxFxsOpeFaxEnable": cxMcVoxFxsOpeFaxEnable,
       "cxMcVoxFxsOpeBroadcast": cxMcVoxFxsOpeBroadcast,
       "cxMcVoxFxoOpeTable": cxMcVoxFxoOpeTable,
       "cxMcVoxFxoOpeEntry": cxMcVoxFxoOpeEntry,
       "cxMcVoxFxoOpeCardUsed": cxMcVoxFxoOpeCardUsed,
       "cxMcVoxFxoOpePortUsed": cxMcVoxFxoOpePortUsed,
       "cxMcVoxFxoOpePortStatus": cxMcVoxFxoOpePortStatus,
       "cxMcVoxFxoOpeVocoder": cxMcVoxFxoOpeVocoder,
       "cxMcVoxFxoOpeFaxBw": cxMcVoxFxoOpeFaxBw,
       "cxMcVoxFxoOpeAutoCnx": cxMcVoxFxoOpeAutoCnx,
       "cxMcVoxFxoOpePathId": cxMcVoxFxoOpePathId,
       "cxMcVoxFxoOpeTxGain": cxMcVoxFxoOpeTxGain,
       "cxMcVoxFxoOpeRxGain": cxMcVoxFxoOpeRxGain,
       "cxMcVoxFxoOpeEchoCancel": cxMcVoxFxoOpeEchoCancel,
       "cxMcVoxFxoOpeSignaling": cxMcVoxFxoOpeSignaling,
       "cxMcVoxFxoOpeCnctType": cxMcVoxFxoOpeCnctType,
       "cxMcVoxFxoOpeRingType": cxMcVoxFxoOpeRingType,
       "cxMcVoxFxoOpeImpedance": cxMcVoxFxoOpeImpedance,
       "cxMcVoxFxoOpeDialType": cxMcVoxFxoOpeDialType,
       "cxMcVoxFxoOpeDidSignalType": cxMcVoxFxoOpeDidSignalType,
       "cxMcVoxFxoOpeRmtExt": cxMcVoxFxoOpeRmtExt,
       "cxMcVoxFxoOpeRmtId": cxMcVoxFxoOpeRmtId,
       "cxMcVoxFxoOpeTranspMode": cxMcVoxFxoOpeTranspMode,
       "cxMcVoxFxoOpeFaxEnable": cxMcVoxFxoOpeFaxEnable,
       "cxMcVoxFxoOpeBroadcast": cxMcVoxFxoOpeBroadcast,
       "cxMcVoxGrpIdAdmTable": cxMcVoxGrpIdAdmTable,
       "cxMcVoxGrpIdAdmEntry": cxMcVoxGrpIdAdmEntry,
       "cxMcVoxGrpIdAdmIndex": cxMcVoxGrpIdAdmIndex,
       "cxMcVoxGrpIdAdm": cxMcVoxGrpIdAdm,
       "cxMcVoxGrpIdLenAdm": cxMcVoxGrpIdLenAdm,
       "cxMcVoxGrpIdAdmRowStatus": cxMcVoxGrpIdAdmRowStatus,
       "cxMcVoxGrpIdAdmNbPoll": cxMcVoxGrpIdAdmNbPoll,
       "cxMcVoxGrpIdOpeTable": cxMcVoxGrpIdOpeTable,
       "cxMcVoxGrpIdOpeEntry": cxMcVoxGrpIdOpeEntry,
       "cxMcVoxGrpIdOpeIndex": cxMcVoxGrpIdOpeIndex,
       "cxMcVoxGrpIdOpe": cxMcVoxGrpIdOpe,
       "cxMcVoxGrpIdLenOpe": cxMcVoxGrpIdLenOpe,
       "cxMcVoxGrpIdOpeNbPoll": cxMcVoxGrpIdOpeNbPoll,
       "cxMcVoxGrpDefAdmTable": cxMcVoxGrpDefAdmTable,
       "cxMcVoxGrpDefAdmEntry": cxMcVoxGrpDefAdmEntry,
       "cxMcVoxGrpDefAdmIndex": cxMcVoxGrpDefAdmIndex,
       "cxMcVoxGrpDefAdmPriority": cxMcVoxGrpDefAdmPriority,
       "cxMcVoxGrpDefAdmRowStatus": cxMcVoxGrpDefAdmRowStatus,
       "cxMcVoxGrpDefAdmPathId": cxMcVoxGrpDefAdmPathId,
       "cxMcVoxGrpDefAdmRmtExt": cxMcVoxGrpDefAdmRmtExt,
       "cxMcVoxGrpDefOpeTable": cxMcVoxGrpDefOpeTable,
       "cxMcVoxGrpDefOpeEntry": cxMcVoxGrpDefOpeEntry,
       "cxMcVoxGrpDefOpeIndex": cxMcVoxGrpDefOpeIndex,
       "cxMcVoxGrpDefOpePriority": cxMcVoxGrpDefOpePriority,
       "cxMcVoxGrpDefOpePathId": cxMcVoxGrpDefOpePathId,
       "cxMcVoxGrpDefOpeRmtExt": cxMcVoxGrpDefOpeRmtExt,
       "cxMcVoxAdmPinTable": cxMcVoxAdmPinTable,
       "cxMcVoxAdmPinEntry": cxMcVoxAdmPinEntry,
       "cxMcVoxAdmPinIndex": cxMcVoxAdmPinIndex,
       "cxMcVoxAdmPinCode": cxMcVoxAdmPinCode,
       "cxMcVoxAdmPinRowStatus": cxMcVoxAdmPinRowStatus,
       "cxMcVoxOpePinTable": cxMcVoxOpePinTable,
       "cxMcVoxOpePinEntry": cxMcVoxOpePinEntry,
       "cxMcVoxOpePinIndex": cxMcVoxOpePinIndex,
       "cxMcVoxOpePinCode": cxMcVoxOpePinCode,
       "cxMcVoxAdmLclZoneTable": cxMcVoxAdmLclZoneTable,
       "cxMcVoxAdmLclZoneEntry": cxMcVoxAdmLclZoneEntry,
       "cxMcVoxAdmLclZoneIndex": cxMcVoxAdmLclZoneIndex,
       "cxMcVoxAdmLclZoneCode": cxMcVoxAdmLclZoneCode,
       "cxMcVoxAdmLclZoneLng": cxMcVoxAdmLclZoneLng,
       "cxMcVoxAdmLclZoneRowStatus": cxMcVoxAdmLclZoneRowStatus,
       "cxMcVoxOpeLclZoneTable": cxMcVoxOpeLclZoneTable,
       "cxMcVoxOpeLclZoneEntry": cxMcVoxOpeLclZoneEntry,
       "cxMcVoxOpeLclZoneIndex": cxMcVoxOpeLclZoneIndex,
       "cxMcVoxOpeLclZoneCode": cxMcVoxOpeLclZoneCode,
       "cxMcVoxOpeLclZoneLng": cxMcVoxOpeLclZoneLng,
       "cxMcVoxAdmRTC": cxMcVoxAdmRTC,
       "cxMcVoxAdmRTCCountry": cxMcVoxAdmRTCCountry,
       "cxMcVoxAdmRTCCountryLng": cxMcVoxAdmRTCCountryLng,
       "cxMcVoxAdmRTCNonLclCountry": cxMcVoxAdmRTCNonLclCountry,
       "cxMcVoxAdmRTCNonLclCountryLng": cxMcVoxAdmRTCNonLclCountryLng,
       "cxMcVoxAdmRTCArea": cxMcVoxAdmRTCArea,
       "cxMcVoxAdmRTCAreaLng": cxMcVoxAdmRTCAreaLng,
       "cxMcVoxAdmRTCNonLclArea": cxMcVoxAdmRTCNonLclArea,
       "cxMcVoxAdmRTCNonLclAreaLng": cxMcVoxAdmRTCNonLclAreaLng,
       "cxMcVoxAdmRTCNonLclZone": cxMcVoxAdmRTCNonLclZone,
       "cxMcVoxAdmRTCNonLclZoneLng": cxMcVoxAdmRTCNonLclZoneLng,
       "cxMcVoxOpeRTC": cxMcVoxOpeRTC,
       "cxMcVoxOpeRTCCountry": cxMcVoxOpeRTCCountry,
       "cxMcVoxOpeRTCCountryLng": cxMcVoxOpeRTCCountryLng,
       "cxMcVoxOpeRTCNonLclCountry": cxMcVoxOpeRTCNonLclCountry,
       "cxMcVoxOpeRTCNonLclCountryLng": cxMcVoxOpeRTCNonLclCountryLng,
       "cxMcVoxOpeRTCArea": cxMcVoxOpeRTCArea,
       "cxMcVoxOpeRTCAreaLng": cxMcVoxOpeRTCAreaLng,
       "cxMcVoxOpeRTCNonLclArea": cxMcVoxOpeRTCNonLclArea,
       "cxMcVoxOpeRTCNonLclAreaLng": cxMcVoxOpeRTCNonLclAreaLng,
       "cxMcVoxOpeRTCNonLclZone": cxMcVoxOpeRTCNonLclZone,
       "cxMcVoxOpeRTCNonLclZoneLng": cxMcVoxOpeRTCNonLclZoneLng,
       "cxMcVoxDriverAdmPriv": cxMcVoxDriverAdmPriv,
       "cxMcVoxAdmPortPrivTable": cxMcVoxAdmPortPrivTable,
       "cxMcVoxAdmPortPrivEntry": cxMcVoxAdmPortPrivEntry,
       "cxMcVoxAdmCardUsed": cxMcVoxAdmCardUsed,
       "cxMcVoxAdmPortUsed": cxMcVoxAdmPortUsed,
       "cxMcVoxAdmRingTimeOn": cxMcVoxAdmRingTimeOn,
       "cxMcVoxAdmRingTimeOff1": cxMcVoxAdmRingTimeOff1,
       "cxMcVoxAdmRingTimeOff2": cxMcVoxAdmRingTimeOff2,
       "cxMcVoxAdmEchoCancelLevel": cxMcVoxAdmEchoCancelLevel,
       "cxMcVoxAdmToneDelayAfterCnct": cxMcVoxAdmToneDelayAfterCnct,
       "cxMcVoxAdmToneDelayAfterFlash": cxMcVoxAdmToneDelayAfterFlash,
       "cxMcVoxAdmToneOffsetTxGain": cxMcVoxAdmToneOffsetTxGain,
       "cxMcVoxAdmVoiceOffsetTxGain": cxMcVoxAdmVoiceOffsetTxGain,
       "cxMcVoxAdmAc15InterDigit": cxMcVoxAdmAc15InterDigit,
       "cxMcVoxAdmMfToneThold": cxMcVoxAdmMfToneThold,
       "cxMcVoxAdmPulseTmin": cxMcVoxAdmPulseTmin,
       "cxMcVoxAdmPulseTmax": cxMcVoxAdmPulseTmax,
       "cxMcVoxAdmPulseInterDigit": cxMcVoxAdmPulseInterDigit,
       "cxMcVoxAdmDtmfGuard": cxMcVoxAdmDtmfGuard,
       "cxMcVoxAdmDtmfOpeLevel": cxMcVoxAdmDtmfOpeLevel,
       "cxMcVoxAdmDtmfTxTimeOn": cxMcVoxAdmDtmfTxTimeOn,
       "cxMcVoxAdmDtmfTxTimeOff": cxMcVoxAdmDtmfTxTimeOff,
       "cxMcVoxAdmFlashTmin": cxMcVoxAdmFlashTmin,
       "cxMcVoxAdmFlashTmax": cxMcVoxAdmFlashTmax,
       "cxMcVoxAdmFlashTgen": cxMcVoxAdmFlashTgen,
       "cxMcVoxAdmAfterToneSilences": cxMcVoxAdmAfterToneSilences,
       "cxMcVoxAdmFaxTxGain": cxMcVoxAdmFaxTxGain,
       "cxMcVoxAdmFaxRxGain": cxMcVoxAdmFaxRxGain,
       "cxMcVoxAdmFaxHdlcFlags": cxMcVoxAdmFaxHdlcFlags,
       "cxMcVoxAdmFaxPreambleDuration": cxMcVoxAdmFaxPreambleDuration,
       "cxMcVoxAdmFaxPreambleDelay": cxMcVoxAdmFaxPreambleDelay,
       "cxMcVoxAdmFaxCedToneDuration": cxMcVoxAdmFaxCedToneDuration,
       "cxMcVoxAdmFaxInterProtoGap": cxMcVoxAdmFaxInterProtoGap,
       "cxMcVoxAdmFaxTimerDetectSync": cxMcVoxAdmFaxTimerDetectSync,
       "cxMcVoxAdmFaxTimerWaitId": cxMcVoxAdmFaxTimerWaitId,
       "cxMcVoxAdmFaxMinPreambleDur": cxMcVoxAdmFaxMinPreambleDur,
       "cxMcVoxAdmFaxMaxPreambleDur": cxMcVoxAdmFaxMaxPreambleDur,
       "cxMcVoxAdmFaxMinPreambleDly": cxMcVoxAdmFaxMinPreambleDly,
       "cxMcVoxAdmFaxMaxPreambleDly": cxMcVoxAdmFaxMaxPreambleDly,
       "cxMcVoxAdmFaxCedToneDetection": cxMcVoxAdmFaxCedToneDetection,
       "cxMcVoxAdmFaxCedMinToneDur": cxMcVoxAdmFaxCedMinToneDur,
       "cxMcVoxAdmFaxCedMaxToneDur": cxMcVoxAdmFaxCedMaxToneDur,
       "cxMcVoxAdmFaxMaxHdlcFlags": cxMcVoxAdmFaxMaxHdlcFlags,
       "cxMcVoxDriverOpePriv": cxMcVoxDriverOpePriv,
       "cxMcVoxOpePortPrivTable": cxMcVoxOpePortPrivTable,
       "cxMcVoxOpePortPrivEntry": cxMcVoxOpePortPrivEntry,
       "cxMcVoxOpeCardUsed": cxMcVoxOpeCardUsed,
       "cxMcVoxOpePortUsed": cxMcVoxOpePortUsed,
       "cxMcVoxOpeRingTimeOn": cxMcVoxOpeRingTimeOn,
       "cxMcVoxOpeRingTimeOff1": cxMcVoxOpeRingTimeOff1,
       "cxMcVoxOpeRingTimeOff2": cxMcVoxOpeRingTimeOff2,
       "cxMcVoxOpeEchoCancelLevel": cxMcVoxOpeEchoCancelLevel,
       "cxMcVoxOpeToneDelayAfterCnct": cxMcVoxOpeToneDelayAfterCnct,
       "cxMcVoxOpeToneDelayAfterFlash": cxMcVoxOpeToneDelayAfterFlash,
       "cxMcVoxOpeToneOffsetTxGain": cxMcVoxOpeToneOffsetTxGain,
       "cxMcVoxOpeVoiceOffsetTxGain": cxMcVoxOpeVoiceOffsetTxGain,
       "cxMcVoxOpeAc15InterDigit": cxMcVoxOpeAc15InterDigit,
       "cxMcVoxOpeMfToneThold": cxMcVoxOpeMfToneThold,
       "cxMcVoxOpePulseTmin": cxMcVoxOpePulseTmin,
       "cxMcVoxOpePulseTmax": cxMcVoxOpePulseTmax,
       "cxMcVoxOpePulseInterDigit": cxMcVoxOpePulseInterDigit,
       "cxMcVoxOpeDtmfGuard": cxMcVoxOpeDtmfGuard,
       "cxMcVoxOpeDtmfOpeLevel": cxMcVoxOpeDtmfOpeLevel,
       "cxMcVoxOpeDtmfTxTimeOn": cxMcVoxOpeDtmfTxTimeOn,
       "cxMcVoxOpeDtmfTxTimeOff": cxMcVoxOpeDtmfTxTimeOff,
       "cxMcVoxOpeFlashTmin": cxMcVoxOpeFlashTmin,
       "cxMcVoxOpeFlashTmax": cxMcVoxOpeFlashTmax,
       "cxMcVoxOpeFlashTgen": cxMcVoxOpeFlashTgen,
       "cxMcVoxOpeAfterToneSilences": cxMcVoxOpeAfterToneSilences,
       "cxMcVoxOpeFaxTxGain": cxMcVoxOpeFaxTxGain,
       "cxMcVoxOpeFaxRxGain": cxMcVoxOpeFaxRxGain,
       "cxMcVoxOpeFaxHdlcFlags": cxMcVoxOpeFaxHdlcFlags,
       "cxMcVoxOpeFaxPreambleDuration": cxMcVoxOpeFaxPreambleDuration,
       "cxMcVoxOpeFaxPreambleDelay": cxMcVoxOpeFaxPreambleDelay,
       "cxMcVoxOpeFaxCedToneDuration": cxMcVoxOpeFaxCedToneDuration,
       "cxMcVoxOpeFaxInterProtoGap": cxMcVoxOpeFaxInterProtoGap,
       "cxMcVoxOpeFaxTimerDetectSync": cxMcVoxOpeFaxTimerDetectSync,
       "cxMcVoxOpeFaxTimerWaitId": cxMcVoxOpeFaxTimerWaitId,
       "cxMcVoxOpeFaxMinPreambleDur": cxMcVoxOpeFaxMinPreambleDur,
       "cxMcVoxOpeFaxMaxPreambleDur": cxMcVoxOpeFaxMaxPreambleDur,
       "cxMcVoxOpeFaxMinPreambleDly": cxMcVoxOpeFaxMinPreambleDly,
       "cxMcVoxOpeFaxMaxPreambleDly": cxMcVoxOpeFaxMaxPreambleDly,
       "cxMcVoxOpeFaxCedToneDetection": cxMcVoxOpeFaxCedToneDetection,
       "cxMcVoxOpeFaxCedMinToneDur": cxMcVoxOpeFaxCedMinToneDur,
       "cxMcVoxOpeFaxCedMaxToneDur": cxMcVoxOpeFaxCedMaxToneDur,
       "cxMcVoxOpeFaxMaxHdlcFlags": cxMcVoxOpeFaxMaxHdlcFlags,
       "cxMcVoxTimerOpePriv": cxMcVoxTimerOpePriv,
       "cxMcVoxOpeTimerPrivTable": cxMcVoxOpeTimerPrivTable,
       "cxMcVoxOpeTimerPrivEntry": cxMcVoxOpeTimerPrivEntry,
       "cxMcVoxOpeInterfaceType": cxMcVoxOpeInterfaceType,
       "cxMcVoxOpeTimeSeizeIn": cxMcVoxOpeTimeSeizeIn,
       "cxMcVoxOpeTimeWaitDialOut": cxMcVoxOpeTimeWaitDialOut,
       "cxMcVoxOpeTimeWaitDialIn": cxMcVoxOpeTimeWaitDialIn,
       "cxMcVoxOpeTimeDialOut": cxMcVoxOpeTimeDialOut,
       "cxMcVoxOpeTimeDialIn": cxMcVoxOpeTimeDialIn,
       "cxMcVoxOpeTimeSiOff": cxMcVoxOpeTimeSiOff,
       "cxMcVoxOpeTimeProceed": cxMcVoxOpeTimeProceed,
       "cxMcVoxOpeTimeAnswer": cxMcVoxOpeTimeAnswer,
       "cxMcVoxOpeTimeBeforeToneOff": cxMcVoxOpeTimeBeforeToneOff,
       "cxMcVoxOpeTimeWinkStartIn": cxMcVoxOpeTimeWinkStartIn,
       "cxMcVoxOpeTimeWinkStartOut": cxMcVoxOpeTimeWinkStartOut,
       "cxMcVoxOpeTimeWinkMin": cxMcVoxOpeTimeWinkMin,
       "cxMcVoxOpeTimeWinkMax": cxMcVoxOpeTimeWinkMax,
       "cxMcVoxOpeTimeSeize": cxMcVoxOpeTimeSeize,
       "cxMcVoxOpeTimeDial": cxMcVoxOpeTimeDial,
       "cxMcVoxOpeTimeOffIn": cxMcVoxOpeTimeOffIn,
       "cxMcVoxOpeTimeSiOn": cxMcVoxOpeTimeSiOn,
       "cxMcVoxOpeTimeOffOut": cxMcVoxOpeTimeOffOut,
       "cxMcVoxOpeTimeDiscIn": cxMcVoxOpeTimeDiscIn,
       "cxMcVoxOpeTimeDiscOut": cxMcVoxOpeTimeDiscOut,
       "cxMcVoxOpeTimeToneOut": cxMcVoxOpeTimeToneOut,
       "cxMcVoxDiagTable": cxMcVoxDiagTable,
       "cxMcVoxDiagEntry": cxMcVoxDiagEntry,
       "cxMcVoxDiagCardIndex": cxMcVoxDiagCardIndex,
       "cxMcVoxDiagPortIndex": cxMcVoxDiagPortIndex,
       "cxMcVoxDiagScvEvents": cxMcVoxDiagScvEvents,
       "cxMcVoxDiagGsdEvents": cxMcVoxDiagGsdEvents,
       "cxMcVoxDiagToneInEvents": cxMcVoxDiagToneInEvents,
       "cxMcVoxDiagToneOutEvents": cxMcVoxDiagToneOutEvents,
       "cxMcVoxDiagFaxInEvents": cxMcVoxDiagFaxInEvents,
       "cxMcVoxDiagFaxOutEvents": cxMcVoxDiagFaxOutEvents,
       "cxMcVoxDiagGlmEvents": cxMcVoxDiagGlmEvents,
       "cxMcVoxDiagIbvDiags": cxMcVoxDiagIbvDiags,
       "cxMcVoxDiagPcvDiags": cxMcVoxDiagPcvDiags,
       "cxMcVoxDiagGcvDiags": cxMcVoxDiagGcvDiags,
       "cxMcVoxDiagFaxDiags": cxMcVoxDiagFaxDiags,
       "cxMcVoxDiagLseDiags": cxMcVoxDiagLseDiags,
       "cxMcVoxDiagScvDiags": cxMcVoxDiagScvDiags,
       "cxMcVoxDiagGlmDiags": cxMcVoxDiagGlmDiags,
       "cxMcVoxDownload": cxMcVoxDownload,
       "cxMcVoxLclExtAdmTable": cxMcVoxLclExtAdmTable,
       "cxMcVoxLclExtAdmEntry": cxMcVoxLclExtAdmEntry,
       "cxMcVoxLclExtAdmIndex": cxMcVoxLclExtAdmIndex,
       "cxMcVoxLclExtAdmRowStatus": cxMcVoxLclExtAdmRowStatus,
       "cxMcVoxLclExtAdmExt": cxMcVoxLclExtAdmExt,
       "cxMcVoxLclExtAdmHuntChnl": cxMcVoxLclExtAdmHuntChnl,
       "cxMcVoxLclExtOpeTable": cxMcVoxLclExtOpeTable,
       "cxMcVoxLclExtOpeEntry": cxMcVoxLclExtOpeEntry,
       "cxMcVoxLclExtOpeIndex": cxMcVoxLclExtOpeIndex,
       "cxMcVoxLclExtOpeExt": cxMcVoxLclExtOpeExt,
       "cxMcVoxLclExtOpeHuntChnl": cxMcVoxLclExtOpeHuntChnl,
       "cxMcVoxRegenOpe": cxMcVoxRegenOpe,
       "cxMcVoxRegenOpeExt": cxMcVoxRegenOpeExt,
       "cxMcVoxRegenOpeGid": cxMcVoxRegenOpeGid,
       "cxMcVoxRegenOpeNbDigits": cxMcVoxRegenOpeNbDigits,
       "cxMcVoxRegenOpeExtBitMask": cxMcVoxRegenOpeExtBitMask,
       "cxMcVoxTranslOpe": cxMcVoxTranslOpe,
       "cxMcVoxTranslOpeCntryCodeEnable": cxMcVoxTranslOpeCntryCodeEnable,
       "cxMcVoxTranslOpeCntryCode": cxMcVoxTranslOpeCntryCode,
       "cxMcVoxTranslOpeCntryCodeLng": cxMcVoxTranslOpeCntryCodeLng,
       "cxMcVoxTranslOpeCCPrefix": cxMcVoxTranslOpeCCPrefix,
       "cxMcVoxTranslOpeCCPrefixLng": cxMcVoxTranslOpeCCPrefixLng,
       "cxMcVoxTranslOpeAreaCodeEnable": cxMcVoxTranslOpeAreaCodeEnable,
       "cxMcVoxTranslOpeAreaCode": cxMcVoxTranslOpeAreaCode,
       "cxMcVoxTranslOpeAreaCodeLng": cxMcVoxTranslOpeAreaCodeLng,
       "cxMcVoxTranslOpeACPrefix": cxMcVoxTranslOpeACPrefix,
       "cxMcVoxTranslOpeACPrefixLng": cxMcVoxTranslOpeACPrefixLng,
       "cxMcVoxTranslOpeZoneCodeEnable": cxMcVoxTranslOpeZoneCodeEnable,
       "cxMcVoxTranslOpeZCPrefix": cxMcVoxTranslOpeZCPrefix,
       "cxMcVoxTranslOpeZCPrefixLng": cxMcVoxTranslOpeZCPrefixLng,
       "cxMcVoxHistoryTable": cxMcVoxHistoryTable,
       "cxMcVoxHistoryEntry": cxMcVoxHistoryEntry,
       "cxMcVoxHistoryIndex": cxMcVoxHistoryIndex,
       "cxMcVoxHistoryLclCardNumber": cxMcVoxHistoryLclCardNumber,
       "cxMcVoxHistoryLclPortNumber": cxMcVoxHistoryLclPortNumber,
       "cxMcVoxHistoryRmtCardNumber": cxMcVoxHistoryRmtCardNumber,
       "cxMcVoxHistoryRmtPortNumber": cxMcVoxHistoryRmtPortNumber,
       "cxMcVoxHistoryTimeStampOnLine": cxMcVoxHistoryTimeStampOnLine,
       "cxMcVoxHistoryTimeStampOffLine": cxMcVoxHistoryTimeStampOffLine,
       "cxMcVoxHistoryLnkState": cxMcVoxHistoryLnkState,
       "cxMcVoxHistoryPin": cxMcVoxHistoryPin,
       "cxMcVoxHistoryExtensionOrGrpId": cxMcVoxHistoryExtensionOrGrpId,
       "cxMcVoxHistoryPhoneNumber": cxMcVoxHistoryPhoneNumber}
)
