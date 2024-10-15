# SNMP MIB module (ACD-VSET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACD-VSET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:26 2024
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

acdVSet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13)
)
acdVSet.setRevisions(
        ("2012-01-11 01:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AcdVsetVlanType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cvlan", 1),
          ("svlan", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AcdVSetNotifications_ObjectIdentity = ObjectIdentity
acdVSetNotifications = _AcdVSetNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 0)
)
_AcdVSetMIBObjects_ObjectIdentity = ObjectIdentity
acdVSetMIBObjects = _AcdVSetMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 1)
)
_AcdVSetConfig_ObjectIdentity = ObjectIdentity
acdVSetConfig = _AcdVSetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1)
)
_AcdVSetConfigTable_Object = MibTable
acdVSetConfigTable = _AcdVSetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acdVSetConfigTable.setStatus("current")
_AcdVSetConfigEntry_Object = MibTableRow
acdVSetConfigEntry = _AcdVSetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1)
)
acdVSetConfigEntry.setIndexNames(
    (0, "ACD-VSET-MIB", "acdVSetConfigPolicyListID"),
    (0, "ACD-VSET-MIB", "acdVSetConfigID"),
)
if mibBuilder.loadTexts:
    acdVSetConfigEntry.setStatus("current")
_AcdVSetConfigPolicyListID_Type = Unsigned32
_AcdVSetConfigPolicyListID_Object = MibTableColumn
acdVSetConfigPolicyListID = _AcdVSetConfigPolicyListID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 1),
    _AcdVSetConfigPolicyListID_Type()
)
acdVSetConfigPolicyListID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdVSetConfigPolicyListID.setStatus("current")
_AcdVSetConfigID_Type = Unsigned32
_AcdVSetConfigID_Object = MibTableColumn
acdVSetConfigID = _AcdVSetConfigID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 2),
    _AcdVSetConfigID_Type()
)
acdVSetConfigID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdVSetConfigID.setStatus("current")
_AcdVSetConfigRowStatus_Type = RowStatus
_AcdVSetConfigRowStatus_Object = MibTableColumn
acdVSetConfigRowStatus = _AcdVSetConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 3),
    _AcdVSetConfigRowStatus_Type()
)
acdVSetConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdVSetConfigRowStatus.setStatus("current")


class _AcdVSetConfigName_Type(DisplayString):
    """Custom type acdVSetConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdVSetConfigName_Type.__name__ = "DisplayString"
_AcdVSetConfigName_Object = MibTableColumn
acdVSetConfigName = _AcdVSetConfigName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 4),
    _AcdVSetConfigName_Type()
)
acdVSetConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdVSetConfigName.setStatus("current")


class _AcdVSetConfigVlanType_Type(AcdVsetVlanType):
    """Custom type acdVSetConfigVlanType based on AcdVsetVlanType"""


_AcdVSetConfigVlanType_Object = MibTableColumn
acdVSetConfigVlanType = _AcdVSetConfigVlanType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 5),
    _AcdVSetConfigVlanType_Type()
)
acdVSetConfigVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdVSetConfigVlanType.setStatus("current")


class _AcdVSetConfigVlanIDs0to1023_Type(OctetString):
    """Custom type acdVSetConfigVlanIDs0to1023 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdVSetConfigVlanIDs0to1023_Type.__name__ = "OctetString"
_AcdVSetConfigVlanIDs0to1023_Object = MibTableColumn
acdVSetConfigVlanIDs0to1023 = _AcdVSetConfigVlanIDs0to1023_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 6),
    _AcdVSetConfigVlanIDs0to1023_Type()
)
acdVSetConfigVlanIDs0to1023.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdVSetConfigVlanIDs0to1023.setStatus("current")


class _AcdVSetConfigVlanIDs1024to2047_Type(OctetString):
    """Custom type acdVSetConfigVlanIDs1024to2047 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdVSetConfigVlanIDs1024to2047_Type.__name__ = "OctetString"
_AcdVSetConfigVlanIDs1024to2047_Object = MibTableColumn
acdVSetConfigVlanIDs1024to2047 = _AcdVSetConfigVlanIDs1024to2047_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 7),
    _AcdVSetConfigVlanIDs1024to2047_Type()
)
acdVSetConfigVlanIDs1024to2047.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdVSetConfigVlanIDs1024to2047.setStatus("current")


class _AcdVSetConfigVlanIDs2048to3071_Type(OctetString):
    """Custom type acdVSetConfigVlanIDs2048to3071 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdVSetConfigVlanIDs2048to3071_Type.__name__ = "OctetString"
