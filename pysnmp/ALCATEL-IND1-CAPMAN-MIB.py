# SNMP MIB module (ALCATEL-IND1-CAPMAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-CAPMAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:45 2024
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

(softentIND1CapMan,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1CapMan")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1CapManMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1)
)
alcatelIND1CapManMIB.setRevisions(
        ("2009-11-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1CapManMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1CapManMIBObjects = _AlcatelIND1CapManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1CapManMIBObjects.setStatus("current")
_AlaCapabilityManager_ObjectIdentity = ObjectIdentity
alaCapabilityManager = _AlaCapabilityManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1)
)
_AlaCapManVrfTable_Object = MibTable
alaCapManVrfTable = _AlaCapManVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaCapManVrfTable.setStatus("deprecated")
_AlaCapManVrfEntry_Object = MibTableRow
alaCapManVrfEntry = _AlaCapManVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 1, 1)
)
alaCapManVrfEntry.setIndexNames(
    (0, "ALCATEL-IND1-CAPMAN-MIB", "alaCapabilityVrfContext"),
    (0, "ALCATEL-IND1-CAPMAN-MIB", "alaCapabilityVrfCapability"),
)
if mibBuilder.loadTexts:
    alaCapManVrfEntry.setStatus("deprecated")


class _AlaCapabilityVrfContext_Type(Integer32):
    """Custom type alaCapabilityVrfContext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 1),
          ("primary", 2),
          ("subsidiary", 3))
    )


_AlaCapabilityVrfContext_Type.__name__ = "Integer32"
_AlaCapabilityVrfContext_Object = MibTableColumn
alaCapabilityVrfContext = _AlaCapabilityVrfContext_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 1, 1, 1),
    _AlaCapabilityVrfContext_Type()
)
alaCapabilityVrfContext.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaCapabilityVrfContext.setStatus("deprecated")


class _AlaCapabilityVrfCapability_Type(Integer32):
    """Custom type alaCapabilityVrfCapability based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("bgpPeers", 7),
          ("bgpRoutes", 8),
          ("ipv4Interfaces", 3),
          ("ipv4Routes", 1),
          ("ipv6Interfaces", 4),
          ("ipv6Routes", 2),
          ("maxOSPF", 11),
          ("mcastInterfaces", 5),
          ("pimRPS", 6),
          ("ripRoutes", 9),
          ("routingProtocols", 10))
    )


_AlaCapabilityVrfCapability_Type.__name__ = "Integer32"
_AlaCapabilityVrfCapability_Object = MibTableColumn
alaCapabilityVrfCapability = _AlaCapabilityVrfCapability_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 1, 1, 2),
    _AlaCapabilityVrfCapability_Type()
)
alaCapabilityVrfCapability.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaCapabilityVrfCapability.setStatus("deprecated")


class _AlaCapabilityVrfLimit_Type(Integer32):
    """Custom type alaCapabilityVrfLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524288),
    )


_AlaCapabilityVrfLimit_Type.__name__ = "Integer32"
_AlaCapabilityVrfLimit_Object = MibTableColumn
alaCapabilityVrfLimit = _AlaCapabilityVrfLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 1, 1, 3),
    _AlaCapabilityVrfLimit_Type()
)
alaCapabilityVrfLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCapabilityVrfLimit.setStatus("deprecated")
_AlaCapManTcamTable_Object = MibTable
alaCapManTcamTable = _AlaCapManTcamTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaCapManTcamTable.setStatus("deprecated")
_AlaCapManTcamEntry_Object = MibTableRow
alaCapManTcamEntry = _AlaCapManTcamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 2, 1)
)
alaCapManTcamEntry.setIndexNames(
    (0, "ALCATEL-IND1-CAPMAN-MIB", "alaCapabilityTcamContext"),
    (0, "ALCATEL-IND1-CAPMAN-MIB", "alaCapabilityTcamCapability"),
)
if mibBuilder.loadTexts:
    alaCapManTcamEntry.setStatus("deprecated")


class _AlaCapabilityTcamContext_Type(Integer32):
    """Custom type alaCapabilityTcamContext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("global", 1)
    )


