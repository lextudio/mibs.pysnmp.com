# SNMP MIB module (IBMBNA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBMBNA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:49 2024
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



class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmArchitecture_ObjectIdentity = ObjectIdentity
ibmArchitecture = _IbmArchitecture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5)
)
_IbmBna_ObjectIdentity = ObjectIdentity
ibmBna = _IbmBna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 21)
)
_IbmBnaObjects_ObjectIdentity = ObjectIdentity
ibmBnaObjects = _IbmBnaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1)
)
_IbmBnaLocalTgTable_Object = MibTable
ibmBnaLocalTgTable = _IbmBnaLocalTgTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 1)
)
if mibBuilder.loadTexts:
    ibmBnaLocalTgTable.setStatus("mandatory")
_IbmBnaLocalTgEntry_Object = MibTableRow
ibmBnaLocalTgEntry = _IbmBnaLocalTgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 1, 1)
)
ibmBnaLocalTgEntry.setIndexNames(
    (0, "IBMBNA-MIB", "ibmBnaLocalTgDest"),
    (0, "IBMBNA-MIB", "ibmBnaLocalTgNum"),
)
if mibBuilder.loadTexts:
    ibmBnaLocalTgEntry.setStatus("mandatory")


class _IbmBnaLocalTgDest_Type(DisplayString):
    """Custom type ibmBnaLocalTgDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmBnaLocalTgDest_Type.__name__ = "DisplayString"
_IbmBnaLocalTgDest_Object = MibTableColumn
ibmBnaLocalTgDest = _IbmBnaLocalTgDest_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 1, 1, 1),
    _IbmBnaLocalTgDest_Type()
)
ibmBnaLocalTgDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBnaLocalTgDest.setStatus("mandatory")


class _IbmBnaLocalTgNum_Type(Integer32):
    """Custom type ibmBnaLocalTgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmBnaLocalTgNum_Type.__name__ = "Integer32"
_IbmBnaLocalTgNum_Object = MibTableColumn
ibmBnaLocalTgNum = _IbmBnaLocalTgNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 1, 1, 2),
    _IbmBnaLocalTgNum_Type()
)
ibmBnaLocalTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBnaLocalTgNum.setStatus("mandatory")


class _IbmBnaLocalTgLinkType_Type(Integer32):
    """Custom type ibmBnaLocalTgLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("downlink", 3),
          ("downlinkToBranchNetworkNode", 4),
          ("other", 1),
          ("unknown", 255),
          ("uplink", 2))
    )


_IbmBnaLocalTgLinkType_Type.__name__ = "Integer32"
_IbmBnaLocalTgLinkType_Object = MibTableColumn
ibmBnaLocalTgLinkType = _IbmBnaLocalTgLinkType_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 1, 1, 3),
    _IbmBnaLocalTgLinkType_Type()
)
ibmBnaLocalTgLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBnaLocalTgLinkType.setStatus("mandatory")
_IbmBnaNnTopologyFRTable_Object = MibTable
ibmBnaNnTopologyFRTable = _IbmBnaNnTopologyFRTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 2)
)
if mibBuilder.loadTexts:
    ibmBnaNnTopologyFRTable.setStatus("mandatory")
_IbmBnaNnTopologyFREntry_Object = MibTableRow
ibmBnaNnTopologyFREntry = _IbmBnaNnTopologyFREntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 2, 1)
)
ibmBnaNnTopologyFREntry.setIndexNames(
    (0, "IBMBNA-MIB", "ibmBnaNnNodeFRFrsn"),
    (0, "IBMBNA-MIB", "ibmBnaNnNodeFRName"),
)
if mibBuilder.loadTexts:
    ibmBnaNnTopologyFREntry.setStatus("mandatory")
_IbmBnaNnNodeFRFrsn_Type = Gauge32
_IbmBnaNnNodeFRFrsn_Object = MibTableColumn
ibmBnaNnNodeFRFrsn = _IbmBnaNnNodeFRFrsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 2, 1, 1),
    _IbmBnaNnNodeFRFrsn_Type()
)
ibmBnaNnNodeFRFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBnaNnNodeFRFrsn.setStatus("mandatory")


class _IbmBnaNnNodeFRName_Type(DisplayString):
    """Custom type ibmBnaNnNodeFRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmBnaNnNodeFRName_Type.__name__ = "DisplayString"
