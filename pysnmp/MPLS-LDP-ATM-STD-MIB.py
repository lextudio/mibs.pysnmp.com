# SNMP MIB module (MPLS-LDP-ATM-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-LDP-ATM-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:11 2024
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

(AtmVpIdentifier,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVpIdentifier")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(mplsLdpEntityIndex,
 mplsLdpEntityLdpId,
 mplsLdpPeerLdpId) = mibBuilder.importSymbols(
    "MPLS-LDP-STD-MIB",
    "mplsLdpEntityIndex",
    "mplsLdpEntityLdpId",
    "mplsLdpPeerLdpId")

(MplsAtmVcIdentifier,
 mplsStdMIB) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsAtmVcIdentifier",
    "mplsStdMIB")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

mplsLdpAtmStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 5)
)
mplsLdpAtmStdMIB.setRevisions(
        ("2004-06-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsLdpAtmObjects_ObjectIdentity = ObjectIdentity
mplsLdpAtmObjects = _MplsLdpAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1)
)
_MplsLdpEntityAtmObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityAtmObjects = _MplsLdpEntityAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1)
)
_MplsLdpEntityAtmTable_Object = MibTable
mplsLdpEntityAtmTable = _MplsLdpEntityAtmTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityAtmTable.setStatus("current")
_MplsLdpEntityAtmEntry_Object = MibTableRow
mplsLdpEntityAtmEntry = _MplsLdpEntityAtmEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1)
)
mplsLdpEntityAtmEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityAtmEntry.setStatus("current")
_MplsLdpEntityAtmIfIndexOrZero_Type = InterfaceIndexOrZero
_MplsLdpEntityAtmIfIndexOrZero_Object = MibTableColumn
mplsLdpEntityAtmIfIndexOrZero = _MplsLdpEntityAtmIfIndexOrZero_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 1),
    _MplsLdpEntityAtmIfIndexOrZero_Type()
)
mplsLdpEntityAtmIfIndexOrZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmIfIndexOrZero.setStatus("current")


class _MplsLdpEntityAtmMergeCap_Type(Integer32):
    """Custom type mplsLdpEntityAtmMergeCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("vcMerge", 2),
          ("vpAndVcMerge", 3),
          ("vpMerge", 1))
    )


_MplsLdpEntityAtmMergeCap_Type.__name__ = "Integer32"
_MplsLdpEntityAtmMergeCap_Object = MibTableColumn
mplsLdpEntityAtmMergeCap = _MplsLdpEntityAtmMergeCap_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 2),
    _MplsLdpEntityAtmMergeCap_Type()
)
mplsLdpEntityAtmMergeCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmMergeCap.setStatus("current")


class _MplsLdpEntityAtmLRComponents_Type(Unsigned32):
    """Custom type mplsLdpEntityAtmLRComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpEntityAtmLRComponents_Type.__name__ = "Unsigned32"
_MplsLdpEntityAtmLRComponents_Object = MibTableColumn
mplsLdpEntityAtmLRComponents = _MplsLdpEntityAtmLRComponents_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 3),
    _MplsLdpEntityAtmLRComponents_Type()
)
mplsLdpEntityAtmLRComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLRComponents.setStatus("current")


class _MplsLdpEntityAtmVcDirectionality_Type(Integer32):
    """Custom type mplsLdpEntityAtmVcDirectionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 0),
          ("unidirectional", 1))
    )


_MplsLdpEntityAtmVcDirectionality_Type.__name__ = "Integer32"
_MplsLdpEntityAtmVcDirectionality_Object = MibTableColumn
mplsLdpEntityAtmVcDirectionality = _MplsLdpEntityAtmVcDirectionality_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 4),
    _MplsLdpEntityAtmVcDirectionality_Type()
)
mplsLdpEntityAtmVcDirectionality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmVcDirectionality.setStatus("current")


class _MplsLdpEntityAtmLsrConnectivity_Type(Integer32):
    """Custom type mplsLdpEntityAtmLsrConnectivity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("indirect", 2))
    )


_MplsLdpEntityAtmLsrConnectivity_Type.__name__ = "Integer32"
_MplsLdpEntityAtmLsrConnectivity_Object = MibTableColumn
mplsLdpEntityAtmLsrConnectivity = _MplsLdpEntityAtmLsrConnectivity_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 5),
    _MplsLdpEntityAtmLsrConnectivity_Type()
)
mplsLdpEntityAtmLsrConnectivity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLsrConnectivity.setStatus("current")


class _MplsLdpEntityAtmDefaultControlVpi_Type(AtmVpIdentifier):
    """Custom type mplsLdpEntityAtmDefaultControlVpi based on AtmVpIdentifier"""
    defaultValue = 0


