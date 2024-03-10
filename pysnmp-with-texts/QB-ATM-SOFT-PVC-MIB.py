"""SNMP MIB module (QB-ATM-SOFT-PVC-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QB-ATM-SOFT-PVC-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 11:37:29 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
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

(atmVclVci,
 atmVclVpi,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi",
    "atmVplVpi")

(atmSoftPVccEntry,
 atmSoftPVpcEntry) = mibBuilder.importSymbols(
    "ATM-SOFT-PVC-MIB",
    "atmSoftPVccEntry",
    "atmSoftPVpcEntry")

(AtmVorXLastChange,
 AtmVorXAdminStatus,
 AtmTrafficDescrParamIndex,
 atmNoClpNoScr,
 AtmConnCastType,
 AtmServiceCategory,
 AtmConnKind,
 AtmVpIdentifier,
 AtmVorXOperStatus,
 AtmAddr,
 AtmVcIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVorXLastChange",
    "AtmVorXAdminStatus",
    "AtmTrafficDescrParamIndex",
    "atmNoClpNoScr",
    "AtmConnCastType",
    "AtmServiceCategory",
    "AtmConnKind",
    "AtmVpIdentifier",
    "AtmVorXOperStatus",
    "AtmAddr",
    "AtmVcIdentifier")

(ifIndex,
 InterfaceIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "InterfaceIndex")

(qbVTConfVTId,) = mibBuilder.importSymbols(
    "QB-VT15-MIB",
    "qbVTConfVTId")

(qbSysModuleSlot,) = mibBuilder.importSymbols(
    "QBSYS-SYSTEM-MIB",
    "qbSysModuleSlot")

(qbMibs,) = mibBuilder.importSymbols(
    "QUANTUMBRIDGE-REG",
    "qbMibs")

(ObjectGroup,
 NotificationGroup,
 ModuleCompliance) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ObjectGroup",
    "NotificationGroup",
    "ModuleCompliance")

(Bits,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Counter64,
 iso,
 enterprises,
 ObjectIdentity,
 TimeTicks,
 IpAddress,
 Gauge32,
 NotificationType,
 Counter32,
 MibIdentifier,
 Integer32,
 ModuleIdentity,
 Unsigned32) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Counter64",
    "iso",
    "enterprises",
    "ObjectIdentity",
    "TimeTicks",
    "IpAddress",
    "Gauge32",
    "NotificationType",
    "Counter32",
    "MibIdentifier",
    "Integer32",
    "ModuleIdentity",
    "Unsigned32")

(DisplayString,
 TextualConvention,
 TruthValue,
 RowStatus,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue",
    "RowStatus",
    "TimeStamp")


# MODULE-IDENTITY

qbAtmSoftPvcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12)
)
qbAtmSoftPvcMIB.setLastUpdated("9606210000Z")
if mibBuilder.loadTexts:
    qbAtmSoftPvcMIB.setOrganization("""\
Quantum Bridge Inc.
""")
qbAtmSoftPvcMIB.setContactInfo("""\
akoifman@quantumbridge.com
""")
if mibBuilder.loadTexts:
    qbAtmSoftPvcMIB.setDescription("""\
QB ATM Soft PVC MIB
""")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QbAtmSoftPvcMIBObjects_ObjectIdentity = ObjectIdentity
qbAtmSoftPvcMIBObjects = _QbAtmSoftPvcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 1)
)
_QbIfIndexToVclTable_Object = MibTable
qbIfIndexToVclTable = _QbIfIndexToVclTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 1, 1)
)
if mibBuilder.loadTexts:
    qbIfIndexToVclTable.setStatus("current")
if mibBuilder.loadTexts:
    qbIfIndexToVclTable.setDescription("""\
The QB table to map ifIndex to VPI/VCI for non-native interfaces
""")
_QbIfIndexToVclEntry_Object = MibTableRow
qbIfIndexToVclEntry = _QbIfIndexToVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 1, 1, 1)
)
qbIfIndexToVclEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "QB-VT15-MIB", "qbVTConfVTId"),
)
if mibBuilder.loadTexts:
    qbIfIndexToVclEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbIfIndexToVclEntry.setDescription("""\