_AlaCapabilityTcamContext_Type.__name__ = "Integer32"
_AlaCapabilityTcamContext_Object = MibTableColumn
alaCapabilityTcamContext = _AlaCapabilityTcamContext_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 2, 1, 1),
    _AlaCapabilityTcamContext_Type()
)
alaCapabilityTcamContext.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaCapabilityTcamContext.setStatus("deprecated")


class _AlaCapabilityTcamCapability_Type(Integer32):
    """Custom type alaCapabilityTcamCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mode", 1)
    )


_AlaCapabilityTcamCapability_Type.__name__ = "Integer32"
_AlaCapabilityTcamCapability_Object = MibTableColumn
alaCapabilityTcamCapability = _AlaCapabilityTcamCapability_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 2, 1, 2),
    _AlaCapabilityTcamCapability_Type()
)
alaCapabilityTcamCapability.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaCapabilityTcamCapability.setStatus("deprecated")


class _AlaCapabilityTcamMode_Type(Integer32):
    """Custom type alaCapabilityTcamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_AlaCapabilityTcamMode_Type.__name__ = "Integer32"
_AlaCapabilityTcamMode_Object = MibTableColumn
alaCapabilityTcamMode = _AlaCapabilityTcamMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 2, 1, 3),
    _AlaCapabilityTcamMode_Type()
)
alaCapabilityTcamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCapabilityTcamMode.setStatus("deprecated")
_AlaCapManMirrorTable_Object = MibTable
alaCapManMirrorTable = _AlaCapManMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaCapManMirrorTable.setStatus("deprecated")
_AlaCapManMirrorEntry_Object = MibTableRow
alaCapManMirrorEntry = _AlaCapManMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 3, 1)
)
alaCapManMirrorEntry.setIndexNames(
    (0, "ALCATEL-IND1-CAPMAN-MIB", "alaCapabilityMirrorContext"),
    (0, "ALCATEL-IND1-CAPMAN-MIB", "alaCapabilityMirrorCapability"),
)
if mibBuilder.loadTexts:
    alaCapManMirrorEntry.setStatus("deprecated")


class _AlaCapabilityMirrorContext_Type(Integer32):
    """Custom type alaCapabilityMirrorContext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("global", 1)
    )


_AlaCapabilityMirrorContext_Type.__name__ = "Integer32"
_AlaCapabilityMirrorContext_Object = MibTableColumn
alaCapabilityMirrorContext = _AlaCapabilityMirrorContext_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 3, 1, 1),
    _AlaCapabilityMirrorContext_Type()
)
alaCapabilityMirrorContext.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaCapabilityMirrorContext.setStatus("deprecated")


class _AlaCapabilityMirrorCapability_Type(Integer32):
    """Custom type alaCapabilityMirrorCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("maxMonitorSess", 1)
    )


_AlaCapabilityMirrorCapability_Type.__name__ = "Integer32"
_AlaCapabilityMirrorCapability_Object = MibTableColumn
alaCapabilityMirrorCapability = _AlaCapabilityMirrorCapability_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 3, 1, 2),
    _AlaCapabilityMirrorCapability_Type()
)
alaCapabilityMirrorCapability.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaCapabilityMirrorCapability.setStatus("deprecated")


class _AlaCapabilityMirrorLimit_Type(Integer32):
    """Custom type alaCapabilityMirrorLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaCapabilityMirrorLimit_Type.__name__ = "Integer32"
_AlaCapabilityMirrorLimit_Object = MibTableColumn
alaCapabilityMirrorLimit = _AlaCapabilityMirrorLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 3, 1, 3),
    _AlaCapabilityMirrorLimit_Type()
)
alaCapabilityMirrorLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCapabilityMirrorLimit.setStatus("deprecated")
_AlaCapManSourceLearningTable_Object = MibTable
alaCapManSourceLearningTable = _AlaCapManSourceLearningTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaCapManSourceLearningTable.setStatus("deprecated")
_AlaCapManSourceLearningEntry_Object = MibTableRow
alaCapManSourceLearningEntry = _AlaCapManSourceLearningEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 4, 1)
)
alaCapManSourceLearningEntry.setIndexNames(
    (0, "ALCATEL-IND1-CAPMAN-MIB", "alaCapabilitySourceLearningContext"),
    (0, "ALCATEL-IND1-CAPMAN-MIB", "alaCapabilitySourceLearningCapability"),
)
if mibBuilder.loadTexts:
    alaCapManSourceLearningEntry.setStatus("deprecated")


class _AlaCapabilitySourceLearningContext_Type(Integer32):
    """Custom type alaCapabilitySourceLearningContext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("global", 1)
    )


