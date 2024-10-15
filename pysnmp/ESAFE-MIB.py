# SNMP MIB module (ESAFE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ESAFE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:47 2024
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

esafeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14)
)
esafeMib.setRevisions(
        ("2017-06-15 00:00",
         "2014-04-03 00:00",
         "2013-08-08 00:00",
         "2013-04-04 00:00",
         "2007-08-03 00:00",
         "2006-07-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EsafeMibObjects_ObjectIdentity = ObjectIdentity
esafeMibObjects = _EsafeMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1)
)
_EsafeBase_ObjectIdentity = ObjectIdentity
esafeBase = _EsafeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1)
)
_EsafeProvisioningStatusTable_Object = MibTable
esafeProvisioningStatusTable = _EsafeProvisioningStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1)
)
if mibBuilder.loadTexts:
    esafeProvisioningStatusTable.setStatus("current")
_EsafeProvisioningStatusEntry_Object = MibTableRow
esafeProvisioningStatusEntry = _EsafeProvisioningStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1, 1)
)
esafeProvisioningStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    esafeProvisioningStatusEntry.setStatus("current")


class _EsafeProvisioningStatusProgress_Type(Integer32):
    """Custom type esafeProvisioningStatusProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("finished", 3),
          ("inProgress", 2),
          ("notInitiated", 1))
    )


_EsafeProvisioningStatusProgress_Type.__name__ = "Integer32"
_EsafeProvisioningStatusProgress_Object = MibTableColumn
esafeProvisioningStatusProgress = _EsafeProvisioningStatusProgress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1, 1, 1),
    _EsafeProvisioningStatusProgress_Type()
)
esafeProvisioningStatusProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esafeProvisioningStatusProgress.setStatus("current")
_EsafeProvisioningStatusFailureFound_Type = TruthValue
_EsafeProvisioningStatusFailureFound_Object = MibTableColumn
esafeProvisioningStatusFailureFound = _EsafeProvisioningStatusFailureFound_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1, 1, 2),
    _EsafeProvisioningStatusFailureFound_Type()
)
esafeProvisioningStatusFailureFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esafeProvisioningStatusFailureFound.setStatus("current")
_EsafeProvisioningStatusFailureFlow_Type = SnmpAdminString
_EsafeProvisioningStatusFailureFlow_Object = MibTableColumn
esafeProvisioningStatusFailureFlow = _EsafeProvisioningStatusFailureFlow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1, 1, 3),
    _EsafeProvisioningStatusFailureFlow_Type()
)
esafeProvisioningStatusFailureFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esafeProvisioningStatusFailureFlow.setStatus("current")


class _EsafeProvisioningStatusFailureEventID_Type(Unsigned32):
    """Custom type esafeProvisioningStatusFailureEventID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EsafeProvisioningStatusFailureEventID_Type.__name__ = "Unsigned32"
_EsafeProvisioningStatusFailureEventID_Object = MibTableColumn
esafeProvisioningStatusFailureEventID = _EsafeProvisioningStatusFailureEventID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1, 1, 4),
    _EsafeProvisioningStatusFailureEventID_Type()
)
esafeProvisioningStatusFailureEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esafeProvisioningStatusFailureEventID.setStatus("current")
_EsafeProvisioningStatusFailureErrorText_Type = SnmpAdminString
_EsafeProvisioningStatusFailureErrorText_Object = MibTableColumn
esafeProvisioningStatusFailureErrorText = _EsafeProvisioningStatusFailureErrorText_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1, 1, 5),
    _EsafeProvisioningStatusFailureErrorText_Type()
)
esafeProvisioningStatusFailureErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esafeProvisioningStatusFailureErrorText.setStatus("current")
_EsafeProvisioningStatusLastUpdate_Type = DateAndTime
_EsafeProvisioningStatusLastUpdate_Object = MibTableColumn
esafeProvisioningStatusLastUpdate = _EsafeProvisioningStatusLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1, 1, 6),
    _EsafeProvisioningStatusLastUpdate_Type()
)
esafeProvisioningStatusLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esafeProvisioningStatusLastUpdate.setStatus("current")
_EsafeDevStatusTable_Object = MibTable
esafeDevStatusTable = _EsafeDevStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 2)
)
if mibBuilder.loadTexts:
    esafeDevStatusTable.setStatus("current")
_EsafeDevStatusEntry_Object = MibTableRow
esafeDevStatusEntry = _EsafeDevStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 2, 1)
)
esafeDevStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    esafeDevStatusEntry.setStatus("current")


