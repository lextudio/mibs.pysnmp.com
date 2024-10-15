# SNMP MIB module (BRS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BRS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:37 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class BRSPriority(Integer32):
    """Custom type BRSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("normal", 2),
          ("urgent", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Proteon_ObjectIdentity = ObjectIdentity
proteon = _Proteon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1)
)
_ProAdmin_ObjectIdentity = ObjectIdentity
proAdmin = _ProAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1)
)
_ProFeature_ObjectIdentity = ObjectIdentity
proFeature = _ProFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 7)
)
_ProFeatureBrs_ObjectIdentity = ObjectIdentity
proFeatureBrs = _ProFeatureBrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1)
)
_ProBrsMib_ObjectIdentity = ObjectIdentity
proBrsMib = _ProBrsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1)
)
_ProBrsNumber_Type = Integer32
_ProBrsNumber_Object = MibScalar
proBrsNumber = _ProBrsNumber_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 1),
    _ProBrsNumber_Type()
)
proBrsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsNumber.setStatus("mandatory")
_ProBrsPortTable_Object = MibTable
proBrsPortTable = _ProBrsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    proBrsPortTable.setStatus("mandatory")
_ProBrsPortEntry_Object = MibTableRow
proBrsPortEntry = _ProBrsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 2, 1)
)
proBrsPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    proBrsPortEntry.setStatus("mandatory")
_ProBrsClassNumber_Type = Integer32
_ProBrsClassNumber_Object = MibTableColumn
proBrsClassNumber = _ProBrsClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 2, 1, 1),
    _ProBrsClassNumber_Type()
)
proBrsClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsClassNumber.setStatus("mandatory")


class _ProBrsDefaultClassName_Type(DisplayString):
    """Custom type proBrsDefaultClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ProBrsDefaultClassName_Type.__name__ = "DisplayString"
_ProBrsDefaultClassName_Object = MibTableColumn
proBrsDefaultClassName = _ProBrsDefaultClassName_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 2, 1, 2),
    _ProBrsDefaultClassName_Type()
)
proBrsDefaultClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsDefaultClassName.setStatus("mandatory")
_ProBrsDefaultPriority_Type = BRSPriority
_ProBrsDefaultPriority_Object = MibTableColumn
proBrsDefaultPriority = _ProBrsDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 2, 1, 3),
    _ProBrsDefaultPriority_Type()
)
proBrsDefaultPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsDefaultPriority.setStatus("mandatory")
_ProBrsClassTable_Object = MibTable
proBrsClassTable = _ProBrsClassTable_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    proBrsClassTable.setStatus("mandatory")
_ProBrsClassEntry_Object = MibTableRow
proBrsClassEntry = _ProBrsClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 3, 1)
)
proBrsClassEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BRS-MIB", "proBrsClassId"),
)
if mibBuilder.loadTexts:
    proBrsClassEntry.setStatus("mandatory")
_ProBrsClassId_Type = Integer32
_ProBrsClassId_Object = MibTableColumn
proBrsClassId = _ProBrsClassId_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 3, 1, 1),
    _ProBrsClassId_Type()
)
proBrsClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsClassId.setStatus("mandatory")


class _ProBrsClassName_Type(DisplayString):
    """Custom type proBrsClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ProBrsClassName_Type.__name__ = "DisplayString"
_ProBrsClassName_Object = MibTableColumn
proBrsClassName = _ProBrsClassName_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 3, 1, 2),
    _ProBrsClassName_Type()
)
proBrsClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsClassName.setStatus("mandatory")
_ProBrsClassAlloc_Type = Integer32
_ProBrsClassAlloc_Object = MibTableColumn
proBrsClassAlloc = _ProBrsClassAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 3, 1, 3),
    _ProBrsClassAlloc_Type()
)
proBrsClassAlloc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proBrsClassAlloc.setStatus("mandatory")
_ProBrsClassBytes_Type = Integer32
_ProBrsClassBytes_Object = MibTableColumn
proBrsClassBytes = _ProBrsClassBytes_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 3, 1, 4),
    _ProBrsClassBytes_Type()
)
proBrsClassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsClassBytes.setStatus("mandatory")
_ProBrsClassPkts_Type = Integer32
_ProBrsClassPkts_Object = MibTableColumn
proBrsClassPkts = _ProBrsClassPkts_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 3, 1, 5),
    _ProBrsClassPkts_Type()
)
proBrsClassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsClassPkts.setStatus("mandatory")
_ProBrsClassDiscs_Type = Integer32
_ProBrsClassDiscs_Object = MibTableColumn
proBrsClassDiscs = _ProBrsClassDiscs_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 3, 1, 6),
    _ProBrsClassDiscs_Type()
)
proBrsClassDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsClassDiscs.setStatus("mandatory")
_ProBrsFilterTable_Object = MibTable
proBrsFilterTable = _ProBrsFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 4)
)
if mibBuilder.loadTexts:
    proBrsFilterTable.setStatus("mandatory")
_ProBrsFilterEntry_Object = MibTableRow
proBrsFilterEntry = _ProBrsFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 4, 1)
)
proBrsFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BRS-MIB", "proBrsClassId"),
    (0, "BRS-MIB", "proBrsFilterId"),
)
if mibBuilder.loadTexts:
    proBrsFilterEntry.setStatus("mandatory")
_ProBrsFilterId_Type = Integer32
_ProBrsFilterId_Object = MibTableColumn
proBrsFilterId = _ProBrsFilterId_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 4, 1, 1),
    _ProBrsFilterId_Type()
)
proBrsFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsFilterId.setStatus("mandatory")


class _ProBrsFilterName_Type(DisplayString):
    """Custom type proBrsFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ProBrsFilterName_Type.__name__ = "DisplayString"