_AlaCapabilitySourceLearningContext_Type.__name__ = "Integer32"
_AlaCapabilitySourceLearningContext_Object = MibTableColumn
alaCapabilitySourceLearningContext = _AlaCapabilitySourceLearningContext_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 4, 1, 1),
    _AlaCapabilitySourceLearningContext_Type()
)
alaCapabilitySourceLearningContext.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaCapabilitySourceLearningContext.setStatus("deprecated")


class _AlaCapabilitySourceLearningCapability_Type(Integer32):
    """Custom type alaCapabilitySourceLearningCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mode", 1)
    )


_AlaCapabilitySourceLearningCapability_Type.__name__ = "Integer32"
_AlaCapabilitySourceLearningCapability_Object = MibTableColumn
alaCapabilitySourceLearningCapability = _AlaCapabilitySourceLearningCapability_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 4, 1, 2),
    _AlaCapabilitySourceLearningCapability_Type()
)
alaCapabilitySourceLearningCapability.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaCapabilitySourceLearningCapability.setStatus("deprecated")


class _AlaCapabilitySourceLearningMode_Type(Integer32):
    """Custom type alaCapabilitySourceLearningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("centralized", 1),
          ("distributed", 2))
    )


_AlaCapabilitySourceLearningMode_Type.__name__ = "Integer32"
_AlaCapabilitySourceLearningMode_Object = MibTableColumn
alaCapabilitySourceLearningMode = _AlaCapabilitySourceLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 4, 1, 3),
    _AlaCapabilitySourceLearningMode_Type()
)
alaCapabilitySourceLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCapabilitySourceLearningMode.setStatus("deprecated")
_AlaCapManHashControlCommands_ObjectIdentity = ObjectIdentity
alaCapManHashControlCommands = _AlaCapManHashControlCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaCapManHashControlCommands.setStatus("current")


class _AlaCapManHashMode_Type(Integer32):
    """Custom type alaCapManHashMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("brief", 1),
          ("extended", 2))
    )


_AlaCapManHashMode_Type.__name__ = "Integer32"
_AlaCapManHashMode_Object = MibScalar
alaCapManHashMode = _AlaCapManHashMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 5, 1),
    _AlaCapManHashMode_Type()
)
alaCapManHashMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCapManHashMode.setStatus("current")


class _AlaCapManUdpTcpPortMode_Type(Integer32):
    """Custom type alaCapManUdpTcpPortMode based on Integer32"""
    defaultValue = 2

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


_AlaCapManUdpTcpPortMode_Type.__name__ = "Integer32"
_AlaCapManUdpTcpPortMode_Object = MibScalar
alaCapManUdpTcpPortMode = _AlaCapManUdpTcpPortMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 5, 2),
    _AlaCapManUdpTcpPortMode_Type()
)
alaCapManUdpTcpPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCapManUdpTcpPortMode.setStatus("current")


class _AlaCapManNonUCHashControl_Type(Integer32):
    """Custom type alaCapManNonUCHashControl based on Integer32"""
    defaultValue = 2

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


_AlaCapManNonUCHashControl_Type.__name__ = "Integer32"
_AlaCapManNonUCHashControl_Object = MibScalar
alaCapManNonUCHashControl = _AlaCapManNonUCHashControl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 5, 3),
    _AlaCapManNonUCHashControl_Type()
)
alaCapManNonUCHashControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCapManNonUCHashControl.setStatus("current")
_AlaCapManSwLicensingConfig_ObjectIdentity = ObjectIdentity
alaCapManSwLicensingConfig = _AlaCapManSwLicensingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 6)
)


class _AlaCapManSwLicensingAction_Type(Integer32):
    """Custom type alaCapManSwLicensingAction based on Integer32"""
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
        *(("applyFile", 1),
          ("applyKey", 2),
          ("deactivate", 3),
          ("default", 0))
    )


_AlaCapManSwLicensingAction_Type.__name__ = "Integer32"
_AlaCapManSwLicensingAction_Object = MibScalar
alaCapManSwLicensingAction = _AlaCapManSwLicensingAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 6, 1),
    _AlaCapManSwLicensingAction_Type()
)
alaCapManSwLicensingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCapManSwLicensingAction.setStatus("current")


class _AlaCapManSwLicensingActionArg_Type(SnmpAdminString):
    """Custom type alaCapManSwLicensingActionArg based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaCapManSwLicensingActionArg_Type.__name__ = "SnmpAdminString"
