# SNMP MIB module (CISCO-WAN-ATM-CUG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-ATM-CUG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:49 2024
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

(AtmAddr,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoWanAtmCugMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999)
)
ciscoWanAtmCugMIB.setRevisions(
        ("2002-03-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoAtmAddressType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              8)
        )
    )
    namedValues = NamedValues(
        *(("e164", 3),
          ("nsap", 8))
    )



class CiscoAtmAddressLength(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )



class CiscoAtmInterlockCode(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )



# MIB Managed Objects in the order of their OIDs

_CwaCugMIBNotifications_ObjectIdentity = ObjectIdentity
cwaCugMIBNotifications = _CwaCugMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 0)
)
_CwaCugMIBObjects_ObjectIdentity = ObjectIdentity
cwaCugMIBObjects = _CwaCugMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1)
)
_CwaCug_ObjectIdentity = ObjectIdentity
cwaCug = _CwaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1)
)
_CwaCugTable_Object = MibTable
cwaCugTable = _CwaCugTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwaCugTable.setStatus("current")
_CwaCugEntry_Object = MibTableRow
cwaCugEntry = _CwaCugEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1)
)
cwaCugEntry.setIndexNames(
    (0, "CISCO-WAN-ATM-CUG-MIB", "cwaAtmAddress"),
    (0, "CISCO-WAN-ATM-CUG-MIB", "cwaAddressLength"),
    (0, "CISCO-WAN-ATM-CUG-MIB", "cwaCugIndex"),
)
if mibBuilder.loadTexts:
    cwaCugEntry.setStatus("current")
_CwaAtmAddress_Type = AtmAddr
_CwaAtmAddress_Object = MibTableColumn
cwaAtmAddress = _CwaAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 1),
    _CwaAtmAddress_Type()
)
cwaAtmAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwaAtmAddress.setStatus("current")
_CwaAddressLength_Type = CiscoAtmAddressLength
_CwaAddressLength_Object = MibTableColumn
cwaAddressLength = _CwaAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 2),
    _CwaAddressLength_Type()
)
cwaAddressLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwaAddressLength.setStatus("current")


class _CwaCugIndex_Type(Integer32):
    """Custom type cwaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CwaCugIndex_Type.__name__ = "Integer32"
_CwaCugIndex_Object = MibTableColumn
cwaCugIndex = _CwaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 3),
    _CwaCugIndex_Type()
)
cwaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwaCugIndex.setStatus("current")
_CwaAddressPlan_Type = CiscoAtmAddressType
_CwaAddressPlan_Object = MibTableColumn
cwaAddressPlan = _CwaAddressPlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 4),
    _CwaAddressPlan_Type()
)
cwaAddressPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaAddressPlan.setStatus("current")
_CwaInterlockCode_Type = CiscoAtmInterlockCode
_CwaInterlockCode_Object = MibTableColumn
cwaInterlockCode = _CwaInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 5),
    _CwaInterlockCode_Type()
)
cwaInterlockCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaInterlockCode.setStatus("current")


class _CwaCallsBarred_Type(Integer32):
    """Custom type cwaCallsBarred based on Integer32"""
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
        *(("incoming", 2),
          ("none", 1),
          ("outgoing", 3))
    )


_CwaCallsBarred_Type.__name__ = "Integer32"
_CwaCallsBarred_Object = MibTableColumn
cwaCallsBarred = _CwaCallsBarred_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 6),
    _CwaCallsBarred_Type()
)
cwaCallsBarred.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaCallsBarred.setStatus("current")
_CwaCugRowStatus_Type = RowStatus
_CwaCugRowStatus_Object = MibTableColumn
cwaCugRowStatus = _CwaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 7),
    _CwaCugRowStatus_Type()
)
cwaCugRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaCugRowStatus.setStatus("current")
_CwaAddressCug_ObjectIdentity = ObjectIdentity
cwaAddressCug = _CwaAddressCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2)
)
_CwaAddressCugTable_Object = MibTable
cwaAddressCugTable = _CwaAddressCugTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwaAddressCugTable.setStatus("current")
_CwaAddressCugEntry_Object = MibTableRow
cwaAddressCugEntry = _CwaAddressCugEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1)
)
cwaAddressCugEntry.setIndexNames(
    (0, "CISCO-WAN-ATM-CUG-MIB", "cwaAtmAddress"),
    (0, "CISCO-WAN-ATM-CUG-MIB", "cwaAddressLength"),
)
if mibBuilder.loadTexts:
    cwaAddressCugEntry.setStatus("current")
_CwaCugAtmAddressPlan_Type = CiscoAtmAddressType
_CwaCugAtmAddressPlan_Object = MibTableColumn
cwaCugAtmAddressPlan = _CwaCugAtmAddressPlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 1),
    _CwaCugAtmAddressPlan_Type()
)
cwaCugAtmAddressPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwaCugAtmAddressPlan.setStatus("current")


class _CwaIncomingAccess_Type(Integer32):
    """Custom type cwaIncomingAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 2),
          ("notAllowed", 1))
    )


