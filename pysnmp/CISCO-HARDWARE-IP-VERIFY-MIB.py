# SNMP MIB module (CISCO-HARDWARE-IP-VERIFY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-HARDWARE-IP-VERIFY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:10 2024
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

ciscoHardwareIpVerifyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 804)
)
ciscoHardwareIpVerifyMIB.setRevisions(
        ("2012-09-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoHardwareIpVerifyMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoHardwareIpVerifyMIBNotifs = _CiscoHardwareIpVerifyMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 0)
)
_CiscoHardwareIpVerifyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoHardwareIpVerifyMIBObjects = _CiscoHardwareIpVerifyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 1)
)
_ChivIpVerifyTable_Object = MibTable
chivIpVerifyTable = _ChivIpVerifyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1)
)
if mibBuilder.loadTexts:
    chivIpVerifyTable.setStatus("current")
_ChivIpVerifyEntry_Object = MibTableRow
chivIpVerifyEntry = _ChivIpVerifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1)
)
chivIpVerifyEntry.setIndexNames(
    (0, "CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyCheckIpType"),
    (0, "CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyCheckTypeName"),
)
if mibBuilder.loadTexts:
    chivIpVerifyEntry.setStatus("current")


class _ChivIpVerifyCheckIpType_Type(Integer32):
    """Custom type chivIpVerifyCheckIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_ChivIpVerifyCheckIpType_Type.__name__ = "Integer32"
_ChivIpVerifyCheckIpType_Object = MibTableColumn
chivIpVerifyCheckIpType = _ChivIpVerifyCheckIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 1),
    _ChivIpVerifyCheckIpType_Type()
)
chivIpVerifyCheckIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chivIpVerifyCheckIpType.setStatus("current")


class _ChivIpVerifyCheckTypeName_Type(Integer32):
    """Custom type chivIpVerifyCheckTypeName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("addressClassE", 6),
          ("addressDestZero", 3),
          ("addressIdentical", 4),
          ("addressSrcBroadcast", 1),
          ("addressSrcMulticast", 2),
          ("addressSrcReserved", 5),
          ("checksum", 7),
          ("fragment", 9),
          ("lengthConsistent", 11),
          ("lengthMaximumFragment", 12),
          ("lengthMaximumTcp", 14),
          ("lengthMaximumUdp", 13),
          ("lengthMinimum", 10),
          ("protocol", 8),
          ("tcpFlags", 15),
          ("tcpTinyFlags", 16),
          ("version", 17))
    )


_ChivIpVerifyCheckTypeName_Type.__name__ = "Integer32"
_ChivIpVerifyCheckTypeName_Object = MibTableColumn
chivIpVerifyCheckTypeName = _ChivIpVerifyCheckTypeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 2),
    _ChivIpVerifyCheckTypeName_Type()
)
chivIpVerifyCheckTypeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chivIpVerifyCheckTypeName.setStatus("current")


class _ChivIpVerifyCheckStatus_Type(Integer32):
    """Custom type chivIpVerifyCheckStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChivIpVerifyCheckStatus_Type.__name__ = "Integer32"
_ChivIpVerifyCheckStatus_Object = MibTableColumn
chivIpVerifyCheckStatus = _ChivIpVerifyCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 3),
    _ChivIpVerifyCheckStatus_Type()
)
chivIpVerifyCheckStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chivIpVerifyCheckStatus.setStatus("current")
_ChivIpVerifyPacketsDropped_Type = Counter64
_ChivIpVerifyPacketsDropped_Object = MibTableColumn
chivIpVerifyPacketsDropped = _ChivIpVerifyPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 4),
    _ChivIpVerifyPacketsDropped_Type()
)
chivIpVerifyPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chivIpVerifyPacketsDropped.setStatus("current")
_CiscoHardwareIpVerifyMIBConform_ObjectIdentity = ObjectIdentity
ciscoHardwareIpVerifyMIBConform = _CiscoHardwareIpVerifyMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 2)
)
_CiscoHardwareIpVerifyMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoHardwareIpVerifyMIBCompliances = _CiscoHardwareIpVerifyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 1)
)
_CiscoHardwareIpVerifyMIBGroups_ObjectIdentity = ObjectIdentity
ciscoHardwareIpVerifyMIBGroups = _CiscoHardwareIpVerifyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 2)
)

# Managed Objects groups

ciscoHardwareIpVerifyMIBStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 2, 1)
)
ciscoHardwareIpVerifyMIBStatisticGroup.setObjects(
      *(("CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyCheckStatus"),
        ("CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyPacketsDropped"))
)
if mibBuilder.loadTexts:
    ciscoHardwareIpVerifyMIBStatisticGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoHardwareIpVerifyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoHardwareIpVerifyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-HARDWARE-IP-VERIFY-MIB",
    **{"ciscoHardwareIpVerifyMIB": ciscoHardwareIpVerifyMIB,
       "ciscoHardwareIpVerifyMIBNotifs": ciscoHardwareIpVerifyMIBNotifs,
       "ciscoHardwareIpVerifyMIBObjects": ciscoHardwareIpVerifyMIBObjects,
       "chivIpVerifyTable": chivIpVerifyTable,
       "chivIpVerifyEntry": chivIpVerifyEntry,
       "chivIpVerifyCheckIpType": chivIpVerifyCheckIpType,
       "chivIpVerifyCheckTypeName": chivIpVerifyCheckTypeName,
       "chivIpVerifyCheckStatus": chivIpVerifyCheckStatus,
       "chivIpVerifyPacketsDropped": chivIpVerifyPacketsDropped,
       "ciscoHardwareIpVerifyMIBConform": ciscoHardwareIpVerifyMIBConform,
       "ciscoHardwareIpVerifyMIBCompliances": ciscoHardwareIpVerifyMIBCompliances,
       "ciscoHardwareIpVerifyMIBCompliance": ciscoHardwareIpVerifyMIBCompliance,
       "ciscoHardwareIpVerifyMIBGroups": ciscoHardwareIpVerifyMIBGroups,
       "ciscoHardwareIpVerifyMIBStatisticGroup": ciscoHardwareIpVerifyMIBStatisticGroup}
)
