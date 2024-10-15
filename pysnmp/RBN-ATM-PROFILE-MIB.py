# SNMP MIB module (RBN-ATM-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-ATM-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:54 2024
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

(atmTrafficDescrParamEntry,) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmTrafficDescrParamEntry")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnAtmProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AtmProfileName(OctetString, TextualConvention):
    status = "current"
    displayHint = "80a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



# MIB Managed Objects in the order of their OIDs

_RbnAtmProfileMIBObjects_ObjectIdentity = ObjectIdentity
rbnAtmProfileMIBObjects = _RbnAtmProfileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 2, 1)
)
_RbnAtmProfileTable_Object = MibTable
rbnAtmProfileTable = _RbnAtmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnAtmProfileTable.setStatus("current")
_RbnAtmProfileEntry_Object = MibTableRow
rbnAtmProfileEntry = _RbnAtmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnAtmProfileEntry.setStatus("current")


class _RbnAtmProfileName_Type(AtmProfileName):
    """Custom type rbnAtmProfileName based on AtmProfileName"""
    defaultHexValue = ""


_RbnAtmProfileName_Object = MibTableColumn
rbnAtmProfileName = _RbnAtmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 1),
    _RbnAtmProfileName_Type()
)
rbnAtmProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnAtmProfileName.setStatus("current")


class _RbnAtmCountersEnabled_Type(TruthValue):
    """Custom type rbnAtmCountersEnabled based on TruthValue"""


_RbnAtmCountersEnabled_Object = MibTableColumn
rbnAtmCountersEnabled = _RbnAtmCountersEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 2),
    _RbnAtmCountersEnabled_Type()
)
rbnAtmCountersEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnAtmCountersEnabled.setStatus("current")
_RbnAtmCellLossPriority_Type = TruthValue
_RbnAtmCellLossPriority_Object = MibTableColumn
rbnAtmCellLossPriority = _RbnAtmCellLossPriority_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 3),
    _RbnAtmCellLossPriority_Type()
)
rbnAtmCellLossPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnAtmCellLossPriority.setStatus("current")


class _RbnAtmTransmitBuffers_Type(Integer32):
    """Custom type rbnAtmTransmitBuffers based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_RbnAtmTransmitBuffers_Type.__name__ = "Integer32"
_RbnAtmTransmitBuffers_Object = MibTableColumn
rbnAtmTransmitBuffers = _RbnAtmTransmitBuffers_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 4),
    _RbnAtmTransmitBuffers_Type()
)
rbnAtmTransmitBuffers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnAtmTransmitBuffers.setStatus("current")
_RbnAtmProfileMIBConformance_ObjectIdentity = ObjectIdentity
rbnAtmProfileMIBConformance = _RbnAtmProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 2, 2)
)
_RbnAtmProfileMIBGroups_ObjectIdentity = ObjectIdentity
rbnAtmProfileMIBGroups = _RbnAtmProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 1)
)
_RbnAtmProfileMIBCompliances_ObjectIdentity = ObjectIdentity
rbnAtmProfileMIBCompliances = _RbnAtmProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 2)
)
atmTrafficDescrParamEntry.registerAugmentions(
    ("RBN-ATM-PROFILE-MIB",
     "rbnAtmProfileEntry")
)
rbnAtmProfileEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())

# Managed Objects groups

rbnAtmProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 1, 1)
)
rbnAtmProfileGroup.setObjects(
      *(("RBN-ATM-PROFILE-MIB", "rbnAtmProfileName"),
        ("RBN-ATM-PROFILE-MIB", "rbnAtmCountersEnabled"),
        ("RBN-ATM-PROFILE-MIB", "rbnAtmCellLossPriority"),
        ("RBN-ATM-PROFILE-MIB", "rbnAtmTransmitBuffers"))
)
if mibBuilder.loadTexts:
    rbnAtmProfileGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnAtmProfileMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnAtmProfileMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-ATM-PROFILE-MIB",
    **{"AtmProfileName": AtmProfileName,
       "rbnAtmProfileMIB": rbnAtmProfileMIB,
       "rbnAtmProfileMIBObjects": rbnAtmProfileMIBObjects,
       "rbnAtmProfileTable": rbnAtmProfileTable,
       "rbnAtmProfileEntry": rbnAtmProfileEntry,
       "rbnAtmProfileName": rbnAtmProfileName,
       "rbnAtmCountersEnabled": rbnAtmCountersEnabled,
       "rbnAtmCellLossPriority": rbnAtmCellLossPriority,
       "rbnAtmTransmitBuffers": rbnAtmTransmitBuffers,
       "rbnAtmProfileMIBConformance": rbnAtmProfileMIBConformance,
       "rbnAtmProfileMIBGroups": rbnAtmProfileMIBGroups,
       "rbnAtmProfileGroup": rbnAtmProfileGroup,
       "rbnAtmProfileMIBCompliances": rbnAtmProfileMIBCompliances,
       "rbnAtmProfileMIBCompliance": rbnAtmProfileMIBCompliance}
)
