# SNMP MIB module (APPN-DLUR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPN-DLUR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:53 2024
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

(SnaControlPointName,) = mibBuilder.importSymbols(
    "APPN-MIB",
    "SnaControlPointName")

(snanauMIB,) = mibBuilder.importSymbols(
    "SNA-NAU-MIB",
    "snanauMIB")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlurMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 34, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DlurObjects_ObjectIdentity = ObjectIdentity
dlurObjects = _DlurObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 5, 1)
)
_DlurNodeInfo_ObjectIdentity = ObjectIdentity
dlurNodeInfo = _DlurNodeInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 1)
)
_DlurNodeCapabilities_ObjectIdentity = ObjectIdentity
dlurNodeCapabilities = _DlurNodeCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1)
)
_DlurNodeCpName_Type = SnaControlPointName
_DlurNodeCpName_Object = MibScalar
dlurNodeCpName = _DlurNodeCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1, 1),
    _DlurNodeCpName_Type()
)
dlurNodeCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurNodeCpName.setStatus("current")


class _DlurReleaseLevel_Type(DisplayString):
    """Custom type dlurReleaseLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DlurReleaseLevel_Type.__name__ = "DisplayString"
_DlurReleaseLevel_Object = MibScalar
dlurReleaseLevel = _DlurReleaseLevel_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1, 2),
    _DlurReleaseLevel_Type()
)
dlurReleaseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurReleaseLevel.setStatus("current")


class _DlurAnsSupport_Type(Integer32):
    """Custom type dlurAnsSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continueOrStop", 1),
          ("stopOnly", 2))
    )


_DlurAnsSupport_Type.__name__ = "Integer32"
_DlurAnsSupport_Object = MibScalar
dlurAnsSupport = _DlurAnsSupport_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1, 3),
    _DlurAnsSupport_Type()
)
dlurAnsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurAnsSupport.setStatus("current")
_DlurMultiSubnetSupport_Type = TruthValue
_DlurMultiSubnetSupport_Object = MibScalar
dlurMultiSubnetSupport = _DlurMultiSubnetSupport_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1, 4),
    _DlurMultiSubnetSupport_Type()
)
dlurMultiSubnetSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurMultiSubnetSupport.setStatus("current")
_DlurDefaultDefPrimDlusName_Type = SnaControlPointName
_DlurDefaultDefPrimDlusName_Object = MibScalar
dlurDefaultDefPrimDlusName = _DlurDefaultDefPrimDlusName_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1, 5),
    _DlurDefaultDefPrimDlusName_Type()
)
dlurDefaultDefPrimDlusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurDefaultDefPrimDlusName.setStatus("current")
_DlurNetworkNameForwardingSupport_Type = TruthValue
_DlurNetworkNameForwardingSupport_Object = MibScalar
dlurNetworkNameForwardingSupport = _DlurNetworkNameForwardingSupport_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1, 6),
    _DlurNetworkNameForwardingSupport_Type()
)
dlurNetworkNameForwardingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurNetworkNameForwardingSupport.setStatus("current")
_DlurNondisDlusDlurSessDeactSup_Type = TruthValue
_DlurNondisDlusDlurSessDeactSup_Object = MibScalar
dlurNondisDlusDlurSessDeactSup = _DlurNondisDlusDlurSessDeactSup_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 1, 7),
    _DlurNondisDlusDlurSessDeactSup_Type()
)
dlurNondisDlusDlurSessDeactSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurNondisDlusDlurSessDeactSup.setStatus("current")
_DlurDefaultDefBackupDlusTable_Object = MibTable
dlurDefaultDefBackupDlusTable = _DlurDefaultDefBackupDlusTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dlurDefaultDefBackupDlusTable.setStatus("current")
_DlurDefaultDefBackupDlusEntry_Object = MibTableRow
dlurDefaultDefBackupDlusEntry = _DlurDefaultDefBackupDlusEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 2, 1)
)
dlurDefaultDefBackupDlusEntry.setIndexNames(
    (0, "APPN-DLUR-MIB", "dlurDefaultDefBackupDlusIndex"),
)
if mibBuilder.loadTexts:
    dlurDefaultDefBackupDlusEntry.setStatus("current")