_MplsLdpEntityAtmDefaultControlVpi_Object = MibTableColumn
mplsLdpEntityAtmDefaultControlVpi = _MplsLdpEntityAtmDefaultControlVpi_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 6),
    _MplsLdpEntityAtmDefaultControlVpi_Type()
)
mplsLdpEntityAtmDefaultControlVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmDefaultControlVpi.setStatus("current")


class _MplsLdpEntityAtmDefaultControlVci_Type(MplsAtmVcIdentifier):
    """Custom type mplsLdpEntityAtmDefaultControlVci based on MplsAtmVcIdentifier"""
    defaultValue = 32


_MplsLdpEntityAtmDefaultControlVci_Object = MibTableColumn
mplsLdpEntityAtmDefaultControlVci = _MplsLdpEntityAtmDefaultControlVci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 7),
    _MplsLdpEntityAtmDefaultControlVci_Type()
)
mplsLdpEntityAtmDefaultControlVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmDefaultControlVci.setStatus("current")


class _MplsLdpEntityAtmUnlabTrafVpi_Type(AtmVpIdentifier):
    """Custom type mplsLdpEntityAtmUnlabTrafVpi based on AtmVpIdentifier"""
    defaultValue = 0


_MplsLdpEntityAtmUnlabTrafVpi_Object = MibTableColumn
mplsLdpEntityAtmUnlabTrafVpi = _MplsLdpEntityAtmUnlabTrafVpi_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 8),
    _MplsLdpEntityAtmUnlabTrafVpi_Type()
)
mplsLdpEntityAtmUnlabTrafVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmUnlabTrafVpi.setStatus("current")


class _MplsLdpEntityAtmUnlabTrafVci_Type(MplsAtmVcIdentifier):
    """Custom type mplsLdpEntityAtmUnlabTrafVci based on MplsAtmVcIdentifier"""
    defaultValue = 32


_MplsLdpEntityAtmUnlabTrafVci_Object = MibTableColumn
mplsLdpEntityAtmUnlabTrafVci = _MplsLdpEntityAtmUnlabTrafVci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 9),
    _MplsLdpEntityAtmUnlabTrafVci_Type()
)
mplsLdpEntityAtmUnlabTrafVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmUnlabTrafVci.setStatus("current")


class _MplsLdpEntityAtmStorageType_Type(StorageType):
    """Custom type mplsLdpEntityAtmStorageType based on StorageType"""


_MplsLdpEntityAtmStorageType_Object = MibTableColumn
mplsLdpEntityAtmStorageType = _MplsLdpEntityAtmStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 10),
    _MplsLdpEntityAtmStorageType_Type()
)
mplsLdpEntityAtmStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmStorageType.setStatus("current")
_MplsLdpEntityAtmRowStatus_Type = RowStatus
_MplsLdpEntityAtmRowStatus_Object = MibTableColumn
mplsLdpEntityAtmRowStatus = _MplsLdpEntityAtmRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 11),
    _MplsLdpEntityAtmRowStatus_Type()
)
mplsLdpEntityAtmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmRowStatus.setStatus("current")
_MplsLdpEntityAtmLRTable_Object = MibTable
mplsLdpEntityAtmLRTable = _MplsLdpEntityAtmLRTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLRTable.setStatus("current")
_MplsLdpEntityAtmLREntry_Object = MibTableRow
mplsLdpEntityAtmLREntry = _MplsLdpEntityAtmLREntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2, 1)
)
mplsLdpEntityAtmLREntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLRMinVpi"),
    (0, "MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLRMinVci"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLREntry.setStatus("current")
_MplsLdpEntityAtmLRMinVpi_Type = AtmVpIdentifier
_MplsLdpEntityAtmLRMinVpi_Object = MibTableColumn
mplsLdpEntityAtmLRMinVpi = _MplsLdpEntityAtmLRMinVpi_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2, 1, 1),
    _MplsLdpEntityAtmLRMinVpi_Type()
)
mplsLdpEntityAtmLRMinVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLRMinVpi.setStatus("current")
_MplsLdpEntityAtmLRMinVci_Type = MplsAtmVcIdentifier
_MplsLdpEntityAtmLRMinVci_Object = MibTableColumn
mplsLdpEntityAtmLRMinVci = _MplsLdpEntityAtmLRMinVci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2, 1, 2),
    _MplsLdpEntityAtmLRMinVci_Type()
)
mplsLdpEntityAtmLRMinVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLRMinVci.setStatus("current")
_MplsLdpEntityAtmLRMaxVpi_Type = AtmVpIdentifier
_MplsLdpEntityAtmLRMaxVpi_Object = MibTableColumn
mplsLdpEntityAtmLRMaxVpi = _MplsLdpEntityAtmLRMaxVpi_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2, 1, 3),
    _MplsLdpEntityAtmLRMaxVpi_Type()
)
mplsLdpEntityAtmLRMaxVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLRMaxVpi.setStatus("current")
_MplsLdpEntityAtmLRMaxVci_Type = MplsAtmVcIdentifier
_MplsLdpEntityAtmLRMaxVci_Object = MibTableColumn
mplsLdpEntityAtmLRMaxVci = _MplsLdpEntityAtmLRMaxVci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2, 1, 4),
    _MplsLdpEntityAtmLRMaxVci_Type()
)
mplsLdpEntityAtmLRMaxVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLRMaxVci.setStatus("current")


