# SNMP MIB module (CISCO-WAN-ATM-PARTY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-ATM-PARTY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:50 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoWanAtmPartyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998)
)
ciscoWanAtmPartyMIB.setRevisions(
        ("2002-06-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class WanPartyAdminStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class WanPartyOperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )



class WanNsapAtmAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoWanAtmPartyMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoWanAtmPartyMIBNotifs = _CiscoWanAtmPartyMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 0)
)
_CiscoWanAtmPartyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanAtmPartyMIBObjects = _CiscoWanAtmPartyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1)
)
_CwapConfig_ObjectIdentity = ObjectIdentity
cwapConfig = _CwapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1)
)
_CwapConfigTable_Object = MibTable
cwapConfigTable = _CwapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwapConfigTable.setStatus("current")
_CwapConfigEntry_Object = MibTableRow
cwapConfigEntry = _CwapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1)
)
cwapConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-ATM-PARTY-MIB", "cwapRootVpi"),
    (0, "CISCO-WAN-ATM-PARTY-MIB", "cwapRootVci"),
    (0, "CISCO-WAN-ATM-PARTY-MIB", "cwapReference"),
)
if mibBuilder.loadTexts:
    cwapConfigEntry.setStatus("current")


class _CwapRootVpi_Type(Integer32):
    """Custom type cwapRootVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwapRootVpi_Type.__name__ = "Integer32"
_CwapRootVpi_Object = MibTableColumn
cwapRootVpi = _CwapRootVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 1),
    _CwapRootVpi_Type()
)
cwapRootVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwapRootVpi.setStatus("current")


class _CwapRootVci_Type(Integer32):
    """Custom type cwapRootVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwapRootVci_Type.__name__ = "Integer32"
_CwapRootVci_Object = MibTableColumn
cwapRootVci = _CwapRootVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 2),
    _CwapRootVci_Type()
)
cwapRootVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwapRootVci.setStatus("current")


class _CwapReference_Type(Integer32):
    """Custom type cwapReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CwapReference_Type.__name__ = "Integer32"
_CwapReference_Object = MibTableColumn
cwapReference = _CwapReference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 3),
    _CwapReference_Type()
)
cwapReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwapReference.setStatus("current")
_CwapNSAPAddress_Type = WanNsapAtmAddress
_CwapNSAPAddress_Object = MibTableColumn
cwapNSAPAddress = _CwapNSAPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 4),
    _CwapNSAPAddress_Type()
)
cwapNSAPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwapNSAPAddress.setStatus("current")


class _CwapVpi_Type(Integer32):
    """Custom type cwapVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwapVpi_Type.__name__ = "Integer32"
_CwapVpi_Object = MibTableColumn
cwapVpi = _CwapVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 5),
    _CwapVpi_Type()
)
cwapVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwapVpi.setStatus("current")


class _CwapVci_Type(Integer32):
    """Custom type cwapVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwapVci_Type.__name__ = "Integer32"
_CwapVci_Object = MibTableColumn
cwapVci = _CwapVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 6),
    _CwapVci_Type()
)
cwapVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwapVci.setStatus("current")


class _CwapReroute_Type(TruthValue):
    """Custom type cwapReroute based on TruthValue"""


_CwapReroute_Object = MibTableColumn
cwapReroute = _CwapReroute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 7),
    _CwapReroute_Type()
)
cwapReroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwapReroute.setStatus("current")


class _CwapAdminStatus_Type(WanPartyAdminStatus):
    """Custom type cwapAdminStatus based on WanPartyAdminStatus"""


_CwapAdminStatus_Object = MibTableColumn
cwapAdminStatus = _CwapAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 8),
    _CwapAdminStatus_Type()
)
cwapAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwapAdminStatus.setStatus("current")
_CwapOperStatus_Type = WanPartyOperStatus
_CwapOperStatus_Object = MibTableColumn
cwapOperStatus = _CwapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 9),
    _CwapOperStatus_Type()
)
cwapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwapOperStatus.setStatus("current")


class _CwapIdentifier_Type(Unsigned32):
    """Custom type cwapIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwapIdentifier_Type.__name__ = "Unsigned32"
_CwapIdentifier_Object = MibTableColumn
cwapIdentifier = _CwapIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 10),
    _CwapIdentifier_Type()
)
cwapIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwapIdentifier.setStatus("current")