_AlaCapManSwLicensingActionArg_Object = MibScalar
alaCapManSwLicensingActionArg = _AlaCapManSwLicensingActionArg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 6, 2),
    _AlaCapManSwLicensingActionArg_Type()
)
alaCapManSwLicensingActionArg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCapManSwLicensingActionArg.setStatus("current")


class _AlaCapManVcSwLicensingAction_Type(Integer32):
    """Custom type alaCapManVcSwLicensingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("applyFile", 1),
          ("default", 0))
    )


_AlaCapManVcSwLicensingAction_Type.__name__ = "Integer32"
_AlaCapManVcSwLicensingAction_Object = MibScalar
alaCapManVcSwLicensingAction = _AlaCapManVcSwLicensingAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 6, 3),
    _AlaCapManVcSwLicensingAction_Type()
)
alaCapManVcSwLicensingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCapManVcSwLicensingAction.setStatus("current")


class _AlaCapManVcSwLicensingActionArg_Type(SnmpAdminString):
    """Custom type alaCapManVcSwLicensingActionArg based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaCapManVcSwLicensingActionArg_Type.__name__ = "SnmpAdminString"
_AlaCapManVcSwLicensingActionArg_Object = MibScalar
alaCapManVcSwLicensingActionArg = _AlaCapManVcSwLicensingActionArg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 6, 4),
    _AlaCapManVcSwLicensingActionArg_Type()
)
alaCapManVcSwLicensingActionArg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCapManVcSwLicensingActionArg.setStatus("current")
_AlaCapManSwLicensingInfoTable_Object = MibTable
alaCapManSwLicensingInfoTable = _AlaCapManSwLicensingInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaCapManSwLicensingInfoTable.setStatus("current")
_AlaCapManSwLicensingInfoEntry_Object = MibTableRow
alaCapManSwLicensingInfoEntry = _AlaCapManSwLicensingInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 7, 1)
)
alaCapManSwLicensingInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-CAPMAN-MIB", "alaLicenseId"),
)
if mibBuilder.loadTexts:
    alaCapManSwLicensingInfoEntry.setStatus("current")


class _AlaLicenseId_Type(Unsigned32):
    """Custom type alaLicenseId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaLicenseId_Type.__name__ = "Unsigned32"
_AlaLicenseId_Object = MibTableColumn
alaLicenseId = _AlaLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 7, 1, 1),
    _AlaLicenseId_Type()
)
alaLicenseId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaLicenseId.setStatus("current")


class _AlaLicensedApplication_Type(SnmpAdminString):
    """Custom type alaLicensedApplication based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaLicensedApplication_Type.__name__ = "SnmpAdminString"
_AlaLicensedApplication_Object = MibTableColumn
alaLicensedApplication = _AlaLicensedApplication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 7, 1, 2),
    _AlaLicensedApplication_Type()
)
alaLicensedApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLicensedApplication.setStatus("current")


class _AlaLicenseType_Type(Integer32):
    """Custom type alaLicenseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("demo", 1),
          ("invalid", 0),
          ("permanent", 2))
    )


_AlaLicenseType_Type.__name__ = "Integer32"
_AlaLicenseType_Object = MibTableColumn
alaLicenseType = _AlaLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 7, 1, 3),
    _AlaLicenseType_Type()
)
alaLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLicenseType.setStatus("current")


class _AlaLicenseTimeRemaining_Type(Integer32):
    """Custom type alaLicenseTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 60),
    )