class _EsafeDevServiceIntImpact_Type(Integer32):
    """Custom type esafeDevServiceIntImpact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("significant", 1),
          ("unsupported", 3))
    )


_EsafeDevServiceIntImpact_Type.__name__ = "Integer32"
_EsafeDevServiceIntImpact_Object = MibTableColumn
esafeDevServiceIntImpact = _EsafeDevServiceIntImpact_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 2, 1, 1),
    _EsafeDevServiceIntImpact_Type()
)
esafeDevServiceIntImpact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esafeDevServiceIntImpact.setStatus("current")
_EsafeDevServiceIntImpactInfo_Type = SnmpAdminString
_EsafeDevServiceIntImpactInfo_Object = MibTableColumn
esafeDevServiceIntImpactInfo = _EsafeDevServiceIntImpactInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 2, 1, 2),
    _EsafeDevServiceIntImpactInfo_Type()
)
esafeDevServiceIntImpactInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esafeDevServiceIntImpactInfo.setStatus("current")
_EsafePsMibObjects_ObjectIdentity = ObjectIdentity
esafePsMibObjects = _EsafePsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 2)
)


class _EsafePsCableHomeModeControl_Type(Integer32):
    """Custom type esafePsCableHomeModeControl based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabledMode", 1),
          ("dormantCHMode", 3),
          ("provSystem", 2))
    )


_EsafePsCableHomeModeControl_Type.__name__ = "Integer32"
_EsafePsCableHomeModeControl_Object = MibScalar
esafePsCableHomeModeControl = _EsafePsCableHomeModeControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 2, 1),
    _EsafePsCableHomeModeControl_Type()
)
esafePsCableHomeModeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esafePsCableHomeModeControl.setStatus("current")