class _DlurDefaultDefBackupDlusIndex_Type(Unsigned32):
    """Custom type dlurDefaultDefBackupDlusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DlurDefaultDefBackupDlusIndex_Type.__name__ = "Unsigned32"
_DlurDefaultDefBackupDlusIndex_Object = MibTableColumn
dlurDefaultDefBackupDlusIndex = _DlurDefaultDefBackupDlusIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 2, 1, 1),
    _DlurDefaultDefBackupDlusIndex_Type()
)
dlurDefaultDefBackupDlusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlurDefaultDefBackupDlusIndex.setStatus("current")
_DlurDefaultDefBackupDlusName_Type = SnaControlPointName
_DlurDefaultDefBackupDlusName_Object = MibTableColumn
dlurDefaultDefBackupDlusName = _DlurDefaultDefBackupDlusName_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 1, 2, 1, 2),
    _DlurDefaultDefBackupDlusName_Type()
)
dlurDefaultDefBackupDlusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurDefaultDefBackupDlusName.setStatus("current")
_DlurPuInfo_ObjectIdentity = ObjectIdentity
dlurPuInfo = _DlurPuInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2)
)
_DlurPuTable_Object = MibTable
dlurPuTable = _DlurPuTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dlurPuTable.setStatus("current")
_DlurPuEntry_Object = MibTableRow
dlurPuEntry = _DlurPuEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1)
)
dlurPuEntry.setIndexNames(
    (0, "APPN-DLUR-MIB", "dlurPuName"),
)
if mibBuilder.loadTexts:
    dlurPuEntry.setStatus("current")


class _DlurPuName_Type(DisplayString):
    """Custom type dlurPuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_DlurPuName_Type.__name__ = "DisplayString"
_DlurPuName_Object = MibTableColumn
dlurPuName = _DlurPuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 1),
    _DlurPuName_Type()
)
dlurPuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlurPuName.setStatus("current")


class _DlurPuSscpSuppliedName_Type(DisplayString):
    """Custom type dlurPuSscpSuppliedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_DlurPuSscpSuppliedName_Type.__name__ = "DisplayString"
_DlurPuSscpSuppliedName_Object = MibTableColumn
dlurPuSscpSuppliedName = _DlurPuSscpSuppliedName_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 2),
    _DlurPuSscpSuppliedName_Type()
)
dlurPuSscpSuppliedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurPuSscpSuppliedName.setStatus("current")


class _DlurPuStatus_Type(Integer32):
    """Custom type dlurPuStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("active", 5),
          ("pendActpu", 3),
          ("pendActpuRsp", 4),
          ("pendDactpuRsp", 7),
          ("pendInop", 8),
          ("pendInopActpu", 9),
          ("pendLinkact", 6),
          ("pendReqActpuRsp", 2),
          ("reset", 1))
    )


_DlurPuStatus_Type.__name__ = "Integer32"
_DlurPuStatus_Object = MibTableColumn
dlurPuStatus = _DlurPuStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 3),
    _DlurPuStatus_Type()
)
dlurPuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurPuStatus.setStatus("current")


class _DlurPuAnsSupport_Type(Integer32):
    """Custom type dlurPuAnsSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continue", 1),
          ("stop", 2))
    )


_DlurPuAnsSupport_Type.__name__ = "Integer32"
_DlurPuAnsSupport_Object = MibTableColumn
dlurPuAnsSupport = _DlurPuAnsSupport_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 4),
    _DlurPuAnsSupport_Type()
)
dlurPuAnsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurPuAnsSupport.setStatus("current")


class _DlurPuLocation_Type(Integer32):
    """Custom type dlurPuLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("internal", 1))
    )


_DlurPuLocation_Type.__name__ = "Integer32"
_DlurPuLocation_Object = MibTableColumn
dlurPuLocation = _DlurPuLocation_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 5),
    _DlurPuLocation_Type()
)
dlurPuLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurPuLocation.setStatus("current")


class _DlurPuLsName_Type(DisplayString):
    """Custom type dlurPuLsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DlurPuLsName_Type.__name__ = "DisplayString"
_DlurPuLsName_Object = MibTableColumn
dlurPuLsName = _DlurPuLsName_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 6),
    _DlurPuLsName_Type()
)
dlurPuLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurPuLsName.setStatus("current")


class _DlurPuDlusSessnStatus_Type(Integer32):
    """Custom type dlurPuDlusSessnStatus based on Integer32"""
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
        *(("active", 3),
          ("pendingActive", 2),
          ("pendingInactive", 4),
          ("reset", 1))
    )


_DlurPuDlusSessnStatus_Type.__name__ = "Integer32"
_DlurPuDlusSessnStatus_Object = MibTableColumn
dlurPuDlusSessnStatus = _DlurPuDlusSessnStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 7),
    _DlurPuDlusSessnStatus_Type()
)
dlurPuDlusSessnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurPuDlusSessnStatus.setStatus("current")


class _DlurPuActiveDlusName_Type(DisplayString):
    """Custom type dlurPuActiveDlusName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_DlurPuActiveDlusName_Type.__name__ = "DisplayString"