_IbmBnaNnNodeFRName_Object = MibTableColumn
ibmBnaNnNodeFRName = _IbmBnaNnNodeFRName_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 2, 1, 2),
    _IbmBnaNnNodeFRName_Type()
)
ibmBnaNnNodeFRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBnaNnNodeFRName.setStatus("mandatory")
_IbmBnaNnNodeFRBranchAwareness_Type = TruthValue
_IbmBnaNnNodeFRBranchAwareness_Object = MibTableColumn
ibmBnaNnNodeFRBranchAwareness = _IbmBnaNnNodeFRBranchAwareness_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 2, 1, 3),
    _IbmBnaNnNodeFRBranchAwareness_Type()
)
ibmBnaNnNodeFRBranchAwareness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBnaNnNodeFRBranchAwareness.setStatus("mandatory")
_IbmBnaNnTgTopologyFRTable_Object = MibTable
ibmBnaNnTgTopologyFRTable = _IbmBnaNnTgTopologyFRTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 3)
)
if mibBuilder.loadTexts:
    ibmBnaNnTgTopologyFRTable.setStatus("mandatory")
_IbmBnaNnTgTopologyFREntry_Object = MibTableRow
ibmBnaNnTgTopologyFREntry = _IbmBnaNnTgTopologyFREntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 3, 1)
)
ibmBnaNnTgTopologyFREntry.setIndexNames(
    (0, "IBMBNA-MIB", "ibmBnaNnTgFRFrsn"),
    (0, "IBMBNA-MIB", "ibmBnaNnTgFROwner"),
    (0, "IBMBNA-MIB", "ibmBnaNnTgFRDest"),
    (0, "IBMBNA-MIB", "ibmBnaNnTgFRNum"),
)
if mibBuilder.loadTexts:
    ibmBnaNnTgTopologyFREntry.setStatus("mandatory")
_IbmBnaNnTgFRFrsn_Type = Gauge32
_IbmBnaNnTgFRFrsn_Object = MibTableColumn
ibmBnaNnTgFRFrsn = _IbmBnaNnTgFRFrsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 3, 1, 1),
    _IbmBnaNnTgFRFrsn_Type()
)
ibmBnaNnTgFRFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBnaNnTgFRFrsn.setStatus("mandatory")


class _IbmBnaNnTgFROwner_Type(DisplayString):
    """Custom type ibmBnaNnTgFROwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmBnaNnTgFROwner_Type.__name__ = "DisplayString"
_IbmBnaNnTgFROwner_Object = MibTableColumn
ibmBnaNnTgFROwner = _IbmBnaNnTgFROwner_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 3, 1, 2),
    _IbmBnaNnTgFROwner_Type()
)
ibmBnaNnTgFROwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBnaNnTgFROwner.setStatus("mandatory")


class _IbmBnaNnTgFRDest_Type(DisplayString):
    """Custom type ibmBnaNnTgFRDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmBnaNnTgFRDest_Type.__name__ = "DisplayString"
_IbmBnaNnTgFRDest_Object = MibTableColumn
ibmBnaNnTgFRDest = _IbmBnaNnTgFRDest_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 3, 1, 3),
    _IbmBnaNnTgFRDest_Type()
)
ibmBnaNnTgFRDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBnaNnTgFRDest.setStatus("mandatory")


class _IbmBnaNnTgFRNum_Type(Integer32):
    """Custom type ibmBnaNnTgFRNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmBnaNnTgFRNum_Type.__name__ = "Integer32"
_IbmBnaNnTgFRNum_Object = MibTableColumn
ibmBnaNnTgFRNum = _IbmBnaNnTgFRNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 3, 1, 4),
    _IbmBnaNnTgFRNum_Type()
)
ibmBnaNnTgFRNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBnaNnTgFRNum.setStatus("mandatory")
_IbmBnaNnTgFRBranchTg_Type = TruthValue
_IbmBnaNnTgFRBranchTg_Object = MibTableColumn
ibmBnaNnTgFRBranchTg = _IbmBnaNnTgFRBranchTg_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 3, 1, 5),
    _IbmBnaNnTgFRBranchTg_Type()
)
ibmBnaNnTgFRBranchTg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBnaNnTgFRBranchTg.setStatus("mandatory")
_IbmBnaDirTable_Object = MibTable
ibmBnaDirTable = _IbmBnaDirTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 4)
)
if mibBuilder.loadTexts:
    ibmBnaDirTable.setStatus("mandatory")
_IbmBnaDirEntry_Object = MibTableRow
ibmBnaDirEntry = _IbmBnaDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 4, 1)
)
ibmBnaDirEntry.setIndexNames(
    (0, "IBMBNA-MIB", "ibmBnaDirLuName"),
)
if mibBuilder.loadTexts:
    ibmBnaDirEntry.setStatus("mandatory")


class _IbmBnaDirLuName_Type(DisplayString):
    """Custom type ibmBnaDirLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_IbmBnaDirLuName_Type.__name__ = "DisplayString"
