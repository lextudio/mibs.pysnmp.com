# SNMP MIB module (REDSTONE-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:35 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

(RsTimeSlotMap,) = mibBuilder.importSymbols(
    "REDSTONE-TC",
    "RsTimeSlotMap")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rsDs1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5)
)
rsDs1MIB.setRevisions(
        ("1999-06-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsDs1Objects_ObjectIdentity = ObjectIdentity
rsDs1Objects = _RsDs1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 1)
)
_RsDsx1ConfigTable_Object = MibTable
rsDsx1ConfigTable = _RsDsx1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    rsDsx1ConfigTable.setStatus("current")
_RsDsx1ConfigEntry_Object = MibTableRow
rsDsx1ConfigEntry = _RsDsx1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 1, 1, 1)
)
rsDsx1ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsDsx1ConfigEntry.setStatus("current")
_RsDsx1TimeSlotMap_Type = RsTimeSlotMap
_RsDsx1TimeSlotMap_Object = MibTableColumn
rsDsx1TimeSlotMap = _RsDsx1TimeSlotMap_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 1, 1, 1, 1),
    _RsDsx1TimeSlotMap_Type()
)
rsDsx1TimeSlotMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDsx1TimeSlotMap.setStatus("current")


class _RsDsx1Ds1ChannelNumber_Type(Integer32):
    """Custom type rsDsx1Ds1ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_RsDsx1Ds1ChannelNumber_Type.__name__ = "Integer32"
_RsDsx1Ds1ChannelNumber_Object = MibTableColumn
rsDsx1Ds1ChannelNumber = _RsDsx1Ds1ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 1, 1, 1, 2),
    _RsDsx1Ds1ChannelNumber_Type()
)
rsDsx1Ds1ChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDsx1Ds1ChannelNumber.setStatus("current")


class _RsDsx1Capabilities_Type(Integer32):
    """Custom type rsDsx1Capabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RsDsx1Capabilities_Type.__name__ = "Integer32"
_RsDsx1Capabilities_Object = MibTableColumn
rsDsx1Capabilities = _RsDsx1Capabilities_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 1, 1, 1, 3),
    _RsDsx1Capabilities_Type()
)
rsDsx1Capabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDsx1Capabilities.setStatus("current")


class _RsDsx1Mode_Type(Integer32):
    """Custom type rsDsx1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("j1", 3),
          ("t1", 1))
    )


_RsDsx1Mode_Type.__name__ = "Integer32"
_RsDsx1Mode_Object = MibTableColumn
rsDsx1Mode = _RsDsx1Mode_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 1, 1, 1, 4),
    _RsDsx1Mode_Type()
)
rsDsx1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDsx1Mode.setStatus("current")


class _RsDsx1LineBuildOutCapabilities_Type(Integer32):
    """Custom type rsDsx1LineBuildOutCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_RsDsx1LineBuildOutCapabilities_Type.__name__ = "Integer32"
_RsDsx1LineBuildOutCapabilities_Object = MibTableColumn
rsDsx1LineBuildOutCapabilities = _RsDsx1LineBuildOutCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 1, 1, 1, 5),
    _RsDsx1LineBuildOutCapabilities_Type()
)
rsDsx1LineBuildOutCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDsx1LineBuildOutCapabilities.setStatus("current")


class _RsDsx1LineBuildOutType_Type(Integer32):
    """Custom type rsDsx1LineBuildOutType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("longHaul", 2),
          ("notSupported", 3),
          ("shortHaul", 1))
    )


_RsDsx1LineBuildOutType_Type.__name__ = "Integer32"
_RsDsx1LineBuildOutType_Object = MibTableColumn
rsDsx1LineBuildOutType = _RsDsx1LineBuildOutType_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 1, 1, 1, 6),
    _RsDsx1LineBuildOutType_Type()
)
rsDsx1LineBuildOutType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDsx1LineBuildOutType.setStatus("current")


class _RsDsx1LineAttenuation_Type(Integer32):
    """Custom type rsDsx1LineAttenuation based on Integer32"""
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
        *(("db0", 1),
          ("dbMinus15", 3),
          ("dbMinus22Point5", 4),
          ("dbMinus7Point5", 2),
          ("notSupported", 5))
    )


_RsDsx1LineAttenuation_Type.__name__ = "Integer32"
_RsDsx1LineAttenuation_Object = MibTableColumn
rsDsx1LineAttenuation = _RsDsx1LineAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 1, 1, 1, 7),
    _RsDsx1LineAttenuation_Type()
)
rsDsx1LineAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDsx1LineAttenuation.setStatus("current")


class _RsDsx1LineLength_Type(Integer32):
    """Custom type rsDsx1LineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_RsDsx1LineLength_Type.__name__ = "Integer32"
_RsDsx1LineLength_Object = MibTableColumn
rsDsx1LineLength = _RsDsx1LineLength_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 1, 1, 1, 8),
    _RsDsx1LineLength_Type()
)
rsDsx1LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDsx1LineLength.setStatus("current")
if mibBuilder.loadTexts:
    rsDsx1LineLength.setUnits("meters")
_RsDs1Conformance_ObjectIdentity = ObjectIdentity
rsDs1Conformance = _RsDs1Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 4)
)
_RsDs1Compliances_ObjectIdentity = ObjectIdentity
rsDs1Compliances = _RsDs1Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 4, 1)
)
_RsDs1Groups_ObjectIdentity = ObjectIdentity
rsDs1Groups = _RsDs1Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 4, 2)
)

# Managed Objects groups

rsDs1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 4, 2, 1)
)
rsDs1Group.setObjects(
      *(("REDSTONE-DS1-MIB", "rsDsx1TimeSlotMap"),
        ("REDSTONE-DS1-MIB", "rsDsx1Ds1ChannelNumber"))
)
if mibBuilder.loadTexts:
    rsDs1Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsDs1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 5, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsDs1Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-DS1-MIB",
    **{"rsDs1MIB": rsDs1MIB,
       "rsDs1Objects": rsDs1Objects,
       "rsDsx1ConfigTable": rsDsx1ConfigTable,
       "rsDsx1ConfigEntry": rsDsx1ConfigEntry,
       "rsDsx1TimeSlotMap": rsDsx1TimeSlotMap,
       "rsDsx1Ds1ChannelNumber": rsDsx1Ds1ChannelNumber,
       "rsDsx1Capabilities": rsDsx1Capabilities,
       "rsDsx1Mode": rsDsx1Mode,
       "rsDsx1LineBuildOutCapabilities": rsDsx1LineBuildOutCapabilities,
       "rsDsx1LineBuildOutType": rsDsx1LineBuildOutType,
       "rsDsx1LineAttenuation": rsDsx1LineAttenuation,
       "rsDsx1LineLength": rsDsx1LineLength,
       "rsDs1Conformance": rsDs1Conformance,
       "rsDs1Compliances": rsDs1Compliances,
       "rsDs1Compliance": rsDs1Compliance,
       "rsDs1Groups": rsDs1Groups,
       "rsDs1Group": rsDs1Group}
)