_DlurPuActiveDlusName_Object = MibTableColumn
dlurPuActiveDlusName = _DlurPuActiveDlusName_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 8),
    _DlurPuActiveDlusName_Type()
)
dlurPuActiveDlusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurPuActiveDlusName.setStatus("current")


class _DlurPuDefPrimDlusName_Type(DisplayString):
    """Custom type dlurPuDefPrimDlusName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_DlurPuDefPrimDlusName_Type.__name__ = "DisplayString"
_DlurPuDefPrimDlusName_Object = MibTableColumn
dlurPuDefPrimDlusName = _DlurPuDefPrimDlusName_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 1, 1, 9),
    _DlurPuDefPrimDlusName_Type()
)
dlurPuDefPrimDlusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurPuDefPrimDlusName.setStatus("current")
_DlurPuDefBackupDlusTable_Object = MibTable
dlurPuDefBackupDlusTable = _DlurPuDefBackupDlusTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dlurPuDefBackupDlusTable.setStatus("current")
_DlurPuDefBackupDlusEntry_Object = MibTableRow
dlurPuDefBackupDlusEntry = _DlurPuDefBackupDlusEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 2, 1)
)
dlurPuDefBackupDlusEntry.setIndexNames(
    (0, "APPN-DLUR-MIB", "dlurPuDefBackupDlusPuName"),
    (0, "APPN-DLUR-MIB", "dlurPuDefBackupDlusIndex"),
)
if mibBuilder.loadTexts:
    dlurPuDefBackupDlusEntry.setStatus("current")


class _DlurPuDefBackupDlusPuName_Type(DisplayString):
    """Custom type dlurPuDefBackupDlusPuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_DlurPuDefBackupDlusPuName_Type.__name__ = "DisplayString"
_DlurPuDefBackupDlusPuName_Object = MibTableColumn
dlurPuDefBackupDlusPuName = _DlurPuDefBackupDlusPuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 2, 1, 1),
    _DlurPuDefBackupDlusPuName_Type()
)
dlurPuDefBackupDlusPuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlurPuDefBackupDlusPuName.setStatus("current")