_AlaLicenseTimeRemaining_Type.__name__ = "Integer32"
_AlaLicenseTimeRemaining_Object = MibTableColumn
alaLicenseTimeRemaining = _AlaLicenseTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 7, 1, 4),
    _AlaLicenseTimeRemaining_Type()
)
alaLicenseTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLicenseTimeRemaining.setStatus("current")
_AlaCapabilityIpmcMaxLimits_ObjectIdentity = ObjectIdentity
alaCapabilityIpmcMaxLimits = _AlaCapabilityIpmcMaxLimits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 8)
)


class _AlaCapabilityIpmcMaxAdminLimit_Type(Integer32):
    """Custom type alaCapabilityIpmcMaxAdminLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaCapabilityIpmcMaxAdminLimit_Type.__name__ = "Integer32"
_AlaCapabilityIpmcMaxAdminLimit_Object = MibScalar
alaCapabilityIpmcMaxAdminLimit = _AlaCapabilityIpmcMaxAdminLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 8, 1),
    _AlaCapabilityIpmcMaxAdminLimit_Type()
)
alaCapabilityIpmcMaxAdminLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCapabilityIpmcMaxAdminLimit.setStatus("current")


class _AlaCapabilityIpmcMaxOperLimit_Type(Integer32):
    """Custom type alaCapabilityIpmcMaxOperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaCapabilityIpmcMaxOperLimit_Type.__name__ = "Integer32"
_AlaCapabilityIpmcMaxOperLimit_Object = MibScalar
alaCapabilityIpmcMaxOperLimit = _AlaCapabilityIpmcMaxOperLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 8, 2),
    _AlaCapabilityIpmcMaxOperLimit_Type()
)
alaCapabilityIpmcMaxOperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCapabilityIpmcMaxOperLimit.setStatus("current")
_AlaCapManFeatureControlCommands_ObjectIdentity = ObjectIdentity
alaCapManFeatureControlCommands = _AlaCapManFeatureControlCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 9)
)


class _AlaCapManDcbCfgMode_Type(Integer32):
    """Custom type alaCapManDcbCfgMode based on Integer32"""
    defaultValue = 1

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


_AlaCapManDcbCfgMode_Type.__name__ = "Integer32"
_AlaCapManDcbCfgMode_Object = MibScalar
alaCapManDcbCfgMode = _AlaCapManDcbCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 9, 1),
    _AlaCapManDcbCfgMode_Type()
)
alaCapManDcbCfgMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCapManDcbCfgMode.setStatus("current")


class _AlaCapManDcbOprMode_Type(Integer32):
    """Custom type alaCapManDcbOprMode based on Integer32"""
    defaultValue = 1

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


_AlaCapManDcbOprMode_Type.__name__ = "Integer32"
_AlaCapManDcbOprMode_Object = MibScalar
alaCapManDcbOprMode = _AlaCapManDcbOprMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 9, 2),
    _AlaCapManDcbOprMode_Type()
)
alaCapManDcbOprMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCapManDcbOprMode.setStatus("current")
_AlaCapManVcSwLicensingInfoTable_Object = MibTable
alaCapManVcSwLicensingInfoTable = _AlaCapManVcSwLicensingInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    alaCapManVcSwLicensingInfoTable.setStatus("current")
_AlaCapManVcSwLicensingInfoEntry_Object = MibTableRow
alaCapManVcSwLicensingInfoEntry = _AlaCapManVcSwLicensingInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 10, 1)
)
alaCapManVcSwLicensingInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-CAPMAN-MIB", "alaVcLicensedSerialNum"),
    (0, "ALCATEL-IND1-CAPMAN-MIB", "alaVcLicensedMacAddress"),
)
if mibBuilder.loadTexts:
    alaCapManVcSwLicensingInfoEntry.setStatus("current")