_CwaIncomingAccess_Type.__name__ = "Integer32"
_CwaIncomingAccess_Object = MibTableColumn
cwaIncomingAccess = _CwaIncomingAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 2),
    _CwaIncomingAccess_Type()
)
cwaIncomingAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwaIncomingAccess.setStatus("current")


class _CwaOutgoingAccess_Type(Integer32):
    """Custom type cwaOutgoingAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowedPerCall", 2),
          ("allowedPermanently", 3),
          ("notAllowed", 1))
    )


_CwaOutgoingAccess_Type.__name__ = "Integer32"
_CwaOutgoingAccess_Object = MibTableColumn
cwaOutgoingAccess = _CwaOutgoingAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 3),
    _CwaOutgoingAccess_Type()
)
cwaOutgoingAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwaOutgoingAccess.setStatus("current")


class _CwaPreferentialCug_Type(Integer32):
    """Custom type cwaPreferentialCug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwaPreferentialCug_Type.__name__ = "Integer32"
_CwaPreferentialCug_Object = MibTableColumn
cwaPreferentialCug = _CwaPreferentialCug_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 4),
    _CwaPreferentialCug_Type()
)
cwaPreferentialCug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwaPreferentialCug.setStatus("current")
_CiscoWanAtmCugMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWanAtmCugMIBConformance = _CiscoWanAtmCugMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 3)
)
_CiscoWanAtmCugMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanAtmCugMIBCompliances = _CiscoWanAtmCugMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 1)
)
_CiscoWanAtmCugMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanAtmCugMIBGroups = _CiscoWanAtmCugMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2)
)

# Managed Objects groups

ciscoWanAtmCugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2, 1)
)
ciscoWanAtmCugGroup.setObjects(
      *(("CISCO-WAN-ATM-CUG-MIB", "cwaAddressPlan"),
        ("CISCO-WAN-ATM-CUG-MIB", "cwaInterlockCode"),
        ("CISCO-WAN-ATM-CUG-MIB", "cwaCallsBarred"),
        ("CISCO-WAN-ATM-CUG-MIB", "cwaCugRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoWanAtmCugGroup.setStatus("current")

ciscoWanAtmAddressCugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2, 2)
)
ciscoWanAtmAddressCugGroup.setObjects(
      *(("CISCO-WAN-ATM-CUG-MIB", "cwaCugAtmAddressPlan"),
        ("CISCO-WAN-ATM-CUG-MIB", "cwaIncomingAccess"),
        ("CISCO-WAN-ATM-CUG-MIB", "cwaOutgoingAccess"),
        ("CISCO-WAN-ATM-CUG-MIB", "cwaPreferentialCug"))
)
if mibBuilder.loadTexts:
    ciscoWanAtmAddressCugGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanAtmCugMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWanAtmCugMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-ATM-CUG-MIB",
    **{"CiscoAtmAddressType": CiscoAtmAddressType,
       "CiscoAtmAddressLength": CiscoAtmAddressLength,
       "CiscoAtmInterlockCode": CiscoAtmInterlockCode,
       "ciscoWanAtmCugMIB": ciscoWanAtmCugMIB,
       "cwaCugMIBNotifications": cwaCugMIBNotifications,
       "cwaCugMIBObjects": cwaCugMIBObjects,
       "cwaCug": cwaCug,
       "cwaCugTable": cwaCugTable,
       "cwaCugEntry": cwaCugEntry,
       "cwaAtmAddress": cwaAtmAddress,
       "cwaAddressLength": cwaAddressLength,
       "cwaCugIndex": cwaCugIndex,
       "cwaAddressPlan": cwaAddressPlan,
       "cwaInterlockCode": cwaInterlockCode,
       "cwaCallsBarred": cwaCallsBarred,
       "cwaCugRowStatus": cwaCugRowStatus,
       "cwaAddressCug": cwaAddressCug,
       "cwaAddressCugTable": cwaAddressCugTable,
       "cwaAddressCugEntry": cwaAddressCugEntry,
       "cwaCugAtmAddressPlan": cwaCugAtmAddressPlan,
       "cwaIncomingAccess": cwaIncomingAccess,
       "cwaOutgoingAccess": cwaOutgoingAccess,
       "cwaPreferentialCug": cwaPreferentialCug,
       "ciscoWanAtmCugMIBConformance": ciscoWanAtmCugMIBConformance,
       "ciscoWanAtmCugMIBCompliances": ciscoWanAtmCugMIBCompliances,
       "ciscoWanAtmCugMIBCompliance": ciscoWanAtmCugMIBCompliance,
       "ciscoWanAtmCugMIBGroups": ciscoWanAtmCugMIBGroups,
       "ciscoWanAtmCugGroup": ciscoWanAtmCugGroup,
       "ciscoWanAtmAddressCugGroup": ciscoWanAtmAddressCugGroup}
)
