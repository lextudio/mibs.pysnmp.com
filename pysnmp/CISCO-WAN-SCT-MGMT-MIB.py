# SNMP MIB module (CISCO-WAN-SCT-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-SCT-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:17 2024
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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWanSctMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 236)
)
ciscoWanSctMgmtMIB.setRevisions(
        ("2002-05-21 00:00",
         "2001-11-18 00:00",
         "2001-09-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWanSctMgmtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanSctMgmtMIBObjects = _CiscoWanSctMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 1)
)
_CwSctFileMgmtTable_Object = MibTable
cwSctFileMgmtTable = _CwSctFileMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 1, 1)
)
if mibBuilder.loadTexts:
    cwSctFileMgmtTable.setStatus("current")
_CwSctFileMgmtEntry_Object = MibTableRow
cwSctFileMgmtEntry = _CwSctFileMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 1, 1, 1)
)
cwSctFileMgmtEntry.setIndexNames(
    (0, "CISCO-WAN-SCT-MGMT-MIB", "cwSctCardType"),
    (0, "CISCO-WAN-SCT-MGMT-MIB", "cwSctType"),
    (0, "CISCO-WAN-SCT-MGMT-MIB", "cwSctId"),
    (0, "CISCO-WAN-SCT-MGMT-MIB", "cwSctMajorVersion"),
)
if mibBuilder.loadTexts:
    cwSctFileMgmtEntry.setStatus("current")


class _CwSctCardType_Type(Integer32):
    """Custom type cwSctCardType based on Integer32"""
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
        *(("axsm", 1),
          ("axsme", 2),
          ("axsmxg", 5),
          ("hsfr", 4),
          ("pxm1e", 3))
    )


_CwSctCardType_Type.__name__ = "Integer32"
_CwSctCardType_Object = MibTableColumn
cwSctCardType = _CwSctCardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 1, 1, 1, 1),
    _CwSctCardType_Type()
)
cwSctCardType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwSctCardType.setStatus("current")


class _CwSctType_Type(Integer32):
    """Custom type cwSctType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cardSct", 2),
          ("portSct", 1))
    )


_CwSctType_Type.__name__ = "Integer32"
_CwSctType_Object = MibTableColumn
cwSctType = _CwSctType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 1, 1, 1, 2),
    _CwSctType_Type()
)
cwSctType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwSctType.setStatus("current")


class _CwSctId_Type(Unsigned32):
    """Custom type cwSctId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CwSctId_Type.__name__ = "Unsigned32"
_CwSctId_Object = MibTableColumn
cwSctId = _CwSctId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 1, 1, 1, 3),
    _CwSctId_Type()
)
cwSctId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwSctId.setStatus("current")


class _CwSctMajorVersion_Type(Unsigned32):
    """Custom type cwSctMajorVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CwSctMajorVersion_Type.__name__ = "Unsigned32"
_CwSctMajorVersion_Object = MibTableColumn
cwSctMajorVersion = _CwSctMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 1, 1, 1, 4),
    _CwSctMajorVersion_Type()
)
cwSctMajorVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwSctMajorVersion.setStatus("current")


class _CwSctFileName_Type(SnmpAdminString):
    """Custom type cwSctFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 132),
    )


_CwSctFileName_Type.__name__ = "SnmpAdminString"
_CwSctFileName_Object = MibTableColumn
cwSctFileName = _CwSctFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 1, 1, 1, 5),
    _CwSctFileName_Type()
)
cwSctFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSctFileName.setStatus("current")


class _CwSctFileMinorVersion_Type(Unsigned32):
    """Custom type cwSctFileMinorVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwSctFileMinorVersion_Type.__name__ = "Unsigned32"
_CwSctFileMinorVersion_Object = MibTableColumn
cwSctFileMinorVersion = _CwSctFileMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 1, 1, 1, 6),
    _CwSctFileMinorVersion_Type()
)
cwSctFileMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSctFileMinorVersion.setStatus("current")
_CwSctFileChecksum_Type = Unsigned32
_CwSctFileChecksum_Object = MibTableColumn
cwSctFileChecksum = _CwSctFileChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 1, 1, 1, 7),
    _CwSctFileChecksum_Type()
)
cwSctFileChecksum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwSctFileChecksum.setStatus("current")


class _CwSctFileDescription_Type(SnmpAdminString):
    """Custom type cwSctFileDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 132),
    )