class _AlaVcLicensedSerialNum_Type(OctetString):
    """Custom type alaVcLicensedSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_AlaVcLicensedSerialNum_Type.__name__ = "OctetString"
_AlaVcLicensedSerialNum_Object = MibTableColumn
alaVcLicensedSerialNum = _AlaVcLicensedSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 10, 1, 1),
    _AlaVcLicensedSerialNum_Type()
)
alaVcLicensedSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVcLicensedSerialNum.setStatus("current")
_AlaVcLicensedMacAddress_Type = MacAddress
_AlaVcLicensedMacAddress_Object = MibTableColumn
alaVcLicensedMacAddress = _AlaVcLicensedMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 10, 1, 2),
    _AlaVcLicensedMacAddress_Type()
)
alaVcLicensedMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVcLicensedMacAddress.setStatus("current")


class _AlaVcLicenseType_Type(Integer32):
    """Custom type alaVcLicenseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("demo", 1),
          ("permanent", 2))
    )


_AlaVcLicenseType_Type.__name__ = "Integer32"
_AlaVcLicenseType_Object = MibTableColumn
alaVcLicenseType = _AlaVcLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 10, 1, 3),
    _AlaVcLicenseType_Type()
)
alaVcLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVcLicenseType.setStatus("current")


class _AlaVcLicenseVcSlot_Type(Integer32):
    """Custom type alaVcLicenseVcSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaVcLicenseVcSlot_Type.__name__ = "Integer32"
_AlaVcLicenseVcSlot_Object = MibTableColumn
alaVcLicenseVcSlot = _AlaVcLicenseVcSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 10, 1, 4),
    _AlaVcLicenseVcSlot_Type()
)
alaVcLicenseVcSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVcLicenseVcSlot.setStatus("current")


class _AlaVcLicenseBitMap_Type(Integer32):
    """Custom type alaVcLicenseBitMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaVcLicenseBitMap_Type.__name__ = "Integer32"
_AlaVcLicenseBitMap_Object = MibTableColumn
alaVcLicenseBitMap = _AlaVcLicenseBitMap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 10, 1, 5),
    _AlaVcLicenseBitMap_Type()
)
alaVcLicenseBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVcLicenseBitMap.setStatus("current")