class _CwapUploadCounter_Type(Unsigned32):
    """Custom type cwapUploadCounter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwapUploadCounter_Type.__name__ = "Unsigned32"
_CwapUploadCounter_Object = MibTableColumn
cwapUploadCounter = _CwapUploadCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 11),
    _CwapUploadCounter_Type()
)
cwapUploadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwapUploadCounter.setStatus("current")
_CwapRootPhysicalId_Type = DisplayString
_CwapRootPhysicalId_Object = MibTableColumn
cwapRootPhysicalId = _CwapRootPhysicalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 12),
    _CwapRootPhysicalId_Type()
)
cwapRootPhysicalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwapRootPhysicalId.setStatus("current")
_CwapRowStatus_Type = RowStatus
_CwapRowStatus_Object = MibTableColumn
cwapRowStatus = _CwapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 13),
    _CwapRowStatus_Type()
)
cwapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwapRowStatus.setStatus("current")
_CiscoWanAtmPartyMIBConform_ObjectIdentity = ObjectIdentity
ciscoWanAtmPartyMIBConform = _CiscoWanAtmPartyMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 2)
)
_CiscoWanAtmPartyMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanAtmPartyMIBCompliances = _CiscoWanAtmPartyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 1)
)
_CiscoWanAtmPartyMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanAtmPartyMIBGroups = _CiscoWanAtmPartyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 2)
)

# Managed Objects groups

ciscoWanAtmPartyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 2, 2)
)
ciscoWanAtmPartyGroup.setObjects(
      *(("CISCO-WAN-ATM-PARTY-MIB", "cwapNSAPAddress"),
        ("CISCO-WAN-ATM-PARTY-MIB", "cwapVpi"),
        ("CISCO-WAN-ATM-PARTY-MIB", "cwapVci"),
        ("CISCO-WAN-ATM-PARTY-MIB", "cwapAdminStatus"),
        ("CISCO-WAN-ATM-PARTY-MIB", "cwapOperStatus"),
        ("CISCO-WAN-ATM-PARTY-MIB", "cwapReroute"),
        ("CISCO-WAN-ATM-PARTY-MIB", "cwapIdentifier"),
        ("CISCO-WAN-ATM-PARTY-MIB", "cwapUploadCounter"),
        ("CISCO-WAN-ATM-PARTY-MIB", "cwapRootPhysicalId"),
        ("CISCO-WAN-ATM-PARTY-MIB", "cwapRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoWanAtmPartyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanAtmPartyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWanAtmPartyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-ATM-PARTY-MIB",
    **{"WanPartyAdminStatus": WanPartyAdminStatus,
       "WanPartyOperStatus": WanPartyOperStatus,
       "WanNsapAtmAddress": WanNsapAtmAddress,
       "ciscoWanAtmPartyMIB": ciscoWanAtmPartyMIB,
       "ciscoWanAtmPartyMIBNotifs": ciscoWanAtmPartyMIBNotifs,
       "ciscoWanAtmPartyMIBObjects": ciscoWanAtmPartyMIBObjects,
       "cwapConfig": cwapConfig,
       "cwapConfigTable": cwapConfigTable,
       "cwapConfigEntry": cwapConfigEntry,
       "cwapRootVpi": cwapRootVpi,
       "cwapRootVci": cwapRootVci,
       "cwapReference": cwapReference,
       "cwapNSAPAddress": cwapNSAPAddress,
       "cwapVpi": cwapVpi,
       "cwapVci": cwapVci,
       "cwapReroute": cwapReroute,
       "cwapAdminStatus": cwapAdminStatus,
       "cwapOperStatus": cwapOperStatus,
       "cwapIdentifier": cwapIdentifier,
       "cwapUploadCounter": cwapUploadCounter,
       "cwapRootPhysicalId": cwapRootPhysicalId,
       "cwapRowStatus": cwapRowStatus,
       "ciscoWanAtmPartyMIBConform": ciscoWanAtmPartyMIBConform,
       "ciscoWanAtmPartyMIBCompliances": ciscoWanAtmPartyMIBCompliances,
       "ciscoWanAtmPartyMIBCompliance": ciscoWanAtmPartyMIBCompliance,
       "ciscoWanAtmPartyMIBGroups": ciscoWanAtmPartyMIBGroups,
       "ciscoWanAtmPartyGroup": ciscoWanAtmPartyGroup}
)