_CwSctFileDescription_Type.__name__ = "SnmpAdminString"
_CwSctFileDescription_Object = MibTableColumn
cwSctFileDescription = _CwSctFileDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 1, 1, 1, 8),
    _CwSctFileDescription_Type()
)
cwSctFileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwSctFileDescription.setStatus("current")


class _CwSctFileOperStatus_Type(Integer32):
    """Custom type cwSctFileOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 3),
          ("invalid", 2),
          ("valid", 1))
    )


_CwSctFileOperStatus_Type.__name__ = "Integer32"
_CwSctFileOperStatus_Object = MibTableColumn
cwSctFileOperStatus = _CwSctFileOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 1, 1, 1, 9),
    _CwSctFileOperStatus_Type()
)
cwSctFileOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSctFileOperStatus.setStatus("current")
_CwSctFileRowStatus_Type = RowStatus
_CwSctFileRowStatus_Object = MibTableColumn
cwSctFileRowStatus = _CwSctFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 1, 1, 1, 10),
    _CwSctFileRowStatus_Type()
)
cwSctFileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwSctFileRowStatus.setStatus("current")
_CiscoWanSctMgmtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWanSctMgmtMIBConformance = _CiscoWanSctMgmtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 3)
)
_CiscoWanSctMgmtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanSctMgmtMIBCompliances = _CiscoWanSctMgmtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 3, 1)
)
_CiscoWanSctMgmtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanSctMgmtMIBGroups = _CiscoWanSctMgmtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 3, 2)
)

# Managed Objects groups

cwSctFileMgmtObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 3, 2, 1)
)
cwSctFileMgmtObjectGroup.setObjects(
      *(("CISCO-WAN-SCT-MGMT-MIB", "cwSctFileName"),
        ("CISCO-WAN-SCT-MGMT-MIB", "cwSctFileMinorVersion"),
        ("CISCO-WAN-SCT-MGMT-MIB", "cwSctFileChecksum"),
        ("CISCO-WAN-SCT-MGMT-MIB", "cwSctFileDescription"),
        ("CISCO-WAN-SCT-MGMT-MIB", "cwSctFileOperStatus"),
        ("CISCO-WAN-SCT-MGMT-MIB", "cwSctFileRowStatus"))
)
if mibBuilder.loadTexts:
    cwSctFileMgmtObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwSctFileMgmtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 236, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cwSctFileMgmtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-SCT-MGMT-MIB",
    **{"ciscoWanSctMgmtMIB": ciscoWanSctMgmtMIB,
       "ciscoWanSctMgmtMIBObjects": ciscoWanSctMgmtMIBObjects,
       "cwSctFileMgmtTable": cwSctFileMgmtTable,
       "cwSctFileMgmtEntry": cwSctFileMgmtEntry,
       "cwSctCardType": cwSctCardType,
       "cwSctType": cwSctType,
       "cwSctId": cwSctId,
       "cwSctMajorVersion": cwSctMajorVersion,
       "cwSctFileName": cwSctFileName,
       "cwSctFileMinorVersion": cwSctFileMinorVersion,
       "cwSctFileChecksum": cwSctFileChecksum,
       "cwSctFileDescription": cwSctFileDescription,
       "cwSctFileOperStatus": cwSctFileOperStatus,
       "cwSctFileRowStatus": cwSctFileRowStatus,
       "ciscoWanSctMgmtMIBConformance": ciscoWanSctMgmtMIBConformance,
       "ciscoWanSctMgmtMIBCompliances": ciscoWanSctMgmtMIBCompliances,
       "cwSctFileMgmtMIBCompliance": cwSctFileMgmtMIBCompliance,
       "ciscoWanSctMgmtMIBGroups": ciscoWanSctMgmtMIBGroups,
       "cwSctFileMgmtObjectGroup": cwSctFileMgmtObjectGroup}
)