class _MplsLdpEntityAtmLRStorageType_Type(StorageType):
    """Custom type mplsLdpEntityAtmLRStorageType based on StorageType"""


_MplsLdpEntityAtmLRStorageType_Object = MibTableColumn
mplsLdpEntityAtmLRStorageType = _MplsLdpEntityAtmLRStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2, 1, 5),
    _MplsLdpEntityAtmLRStorageType_Type()
)
mplsLdpEntityAtmLRStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLRStorageType.setStatus("current")
_MplsLdpEntityAtmLRRowStatus_Type = RowStatus
_MplsLdpEntityAtmLRRowStatus_Object = MibTableColumn
mplsLdpEntityAtmLRRowStatus = _MplsLdpEntityAtmLRRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2, 1, 6),
    _MplsLdpEntityAtmLRRowStatus_Type()
)
mplsLdpEntityAtmLRRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLRRowStatus.setStatus("current")
_MplsLdpAtmSessionObjects_ObjectIdentity = ObjectIdentity
mplsLdpAtmSessionObjects = _MplsLdpAtmSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 2)
)
_MplsLdpAtmSessionTable_Object = MibTable
mplsLdpAtmSessionTable = _MplsLdpAtmSessionTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLdpAtmSessionTable.setStatus("current")
_MplsLdpAtmSessionEntry_Object = MibTableRow
mplsLdpAtmSessionEntry = _MplsLdpAtmSessionEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 2, 1, 1)
)
mplsLdpAtmSessionEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-ATM-STD-MIB", "mplsLdpSessionAtmLRLowerBoundVpi"),
    (0, "MPLS-LDP-ATM-STD-MIB", "mplsLdpSessionAtmLRLowerBoundVci"),
)
if mibBuilder.loadTexts:
    mplsLdpAtmSessionEntry.setStatus("current")
_MplsLdpSessionAtmLRLowerBoundVpi_Type = AtmVpIdentifier
_MplsLdpSessionAtmLRLowerBoundVpi_Object = MibTableColumn
mplsLdpSessionAtmLRLowerBoundVpi = _MplsLdpSessionAtmLRLowerBoundVpi_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 2, 1, 1, 1),
    _MplsLdpSessionAtmLRLowerBoundVpi_Type()
)
mplsLdpSessionAtmLRLowerBoundVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLRLowerBoundVpi.setStatus("current")
_MplsLdpSessionAtmLRLowerBoundVci_Type = MplsAtmVcIdentifier
_MplsLdpSessionAtmLRLowerBoundVci_Object = MibTableColumn
mplsLdpSessionAtmLRLowerBoundVci = _MplsLdpSessionAtmLRLowerBoundVci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 2, 1, 1, 2),
    _MplsLdpSessionAtmLRLowerBoundVci_Type()
)
mplsLdpSessionAtmLRLowerBoundVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLRLowerBoundVci.setStatus("current")
_MplsLdpSessionAtmLRUpperBoundVpi_Type = AtmVpIdentifier
_MplsLdpSessionAtmLRUpperBoundVpi_Object = MibTableColumn
mplsLdpSessionAtmLRUpperBoundVpi = _MplsLdpSessionAtmLRUpperBoundVpi_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 2, 1, 1, 3),
    _MplsLdpSessionAtmLRUpperBoundVpi_Type()
)
mplsLdpSessionAtmLRUpperBoundVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLRUpperBoundVpi.setStatus("current")
_MplsLdpSessionAtmLRUpperBoundVci_Type = MplsAtmVcIdentifier
_MplsLdpSessionAtmLRUpperBoundVci_Object = MibTableColumn
mplsLdpSessionAtmLRUpperBoundVci = _MplsLdpSessionAtmLRUpperBoundVci_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 2, 1, 1, 4),
    _MplsLdpSessionAtmLRUpperBoundVci_Type()
)
mplsLdpSessionAtmLRUpperBoundVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLRUpperBoundVci.setStatus("current")
_MplsLdpAtmConformance_ObjectIdentity = ObjectIdentity
mplsLdpAtmConformance = _MplsLdpAtmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 2)
)
_MplsLdpAtmGroups_ObjectIdentity = ObjectIdentity
mplsLdpAtmGroups = _MplsLdpAtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 2, 1)
)
_MplsLdpAtmCompliances_ObjectIdentity = ObjectIdentity
mplsLdpAtmCompliances = _MplsLdpAtmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 2, 2)
)