class _AlaVcLicenseTimeRemain_Type(Integer32):
    """Custom type alaVcLicenseTimeRemain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 60),
    )


_AlaVcLicenseTimeRemain_Type.__name__ = "Integer32"
_AlaVcLicenseTimeRemain_Object = MibTableColumn
alaVcLicenseTimeRemain = _AlaVcLicenseTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 1, 10, 1, 6),
    _AlaVcLicenseTimeRemain_Type()
)
alaVcLicenseTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVcLicenseTimeRemain.setStatus("current")
_AlaCapManConformance_ObjectIdentity = ObjectIdentity
alaCapManConformance = _AlaCapManConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 2)
)
_AlaCapManGroups_ObjectIdentity = ObjectIdentity
alaCapManGroups = _AlaCapManGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 2, 1)
)
_AlaCapManCompliances_ObjectIdentity = ObjectIdentity
alaCapManCompliances = _AlaCapManCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 2, 2)
)

# Managed Objects groups

alaCapManVrfTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 2, 1, 1)
)
alaCapManVrfTableGroup.setObjects(
    ("ALCATEL-IND1-CAPMAN-MIB", "alaCapabilityVrfLimit")
)
if mibBuilder.loadTexts:
    alaCapManVrfTableGroup.setStatus("current")

alaCapManTcamTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 2, 1, 2)
)
alaCapManTcamTableGroup.setObjects(
    ("ALCATEL-IND1-CAPMAN-MIB", "alaCapabilityTcamMode")
)
if mibBuilder.loadTexts:
    alaCapManTcamTableGroup.setStatus("current")

alaCapManMirrorTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 2, 1, 3)
)
alaCapManMirrorTableGroup.setObjects(
    ("ALCATEL-IND1-CAPMAN-MIB", "alaCapabilityMirrorLimit")
)
if mibBuilder.loadTexts:
    alaCapManMirrorTableGroup.setStatus("current")

alaCapManSourceLearningTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 2, 1, 4)
)
alaCapManSourceLearningTableGroup.setObjects(
    ("ALCATEL-IND1-CAPMAN-MIB", "alaCapabilitySourceLearningMode")
)
if mibBuilder.loadTexts:
    alaCapManSourceLearningTableGroup.setStatus("current")

alaCapManHashControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 2, 1, 5)
)
alaCapManHashControlGroup.setObjects(
      *(("ALCATEL-IND1-CAPMAN-MIB", "alaCapManHashMode"),
        ("ALCATEL-IND1-CAPMAN-MIB", "alaCapManUdpTcpPortMode"),
        ("ALCATEL-IND1-CAPMAN-MIB", "alaCapManNonUCHashControl"))
)
if mibBuilder.loadTexts:
    alaCapManHashControlGroup.setStatus("current")

alaCapManSwLicensingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 2, 1, 6)
)
alaCapManSwLicensingGroup.setObjects(
      *(("ALCATEL-IND1-CAPMAN-MIB", "alaCapManSwLicensingAction"),
        ("ALCATEL-IND1-CAPMAN-MIB", "alaCapManSwLicensingActionArg"),
        ("ALCATEL-IND1-CAPMAN-MIB", "alaCapManVcSwLicensingAction"),
        ("ALCATEL-IND1-CAPMAN-MIB", "alaCapManVcSwLicensingActionArg"))
)
if mibBuilder.loadTexts:
    alaCapManSwLicensingGroup.setStatus("current")

alaCapManSwLicensingInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 2, 1, 7)
)
alaCapManSwLicensingInfoGroup.setObjects(
      *(("ALCATEL-IND1-CAPMAN-MIB", "alaLicensedApplication"),
        ("ALCATEL-IND1-CAPMAN-MIB", "alaLicenseType"),
        ("ALCATEL-IND1-CAPMAN-MIB", "alaLicenseTimeRemaining"))
)
if mibBuilder.loadTexts:
    alaCapManSwLicensingInfoGroup.setStatus("current")

alaCapabilityIpmcMaxLimitsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 2, 1, 8)
)
alaCapabilityIpmcMaxLimitsGroup.setObjects(
      *(("ALCATEL-IND1-CAPMAN-MIB", "alaCapabilityIpmcMaxAdminLimit"),
        ("ALCATEL-IND1-CAPMAN-MIB", "alaCapabilityIpmcMaxOperLimit"))
)
if mibBuilder.loadTexts:
    alaCapabilityIpmcMaxLimitsGroup.setStatus("current")

alaCapManDcbCfgModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 2, 1, 9)
)
alaCapManDcbCfgModeGroup.setObjects(
      *(("ALCATEL-IND1-CAPMAN-MIB", "alaCapManDcbCfgMode"),
        ("ALCATEL-IND1-CAPMAN-MIB", "alaCapManDcbOprMode"))
)
if mibBuilder.loadTexts:
    alaCapManDcbCfgModeGroup.setStatus("current")

alaVcLicenseCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 2, 1, 10)
)
alaVcLicenseCfgGroup.setObjects(
      *(("ALCATEL-IND1-CAPMAN-MIB", "alaVcLicenseBitMap"),
        ("ALCATEL-IND1-CAPMAN-MIB", "alaVcLicenseTimeRemain"),
        ("ALCATEL-IND1-CAPMAN-MIB", "alaVcLicenseType"),
        ("ALCATEL-IND1-CAPMAN-MIB", "alaVcLicenseVcSlot"))
)
if mibBuilder.loadTexts:
    alaVcLicenseCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaCapManCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alaCapManCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-CAPMAN-MIB",
    **{"alcatelIND1CapManMIB": alcatelIND1CapManMIB,
       "alcatelIND1CapManMIBObjects": alcatelIND1CapManMIBObjects,
       "alaCapabilityManager": alaCapabilityManager,
       "alaCapManVrfTable": alaCapManVrfTable,
       "alaCapManVrfEntry": alaCapManVrfEntry,
       "alaCapabilityVrfContext": alaCapabilityVrfContext,
       "alaCapabilityVrfCapability": alaCapabilityVrfCapability,
       "alaCapabilityVrfLimit": alaCapabilityVrfLimit,
       "alaCapManTcamTable": alaCapManTcamTable,
       "alaCapManTcamEntry": alaCapManTcamEntry,
       "alaCapabilityTcamContext": alaCapabilityTcamContext,
       "alaCapabilityTcamCapability": alaCapabilityTcamCapability,
       "alaCapabilityTcamMode": alaCapabilityTcamMode,
       "alaCapManMirrorTable": alaCapManMirrorTable,
       "alaCapManMirrorEntry": alaCapManMirrorEntry,
       "alaCapabilityMirrorContext": alaCapabilityMirrorContext,
       "alaCapabilityMirrorCapability": alaCapabilityMirrorCapability,
       "alaCapabilityMirrorLimit": alaCapabilityMirrorLimit,
       "alaCapManSourceLearningTable": alaCapManSourceLearningTable,
       "alaCapManSourceLearningEntry": alaCapManSourceLearningEntry,
       "alaCapabilitySourceLearningContext": alaCapabilitySourceLearningContext,
       "alaCapabilitySourceLearningCapability": alaCapabilitySourceLearningCapability,
       "alaCapabilitySourceLearningMode": alaCapabilitySourceLearningMode,
       "alaCapManHashControlCommands": alaCapManHashControlCommands,
       "alaCapManHashMode": alaCapManHashMode,
       "alaCapManUdpTcpPortMode": alaCapManUdpTcpPortMode,
       "alaCapManNonUCHashControl": alaCapManNonUCHashControl,
       "alaCapManSwLicensingConfig": alaCapManSwLicensingConfig,
       "alaCapManSwLicensingAction": alaCapManSwLicensingAction,
       "alaCapManSwLicensingActionArg": alaCapManSwLicensingActionArg,
       "alaCapManVcSwLicensingAction": alaCapManVcSwLicensingAction,
       "alaCapManVcSwLicensingActionArg": alaCapManVcSwLicensingActionArg,
       "alaCapManSwLicensingInfoTable": alaCapManSwLicensingInfoTable,
       "alaCapManSwLicensingInfoEntry": alaCapManSwLicensingInfoEntry,
       "alaLicenseId": alaLicenseId,
       "alaLicensedApplication": alaLicensedApplication,
       "alaLicenseType": alaLicenseType,
       "alaLicenseTimeRemaining": alaLicenseTimeRemaining,
       "alaCapabilityIpmcMaxLimits": alaCapabilityIpmcMaxLimits,
       "alaCapabilityIpmcMaxAdminLimit": alaCapabilityIpmcMaxAdminLimit,
       "alaCapabilityIpmcMaxOperLimit": alaCapabilityIpmcMaxOperLimit,
       "alaCapManFeatureControlCommands": alaCapManFeatureControlCommands,
       "alaCapManDcbCfgMode": alaCapManDcbCfgMode,
       "alaCapManDcbOprMode": alaCapManDcbOprMode,
       "alaCapManVcSwLicensingInfoTable": alaCapManVcSwLicensingInfoTable,
       "alaCapManVcSwLicensingInfoEntry": alaCapManVcSwLicensingInfoEntry,
       "alaVcLicensedSerialNum": alaVcLicensedSerialNum,
       "alaVcLicensedMacAddress": alaVcLicensedMacAddress,
       "alaVcLicenseType": alaVcLicenseType,
       "alaVcLicenseVcSlot": alaVcLicenseVcSlot,
       "alaVcLicenseBitMap": alaVcLicenseBitMap,
       "alaVcLicenseTimeRemain": alaVcLicenseTimeRemain,
       "alaCapManConformance": alaCapManConformance,
       "alaCapManGroups": alaCapManGroups,
       "alaCapManVrfTableGroup": alaCapManVrfTableGroup,
       "alaCapManTcamTableGroup": alaCapManTcamTableGroup,
       "alaCapManMirrorTableGroup": alaCapManMirrorTableGroup,
       "alaCapManSourceLearningTableGroup": alaCapManSourceLearningTableGroup,
       "alaCapManHashControlGroup": alaCapManHashControlGroup,
       "alaCapManSwLicensingGroup": alaCapManSwLicensingGroup,
       "alaCapManSwLicensingInfoGroup": alaCapManSwLicensingInfoGroup,
       "alaCapabilityIpmcMaxLimitsGroup": alaCapabilityIpmcMaxLimitsGroup,
       "alaCapManDcbCfgModeGroup": alaCapManDcbCfgModeGroup,
       "alaVcLicenseCfgGroup": alaVcLicenseCfgGroup,
       "alaCapManCompliances": alaCapManCompliances,
       "alaCapManCompliance": alaCapManCompliance}
)
