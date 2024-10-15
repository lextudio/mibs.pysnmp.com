# SNMP MIB module (ALCATEL-IND1-IPMRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-IPMRM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:15 2024
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

(routingIND1Ipmrm,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Ipmrm")

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

alcatelIND1IPMRMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1)
)
alcatelIND1IPMRMMIB.setRevisions(
        ("2012-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1IPMRMMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1IPMRMMIBObjects = _AlcatelIND1IPMRMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1)
)
_AlaIpmrmGlobalConfig_ObjectIdentity = ObjectIdentity
alaIpmrmGlobalConfig = _AlaIpmrmGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1)
)


class _AlaIpmrmMbrStatus_Type(Integer32):
    """Custom type alaIpmrmMbrStatus based on Integer32"""
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


_AlaIpmrmMbrStatus_Type.__name__ = "Integer32"
_AlaIpmrmMbrStatus_Object = MibScalar
alaIpmrmMbrStatus = _AlaIpmrmMbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1, 1),
    _AlaIpmrmMbrStatus_Type()
)
alaIpmrmMbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmrmMbrStatus.setStatus("current")


class _AlaIpmrmMbrProtocolApps_Type(Bits):
    """Custom type alaIpmrmMbrProtocolApps based on Bits"""
    namedValues = NamedValues(
        *(("dvmrp", 0),
          ("pim", 1))
    )

_AlaIpmrmMbrProtocolApps_Type.__name__ = "Bits"
_AlaIpmrmMbrProtocolApps_Object = MibScalar
alaIpmrmMbrProtocolApps = _AlaIpmrmMbrProtocolApps_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1, 2),
    _AlaIpmrmMbrProtocolApps_Type()
)
alaIpmrmMbrProtocolApps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmrmMbrProtocolApps.setStatus("current")
_AlcatelIND1IPMRMMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1IPMRMMIBConformance = _AlcatelIND1IPMRMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2)
)
_AlcatelIND1IPMRMMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1IPMRMMIBCompliances = _AlcatelIND1IPMRMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 1)
)
_AlcatelIND1IPMRMMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1IPMRMMIBGroups = _AlcatelIND1IPMRMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 2)
)

# Managed Objects groups

alaIpmrmConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 2, 1)
)
alaIpmrmConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmMbrStatus"),
        ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmMbrProtocolApps"))
)
if mibBuilder.loadTexts:
    alaIpmrmConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaIpmrmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaIpmrmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-IPMRM-MIB",
    **{"alcatelIND1IPMRMMIB": alcatelIND1IPMRMMIB,
       "alcatelIND1IPMRMMIBObjects": alcatelIND1IPMRMMIBObjects,
       "alaIpmrmGlobalConfig": alaIpmrmGlobalConfig,
       "alaIpmrmMbrStatus": alaIpmrmMbrStatus,
       "alaIpmrmMbrProtocolApps": alaIpmrmMbrProtocolApps,
       "alcatelIND1IPMRMMIBConformance": alcatelIND1IPMRMMIBConformance,
       "alcatelIND1IPMRMMIBCompliances": alcatelIND1IPMRMMIBCompliances,
       "alaIpmrmCompliance": alaIpmrmCompliance,
       "alcatelIND1IPMRMMIBGroups": alcatelIND1IPMRMMIBGroups,
       "alaIpmrmConfigMIBGroup": alaIpmrmConfigMIBGroup}
)