class _EsafePsCableHomeModeStatus_Type(Integer32):
    """Custom type esafePsCableHomeModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cableHomeMode", 3),
          ("disabledMode", 1),
          ("dormantCHMode", 2))
    )


_EsafePsCableHomeModeStatus_Type.__name__ = "Integer32"
_EsafePsCableHomeModeStatus_Object = MibScalar
esafePsCableHomeModeStatus = _EsafePsCableHomeModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 2, 2),
    _EsafePsCableHomeModeStatus_Type()
)
esafePsCableHomeModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esafePsCableHomeModeStatus.setStatus("current")
_EsafeMtaMibObjects_ObjectIdentity = ObjectIdentity
esafeMtaMibObjects = _EsafeMtaMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 3)
)
_EsafeStbMibObjects_ObjectIdentity = ObjectIdentity
esafeStbMibObjects = _EsafeStbMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 4)
)
_EsafeErouterMibObjects_ObjectIdentity = ObjectIdentity
esafeErouterMibObjects = _EsafeErouterMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 5)
)


class _EsafeErouterAdminMode_Type(Integer32):
    """Custom type esafeErouterAdminMode based on Integer32"""
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
        *(("disabled", 1),
          ("ipv4AndIpv6", 4),
          ("ipv4Only", 2),
          ("ipv6Only", 3),
          ("noTLV202dot1Present", 5))
    )


_EsafeErouterAdminMode_Type.__name__ = "Integer32"
_EsafeErouterAdminMode_Object = MibScalar
esafeErouterAdminMode = _EsafeErouterAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 5, 1),
    _EsafeErouterAdminMode_Type()
)
esafeErouterAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esafeErouterAdminMode.setStatus("current")


class _EsafeErouterOperMode_Type(Integer32):
    """Custom type esafeErouterOperMode based on Integer32"""
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
        *(("disabled", 1),
          ("ipv4AndIpv6Fwding", 4),
          ("ipv4OnlyFwding", 2),
          ("ipv6OnlyFwding", 3),
          ("noIpv4AndNoIpv6Fwding", 5))
    )


_EsafeErouterOperMode_Type.__name__ = "Integer32"
_EsafeErouterOperMode_Object = MibScalar
esafeErouterOperMode = _EsafeErouterOperMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 5, 2),
    _EsafeErouterOperMode_Type()
)
esafeErouterOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esafeErouterOperMode.setStatus("current")
_EsafeErouterPhysAddress_Type = PhysAddress
_EsafeErouterPhysAddress_Object = MibScalar
esafeErouterPhysAddress = _EsafeErouterPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 5, 3),
    _EsafeErouterPhysAddress_Type()
)
esafeErouterPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esafeErouterPhysAddress.setStatus("current")


class _EsafeErouterInitModeControl_Type(Integer32):
    """Custom type esafeErouterInitModeControl based on Integer32"""
    defaultValue = 5

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
        *(("honoreRouterInitMode", 5),
          ("ipDisabled", 1),
          ("ipv4AndIpv6", 4),
          ("ipv4Only", 2),
          ("ipv6Only", 3))
    )


_EsafeErouterInitModeControl_Type.__name__ = "Integer32"
_EsafeErouterInitModeControl_Object = MibScalar
esafeErouterInitModeControl = _EsafeErouterInitModeControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 5, 4),
    _EsafeErouterInitModeControl_Type()
)
esafeErouterInitModeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esafeErouterInitModeControl.setStatus("current")
_EsafeErouterSoftReset_Type = TruthValue
_EsafeErouterSoftReset_Object = MibScalar
esafeErouterSoftReset = _EsafeErouterSoftReset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 5, 5),
    _EsafeErouterSoftReset_Type()
)
esafeErouterSoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esafeErouterSoftReset.setStatus("current")
_EsafeMibConformance_ObjectIdentity = ObjectIdentity
esafeMibConformance = _EsafeMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 2)
)
_EsafeMibCompliances_ObjectIdentity = ObjectIdentity
esafeMibCompliances = _EsafeMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 2, 1)
)
_EsafeMibGroups_ObjectIdentity = ObjectIdentity
esafeMibGroups = _EsafeMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 2, 2)
)

# Managed Objects groups

esafeBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 2, 2, 1)
)
esafeBaseGroup.setObjects(
      *(("ESAFE-MIB", "esafeProvisioningStatusProgress"),
        ("ESAFE-MIB", "esafeProvisioningStatusFailureFound"),
        ("ESAFE-MIB", "esafeProvisioningStatusFailureFlow"),
        ("ESAFE-MIB", "esafeProvisioningStatusFailureEventID"),
        ("ESAFE-MIB", "esafeProvisioningStatusFailureErrorText"),
        ("ESAFE-MIB", "esafeProvisioningStatusLastUpdate"),
        ("ESAFE-MIB", "esafeDevServiceIntImpact"),
        ("ESAFE-MIB", "esafeDevServiceIntImpactInfo"))
)
if mibBuilder.loadTexts:
    esafeBaseGroup.setStatus("current")

esafePsMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 2, 2, 2)
)
esafePsMibGroup.setObjects(
      *(("ESAFE-MIB", "esafePsCableHomeModeControl"),
        ("ESAFE-MIB", "esafePsCableHomeModeStatus"))
)
if mibBuilder.loadTexts:
    esafePsMibGroup.setStatus("current")

esafeErouterMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 2, 2, 3)
)
esafeErouterMibGroup.setObjects(
      *(("ESAFE-MIB", "esafeErouterAdminMode"),
        ("ESAFE-MIB", "esafeErouterOperMode"),
        ("ESAFE-MIB", "esafeErouterPhysAddress"),
        ("ESAFE-MIB", "esafeErouterInitModeControl"),
        ("ESAFE-MIB", "esafeErouterSoftReset"))
)
if mibBuilder.loadTexts:
    esafeErouterMibGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

esafeMibBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 2, 1, 1)
)
if mibBuilder.loadTexts:
    esafeMibBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ESAFE-MIB",
    **{"esafeMib": esafeMib,
       "esafeMibObjects": esafeMibObjects,
       "esafeBase": esafeBase,
       "esafeProvisioningStatusTable": esafeProvisioningStatusTable,
       "esafeProvisioningStatusEntry": esafeProvisioningStatusEntry,
       "esafeProvisioningStatusProgress": esafeProvisioningStatusProgress,
       "esafeProvisioningStatusFailureFound": esafeProvisioningStatusFailureFound,
       "esafeProvisioningStatusFailureFlow": esafeProvisioningStatusFailureFlow,
       "esafeProvisioningStatusFailureEventID": esafeProvisioningStatusFailureEventID,
       "esafeProvisioningStatusFailureErrorText": esafeProvisioningStatusFailureErrorText,
       "esafeProvisioningStatusLastUpdate": esafeProvisioningStatusLastUpdate,
       "esafeDevStatusTable": esafeDevStatusTable,
       "esafeDevStatusEntry": esafeDevStatusEntry,
       "esafeDevServiceIntImpact": esafeDevServiceIntImpact,
       "esafeDevServiceIntImpactInfo": esafeDevServiceIntImpactInfo,
       "esafePsMibObjects": esafePsMibObjects,
       "esafePsCableHomeModeControl": esafePsCableHomeModeControl,
       "esafePsCableHomeModeStatus": esafePsCableHomeModeStatus,
       "esafeMtaMibObjects": esafeMtaMibObjects,
       "esafeStbMibObjects": esafeStbMibObjects,
       "esafeErouterMibObjects": esafeErouterMibObjects,
       "esafeErouterAdminMode": esafeErouterAdminMode,
       "esafeErouterOperMode": esafeErouterOperMode,
       "esafeErouterPhysAddress": esafeErouterPhysAddress,
       "esafeErouterInitModeControl": esafeErouterInitModeControl,
       "esafeErouterSoftReset": esafeErouterSoftReset,
       "esafeMibConformance": esafeMibConformance,
       "esafeMibCompliances": esafeMibCompliances,
       "esafeMibBasicCompliance": esafeMibBasicCompliance,
       "esafeMibGroups": esafeMibGroups,
       "esafeBaseGroup": esafeBaseGroup,
       "esafePsMibGroup": esafePsMibGroup,
       "esafeErouterMibGroup": esafeErouterMibGroup}
)
