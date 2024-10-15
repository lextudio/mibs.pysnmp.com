# SNMP MIB module (CISCO-MGX82XX-ATM-UNI-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MGX82XX-ATM-UNI-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:30 2024
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

(AtmAddress,
 NetPrefix) = mibBuilder.importSymbols(
    "ATM-FORUM-TC-MIB",
    "AtmAddress",
    "NetPrefix")

(atmAddressRegistration,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "atmAddressRegistration")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoMgx82xxAtmUniPortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 71)
)
ciscoMgx82xxAtmUniPortMIB.setRevisions(
        ("2003-04-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmNetPrefixGroup_ObjectIdentity = ObjectIdentity
atmNetPrefixGroup = _AtmNetPrefixGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 4, 1, 1)
)
_AtmNetPrefixTable_Object = MibTable
atmNetPrefixTable = _AtmNetPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    atmNetPrefixTable.setStatus("current")
_AtmNetPrefixEntry_Object = MibTableRow
atmNetPrefixEntry = _AtmNetPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 4, 1, 1, 1, 1)
)
atmNetPrefixEntry.setIndexNames(
    (0, "CISCO-MGX82XX-ATM-UNI-PORT-MIB", "axisAtmNetPrefixPort"),
    (0, "CISCO-MGX82XX-ATM-UNI-PORT-MIB", "axisAtmNetPrefixPrefix"),
)
if mibBuilder.loadTexts:
    atmNetPrefixEntry.setStatus("current")


class _AxisAtmNetPrefixPort_Type(Integer32):
    """Custom type axisAtmNetPrefixPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AxisAtmNetPrefixPort_Type.__name__ = "Integer32"
_AxisAtmNetPrefixPort_Object = MibTableColumn
axisAtmNetPrefixPort = _AxisAtmNetPrefixPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 4, 1, 1, 1, 1, 1),
    _AxisAtmNetPrefixPort_Type()
)
axisAtmNetPrefixPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axisAtmNetPrefixPort.setStatus("current")
_AxisAtmNetPrefixPrefix_Type = NetPrefix
_AxisAtmNetPrefixPrefix_Object = MibTableColumn
axisAtmNetPrefixPrefix = _AxisAtmNetPrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 4, 1, 1, 1, 1, 2),
    _AxisAtmNetPrefixPrefix_Type()
)
axisAtmNetPrefixPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axisAtmNetPrefixPrefix.setStatus("current")


class _AxisAtmNetPrefixAdminStatus_Type(Integer32):
    """Custom type axisAtmNetPrefixAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AxisAtmNetPrefixAdminStatus_Type.__name__ = "Integer32"
_AxisAtmNetPrefixAdminStatus_Object = MibTableColumn
axisAtmNetPrefixAdminStatus = _AxisAtmNetPrefixAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 4, 1, 1, 1, 1, 3),
    _AxisAtmNetPrefixAdminStatus_Type()
)
axisAtmNetPrefixAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    axisAtmNetPrefixAdminStatus.setStatus("current")


class _AxisAtmNetPrefixOperStatus_Type(Integer32):
    """Custom type axisAtmNetPrefixOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("de-registered", 4),
          ("de-registering", 2),
          ("failDe-registering", 6),
          ("failRegistering", 5),
          ("registered", 3),
          ("registering", 1))
    )


_AxisAtmNetPrefixOperStatus_Type.__name__ = "Integer32"
_AxisAtmNetPrefixOperStatus_Object = MibTableColumn
axisAtmNetPrefixOperStatus = _AxisAtmNetPrefixOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 4, 1, 1, 1, 1, 4),
    _AxisAtmNetPrefixOperStatus_Type()
)
axisAtmNetPrefixOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axisAtmNetPrefixOperStatus.setStatus("current")
_AtmAddressGroup_ObjectIdentity = ObjectIdentity
atmAddressGroup = _AtmAddressGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 4, 1, 2)
)
_AtmAddressTable_Object = MibTable
atmAddressTable = _AtmAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    atmAddressTable.setStatus("current")
_AtmAddressEntry_Object = MibTableRow
atmAddressEntry = _AtmAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 4, 1, 2, 1, 1)
)
atmAddressEntry.setIndexNames(
    (0, "CISCO-MGX82XX-ATM-UNI-PORT-MIB", "axisAtmAddressPort"),
    (0, "CISCO-MGX82XX-ATM-UNI-PORT-MIB", "axisAtmAddressAtmAddress"),
)
if mibBuilder.loadTexts:
    atmAddressEntry.setStatus("current")


class _AxisAtmAddressPort_Type(Integer32):
    """Custom type axisAtmAddressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AxisAtmAddressPort_Type.__name__ = "Integer32"
