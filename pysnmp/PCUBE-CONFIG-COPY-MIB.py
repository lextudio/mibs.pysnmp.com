# SNMP MIB module (PCUBE-CONFIG-COPY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PCUBE-CONFIG-COPY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:10 2024
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

(pcubeMgmt,) = mibBuilder.importSymbols(
    "PCUBE-SMI",
    "pcubeMgmt")

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

pcubeConfigCopyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 3, 1)
)
pcubeConfigCopyMIB.setRevisions(
        ("2006-04-06 20:00",
         "2002-01-14 20:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigFileType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("runningConfig", 2),
          ("startupConfig", 1))
    )



# MIB Managed Objects in the order of their OIDs

_PcubeConfigCopyMIBObjects_ObjectIdentity = ObjectIdentity
pcubeConfigCopyMIBObjects = _PcubeConfigCopyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 3, 1, 1)
)
_PcubeCopy_ObjectIdentity = ObjectIdentity
pcubeCopy = _PcubeCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1)
)
_PcubeCopyTable_Object = MibTable
pcubeCopyTable = _PcubeCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pcubeCopyTable.setStatus("current")
_PcubeCopyEntry_Object = MibTableRow
pcubeCopyEntry = _PcubeCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1)
)
pcubeCopyEntry.setIndexNames(
    (0, "PCUBE-CONFIG-COPY-MIB", "pcubeCopyIndex"),
)
if mibBuilder.loadTexts:
    pcubeCopyEntry.setStatus("current")


class _PcubeCopyIndex_Type(Integer32):
    """Custom type pcubeCopyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PcubeCopyIndex_Type.__name__ = "Integer32"
_PcubeCopyIndex_Object = MibTableColumn
pcubeCopyIndex = _PcubeCopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 1),
    _PcubeCopyIndex_Type()
)
pcubeCopyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pcubeCopyIndex.setStatus("current")
_PcubeCopyEntryRowStatus_Type = RowStatus
_PcubeCopyEntryRowStatus_Object = MibTableColumn
pcubeCopyEntryRowStatus = _PcubeCopyEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 2),
    _PcubeCopyEntryRowStatus_Type()
)
pcubeCopyEntryRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcubeCopyEntryRowStatus.setStatus("current")
_PcubeCopySourceFileType_Type = ConfigFileType
_PcubeCopySourceFileType_Object = MibTableColumn
pcubeCopySourceFileType = _PcubeCopySourceFileType_Object(
    (1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 3),
    _PcubeCopySourceFileType_Type()
)
pcubeCopySourceFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcubeCopySourceFileType.setStatus("current")
_PcubeCopyDestFileType_Type = ConfigFileType
_PcubeCopyDestFileType_Object = MibTableColumn
pcubeCopyDestFileType = _PcubeCopyDestFileType_Object(
    (1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 4),
    _PcubeCopyDestFileType_Type()
)
pcubeCopyDestFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcubeCopyDestFileType.setStatus("current")
_PcubeConfigCopyMIBConformance_ObjectIdentity = ObjectIdentity
pcubeConfigCopyMIBConformance = _PcubeConfigCopyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 3, 1, 2)
)
_PcubeConfigCopyMIBGroups_ObjectIdentity = ObjectIdentity
pcubeConfigCopyMIBGroups = _PcubeConfigCopyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 1)
)
_PcubeConfigCopyMIBCompliances_ObjectIdentity = ObjectIdentity
pcubeConfigCopyMIBCompliances = _PcubeConfigCopyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 2)
)

# Managed Objects groups

pcubeCopyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 1, 1)
)
pcubeCopyGroup.setObjects(
      *(("PCUBE-CONFIG-COPY-MIB", "pcubeCopyEntryRowStatus"),
        ("PCUBE-CONFIG-COPY-MIB", "pcubeCopySourceFileType"),
        ("PCUBE-CONFIG-COPY-MIB", "pcubeCopyDestFileType"))
)
if mibBuilder.loadTexts:
    pcubeCopyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pcubeConfigCopyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pcubeConfigCopyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PCUBE-CONFIG-COPY-MIB",
    **{"ConfigFileType": ConfigFileType,
       "pcubeConfigCopyMIB": pcubeConfigCopyMIB,
       "pcubeConfigCopyMIBObjects": pcubeConfigCopyMIBObjects,
       "pcubeCopy": pcubeCopy,
       "pcubeCopyTable": pcubeCopyTable,
       "pcubeCopyEntry": pcubeCopyEntry,
       "pcubeCopyIndex": pcubeCopyIndex,
       "pcubeCopyEntryRowStatus": pcubeCopyEntryRowStatus,
       "pcubeCopySourceFileType": pcubeCopySourceFileType,
       "pcubeCopyDestFileType": pcubeCopyDestFileType,
       "pcubeConfigCopyMIBConformance": pcubeConfigCopyMIBConformance,
       "pcubeConfigCopyMIBGroups": pcubeConfigCopyMIBGroups,
       "pcubeCopyGroup": pcubeCopyGroup,
       "pcubeConfigCopyMIBCompliances": pcubeConfigCopyMIBCompliances,
       "pcubeConfigCopyMIBCompliance": pcubeConfigCopyMIBCompliance}
)
