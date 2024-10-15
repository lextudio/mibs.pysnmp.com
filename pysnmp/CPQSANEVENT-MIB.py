# SNMP MIB module (CPQSANEVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQSANEVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:39 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Compaq_ObjectIdentity = ObjectIdentity
compaq = _Compaq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232)
)
_CpqSanAppliance_ObjectIdentity = ObjectIdentity
cpqSanAppliance = _CpqSanAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 151)
)
_SanEvent_ObjectIdentity = ObjectIdentity
sanEvent = _SanEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 151, 101)
)
_SanEventObj_ObjectIdentity = ObjectIdentity
sanEventObj = _SanEventObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 151, 101, 100)
)


class _SanEventEventCode_Type(OctetString):
    """Custom type sanEventEventCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_SanEventEventCode_Type.__name__ = "OctetString"
_SanEventEventCode_Object = MibScalar
sanEventEventCode = _SanEventEventCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 101, 100, 1),
    _SanEventEventCode_Type()
)
sanEventEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sanEventEventCode.setStatus("mandatory")


class _SanEventIPAddress_Type(OctetString):
    """Custom type sanEventIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_SanEventIPAddress_Type.__name__ = "OctetString"
_SanEventIPAddress_Object = MibScalar
sanEventIPAddress = _SanEventIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 101, 100, 2),
    _SanEventIPAddress_Type()
)
sanEventIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sanEventIPAddress.setStatus("mandatory")
_SanEventSeverity_Type = Integer32
_SanEventSeverity_Object = MibScalar
sanEventSeverity = _SanEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 101, 100, 3),
    _SanEventSeverity_Type()
)
sanEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sanEventSeverity.setStatus("mandatory")
_SanEventCategory_Type = Integer32
_SanEventCategory_Object = MibScalar
sanEventCategory = _SanEventCategory_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 101, 100, 4),
    _SanEventCategory_Type()
)
sanEventCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sanEventCategory.setStatus("mandatory")


class _SanEventGroup_Type(OctetString):
    """Custom type sanEventGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_SanEventGroup_Type.__name__ = "OctetString"
_SanEventGroup_Object = MibScalar
sanEventGroup = _SanEventGroup_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 101, 100, 5),
    _SanEventGroup_Type()
)
sanEventGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sanEventGroup.setStatus("optional")


class _SanEventSourceType_Type(OctetString):
    """Custom type sanEventSourceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_SanEventSourceType_Type.__name__ = "OctetString"
_SanEventSourceType_Object = MibScalar
sanEventSourceType = _SanEventSourceType_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 101, 100, 6),
    _SanEventSourceType_Type()
)
sanEventSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sanEventSourceType.setStatus("optional")


class _SanEventSourceSubtype_Type(OctetString):
    """Custom type sanEventSourceSubtype based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_SanEventSourceSubtype_Type.__name__ = "OctetString"
_SanEventSourceSubtype_Object = MibScalar
sanEventSourceSubtype = _SanEventSourceSubtype_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 101, 100, 7),
    _SanEventSourceSubtype_Type()
)
sanEventSourceSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sanEventSourceSubtype.setStatus("optional")


class _SanEventURL_Type(OctetString):
    """Custom type sanEventURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_SanEventURL_Type.__name__ = "OctetString"
_SanEventURL_Object = MibScalar
sanEventURL = _SanEventURL_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 101, 100, 8),
    _SanEventURL_Type()
)
sanEventURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sanEventURL.setStatus("optional")


class _SanEventDesc_Type(OctetString):
    """Custom type sanEventDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_SanEventDesc_Type.__name__ = "OctetString"
_SanEventDesc_Object = MibScalar
sanEventDesc = _SanEventDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 101, 100, 9),
    _SanEventDesc_Type()
)
sanEventDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sanEventDesc.setStatus("optional")

# Managed Objects groups


# Notification objects

sanEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 151, 101, 0, 1)
)
sanEventTrap.setObjects(
      *(("CPQSANEVENT-MIB", "sanEventEventCode"),
        ("CPQSANEVENT-MIB", "sanEventIPAddress"),
        ("CPQSANEVENT-MIB", "sanEventSeverity"),
        ("CPQSANEVENT-MIB", "sanEventCategory"),
        ("CPQSANEVENT-MIB", "sanEventGroup"),
        ("CPQSANEVENT-MIB", "sanEventSourceType"),
        ("CPQSANEVENT-MIB", "sanEventSourceSubtype"),
        ("CPQSANEVENT-MIB", "sanEventURL"),
        ("CPQSANEVENT-MIB", "sanEventDesc"))
)
if mibBuilder.loadTexts:
    sanEventTrap.setStatus(
        ""
    )

sanTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 151, 101, 0, 2)
)
sanTestTrap.setObjects(
      *(("CPQSANEVENT-MIB", "sanEventIPAddress"),
        ("CPQSANEVENT-MIB", "sanEventSeverity"),
        ("CPQSANEVENT-MIB", "sanEventSourceType"),
        ("CPQSANEVENT-MIB", "sanEventSourceSubtype"),
        ("CPQSANEVENT-MIB", "sanEventURL"))
)
if mibBuilder.loadTexts:
    sanTestTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQSANEVENT-MIB",
    **{"compaq": compaq,
       "cpqSanAppliance": cpqSanAppliance,
       "sanEvent": sanEvent,
       "sanEventTrap": sanEventTrap,
       "sanTestTrap": sanTestTrap,
       "sanEventObj": sanEventObj,
       "sanEventEventCode": sanEventEventCode,
       "sanEventIPAddress": sanEventIPAddress,
       "sanEventSeverity": sanEventSeverity,
       "sanEventCategory": sanEventCategory,
       "sanEventGroup": sanEventGroup,
       "sanEventSourceType": sanEventSourceType,
       "sanEventSourceSubtype": sanEventSourceSubtype,
       "sanEventURL": sanEventURL,
       "sanEventDesc": sanEventDesc}
)