_AxisAtmAddressPort_Object = MibTableColumn
axisAtmAddressPort = _AxisAtmAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 4, 1, 2, 1, 1, 1),
    _AxisAtmAddressPort_Type()
)
axisAtmAddressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axisAtmAddressPort.setStatus("current")
_AxisAtmAddressAtmAddress_Type = AtmAddress
_AxisAtmAddressAtmAddress_Object = MibTableColumn
axisAtmAddressAtmAddress = _AxisAtmAddressAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 4, 1, 2, 1, 1, 2),
    _AxisAtmAddressAtmAddress_Type()
)
axisAtmAddressAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axisAtmAddressAtmAddress.setStatus("current")


class _AxisAtmAddressStatus_Type(Integer32):
    """Custom type axisAtmAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AxisAtmAddressStatus_Type.__name__ = "Integer32"
_AxisAtmAddressStatus_Object = MibTableColumn
axisAtmAddressStatus = _AxisAtmAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 4, 1, 2, 1, 1, 3),
    _AxisAtmAddressStatus_Type()
)
axisAtmAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axisAtmAddressStatus.setStatus("current")
_CmauPortMIBConformance_ObjectIdentity = ObjectIdentity
cmauPortMIBConformance = _CmauPortMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 71, 2)
)
_CmauPortMIBGroups_ObjectIdentity = ObjectIdentity
cmauPortMIBGroups = _CmauPortMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 71, 2, 1)
)
_CmauPortMIBCompliances_ObjectIdentity = ObjectIdentity
cmauPortMIBCompliances = _CmauPortMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 71, 2, 2)
)

# Managed Objects groups

cmauAtmAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 71, 2, 1, 1)
)
cmauAtmAddressGroup.setObjects(
      *(("CISCO-MGX82XX-ATM-UNI-PORT-MIB", "axisAtmAddressPort"),
        ("CISCO-MGX82XX-ATM-UNI-PORT-MIB", "axisAtmAddressAtmAddress"),
        ("CISCO-MGX82XX-ATM-UNI-PORT-MIB", "axisAtmAddressStatus"))
)
if mibBuilder.loadTexts:
    cmauAtmAddressGroup.setStatus("current")

cmauNetPrefixGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 71, 2, 1, 2)
)
cmauNetPrefixGroup.setObjects(
      *(("CISCO-MGX82XX-ATM-UNI-PORT-MIB", "axisAtmNetPrefixPort"),
        ("CISCO-MGX82XX-ATM-UNI-PORT-MIB", "axisAtmNetPrefixPrefix"),
        ("CISCO-MGX82XX-ATM-UNI-PORT-MIB", "axisAtmNetPrefixAdminStatus"),
        ("CISCO-MGX82XX-ATM-UNI-PORT-MIB", "axisAtmNetPrefixOperStatus"))
)
if mibBuilder.loadTexts:
    cmauNetPrefixGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmauPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 71, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cmauPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MGX82XX-ATM-UNI-PORT-MIB",
    **{"atmNetPrefixGroup": atmNetPrefixGroup,
       "atmNetPrefixTable": atmNetPrefixTable,
       "atmNetPrefixEntry": atmNetPrefixEntry,
       "axisAtmNetPrefixPort": axisAtmNetPrefixPort,
       "axisAtmNetPrefixPrefix": axisAtmNetPrefixPrefix,
       "axisAtmNetPrefixAdminStatus": axisAtmNetPrefixAdminStatus,
       "axisAtmNetPrefixOperStatus": axisAtmNetPrefixOperStatus,
       "atmAddressGroup": atmAddressGroup,
       "atmAddressTable": atmAddressTable,
       "atmAddressEntry": atmAddressEntry,
       "axisAtmAddressPort": axisAtmAddressPort,
       "axisAtmAddressAtmAddress": axisAtmAddressAtmAddress,
       "axisAtmAddressStatus": axisAtmAddressStatus,
       "ciscoMgx82xxAtmUniPortMIB": ciscoMgx82xxAtmUniPortMIB,
       "cmauPortMIBConformance": cmauPortMIBConformance,
       "cmauPortMIBGroups": cmauPortMIBGroups,
       "cmauAtmAddressGroup": cmauAtmAddressGroup,
       "cmauNetPrefixGroup": cmauNetPrefixGroup,
       "cmauPortMIBCompliances": cmauPortMIBCompliances,
       "cmauPortCompliance": cmauPortCompliance}
)