_AcdVSetConfigVlanIDs2048to3071_Object = MibTableColumn
acdVSetConfigVlanIDs2048to3071 = _AcdVSetConfigVlanIDs2048to3071_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 8),
    _AcdVSetConfigVlanIDs2048to3071_Type()
)
acdVSetConfigVlanIDs2048to3071.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdVSetConfigVlanIDs2048to3071.setStatus("current")


class _AcdVSetConfigVlanIDs3072to4095_Type(OctetString):
    """Custom type acdVSetConfigVlanIDs3072to4095 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdVSetConfigVlanIDs3072to4095_Type.__name__ = "OctetString"
_AcdVSetConfigVlanIDs3072to4095_Object = MibTableColumn
acdVSetConfigVlanIDs3072to4095 = _AcdVSetConfigVlanIDs3072to4095_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 9),
    _AcdVSetConfigVlanIDs3072to4095_Type()
)
acdVSetConfigVlanIDs3072to4095.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdVSetConfigVlanIDs3072to4095.setStatus("current")
_AcdVSetConformance_ObjectIdentity = ObjectIdentity
acdVSetConformance = _AcdVSetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 2)
)
_AcdVSetCompliances_ObjectIdentity = ObjectIdentity
acdVSetCompliances = _AcdVSetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 2, 1)
)
_AcdVSetGroups_ObjectIdentity = ObjectIdentity
acdVSetGroups = _AcdVSetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 2, 2)
)

# Managed Objects groups

acdVSetConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 2, 2, 1)
)
acdVSetConfigGroup.setObjects(
      *(("ACD-VSET-MIB", "acdVSetConfigRowStatus"),
        ("ACD-VSET-MIB", "acdVSetConfigName"),
        ("ACD-VSET-MIB", "acdVSetConfigVlanType"),
        ("ACD-VSET-MIB", "acdVSetConfigVlanIDs0to1023"),
        ("ACD-VSET-MIB", "acdVSetConfigVlanIDs1024to2047"),
        ("ACD-VSET-MIB", "acdVSetConfigVlanIDs2048to3071"),
        ("ACD-VSET-MIB", "acdVSetConfigVlanIDs3072to4095"))
)
if mibBuilder.loadTexts:
    acdVSetConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdVSetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 13, 2, 1, 1)
)
if mibBuilder.loadTexts:
    acdVSetCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-VSET-MIB",
    **{"AcdVsetVlanType": AcdVsetVlanType,
       "acdVSet": acdVSet,
       "acdVSetNotifications": acdVSetNotifications,
       "acdVSetMIBObjects": acdVSetMIBObjects,
       "acdVSetConfig": acdVSetConfig,
       "acdVSetConfigTable": acdVSetConfigTable,
       "acdVSetConfigEntry": acdVSetConfigEntry,
       "acdVSetConfigPolicyListID": acdVSetConfigPolicyListID,
       "acdVSetConfigID": acdVSetConfigID,
       "acdVSetConfigRowStatus": acdVSetConfigRowStatus,
       "acdVSetConfigName": acdVSetConfigName,
       "acdVSetConfigVlanType": acdVSetConfigVlanType,
       "acdVSetConfigVlanIDs0to1023": acdVSetConfigVlanIDs0to1023,
       "acdVSetConfigVlanIDs1024to2047": acdVSetConfigVlanIDs1024to2047,
       "acdVSetConfigVlanIDs2048to3071": acdVSetConfigVlanIDs2048to3071,
       "acdVSetConfigVlanIDs3072to4095": acdVSetConfigVlanIDs3072to4095,
       "acdVSetConformance": acdVSetConformance,
       "acdVSetCompliances": acdVSetCompliances,
       "acdVSetCompliance": acdVSetCompliance,
       "acdVSetGroups": acdVSetGroups,
       "acdVSetConfigGroup": acdVSetConfigGroup}
)