Contains VPI, VCI for hidden interfaces
""")
_QbIfIndexToVclIfIndex_Type = InterfaceIndex
_QbIfIndexToVclIfIndex_Object = MibTableColumn
qbIfIndexToVclIfIndex = _QbIfIndexToVclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 1, 1, 1, 1),
    _QbIfIndexToVclIfIndex_Type()
)
qbIfIndexToVclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbIfIndexToVclIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbIfIndexToVclIfIndex.setDescription("""\
ifIndex value for non-native ATM interfaces.
""")
_QbIfIndexToVclVpi_Type = AtmVpIdentifier
_QbIfIndexToVclVpi_Object = MibTableColumn
qbIfIndexToVclVpi = _QbIfIndexToVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 1, 1, 1, 2),
    _QbIfIndexToVclVpi_Type()
)
qbIfIndexToVclVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbIfIndexToVclVpi.setStatus("current")
if mibBuilder.loadTexts:
    qbIfIndexToVclVpi.setDescription("""\
The VPI value of the VCL.
""")
_QbIfIndexToVclVci_Type = AtmVcIdentifier
_QbIfIndexToVclVci_Object = MibTableColumn
qbIfIndexToVclVci = _QbIfIndexToVclVci_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 1, 1, 1, 3),
    _QbIfIndexToVclVci_Type()
)
qbIfIndexToVclVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbIfIndexToVclVci.setStatus("current")
if mibBuilder.loadTexts:
    qbIfIndexToVclVci.setDescription("""\
The VCI value of the VCL.
""")
_QbAtmSoftPVccTable_Object = MibTable
qbAtmSoftPVccTable = _QbAtmSoftPVccTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 1, 2)
)
if mibBuilder.loadTexts:
    qbAtmSoftPVccTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmSoftPVccTable.setDescription("""\
The QB table with extensions to atmSoftPVccTable
""")
_QbAtmSoftPVccEntry_Object = MibTableRow
qbAtmSoftPVccEntry = _QbAtmSoftPVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 1, 2, 1)
)
atmSoftPVccEntry.registerAugmentions(
    ("QB-ATM-SOFT-PVC-MIB",
     "qbAtmSoftPVccEntry")
)
qbAtmSoftPVccEntry.setIndexNames(*atmSoftPVccEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbAtmSoftPVccEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmSoftPVccEntry.setDescription("""\
Entry in qbAtmSoftPVccTable
""")


class _QbAtmSoftPVccName_Type(DisplayString):
    """Custom type qbAtmSoftPVccName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbAtmSoftPVccName_Type.__name__ = "DisplayString"
_QbAtmSoftPVccName_Object = MibTableColumn
qbAtmSoftPVccName = _QbAtmSoftPVccName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 1, 2, 1, 1),
    _QbAtmSoftPVccName_Type()
)
qbAtmSoftPVccName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmSoftPVccName.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmSoftPVccName.setDescription("""\
A textual description for the SPVC name.
""")


class _QbAtmSoftPVccType_Type(Integer32):
    """Custom type qbAtmSoftPVccType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("native", 1),
          ("non-native", 2))
    )


_QbAtmSoftPVccType_Type.__name__ = "Integer32"
_QbAtmSoftPVccType_Object = MibTableColumn
qbAtmSoftPVccType = _QbAtmSoftPVccType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 1, 2, 1, 2),
    _QbAtmSoftPVccType_Type()
)
qbAtmSoftPVccType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmSoftPVccType.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmSoftPVccType.setDescription("""\
Value for the interface type. Native ATM - Q155, S622; non-native - E1, DS1,
ENET, VT
""")
_QbAtmSoftPVccIfIndex_Type = InterfaceIndex
_QbAtmSoftPVccIfIndex_Object = MibTableColumn
qbAtmSoftPVccIfIndex = _QbAtmSoftPVccIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 1, 2, 1, 3),
    _QbAtmSoftPVccIfIndex_Type()
)
qbAtmSoftPVccIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmSoftPVccIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmSoftPVccIfIndex.setDescription("""\
ifIndex value for IOT interface. This value is not used for native ATM
interfaces.
""")


class _QbAtmSoftPVccVtIndex_Type(Integer32):
    """Custom type qbAtmSoftPVccVtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QbAtmSoftPVccVtIndex_Type.__name__ = "Integer32"