class _DlurPuDefBackupDlusIndex_Type(Unsigned32):
    """Custom type dlurPuDefBackupDlusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DlurPuDefBackupDlusIndex_Type.__name__ = "Unsigned32"
_DlurPuDefBackupDlusIndex_Object = MibTableColumn
dlurPuDefBackupDlusIndex = _DlurPuDefBackupDlusIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 2, 1, 2),
    _DlurPuDefBackupDlusIndex_Type()
)
dlurPuDefBackupDlusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlurPuDefBackupDlusIndex.setStatus("current")
_DlurPuDefBackupDlusName_Type = SnaControlPointName
_DlurPuDefBackupDlusName_Object = MibTableColumn
dlurPuDefBackupDlusName = _DlurPuDefBackupDlusName_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 2, 2, 1, 3),
    _DlurPuDefBackupDlusName_Type()
)
dlurPuDefBackupDlusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurPuDefBackupDlusName.setStatus("current")
_DlurDlusInfo_ObjectIdentity = ObjectIdentity
dlurDlusInfo = _DlurDlusInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 3)
)
_DlurDlusTable_Object = MibTable
dlurDlusTable = _DlurDlusTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dlurDlusTable.setStatus("current")
_DlurDlusEntry_Object = MibTableRow
dlurDlusEntry = _DlurDlusEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 3, 1, 1)
)
dlurDlusEntry.setIndexNames(
    (0, "APPN-DLUR-MIB", "dlurDlusName"),
)
if mibBuilder.loadTexts:
    dlurDlusEntry.setStatus("current")
_DlurDlusName_Type = SnaControlPointName
_DlurDlusName_Object = MibTableColumn
dlurDlusName = _DlurDlusName_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 3, 1, 1, 1),
    _DlurDlusName_Type()
)
dlurDlusName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlurDlusName.setStatus("current")


class _DlurDlusSessnStatus_Type(Integer32):
    """Custom type dlurDlusSessnStatus based on Integer32"""
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
        *(("active", 3),
          ("pendingActive", 2),
          ("pendingInactive", 4),
          ("reset", 1))
    )


_DlurDlusSessnStatus_Type.__name__ = "Integer32"
_DlurDlusSessnStatus_Object = MibTableColumn
dlurDlusSessnStatus = _DlurDlusSessnStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 5, 1, 3, 1, 1, 2),
    _DlurDlusSessnStatus_Type()
)
dlurDlusSessnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlurDlusSessnStatus.setStatus("current")
_DlurConformance_ObjectIdentity = ObjectIdentity
dlurConformance = _DlurConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 5, 2)
)
_DlurCompliances_ObjectIdentity = ObjectIdentity
dlurCompliances = _DlurCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 5, 2, 1)
)
_DlurGroups_ObjectIdentity = ObjectIdentity
dlurGroups = _DlurGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 5, 2, 2)
)

# Managed Objects groups

dlurConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 5, 2, 2, 1)
)
dlurConfGroup.setObjects(
      *(("APPN-DLUR-MIB", "dlurNodeCpName"),
        ("APPN-DLUR-MIB", "dlurReleaseLevel"),
        ("APPN-DLUR-MIB", "dlurAnsSupport"),
        ("APPN-DLUR-MIB", "dlurMultiSubnetSupport"),
        ("APPN-DLUR-MIB", "dlurNetworkNameForwardingSupport"),
        ("APPN-DLUR-MIB", "dlurNondisDlusDlurSessDeactSup"),
        ("APPN-DLUR-MIB", "dlurDefaultDefPrimDlusName"),
        ("APPN-DLUR-MIB", "dlurDefaultDefBackupDlusName"),
        ("APPN-DLUR-MIB", "dlurPuSscpSuppliedName"),
        ("APPN-DLUR-MIB", "dlurPuStatus"),
        ("APPN-DLUR-MIB", "dlurPuAnsSupport"),
        ("APPN-DLUR-MIB", "dlurPuLocation"),
        ("APPN-DLUR-MIB", "dlurPuLsName"),
        ("APPN-DLUR-MIB", "dlurPuDlusSessnStatus"),
        ("APPN-DLUR-MIB", "dlurPuActiveDlusName"),
        ("APPN-DLUR-MIB", "dlurPuDefPrimDlusName"),
        ("APPN-DLUR-MIB", "dlurPuDefBackupDlusName"),
        ("APPN-DLUR-MIB", "dlurDlusSessnStatus"))
)
if mibBuilder.loadTexts:
    dlurConfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dlurCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 34, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dlurCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPN-DLUR-MIB",
    **{"dlurMIB": dlurMIB,
       "dlurObjects": dlurObjects,
       "dlurNodeInfo": dlurNodeInfo,
       "dlurNodeCapabilities": dlurNodeCapabilities,
       "dlurNodeCpName": dlurNodeCpName,
       "dlurReleaseLevel": dlurReleaseLevel,
       "dlurAnsSupport": dlurAnsSupport,
       "dlurMultiSubnetSupport": dlurMultiSubnetSupport,
       "dlurDefaultDefPrimDlusName": dlurDefaultDefPrimDlusName,
       "dlurNetworkNameForwardingSupport": dlurNetworkNameForwardingSupport,
       "dlurNondisDlusDlurSessDeactSup": dlurNondisDlusDlurSessDeactSup,
       "dlurDefaultDefBackupDlusTable": dlurDefaultDefBackupDlusTable,
       "dlurDefaultDefBackupDlusEntry": dlurDefaultDefBackupDlusEntry,
       "dlurDefaultDefBackupDlusIndex": dlurDefaultDefBackupDlusIndex,
       "dlurDefaultDefBackupDlusName": dlurDefaultDefBackupDlusName,
       "dlurPuInfo": dlurPuInfo,
       "dlurPuTable": dlurPuTable,
       "dlurPuEntry": dlurPuEntry,
       "dlurPuName": dlurPuName,
       "dlurPuSscpSuppliedName": dlurPuSscpSuppliedName,
       "dlurPuStatus": dlurPuStatus,
       "dlurPuAnsSupport": dlurPuAnsSupport,
       "dlurPuLocation": dlurPuLocation,
       "dlurPuLsName": dlurPuLsName,
       "dlurPuDlusSessnStatus": dlurPuDlusSessnStatus,
       "dlurPuActiveDlusName": dlurPuActiveDlusName,
       "dlurPuDefPrimDlusName": dlurPuDefPrimDlusName,
       "dlurPuDefBackupDlusTable": dlurPuDefBackupDlusTable,
       "dlurPuDefBackupDlusEntry": dlurPuDefBackupDlusEntry,
       "dlurPuDefBackupDlusPuName": dlurPuDefBackupDlusPuName,
       "dlurPuDefBackupDlusIndex": dlurPuDefBackupDlusIndex,
       "dlurPuDefBackupDlusName": dlurPuDefBackupDlusName,
       "dlurDlusInfo": dlurDlusInfo,
       "dlurDlusTable": dlurDlusTable,
       "dlurDlusEntry": dlurDlusEntry,
       "dlurDlusName": dlurDlusName,
       "dlurDlusSessnStatus": dlurDlusSessnStatus,
       "dlurConformance": dlurConformance,
       "dlurCompliances": dlurCompliances,
       "dlurCompliance": dlurCompliance,
       "dlurGroups": dlurGroups,
       "dlurConfGroup": dlurConfGroup}
)