# Managed Objects groups

mplsLdpAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 2, 1, 1)
)
mplsLdpAtmGroup.setObjects(
      *(("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmIfIndexOrZero"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmMergeCap"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLRComponents"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmVcDirectionality"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLsrConnectivity"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmDefaultControlVpi"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmDefaultControlVci"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmUnlabTrafVpi"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmUnlabTrafVci"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmStorageType"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmRowStatus"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLRMaxVpi"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLRMaxVci"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLRStorageType"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLRRowStatus"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpSessionAtmLRUpperBoundVpi"),
        ("MPLS-LDP-ATM-STD-MIB", "mplsLdpSessionAtmLRUpperBoundVci"))
)
if mibBuilder.loadTexts:
    mplsLdpAtmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mplsLdpAtmModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLdpAtmModuleFullCompliance.setStatus(
        "current"
    )

mplsLdpAtmModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 5, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mplsLdpAtmModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-LDP-ATM-STD-MIB",
    **{"mplsLdpAtmStdMIB": mplsLdpAtmStdMIB,
       "mplsLdpAtmObjects": mplsLdpAtmObjects,
       "mplsLdpEntityAtmObjects": mplsLdpEntityAtmObjects,
       "mplsLdpEntityAtmTable": mplsLdpEntityAtmTable,
       "mplsLdpEntityAtmEntry": mplsLdpEntityAtmEntry,
       "mplsLdpEntityAtmIfIndexOrZero": mplsLdpEntityAtmIfIndexOrZero,
       "mplsLdpEntityAtmMergeCap": mplsLdpEntityAtmMergeCap,
       "mplsLdpEntityAtmLRComponents": mplsLdpEntityAtmLRComponents,
       "mplsLdpEntityAtmVcDirectionality": mplsLdpEntityAtmVcDirectionality,
       "mplsLdpEntityAtmLsrConnectivity": mplsLdpEntityAtmLsrConnectivity,
       "mplsLdpEntityAtmDefaultControlVpi": mplsLdpEntityAtmDefaultControlVpi,
       "mplsLdpEntityAtmDefaultControlVci": mplsLdpEntityAtmDefaultControlVci,
       "mplsLdpEntityAtmUnlabTrafVpi": mplsLdpEntityAtmUnlabTrafVpi,
       "mplsLdpEntityAtmUnlabTrafVci": mplsLdpEntityAtmUnlabTrafVci,
       "mplsLdpEntityAtmStorageType": mplsLdpEntityAtmStorageType,
       "mplsLdpEntityAtmRowStatus": mplsLdpEntityAtmRowStatus,
       "mplsLdpEntityAtmLRTable": mplsLdpEntityAtmLRTable,
       "mplsLdpEntityAtmLREntry": mplsLdpEntityAtmLREntry,
       "mplsLdpEntityAtmLRMinVpi": mplsLdpEntityAtmLRMinVpi,
       "mplsLdpEntityAtmLRMinVci": mplsLdpEntityAtmLRMinVci,
       "mplsLdpEntityAtmLRMaxVpi": mplsLdpEntityAtmLRMaxVpi,
       "mplsLdpEntityAtmLRMaxVci": mplsLdpEntityAtmLRMaxVci,
       "mplsLdpEntityAtmLRStorageType": mplsLdpEntityAtmLRStorageType,
       "mplsLdpEntityAtmLRRowStatus": mplsLdpEntityAtmLRRowStatus,
       "mplsLdpAtmSessionObjects": mplsLdpAtmSessionObjects,
       "mplsLdpAtmSessionTable": mplsLdpAtmSessionTable,
       "mplsLdpAtmSessionEntry": mplsLdpAtmSessionEntry,
       "mplsLdpSessionAtmLRLowerBoundVpi": mplsLdpSessionAtmLRLowerBoundVpi,
       "mplsLdpSessionAtmLRLowerBoundVci": mplsLdpSessionAtmLRLowerBoundVci,
       "mplsLdpSessionAtmLRUpperBoundVpi": mplsLdpSessionAtmLRUpperBoundVpi,
       "mplsLdpSessionAtmLRUpperBoundVci": mplsLdpSessionAtmLRUpperBoundVci,
       "mplsLdpAtmConformance": mplsLdpAtmConformance,
       "mplsLdpAtmGroups": mplsLdpAtmGroups,
       "mplsLdpAtmGroup": mplsLdpAtmGroup,
       "mplsLdpAtmCompliances": mplsLdpAtmCompliances,
       "mplsLdpAtmModuleFullCompliance": mplsLdpAtmModuleFullCompliance,
       "mplsLdpAtmModuleReadOnlyCompliance": mplsLdpAtmModuleReadOnlyCompliance}
)