_IbmBnaDirLuName_Object = MibTableColumn
ibmBnaDirLuName = _IbmBnaDirLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 4, 1, 1),
    _IbmBnaDirLuName_Type()
)
ibmBnaDirLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBnaDirLuName.setStatus("mandatory")


class _IbmBnaDirApparentLuOwnerName_Type(DisplayString):
    """Custom type ibmBnaDirApparentLuOwnerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 17),
    )


_IbmBnaDirApparentLuOwnerName_Type.__name__ = "DisplayString"
_IbmBnaDirApparentLuOwnerName_Object = MibTableColumn
ibmBnaDirApparentLuOwnerName = _IbmBnaDirApparentLuOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 4, 1, 2),
    _IbmBnaDirApparentLuOwnerName_Type()
)
ibmBnaDirApparentLuOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBnaDirApparentLuOwnerName.setStatus("mandatory")
_IbmBnaConformance_ObjectIdentity = ObjectIdentity
ibmBnaConformance = _IbmBnaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 2)
)
_IbmBnaCompliances_ObjectIdentity = ObjectIdentity
ibmBnaCompliances = _IbmBnaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 2, 1)
)
_IbmBnaConfGroups_ObjectIdentity = ObjectIdentity
ibmBnaConfGroups = _IbmBnaConfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 21, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBMBNA-MIB",
    **{"TruthValue": TruthValue,
       "ibm": ibm,
       "ibmArchitecture": ibmArchitecture,
       "ibmBna": ibmBna,
       "ibmBnaObjects": ibmBnaObjects,
       "ibmBnaLocalTgTable": ibmBnaLocalTgTable,
       "ibmBnaLocalTgEntry": ibmBnaLocalTgEntry,
       "ibmBnaLocalTgDest": ibmBnaLocalTgDest,
       "ibmBnaLocalTgNum": ibmBnaLocalTgNum,
       "ibmBnaLocalTgLinkType": ibmBnaLocalTgLinkType,
       "ibmBnaNnTopologyFRTable": ibmBnaNnTopologyFRTable,
       "ibmBnaNnTopologyFREntry": ibmBnaNnTopologyFREntry,
       "ibmBnaNnNodeFRFrsn": ibmBnaNnNodeFRFrsn,
       "ibmBnaNnNodeFRName": ibmBnaNnNodeFRName,
       "ibmBnaNnNodeFRBranchAwareness": ibmBnaNnNodeFRBranchAwareness,
       "ibmBnaNnTgTopologyFRTable": ibmBnaNnTgTopologyFRTable,
       "ibmBnaNnTgTopologyFREntry": ibmBnaNnTgTopologyFREntry,
       "ibmBnaNnTgFRFrsn": ibmBnaNnTgFRFrsn,
       "ibmBnaNnTgFROwner": ibmBnaNnTgFROwner,
       "ibmBnaNnTgFRDest": ibmBnaNnTgFRDest,
       "ibmBnaNnTgFRNum": ibmBnaNnTgFRNum,
       "ibmBnaNnTgFRBranchTg": ibmBnaNnTgFRBranchTg,
       "ibmBnaDirTable": ibmBnaDirTable,
       "ibmBnaDirEntry": ibmBnaDirEntry,
       "ibmBnaDirLuName": ibmBnaDirLuName,
       "ibmBnaDirApparentLuOwnerName": ibmBnaDirApparentLuOwnerName,
       "ibmBnaConformance": ibmBnaConformance,
       "ibmBnaCompliances": ibmBnaCompliances,
       "ibmBnaConfGroups": ibmBnaConfGroups}
)
