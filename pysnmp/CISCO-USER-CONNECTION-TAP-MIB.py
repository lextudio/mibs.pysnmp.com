# SNMP MIB module (CISCO-USER-CONNECTION-TAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-USER-CONNECTION-TAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:35 2024
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

(cTap2MediationContentId,
 cTap2StreamIndex) = mibBuilder.importSymbols(
    "CISCO-TAP2-MIB",
    "cTap2MediationContentId",
    "cTap2StreamIndex")

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

ciscoUserConnectionTapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 400)
)
ciscoUserConnectionTapMIB.setRevisions(
        ("2007-08-09 00:00",
         "2004-03-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CUserConnectionTapMIBObjects_ObjectIdentity = ObjectIdentity
cUserConnectionTapMIBObjects = _CUserConnectionTapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 400, 1)
)
_CuctTapStreamEncodePacket_ObjectIdentity = ObjectIdentity
cuctTapStreamEncodePacket = _CuctTapStreamEncodePacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1)
)


class _CuctTapStreamCapabilities_Type(Bits):
    """Custom type cuctTapStreamCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("acctSessionId", 1),
          ("tapEnable", 0))
    )

_CuctTapStreamCapabilities_Type.__name__ = "Bits"
_CuctTapStreamCapabilities_Object = MibScalar
cuctTapStreamCapabilities = _CuctTapStreamCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 1),
    _CuctTapStreamCapabilities_Type()
)
cuctTapStreamCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuctTapStreamCapabilities.setStatus("current")
_CuctTapStreamTable_Object = MibTable
cuctTapStreamTable = _CuctTapStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cuctTapStreamTable.setStatus("current")
_CuctTapStreamEntry_Object = MibTableRow
cuctTapStreamEntry = _CuctTapStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1)
)
cuctTapStreamEntry.setIndexNames(
    (0, "CISCO-TAP2-MIB", "cTap2MediationContentId"),
    (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"),
)
if mibBuilder.loadTexts:
    cuctTapStreamEntry.setStatus("current")


class _CuctTapStreamAcctSessID_Type(Unsigned32):
    """Custom type cuctTapStreamAcctSessID based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CuctTapStreamAcctSessID_Type.__name__ = "Unsigned32"
_CuctTapStreamAcctSessID_Object = MibTableColumn
cuctTapStreamAcctSessID = _CuctTapStreamAcctSessID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1, 1),
    _CuctTapStreamAcctSessID_Type()
)
cuctTapStreamAcctSessID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cuctTapStreamAcctSessID.setStatus("current")
_CuctTapStreamStatus_Type = RowStatus
_CuctTapStreamStatus_Object = MibTableColumn
cuctTapStreamStatus = _CuctTapStreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1, 2),
    _CuctTapStreamStatus_Type()
)
cuctTapStreamStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cuctTapStreamStatus.setStatus("current")
_CUserConnectionTapMIBConform_ObjectIdentity = ObjectIdentity
cUserConnectionTapMIBConform = _CUserConnectionTapMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 400, 2)
)
_CUserConnectionTapMIBCompliances_ObjectIdentity = ObjectIdentity
cUserConnectionTapMIBCompliances = _CUserConnectionTapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 1)
)
_CUserConnectionTapMIBGroups_ObjectIdentity = ObjectIdentity
cUserConnectionTapMIBGroups = _CUserConnectionTapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 2)
)

# Managed Objects groups

cuctTapStreamComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 2, 1)
)
cuctTapStreamComplianceGroup.setObjects(
      *(("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamCapabilities"),
        ("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamAcctSessID"),
        ("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamStatus"))
)
if mibBuilder.loadTexts:
    cuctTapStreamComplianceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cUserConnectionTapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cUserConnectionTapMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-USER-CONNECTION-TAP-MIB",
    **{"ciscoUserConnectionTapMIB": ciscoUserConnectionTapMIB,
       "cUserConnectionTapMIBObjects": cUserConnectionTapMIBObjects,
       "cuctTapStreamEncodePacket": cuctTapStreamEncodePacket,
       "cuctTapStreamCapabilities": cuctTapStreamCapabilities,
       "cuctTapStreamTable": cuctTapStreamTable,
       "cuctTapStreamEntry": cuctTapStreamEntry,
       "cuctTapStreamAcctSessID": cuctTapStreamAcctSessID,
       "cuctTapStreamStatus": cuctTapStreamStatus,
       "cUserConnectionTapMIBConform": cUserConnectionTapMIBConform,
       "cUserConnectionTapMIBCompliances": cUserConnectionTapMIBCompliances,
       "cUserConnectionTapMIBCompliance": cUserConnectionTapMIBCompliance,
       "cUserConnectionTapMIBGroups": cUserConnectionTapMIBGroups,
       "cuctTapStreamComplianceGroup": cuctTapStreamComplianceGroup}
)