_ProBrsFilterName_Object = MibTableColumn
proBrsFilterName = _ProBrsFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 4, 1, 2),
    _ProBrsFilterName_Type()
)
proBrsFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsFilterName.setStatus("mandatory")


class _ProBrsFilterPriority_Type(Integer32):
    """Custom type proBrsFilterPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("normal", 2),
          ("urgent", 4))
    )


_ProBrsFilterPriority_Type.__name__ = "Integer32"
_ProBrsFilterPriority_Object = MibTableColumn
proBrsFilterPriority = _ProBrsFilterPriority_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 4, 1, 3),
    _ProBrsFilterPriority_Type()
)
proBrsFilterPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsFilterPriority.setStatus("mandatory")


class _ProBrsFilterPortType_Type(Integer32):
    """Custom type proBrsFilterPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_ProBrsFilterPortType_Type.__name__ = "Integer32"
_ProBrsFilterPortType_Object = MibTableColumn
proBrsFilterPortType = _ProBrsFilterPortType_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 4, 1, 4),
    _ProBrsFilterPortType_Type()
)
proBrsFilterPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsFilterPortType.setStatus("mandatory")


class _ProBrsFilterLowPortNum_Type(Integer32):
    """Custom type proBrsFilterLowPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ProBrsFilterLowPortNum_Type.__name__ = "Integer32"
_ProBrsFilterLowPortNum_Object = MibTableColumn
proBrsFilterLowPortNum = _ProBrsFilterLowPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 4, 1, 5),
    _ProBrsFilterLowPortNum_Type()
)
proBrsFilterLowPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsFilterLowPortNum.setStatus("mandatory")


class _ProBrsFilterHighPortNum_Type(Integer32):
    """Custom type proBrsFilterHighPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ProBrsFilterHighPortNum_Type.__name__ = "Integer32"
_ProBrsFilterHighPortNum_Object = MibTableColumn
proBrsFilterHighPortNum = _ProBrsFilterHighPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 4, 1, 6),
    _ProBrsFilterHighPortNum_Type()
)
proBrsFilterHighPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsFilterHighPortNum.setStatus("mandatory")
_ProBrsFilterIpAddr_Type = IpAddress
_ProBrsFilterIpAddr_Object = MibTableColumn
proBrsFilterIpAddr = _ProBrsFilterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 4, 1, 7),
    _ProBrsFilterIpAddr_Type()
)
proBrsFilterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsFilterIpAddr.setStatus("mandatory")


class _ProBrsFilterTag_Type(Integer32):
    """Custom type proBrsFilterTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ProBrsFilterTag_Type.__name__ = "Integer32"
_ProBrsFilterTag_Object = MibTableColumn
proBrsFilterTag = _ProBrsFilterTag_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 7, 1, 1, 4, 1, 8),
    _ProBrsFilterTag_Type()
)
proBrsFilterTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proBrsFilterTag.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRS-MIB",
    **{"BRSPriority": BRSPriority,
       "proteon": proteon,
       "proAdmin": proAdmin,
       "proFeature": proFeature,
       "proFeatureBrs": proFeatureBrs,
       "proBrsMib": proBrsMib,
       "proBrsNumber": proBrsNumber,
       "proBrsPortTable": proBrsPortTable,
       "proBrsPortEntry": proBrsPortEntry,
       "proBrsClassNumber": proBrsClassNumber,
       "proBrsDefaultClassName": proBrsDefaultClassName,
       "proBrsDefaultPriority": proBrsDefaultPriority,
       "proBrsClassTable": proBrsClassTable,
       "proBrsClassEntry": proBrsClassEntry,
       "proBrsClassId": proBrsClassId,
       "proBrsClassName": proBrsClassName,
       "proBrsClassAlloc": proBrsClassAlloc,
       "proBrsClassBytes": proBrsClassBytes,
       "proBrsClassPkts": proBrsClassPkts,
       "proBrsClassDiscs": proBrsClassDiscs,
       "proBrsFilterTable": proBrsFilterTable,
       "proBrsFilterEntry": proBrsFilterEntry,
       "proBrsFilterId": proBrsFilterId,
       "proBrsFilterName": proBrsFilterName,
       "proBrsFilterPriority": proBrsFilterPriority,
       "proBrsFilterPortType": proBrsFilterPortType,
       "proBrsFilterLowPortNum": proBrsFilterLowPortNum,
       "proBrsFilterHighPortNum": proBrsFilterHighPortNum,
       "proBrsFilterIpAddr": proBrsFilterIpAddr,
       "proBrsFilterTag": proBrsFilterTag}
)