_QbAtmSoftPVccVtIndex_Object = MibTableColumn
qbAtmSoftPVccVtIndex = _QbAtmSoftPVccVtIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 1, 2, 1, 4),
    _QbAtmSoftPVccVtIndex_Type()
)
qbAtmSoftPVccVtIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmSoftPVccVtIndex.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmSoftPVccVtIndex.setDescription("""\
Address information for a VT card. This value is used for VT card only.
""")
_QbAtmSoftPVpcTable_Object = MibTable
qbAtmSoftPVpcTable = _QbAtmSoftPVpcTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 1, 3)
)
if mibBuilder.loadTexts:
    qbAtmSoftPVpcTable.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmSoftPVpcTable.setDescription("""\
The QB table with extensions to atmSoftPVpcTable
""")
_QbAtmSoftPVpcEntry_Object = MibTableRow
qbAtmSoftPVpcEntry = _QbAtmSoftPVpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 1, 3, 1)
)
atmSoftPVpcEntry.registerAugmentions(
    ("QB-ATM-SOFT-PVC-MIB",
     "qbAtmSoftPVpcEntry")
)
qbAtmSoftPVpcEntry.setIndexNames(*atmSoftPVpcEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbAtmSoftPVpcEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmSoftPVpcEntry.setDescription("""\
Entry in qbAtmSoftPVpcTable
""")


class _QbAtmSoftPVpcName_Type(DisplayString):
    """Custom type qbAtmSoftPVpcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbAtmSoftPVpcName_Type.__name__ = "DisplayString"
_QbAtmSoftPVpcName_Object = MibTableColumn
qbAtmSoftPVpcName = _QbAtmSoftPVpcName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 1, 3, 1, 1),
    _QbAtmSoftPVpcName_Type()
)
qbAtmSoftPVpcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbAtmSoftPVpcName.setStatus("current")
if mibBuilder.loadTexts:
    qbAtmSoftPVpcName.setDescription("""\
A textual description for the SPVC name.
""")
_QbAtmSoftPvcConformance_ObjectIdentity = ObjectIdentity
qbAtmSoftPvcConformance = _QbAtmSoftPvcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 2)
)
_QbSpvcCompliances_ObjectIdentity = ObjectIdentity
qbSpvcCompliances = _QbSpvcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 2, 1)
)
_QbAtmGroups_ObjectIdentity = ObjectIdentity
qbAtmGroups = _QbAtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 2, 2)
)
_QbAtmSoftPvcBaseGroup_ObjectIdentity = ObjectIdentity
qbAtmSoftPvcBaseGroup = _QbAtmSoftPvcBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 3)
)

# Managed Objects groups

qbSpvcAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 2, 2, 1)
)
qbSpvcAllGroup.setObjects(
      *(("QB-ATM-SOFT-PVC-MIB", "qbAtmSoftPVccName"),
        ("QB-ATM-SOFT-PVC-MIB", "qbAtmSoftPVpcName"))
)
if mibBuilder.loadTexts:
    qbSpvcAllGroup.setStatus("current")
if mibBuilder.loadTexts:
    qbSpvcAllGroup.setDescription("""\
The set of all accessible objects in this MIB.
""")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qbSpvcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4323, 2, 12, 2, 1, 1)
)
if mibBuilder.loadTexts:
    qbSpvcCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    qbSpvcCompliance.setDescription("""\
The compliance statement for all agents that support this MIB. A compliant
agent implements all objects defined in this MIB.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QB-ATM-SOFT-PVC-MIB",
    **{"qbAtmSoftPvcMIB": qbAtmSoftPvcMIB,
       "qbAtmSoftPvcMIBObjects": qbAtmSoftPvcMIBObjects,
       "qbIfIndexToVclTable": qbIfIndexToVclTable,
       "qbIfIndexToVclEntry": qbIfIndexToVclEntry,
       "qbIfIndexToVclIfIndex": qbIfIndexToVclIfIndex,
       "qbIfIndexToVclVpi": qbIfIndexToVclVpi,
       "qbIfIndexToVclVci": qbIfIndexToVclVci,
       "qbAtmSoftPVccTable": qbAtmSoftPVccTable,
       "qbAtmSoftPVccEntry": qbAtmSoftPVccEntry,
       "qbAtmSoftPVccName": qbAtmSoftPVccName,
       "qbAtmSoftPVccType": qbAtmSoftPVccType,
       "qbAtmSoftPVccIfIndex": qbAtmSoftPVccIfIndex,
       "qbAtmSoftPVccVtIndex": qbAtmSoftPVccVtIndex,
       "qbAtmSoftPVpcTable": qbAtmSoftPVpcTable,
       "qbAtmSoftPVpcEntry": qbAtmSoftPVpcEntry,
       "qbAtmSoftPVpcName": qbAtmSoftPVpcName,
       "qbAtmSoftPvcConformance": qbAtmSoftPvcConformance,
       "qbSpvcCompliances": qbSpvcCompliances,
       "qbSpvcCompliance": qbSpvcCompliance,
       "qbAtmGroups": qbAtmGroups,
       "qbSpvcAllGroup": qbSpvcAllGroup,
       "qbAtmSoftPvcBaseGroup": qbAtmSoftPvcBaseGroup}
)
