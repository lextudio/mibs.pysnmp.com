# SNMP MIB module (APPLETALK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPLETALK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:49 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class ATNetworkNumber(OctetString):
    """Custom type ATNetworkNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )





class DdpNodeAddress(OctetString):
    """Custom type DdpNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )





class DdpSocketAddress(OctetString):
    """Custom type DdpSocketAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class ATName(OctetString):
    """Custom type ATName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Appletalk_ObjectIdentity = ObjectIdentity
appletalk = _Appletalk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13)
)
_Llap_ObjectIdentity = ObjectIdentity
llap = _Llap_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 1)
)
_LlapTable_Object = MibTable
llapTable = _LlapTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    llapTable.setStatus("mandatory")
_LlapEntry_Object = MibTableRow
llapEntry = _LlapEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1)
)
llapEntry.setIndexNames(
    (0, "APPLETALK-MIB", "llapIfIndex"),
)
if mibBuilder.loadTexts:
    llapEntry.setStatus("mandatory")
_LlapIfIndex_Type = Integer32
_LlapIfIndex_Object = MibTableColumn
llapIfIndex = _LlapIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 1),
    _LlapIfIndex_Type()
)
llapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapIfIndex.setStatus("mandatory")
_LlapInPkts_Type = Counter32
_LlapInPkts_Object = MibTableColumn
llapInPkts = _LlapInPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 2),
    _LlapInPkts_Type()
)
llapInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapInPkts.setStatus("deprecated")
_LlapOutPkts_Type = Counter32
_LlapOutPkts_Object = MibTableColumn
llapOutPkts = _LlapOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 3),
    _LlapOutPkts_Type()
)
llapOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapOutPkts.setStatus("deprecated")
_LlapInNoHandlers_Type = Counter32
_LlapInNoHandlers_Object = MibTableColumn
llapInNoHandlers = _LlapInNoHandlers_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 4),
    _LlapInNoHandlers_Type()
)
llapInNoHandlers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapInNoHandlers.setStatus("deprecated")
_LlapInLengthErrors_Type = Counter32
_LlapInLengthErrors_Object = MibTableColumn
llapInLengthErrors = _LlapInLengthErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 5),
    _LlapInLengthErrors_Type()
)
llapInLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapInLengthErrors.setStatus("mandatory")
_LlapInErrors_Type = Counter32
_LlapInErrors_Object = MibTableColumn
llapInErrors = _LlapInErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 6),
    _LlapInErrors_Type()
)
llapInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapInErrors.setStatus("deprecated")
_LlapCollisions_Type = Counter32
_LlapCollisions_Object = MibTableColumn
llapCollisions = _LlapCollisions_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 7),
    _LlapCollisions_Type()
)
llapCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapCollisions.setStatus("mandatory")
_LlapDefers_Type = Counter32
_LlapDefers_Object = MibTableColumn
llapDefers = _LlapDefers_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 8),
    _LlapDefers_Type()
)
llapDefers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapDefers.setStatus("mandatory")
_LlapNoDataErrors_Type = Counter32
_LlapNoDataErrors_Object = MibTableColumn
llapNoDataErrors = _LlapNoDataErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 9),
    _LlapNoDataErrors_Type()
)
llapNoDataErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapNoDataErrors.setStatus("mandatory")
_LlapRandomCTSErrors_Type = Counter32
_LlapRandomCTSErrors_Object = MibTableColumn
llapRandomCTSErrors = _LlapRandomCTSErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 10),
    _LlapRandomCTSErrors_Type()
)
llapRandomCTSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapRandomCTSErrors.setStatus("mandatory")
_LlapFCSErrors_Type = Counter32
_LlapFCSErrors_Object = MibTableColumn
llapFCSErrors = _LlapFCSErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1, 1, 11),
    _LlapFCSErrors_Type()
)
llapFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llapFCSErrors.setStatus("mandatory")
_Aarp_ObjectIdentity = ObjectIdentity
aarp = _Aarp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 2)
)
_AarpTable_Object = MibTable
aarpTable = _AarpTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1)
)
if mibBuilder.loadTexts:
    aarpTable.setStatus("mandatory")
_AarpEntry_Object = MibTableRow
aarpEntry = _AarpEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 1)
)
aarpEntry.setIndexNames(
    (0, "APPLETALK-MIB", "aarpIfIndex"),
    (0, "APPLETALK-MIB", "aarpNetAddress"),
)
if mibBuilder.loadTexts:
    aarpEntry.setStatus("mandatory")
_AarpIfIndex_Type = Integer32
_AarpIfIndex_Object = MibTableColumn
aarpIfIndex = _AarpIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 1, 1),
    _AarpIfIndex_Type()
)
aarpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aarpIfIndex.setStatus("mandatory")
_AarpPhysAddress_Type = OctetString
_AarpPhysAddress_Object = MibTableColumn
aarpPhysAddress = _AarpPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 1, 2),
    _AarpPhysAddress_Type()
)
aarpPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aarpPhysAddress.setStatus("mandatory")
_AarpNetAddress_Type = DdpNodeAddress
_AarpNetAddress_Object = MibTableColumn
aarpNetAddress = _AarpNetAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 1, 3),
    _AarpNetAddress_Type()
)
aarpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aarpNetAddress.setStatus("mandatory")


class _AarpStatus_Type(Integer32):
    """Custom type aarpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AarpStatus_Type.__name__ = "Integer32"
_AarpStatus_Object = MibTableColumn
aarpStatus = _AarpStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 1, 4),
    _AarpStatus_Type()
)
aarpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aarpStatus.setStatus("mandatory")
_AarpLookups_Type = Counter32
_AarpLookups_Object = MibScalar
aarpLookups = _AarpLookups_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 2),
    _AarpLookups_Type()
)
aarpLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aarpLookups.setStatus("mandatory")
_AarpHits_Type = Counter32
_AarpHits_Object = MibScalar
aarpHits = _AarpHits_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 3),
    _AarpHits_Type()
)
aarpHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aarpHits.setStatus("mandatory")
_Atport_ObjectIdentity = ObjectIdentity
atport = _Atport_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 3)
)
_AtportTable_Object = MibTable
atportTable = _AtportTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1)
)
if mibBuilder.loadTexts:
    atportTable.setStatus("mandatory")
_AtportEntry_Object = MibTableRow
atportEntry = _AtportEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1)
)
atportEntry.setIndexNames(
    (0, "APPLETALK-MIB", "atportIndex"),
)
if mibBuilder.loadTexts:
    atportEntry.setStatus("mandatory")
_AtportIndex_Type = Integer32
_AtportIndex_Object = MibTableColumn
atportIndex = _AtportIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 1),
    _AtportIndex_Type()
)
atportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportIndex.setStatus("mandatory")
_AtportDescr_Type = DisplayString
_AtportDescr_Object = MibTableColumn
atportDescr = _AtportDescr_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 2),
    _AtportDescr_Type()
)
atportDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportDescr.setStatus("mandatory")


class _AtportType_Type(Integer32):
    """Custom type atportType based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("arap", 19),
          ("arctalk", 11),
          ("arns", 23),
          ("aurp", 13),
          ("decnetIV", 18),
          ("ethertalk1", 3),
          ("ethertalk2", 4),
          ("fdditalk", 10),
          ("frameRelay", 14),
          ("hdlc", 24),
          ("ip", 16),
          ("iptalk", 6),
          ("ipx", 22),
          ("isdnInThePacketMode", 20),
          ("localtalk", 2),
          ("nonAppleTalk3Com", 21),
          ("osi", 17),
          ("other", 1),
          ("serialNonstandard", 8),
          ("serialPPP", 7),
          ("smdstalk", 12),
          ("tokentalk", 5),
          ("virtual", 9),
          ("x25", 15))
    )


_AtportType_Type.__name__ = "Integer32"
_AtportType_Object = MibTableColumn
atportType = _AtportType_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 3),
    _AtportType_Type()
)
atportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportType.setStatus("mandatory")
_AtportNetStart_Type = ATNetworkNumber
_AtportNetStart_Object = MibTableColumn
atportNetStart = _AtportNetStart_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 4),
    _AtportNetStart_Type()
)
atportNetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportNetStart.setStatus("mandatory")
_AtportNetEnd_Type = ATNetworkNumber
_AtportNetEnd_Object = MibTableColumn
atportNetEnd = _AtportNetEnd_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 5),
    _AtportNetEnd_Type()
)
atportNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportNetEnd.setStatus("mandatory")
_AtportNetAddress_Type = DdpNodeAddress
_AtportNetAddress_Object = MibTableColumn
atportNetAddress = _AtportNetAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 6),
    _AtportNetAddress_Type()
)
atportNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportNetAddress.setStatus("mandatory")


class _AtportStatus_Type(Integer32):
    """Custom type atportStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("endNode", 5),
          ("invalid", 4),
          ("off", 3),
          ("offDueToConflict", 6),
          ("other", 7),
          ("routing", 1),
          ("unconfigured", 2))
    )


_AtportStatus_Type.__name__ = "Integer32"
_AtportStatus_Object = MibTableColumn
atportStatus = _AtportStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 7),
    _AtportStatus_Type()
)
atportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportStatus.setStatus("mandatory")


class _AtportNetConfig_Type(Integer32):
    """Custom type atportNetConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("conflictAverseSeed", 5),
          ("conflictOrientedSeed", 1),
          ("garnered", 2),
          ("guessed", 3),
          ("softSeed", 6),
          ("unconfigured", 4))
    )


_AtportNetConfig_Type.__name__ = "Integer32"
_AtportNetConfig_Object = MibTableColumn
atportNetConfig = _AtportNetConfig_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 8),
    _AtportNetConfig_Type()
)
atportNetConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportNetConfig.setStatus("mandatory")


class _AtportZoneConfig_Type(Integer32):
    """Custom type atportZoneConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("conflictAverseSeed", 5),
          ("conflictOrientedSeed", 1),
          ("garnered", 2),
          ("guessed", 3),
          ("softSeed", 6),
          ("unconfigured", 4))
    )


_AtportZoneConfig_Type.__name__ = "Integer32"
_AtportZoneConfig_Object = MibTableColumn
atportZoneConfig = _AtportZoneConfig_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 9),
    _AtportZoneConfig_Type()
)
atportZoneConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportZoneConfig.setStatus("mandatory")
_AtportZoneDefault_Type = ATName
_AtportZoneDefault_Object = MibTableColumn
atportZoneDefault = _AtportZoneDefault_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 10),
    _AtportZoneDefault_Type()
)
atportZoneDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportZoneDefault.setStatus("mandatory")
_AtportIfIndex_Type = Integer32
_AtportIfIndex_Object = MibTableColumn
atportIfIndex = _AtportIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 11),
    _AtportIfIndex_Type()
)
atportIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportIfIndex.setStatus("mandatory")
_AtportNetFrom_Type = DdpNodeAddress
_AtportNetFrom_Object = MibTableColumn
atportNetFrom = _AtportNetFrom_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 12),
    _AtportNetFrom_Type()
)
atportNetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportNetFrom.setStatus("mandatory")
_AtportZoneFrom_Type = DdpNodeAddress
_AtportZoneFrom_Object = MibTableColumn
atportZoneFrom = _AtportZoneFrom_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 13),
    _AtportZoneFrom_Type()
)
atportZoneFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportZoneFrom.setStatus("mandatory")
_AtportInPkts_Type = Counter32
_AtportInPkts_Object = MibTableColumn
atportInPkts = _AtportInPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 14),
    _AtportInPkts_Type()
)
atportInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportInPkts.setStatus("mandatory")
_AtportOutPkts_Type = Counter32
_AtportOutPkts_Object = MibTableColumn
atportOutPkts = _AtportOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 15),
    _AtportOutPkts_Type()
)
atportOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportOutPkts.setStatus("mandatory")


class _AtportHome_Type(Integer32):
    """Custom type atportHome based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("home", 1),
          ("notHome", 2))
    )


_AtportHome_Type.__name__ = "Integer32"
_AtportHome_Object = MibTableColumn
atportHome = _AtportHome_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 16),
    _AtportHome_Type()
)
atportHome.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportHome.setStatus("mandatory")
_AtportCurrentZone_Type = ATName
_AtportCurrentZone_Object = MibTableColumn
atportCurrentZone = _AtportCurrentZone_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 17),
    _AtportCurrentZone_Type()
)
atportCurrentZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportCurrentZone.setStatus("mandatory")
_AtportConflictPhysAddr_Type = OctetString
_AtportConflictPhysAddr_Object = MibTableColumn
atportConflictPhysAddr = _AtportConflictPhysAddr_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1, 18),
    _AtportConflictPhysAddr_Type()
)
atportConflictPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportConflictPhysAddr.setStatus("mandatory")
_AtportZoneTable_Object = MibTable
atportZoneTable = _AtportZoneTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 2)
)
if mibBuilder.loadTexts:
    atportZoneTable.setStatus("mandatory")
_AtportZoneEntry_Object = MibTableRow
atportZoneEntry = _AtportZoneEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 2, 1)
)
atportZoneEntry.setIndexNames(
    (0, "APPLETALK-MIB", "atportZonePort"),
    (0, "APPLETALK-MIB", "atportZoneName"),
)
if mibBuilder.loadTexts:
    atportZoneEntry.setStatus("mandatory")
_AtportZonePort_Type = Integer32
_AtportZonePort_Object = MibTableColumn
atportZonePort = _AtportZonePort_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 2, 1, 1),
    _AtportZonePort_Type()
)
atportZonePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atportZonePort.setStatus("mandatory")


class _AtportZoneName_Type(ATName):
    """Custom type atportZoneName based on ATName"""
    subtypeSpec = ATName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AtportZoneName_Type.__name__ = "ATName"
_AtportZoneName_Object = MibTableColumn
atportZoneName = _AtportZoneName_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 2, 1, 2),
    _AtportZoneName_Type()
)
atportZoneName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atportZoneName.setStatus("mandatory")


class _AtportZoneStatus_Type(Integer32):
    """Custom type atportZoneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AtportZoneStatus_Type.__name__ = "Integer32"
_AtportZoneStatus_Object = MibTableColumn
atportZoneStatus = _AtportZoneStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 2, 1, 3),
    _AtportZoneStatus_Type()
)
atportZoneStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportZoneStatus.setStatus("mandatory")
_Ddp_ObjectIdentity = ObjectIdentity
ddp = _Ddp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 4)
)
_DdpOutRequests_Type = Counter32
_DdpOutRequests_Object = MibScalar
ddpOutRequests = _DdpOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 1),
    _DdpOutRequests_Type()
)
ddpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpOutRequests.setStatus("mandatory")
_DdpOutShorts_Type = Counter32
_DdpOutShorts_Object = MibScalar
ddpOutShorts = _DdpOutShorts_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 2),
    _DdpOutShorts_Type()
)
ddpOutShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpOutShorts.setStatus("mandatory")
_DdpOutLongs_Type = Counter32
_DdpOutLongs_Object = MibScalar
ddpOutLongs = _DdpOutLongs_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 3),
    _DdpOutLongs_Type()
)
ddpOutLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpOutLongs.setStatus("mandatory")
_DdpInReceives_Type = Counter32
_DdpInReceives_Object = MibScalar
ddpInReceives = _DdpInReceives_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 4),
    _DdpInReceives_Type()
)
ddpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpInReceives.setStatus("mandatory")
_DdpForwRequests_Type = Counter32
_DdpForwRequests_Object = MibScalar
ddpForwRequests = _DdpForwRequests_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 5),
    _DdpForwRequests_Type()
)
ddpForwRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpForwRequests.setStatus("mandatory")
_DdpInLocalDatagrams_Type = Counter32
_DdpInLocalDatagrams_Object = MibScalar
ddpInLocalDatagrams = _DdpInLocalDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 6),
    _DdpInLocalDatagrams_Type()
)
ddpInLocalDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpInLocalDatagrams.setStatus("mandatory")
_DdpNoProtocolHandlers_Type = Counter32
_DdpNoProtocolHandlers_Object = MibScalar
ddpNoProtocolHandlers = _DdpNoProtocolHandlers_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 7),
    _DdpNoProtocolHandlers_Type()
)
ddpNoProtocolHandlers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpNoProtocolHandlers.setStatus("mandatory")
_DdpOutNoRoutes_Type = Counter32
_DdpOutNoRoutes_Object = MibScalar
ddpOutNoRoutes = _DdpOutNoRoutes_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 8),
    _DdpOutNoRoutes_Type()
)
ddpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpOutNoRoutes.setStatus("mandatory")
_DdpTooShortErrors_Type = Counter32
_DdpTooShortErrors_Object = MibScalar
ddpTooShortErrors = _DdpTooShortErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 9),
    _DdpTooShortErrors_Type()
)
ddpTooShortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpTooShortErrors.setStatus("mandatory")
_DdpTooLongErrors_Type = Counter32
_DdpTooLongErrors_Object = MibScalar
ddpTooLongErrors = _DdpTooLongErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 10),
    _DdpTooLongErrors_Type()
)
ddpTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpTooLongErrors.setStatus("mandatory")
_DdpBroadcastErrors_Type = Counter32
_DdpBroadcastErrors_Object = MibScalar
ddpBroadcastErrors = _DdpBroadcastErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 11),
    _DdpBroadcastErrors_Type()
)
ddpBroadcastErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpBroadcastErrors.setStatus("mandatory")
_DdpShortDDPErrors_Type = Counter32
_DdpShortDDPErrors_Object = MibScalar
ddpShortDDPErrors = _DdpShortDDPErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 12),
    _DdpShortDDPErrors_Type()
)
ddpShortDDPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpShortDDPErrors.setStatus("mandatory")
_DdpHopCountErrors_Type = Counter32
_DdpHopCountErrors_Object = MibScalar
ddpHopCountErrors = _DdpHopCountErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 13),
    _DdpHopCountErrors_Type()
)
ddpHopCountErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpHopCountErrors.setStatus("mandatory")
_DdpChecksumErrors_Type = Counter32
_DdpChecksumErrors_Object = MibScalar
ddpChecksumErrors = _DdpChecksumErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 14),
    _DdpChecksumErrors_Type()
)
ddpChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpChecksumErrors.setStatus("mandatory")
_DdpListenerTable_Object = MibTable
ddpListenerTable = _DdpListenerTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 15)
)
if mibBuilder.loadTexts:
    ddpListenerTable.setStatus("mandatory")
_DdpListenerEntry_Object = MibTableRow
ddpListenerEntry = _DdpListenerEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 15, 1)
)
ddpListenerEntry.setIndexNames(
    (0, "APPLETALK-MIB", "ddpListenerAddress"),
)
if mibBuilder.loadTexts:
    ddpListenerEntry.setStatus("mandatory")
_DdpListenerAddress_Type = DdpSocketAddress
_DdpListenerAddress_Object = MibTableColumn
ddpListenerAddress = _DdpListenerAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 15, 1, 1),
    _DdpListenerAddress_Type()
)
ddpListenerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddpListenerAddress.setStatus("mandatory")
_DdpListenerInPkts_Type = Counter32
_DdpListenerInPkts_Object = MibTableColumn
ddpListenerInPkts = _DdpListenerInPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 15, 1, 2),
    _DdpListenerInPkts_Type()
)
ddpListenerInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpListenerInPkts.setStatus("mandatory")


class _DdpListenerStatus_Type(Integer32):
    """Custom type ddpListenerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_DdpListenerStatus_Type.__name__ = "Integer32"
_DdpListenerStatus_Object = MibTableColumn
ddpListenerStatus = _DdpListenerStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 15, 1, 3),
    _DdpListenerStatus_Type()
)
ddpListenerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddpListenerStatus.setStatus("mandatory")
_DdpForwardingTable_Object = MibTable
ddpForwardingTable = _DdpForwardingTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 16)
)
if mibBuilder.loadTexts:
    ddpForwardingTable.setStatus("mandatory")
_DdpForwardingEntry_Object = MibTableRow
ddpForwardingEntry = _DdpForwardingEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 16, 1)
)
ddpForwardingEntry.setIndexNames(
    (0, "APPLETALK-MIB", "ddpForwardingNetEnd"),
)
if mibBuilder.loadTexts:
    ddpForwardingEntry.setStatus("mandatory")
_DdpForwardingNetEnd_Type = ATNetworkNumber
_DdpForwardingNetEnd_Object = MibTableColumn
ddpForwardingNetEnd = _DdpForwardingNetEnd_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 16, 1, 1),
    _DdpForwardingNetEnd_Type()
)
ddpForwardingNetEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddpForwardingNetEnd.setStatus("mandatory")
_DdpForwardingNetStart_Type = ATNetworkNumber
_DdpForwardingNetStart_Object = MibTableColumn
ddpForwardingNetStart = _DdpForwardingNetStart_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 16, 1, 2),
    _DdpForwardingNetStart_Type()
)
ddpForwardingNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpForwardingNetStart.setStatus("mandatory")
_DdpForwardingNextHop_Type = OctetString
_DdpForwardingNextHop_Object = MibTableColumn
ddpForwardingNextHop = _DdpForwardingNextHop_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 16, 1, 3),
    _DdpForwardingNextHop_Type()
)
ddpForwardingNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpForwardingNextHop.setStatus("mandatory")
_DdpForwardingProto_Type = ObjectIdentifier
_DdpForwardingProto_Object = MibTableColumn
ddpForwardingProto = _DdpForwardingProto_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 16, 1, 4),
    _DdpForwardingProto_Type()
)
ddpForwardingProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpForwardingProto.setStatus("mandatory")
_DdpForwardingModifiedTime_Type = TimeTicks
_DdpForwardingModifiedTime_Object = MibTableColumn
ddpForwardingModifiedTime = _DdpForwardingModifiedTime_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 16, 1, 5),
    _DdpForwardingModifiedTime_Type()
)
ddpForwardingModifiedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpForwardingModifiedTime.setStatus("mandatory")
_DdpForwardingUseCounts_Type = Counter32
_DdpForwardingUseCounts_Object = MibTableColumn
ddpForwardingUseCounts = _DdpForwardingUseCounts_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 16, 1, 6),
    _DdpForwardingUseCounts_Type()
)
ddpForwardingUseCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpForwardingUseCounts.setStatus("mandatory")
_DdpForwardingPort_Type = Integer32
_DdpForwardingPort_Object = MibTableColumn
ddpForwardingPort = _DdpForwardingPort_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 16, 1, 7),
    _DdpForwardingPort_Type()
)
ddpForwardingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpForwardingPort.setStatus("mandatory")
_DdpForwProtoOids_ObjectIdentity = ObjectIdentity
ddpForwProtoOids = _DdpForwProtoOids_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 4, 17)
)
_RtmpRoutingProto_ObjectIdentity = ObjectIdentity
rtmpRoutingProto = _RtmpRoutingProto_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 4, 17, 1)
)
_KipRoutingProto_ObjectIdentity = ObjectIdentity
kipRoutingProto = _KipRoutingProto_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 4, 17, 2)
)
_DdpForwardingTableOverflows_Type = Counter32
_DdpForwardingTableOverflows_Object = MibScalar
ddpForwardingTableOverflows = _DdpForwardingTableOverflows_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 18),
    _DdpForwardingTableOverflows_Type()
)
ddpForwardingTableOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpForwardingTableOverflows.setStatus("mandatory")
_Rtmp_ObjectIdentity = ObjectIdentity
rtmp = _Rtmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 5)
)
_RtmpTable_Object = MibTable
rtmpTable = _RtmpTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1)
)
if mibBuilder.loadTexts:
    rtmpTable.setStatus("mandatory")
_RtmpEntry_Object = MibTableRow
rtmpEntry = _RtmpEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1)
)
rtmpEntry.setIndexNames(
    (0, "APPLETALK-MIB", "rtmpRangeStart"),
)
if mibBuilder.loadTexts:
    rtmpEntry.setStatus("mandatory")
_RtmpRangeStart_Type = ATNetworkNumber
_RtmpRangeStart_Object = MibTableColumn
rtmpRangeStart = _RtmpRangeStart_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1, 1),
    _RtmpRangeStart_Type()
)
rtmpRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpRangeStart.setStatus("mandatory")
_RtmpRangeEnd_Type = ATNetworkNumber
_RtmpRangeEnd_Object = MibTableColumn
rtmpRangeEnd = _RtmpRangeEnd_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1, 2),
    _RtmpRangeEnd_Type()
)
rtmpRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpRangeEnd.setStatus("mandatory")
_RtmpNextHop_Type = OctetString
_RtmpNextHop_Object = MibTableColumn
rtmpNextHop = _RtmpNextHop_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1, 3),
    _RtmpNextHop_Type()
)
rtmpNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpNextHop.setStatus("mandatory")


class _RtmpType_Type(Integer32):
    """Custom type rtmpType based on Integer32"""
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
        *(("appletalk", 2),
          ("other", 1),
          ("serialNonstandard", 4),
          ("serialPPP", 3))
    )


_RtmpType_Type.__name__ = "Integer32"
_RtmpType_Object = MibTableColumn
rtmpType = _RtmpType_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1, 4),
    _RtmpType_Type()
)
rtmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpType.setStatus("mandatory")
_RtmpPort_Type = Integer32
_RtmpPort_Object = MibTableColumn
rtmpPort = _RtmpPort_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1, 5),
    _RtmpPort_Type()
)
rtmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpPort.setStatus("mandatory")
_RtmpHops_Type = Integer32
_RtmpHops_Object = MibTableColumn
rtmpHops = _RtmpHops_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1, 6),
    _RtmpHops_Type()
)
rtmpHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpHops.setStatus("mandatory")


class _RtmpState_Type(Integer32):
    """Custom type rtmpState based on Integer32"""
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
        *(("badOne", 4),
          ("badZero", 3),
          ("good", 1),
          ("invalid", 5),
          ("suspect", 2))
    )


_RtmpState_Type.__name__ = "Integer32"
_RtmpState_Object = MibTableColumn
rtmpState = _RtmpState_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1, 7),
    _RtmpState_Type()
)
rtmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtmpState.setStatus("mandatory")
_RtmpInDataPkts_Type = Counter32
_RtmpInDataPkts_Object = MibScalar
rtmpInDataPkts = _RtmpInDataPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 2),
    _RtmpInDataPkts_Type()
)
rtmpInDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpInDataPkts.setStatus("mandatory")
_RtmpOutDataPkts_Type = Counter32
_RtmpOutDataPkts_Object = MibScalar
rtmpOutDataPkts = _RtmpOutDataPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 3),
    _RtmpOutDataPkts_Type()
)
rtmpOutDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpOutDataPkts.setStatus("mandatory")
_RtmpInRequestPkts_Type = Counter32
_RtmpInRequestPkts_Object = MibScalar
rtmpInRequestPkts = _RtmpInRequestPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 4),
    _RtmpInRequestPkts_Type()
)
rtmpInRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpInRequestPkts.setStatus("mandatory")
_RtmpNextIREqualChanges_Type = Counter32
_RtmpNextIREqualChanges_Object = MibScalar
rtmpNextIREqualChanges = _RtmpNextIREqualChanges_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 5),
    _RtmpNextIREqualChanges_Type()
)
rtmpNextIREqualChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpNextIREqualChanges.setStatus("mandatory")
_RtmpNextIRLessChanges_Type = Counter32
_RtmpNextIRLessChanges_Object = MibScalar
rtmpNextIRLessChanges = _RtmpNextIRLessChanges_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 6),
    _RtmpNextIRLessChanges_Type()
)
rtmpNextIRLessChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpNextIRLessChanges.setStatus("mandatory")
_RtmpRouteDeletes_Type = Counter32
_RtmpRouteDeletes_Object = MibScalar
rtmpRouteDeletes = _RtmpRouteDeletes_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 7),
    _RtmpRouteDeletes_Type()
)
rtmpRouteDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpRouteDeletes.setStatus("mandatory")
_RtmpRoutingTableOverflows_Type = Counter32
_RtmpRoutingTableOverflows_Object = MibScalar
rtmpRoutingTableOverflows = _RtmpRoutingTableOverflows_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 8),
    _RtmpRoutingTableOverflows_Type()
)
rtmpRoutingTableOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpRoutingTableOverflows.setStatus("mandatory")
_Kip_ObjectIdentity = ObjectIdentity
kip = _Kip_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 6)
)
_KipTable_Object = MibTable
kipTable = _KipTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1)
)
if mibBuilder.loadTexts:
    kipTable.setStatus("mandatory")
_KipEntry_Object = MibTableRow
kipEntry = _KipEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1)
)
kipEntry.setIndexNames(
    (0, "APPLETALK-MIB", "kipNetStart"),
)
if mibBuilder.loadTexts:
    kipEntry.setStatus("mandatory")
_KipNetStart_Type = ATNetworkNumber
_KipNetStart_Object = MibTableColumn
kipNetStart = _KipNetStart_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 1),
    _KipNetStart_Type()
)
kipNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kipNetStart.setStatus("mandatory")
_KipNetEnd_Type = ATNetworkNumber
_KipNetEnd_Object = MibTableColumn
kipNetEnd = _KipNetEnd_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 2),
    _KipNetEnd_Type()
)
kipNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipNetEnd.setStatus("mandatory")
_KipNextHop_Type = IpAddress
_KipNextHop_Object = MibTableColumn
kipNextHop = _KipNextHop_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 3),
    _KipNextHop_Type()
)
kipNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipNextHop.setStatus("mandatory")
_KipHopCount_Type = Integer32
_KipHopCount_Object = MibTableColumn
kipHopCount = _KipHopCount_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 4),
    _KipHopCount_Type()
)
kipHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipHopCount.setStatus("mandatory")
_KipBCastAddr_Type = IpAddress
_KipBCastAddr_Object = MibTableColumn
kipBCastAddr = _KipBCastAddr_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 5),
    _KipBCastAddr_Type()
)
kipBCastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipBCastAddr.setStatus("mandatory")


class _KipCore_Type(Integer32):
    """Custom type kipCore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("core", 1),
          ("notcore", 2))
    )


_KipCore_Type.__name__ = "Integer32"
_KipCore_Object = MibTableColumn
kipCore = _KipCore_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 6),
    _KipCore_Type()
)
kipCore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipCore.setStatus("mandatory")


class _KipType_Type(Integer32):
    """Custom type kipType based on Integer32"""
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
        *(("async", 5),
          ("host", 3),
          ("kipRouter", 1),
          ("net", 2),
          ("other", 4))
    )


_KipType_Type.__name__ = "Integer32"
_KipType_Object = MibTableColumn
kipType = _KipType_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 7),
    _KipType_Type()
)
kipType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipType.setStatus("mandatory")


class _KipState_Type(Integer32):
    """Custom type kipState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("invalid", 3),
          ("learned", 2))
    )


_KipState_Type.__name__ = "Integer32"
_KipState_Object = MibTableColumn
kipState = _KipState_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 8),
    _KipState_Type()
)
kipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipState.setStatus("mandatory")


class _KipShare_Type(Integer32):
    """Custom type kipShare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("shared", 1))
    )


_KipShare_Type.__name__ = "Integer32"
_KipShare_Object = MibTableColumn
kipShare = _KipShare_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 9),
    _KipShare_Type()
)
kipShare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipShare.setStatus("mandatory")
_KipFrom_Type = IpAddress
_KipFrom_Object = MibTableColumn
kipFrom = _KipFrom_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1, 10),
    _KipFrom_Type()
)
kipFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kipFrom.setStatus("mandatory")
_ZipRouter_ObjectIdentity = ObjectIdentity
zipRouter = _ZipRouter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 7)
)
_ZipTable_Object = MibTable
zipTable = _ZipTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1)
)
if mibBuilder.loadTexts:
    zipTable.setStatus("mandatory")
_ZipEntry_Object = MibTableRow
zipEntry = _ZipEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 1)
)
zipEntry.setIndexNames(
    (0, "APPLETALK-MIB", "zipZoneNetStart"),
    (0, "APPLETALK-MIB", "zipZoneIndex"),
)
if mibBuilder.loadTexts:
    zipEntry.setStatus("mandatory")
_ZipZoneName_Type = ATName
_ZipZoneName_Object = MibTableColumn
zipZoneName = _ZipZoneName_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 1, 1),
    _ZipZoneName_Type()
)
zipZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipZoneName.setStatus("mandatory")
_ZipZoneIndex_Type = Integer32
_ZipZoneIndex_Object = MibTableColumn
zipZoneIndex = _ZipZoneIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 1, 2),
    _ZipZoneIndex_Type()
)
zipZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipZoneIndex.setStatus("mandatory")
_ZipZoneNetStart_Type = ATNetworkNumber
_ZipZoneNetStart_Object = MibTableColumn
zipZoneNetStart = _ZipZoneNetStart_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 1, 3),
    _ZipZoneNetStart_Type()
)
zipZoneNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipZoneNetStart.setStatus("mandatory")
_ZipZoneNetEnd_Type = ATNetworkNumber
_ZipZoneNetEnd_Object = MibTableColumn
zipZoneNetEnd = _ZipZoneNetEnd_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 1, 4),
    _ZipZoneNetEnd_Type()
)
zipZoneNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipZoneNetEnd.setStatus("mandatory")


class _ZipZoneState_Type(Integer32):
    """Custom type zipZoneState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_ZipZoneState_Type.__name__ = "Integer32"
_ZipZoneState_Object = MibTableColumn
zipZoneState = _ZipZoneState_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 1, 5),
    _ZipZoneState_Type()
)
zipZoneState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zipZoneState.setStatus("mandatory")
_ZipZoneFrom_Type = OctetString
_ZipZoneFrom_Object = MibTableColumn
zipZoneFrom = _ZipZoneFrom_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 1, 6),
    _ZipZoneFrom_Type()
)
zipZoneFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipZoneFrom.setStatus("mandatory")
_ZipZonePort_Type = Integer32
_ZipZonePort_Object = MibTableColumn
zipZonePort = _ZipZonePort_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 1, 7),
    _ZipZonePort_Type()
)
zipZonePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipZonePort.setStatus("mandatory")
_ZipInZipQueries_Type = Counter32
_ZipInZipQueries_Object = MibScalar
zipInZipQueries = _ZipInZipQueries_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 2),
    _ZipInZipQueries_Type()
)
zipInZipQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipInZipQueries.setStatus("mandatory")
_ZipInZipReplies_Type = Counter32
_ZipInZipReplies_Object = MibScalar
zipInZipReplies = _ZipInZipReplies_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 3),
    _ZipInZipReplies_Type()
)
zipInZipReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipInZipReplies.setStatus("mandatory")
_ZipInZipExtendedReplies_Type = Counter32
_ZipInZipExtendedReplies_Object = MibScalar
zipInZipExtendedReplies = _ZipInZipExtendedReplies_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 4),
    _ZipInZipExtendedReplies_Type()
)
zipInZipExtendedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipInZipExtendedReplies.setStatus("mandatory")
_ZipZoneConflictErrors_Type = Counter32
_ZipZoneConflictErrors_Object = MibScalar
zipZoneConflictErrors = _ZipZoneConflictErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 5),
    _ZipZoneConflictErrors_Type()
)
zipZoneConflictErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipZoneConflictErrors.setStatus("mandatory")
_ZipInObsoletes_Type = Counter32
_ZipInObsoletes_Object = MibScalar
zipInObsoletes = _ZipInObsoletes_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 6),
    _ZipInObsoletes_Type()
)
zipInObsoletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipInObsoletes.setStatus("mandatory")
_ZipRouterNetInfoTable_Object = MibTable
zipRouterNetInfoTable = _ZipRouterNetInfoTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 7)
)
if mibBuilder.loadTexts:
    zipRouterNetInfoTable.setStatus("mandatory")
_ZipRouterNetInfoEntry_Object = MibTableRow
zipRouterNetInfoEntry = _ZipRouterNetInfoEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 7, 1)
)
zipRouterNetInfoEntry.setIndexNames(
    (0, "APPLETALK-MIB", "atportIndex"),
)
if mibBuilder.loadTexts:
    zipRouterNetInfoEntry.setStatus("mandatory")
_ZipInGetNetInfos_Type = Counter32
_ZipInGetNetInfos_Object = MibTableColumn
zipInGetNetInfos = _ZipInGetNetInfos_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 7, 1, 1),
    _ZipInGetNetInfos_Type()
)
zipInGetNetInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipInGetNetInfos.setStatus("mandatory")
_ZipOutGetNetInfoReplies_Type = Counter32
_ZipOutGetNetInfoReplies_Object = MibTableColumn
zipOutGetNetInfoReplies = _ZipOutGetNetInfoReplies_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 7, 1, 2),
    _ZipOutGetNetInfoReplies_Type()
)
zipOutGetNetInfoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipOutGetNetInfoReplies.setStatus("mandatory")
_ZipZoneOutInvalids_Type = Counter32
_ZipZoneOutInvalids_Object = MibTableColumn
zipZoneOutInvalids = _ZipZoneOutInvalids_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 7, 1, 3),
    _ZipZoneOutInvalids_Type()
)
zipZoneOutInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipZoneOutInvalids.setStatus("mandatory")
_ZipAddressInvalids_Type = Counter32
_ZipAddressInvalids_Object = MibTableColumn
zipAddressInvalids = _ZipAddressInvalids_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 7, 1, 4),
    _ZipAddressInvalids_Type()
)
zipAddressInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipAddressInvalids.setStatus("mandatory")
_Nbp_ObjectIdentity = ObjectIdentity
nbp = _Nbp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 8)
)
_NbpTable_Object = MibTable
nbpTable = _NbpTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1)
)
if mibBuilder.loadTexts:
    nbpTable.setStatus("mandatory")
_NbpEntry_Object = MibTableRow
nbpEntry = _NbpEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 1)
)
nbpEntry.setIndexNames(
    (0, "APPLETALK-MIB", "nbpIndex"),
)
if mibBuilder.loadTexts:
    nbpEntry.setStatus("mandatory")
_NbpIndex_Type = Integer32
_NbpIndex_Object = MibTableColumn
nbpIndex = _NbpIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 1, 1),
    _NbpIndex_Type()
)
nbpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbpIndex.setStatus("mandatory")


class _NbpObject_Type(ATName):
    """Custom type nbpObject based on ATName"""
    subtypeSpec = ATName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NbpObject_Type.__name__ = "ATName"
_NbpObject_Object = MibTableColumn
nbpObject = _NbpObject_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 1, 2),
    _NbpObject_Type()
)
nbpObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbpObject.setStatus("mandatory")


class _NbpType_Type(ATName):
    """Custom type nbpType based on ATName"""
    subtypeSpec = ATName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NbpType_Type.__name__ = "ATName"
_NbpType_Object = MibTableColumn
nbpType = _NbpType_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 1, 3),
    _NbpType_Type()
)
nbpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbpType.setStatus("mandatory")
_NbpZone_Type = ATName
_NbpZone_Object = MibTableColumn
nbpZone = _NbpZone_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 1, 4),
    _NbpZone_Type()
)
nbpZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbpZone.setStatus("mandatory")


class _NbpState_Type(Integer32):
    """Custom type nbpState based on Integer32"""
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
        *(("invalid", 4),
          ("registering", 2),
          ("registrationFailed", 3),
          ("valid", 1))
    )


_NbpState_Type.__name__ = "Integer32"
_NbpState_Object = MibTableColumn
nbpState = _NbpState_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 1, 5),
    _NbpState_Type()
)
nbpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbpState.setStatus("mandatory")
_NbpAddress_Type = DdpSocketAddress
_NbpAddress_Object = MibTableColumn
nbpAddress = _NbpAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 1, 6),
    _NbpAddress_Type()
)
nbpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbpAddress.setStatus("mandatory")


class _NbpEnumerator_Type(Integer32):
    """Custom type nbpEnumerator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NbpEnumerator_Type.__name__ = "Integer32"
_NbpEnumerator_Object = MibTableColumn
nbpEnumerator = _NbpEnumerator_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 1, 7),
    _NbpEnumerator_Type()
)
nbpEnumerator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbpEnumerator.setStatus("mandatory")
_NbpInLookUpRequests_Type = Counter32
_NbpInLookUpRequests_Object = MibScalar
nbpInLookUpRequests = _NbpInLookUpRequests_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 2),
    _NbpInLookUpRequests_Type()
)
nbpInLookUpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbpInLookUpRequests.setStatus("mandatory")
_NbpInLookUpReplies_Type = Counter32
_NbpInLookUpReplies_Object = MibScalar
nbpInLookUpReplies = _NbpInLookUpReplies_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 3),
    _NbpInLookUpReplies_Type()
)
nbpInLookUpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbpInLookUpReplies.setStatus("mandatory")
_NbpInBroadcastRequests_Type = Counter32
_NbpInBroadcastRequests_Object = MibScalar
nbpInBroadcastRequests = _NbpInBroadcastRequests_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 4),
    _NbpInBroadcastRequests_Type()
)
nbpInBroadcastRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbpInBroadcastRequests.setStatus("mandatory")
_NbpInForwardRequests_Type = Counter32
_NbpInForwardRequests_Object = MibScalar
nbpInForwardRequests = _NbpInForwardRequests_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 5),
    _NbpInForwardRequests_Type()
)
nbpInForwardRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbpInForwardRequests.setStatus("mandatory")
_NbpOutLookUpReplies_Type = Counter32
_NbpOutLookUpReplies_Object = MibScalar
nbpOutLookUpReplies = _NbpOutLookUpReplies_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 6),
    _NbpOutLookUpReplies_Type()
)
nbpOutLookUpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbpOutLookUpReplies.setStatus("mandatory")
_NbpRegistrationFailures_Type = Counter32
_NbpRegistrationFailures_Object = MibScalar
nbpRegistrationFailures = _NbpRegistrationFailures_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 7),
    _NbpRegistrationFailures_Type()
)
nbpRegistrationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbpRegistrationFailures.setStatus("mandatory")
_NbpInErrors_Type = Counter32
_NbpInErrors_Object = MibScalar
nbpInErrors = _NbpInErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 8),
    _NbpInErrors_Type()
)
nbpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbpInErrors.setStatus("mandatory")
_Atecho_ObjectIdentity = ObjectIdentity
atecho = _Atecho_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 9)
)
_AtechoRequests_Type = Counter32
_AtechoRequests_Object = MibScalar
atechoRequests = _AtechoRequests_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 1),
    _AtechoRequests_Type()
)
atechoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atechoRequests.setStatus("mandatory")
_AtechoReplies_Type = Counter32
_AtechoReplies_Object = MibScalar
atechoReplies = _AtechoReplies_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 2),
    _AtechoReplies_Type()
)
atechoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atechoReplies.setStatus("mandatory")
_AtechoOutRequests_Type = Counter32
_AtechoOutRequests_Object = MibScalar
atechoOutRequests = _AtechoOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 3),
    _AtechoOutRequests_Type()
)
atechoOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atechoOutRequests.setStatus("mandatory")
_AtechoInReplies_Type = Counter32
_AtechoInReplies_Object = MibScalar
atechoInReplies = _AtechoInReplies_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 4),
    _AtechoInReplies_Type()
)
atechoInReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atechoInReplies.setStatus("mandatory")
_Atp_ObjectIdentity = ObjectIdentity
atp = _Atp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 10)
)
_AtpInPkts_Type = Counter32
_AtpInPkts_Object = MibScalar
atpInPkts = _AtpInPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 1),
    _AtpInPkts_Type()
)
atpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atpInPkts.setStatus("mandatory")
_AtpOutPkts_Type = Counter32
_AtpOutPkts_Object = MibScalar
atpOutPkts = _AtpOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 2),
    _AtpOutPkts_Type()
)
atpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atpOutPkts.setStatus("mandatory")
_AtpTRequestRetransmissions_Type = Counter32
_AtpTRequestRetransmissions_Object = MibScalar
atpTRequestRetransmissions = _AtpTRequestRetransmissions_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 3),
    _AtpTRequestRetransmissions_Type()
)
atpTRequestRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atpTRequestRetransmissions.setStatus("mandatory")
_AtpTResponseRetransmissions_Type = Counter32
_AtpTResponseRetransmissions_Object = MibScalar
atpTResponseRetransmissions = _AtpTResponseRetransmissions_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 4),
    _AtpTResponseRetransmissions_Type()
)
atpTResponseRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atpTResponseRetransmissions.setStatus("mandatory")
_AtpReleaseTimerExpiredCounts_Type = Counter32
_AtpReleaseTimerExpiredCounts_Object = MibScalar
atpReleaseTimerExpiredCounts = _AtpReleaseTimerExpiredCounts_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 5),
    _AtpReleaseTimerExpiredCounts_Type()
)
atpReleaseTimerExpiredCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atpReleaseTimerExpiredCounts.setStatus("mandatory")
_AtpRetryCountExceededs_Type = Counter32
_AtpRetryCountExceededs_Object = MibScalar
atpRetryCountExceededs = _AtpRetryCountExceededs_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 6),
    _AtpRetryCountExceededs_Type()
)
atpRetryCountExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atpRetryCountExceededs.setStatus("mandatory")
_AtpListenerTable_Object = MibTable
atpListenerTable = _AtpListenerTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 7)
)
if mibBuilder.loadTexts:
    atpListenerTable.setStatus("mandatory")
_AtpListenerEntry_Object = MibTableRow
atpListenerEntry = _AtpListenerEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 7, 1)
)
atpListenerEntry.setIndexNames(
    (0, "APPLETALK-MIB", "atpListenerAddress"),
)
if mibBuilder.loadTexts:
    atpListenerEntry.setStatus("mandatory")
_AtpListenerAddress_Type = DdpSocketAddress
_AtpListenerAddress_Object = MibTableColumn
atpListenerAddress = _AtpListenerAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 7, 1, 1),
    _AtpListenerAddress_Type()
)
atpListenerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atpListenerAddress.setStatus("mandatory")


class _AtpListenerStatus_Type(Integer32):
    """Custom type atpListenerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AtpListenerStatus_Type.__name__ = "Integer32"
_AtpListenerStatus_Object = MibTableColumn
atpListenerStatus = _AtpListenerStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 7, 1, 2),
    _AtpListenerStatus_Type()
)
atpListenerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atpListenerStatus.setStatus("mandatory")
_Pap_ObjectIdentity = ObjectIdentity
pap = _Pap_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 11)
)
_PapInOpenConns_Type = Counter32
_PapInOpenConns_Object = MibScalar
papInOpenConns = _PapInOpenConns_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 1),
    _PapInOpenConns_Type()
)
papInOpenConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    papInOpenConns.setStatus("mandatory")
_PapOutOpenConns_Type = Counter32
_PapOutOpenConns_Object = MibScalar
papOutOpenConns = _PapOutOpenConns_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 2),
    _PapOutOpenConns_Type()
)
papOutOpenConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    papOutOpenConns.setStatus("mandatory")
_PapInDatas_Type = Counter32
_PapInDatas_Object = MibScalar
papInDatas = _PapInDatas_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 3),
    _PapInDatas_Type()
)
papInDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    papInDatas.setStatus("mandatory")
_PapOutDatas_Type = Counter32
_PapOutDatas_Object = MibScalar
papOutDatas = _PapOutDatas_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 4),
    _PapOutDatas_Type()
)
papOutDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    papOutDatas.setStatus("mandatory")
_PapInCloseConns_Type = Counter32
_PapInCloseConns_Object = MibScalar
papInCloseConns = _PapInCloseConns_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 5),
    _PapInCloseConns_Type()
)
papInCloseConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    papInCloseConns.setStatus("mandatory")
_PapOutCloseConns_Type = Counter32
_PapOutCloseConns_Object = MibScalar
papOutCloseConns = _PapOutCloseConns_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 6),
    _PapOutCloseConns_Type()
)
papOutCloseConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    papOutCloseConns.setStatus("mandatory")
_PapTickleTimeoutCloses_Type = Counter32
_PapTickleTimeoutCloses_Object = MibScalar
papTickleTimeoutCloses = _PapTickleTimeoutCloses_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 7),
    _PapTickleTimeoutCloses_Type()
)
papTickleTimeoutCloses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    papTickleTimeoutCloses.setStatus("mandatory")
_PapServerTable_Object = MibTable
papServerTable = _PapServerTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 8)
)
if mibBuilder.loadTexts:
    papServerTable.setStatus("mandatory")
_PapServerEntry_Object = MibTableRow
papServerEntry = _PapServerEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 8, 1)
)
papServerEntry.setIndexNames(
    (0, "APPLETALK-MIB", "papServerIndex"),
)
if mibBuilder.loadTexts:
    papServerEntry.setStatus("mandatory")
_PapServerIndex_Type = Integer32
_PapServerIndex_Object = MibTableColumn
papServerIndex = _PapServerIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 8, 1, 1),
    _PapServerIndex_Type()
)
papServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    papServerIndex.setStatus("mandatory")
_PapServerListeningSocket_Type = DdpSocketAddress
_PapServerListeningSocket_Object = MibTableColumn
papServerListeningSocket = _PapServerListeningSocket_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 8, 1, 2),
    _PapServerListeningSocket_Type()
)
papServerListeningSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    papServerListeningSocket.setStatus("mandatory")
_PapServerStatus_Type = DisplayString
_PapServerStatus_Object = MibTableColumn
papServerStatus = _PapServerStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 8, 1, 3),
    _PapServerStatus_Type()
)
papServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    papServerStatus.setStatus("mandatory")
_PapServerCompletedJobs_Type = Counter32
_PapServerCompletedJobs_Object = MibTableColumn
papServerCompletedJobs = _PapServerCompletedJobs_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 8, 1, 4),
    _PapServerCompletedJobs_Type()
)
papServerCompletedJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    papServerCompletedJobs.setStatus("mandatory")
_PapServerBusyJobs_Type = Integer32
_PapServerBusyJobs_Object = MibTableColumn
papServerBusyJobs = _PapServerBusyJobs_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 8, 1, 5),
    _PapServerBusyJobs_Type()
)
papServerBusyJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    papServerBusyJobs.setStatus("mandatory")
_PapServerFreeJobs_Type = Integer32
_PapServerFreeJobs_Object = MibTableColumn
papServerFreeJobs = _PapServerFreeJobs_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 8, 1, 6),
    _PapServerFreeJobs_Type()
)
papServerFreeJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    papServerFreeJobs.setStatus("mandatory")
_PapServerAuthenticationFailures_Type = Counter32
_PapServerAuthenticationFailures_Object = MibTableColumn
papServerAuthenticationFailures = _PapServerAuthenticationFailures_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 8, 1, 7),
    _PapServerAuthenticationFailures_Type()
)
papServerAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    papServerAuthenticationFailures.setStatus("mandatory")
_PapServerAccountingFailures_Type = Counter32
_PapServerAccountingFailures_Object = MibTableColumn
papServerAccountingFailures = _PapServerAccountingFailures_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 8, 1, 8),
    _PapServerAccountingFailures_Type()
)
papServerAccountingFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    papServerAccountingFailures.setStatus("mandatory")
_PapServerGeneralFailures_Type = Counter32
_PapServerGeneralFailures_Object = MibTableColumn
papServerGeneralFailures = _PapServerGeneralFailures_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 8, 1, 9),
    _PapServerGeneralFailures_Type()
)
papServerGeneralFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    papServerGeneralFailures.setStatus("mandatory")


class _PapServerState_Type(Integer32):
    """Custom type papServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_PapServerState_Type.__name__ = "Integer32"
_PapServerState_Object = MibTableColumn
papServerState = _PapServerState_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 8, 1, 10),
    _PapServerState_Type()
)
papServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    papServerState.setStatus("mandatory")
_PapServerLastStatusMsg_Type = DisplayString
_PapServerLastStatusMsg_Object = MibTableColumn
papServerLastStatusMsg = _PapServerLastStatusMsg_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 8, 1, 11),
    _PapServerLastStatusMsg_Type()
)
papServerLastStatusMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    papServerLastStatusMsg.setStatus("mandatory")
_Asp_ObjectIdentity = ObjectIdentity
asp = _Asp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 12)
)
_AspInputTransactions_Type = Counter32
_AspInputTransactions_Object = MibScalar
aspInputTransactions = _AspInputTransactions_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 1),
    _AspInputTransactions_Type()
)
aspInputTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspInputTransactions.setStatus("mandatory")
_AspOutputTransactions_Type = Counter32
_AspOutputTransactions_Object = MibScalar
aspOutputTransactions = _AspOutputTransactions_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 2),
    _AspOutputTransactions_Type()
)
aspOutputTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspOutputTransactions.setStatus("mandatory")
_AspInOpenSessions_Type = Counter32
_AspInOpenSessions_Object = MibScalar
aspInOpenSessions = _AspInOpenSessions_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 3),
    _AspInOpenSessions_Type()
)
aspInOpenSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspInOpenSessions.setStatus("mandatory")
_AspOutOpenSessions_Type = Counter32
_AspOutOpenSessions_Object = MibScalar
aspOutOpenSessions = _AspOutOpenSessions_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 4),
    _AspOutOpenSessions_Type()
)
aspOutOpenSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspOutOpenSessions.setStatus("mandatory")
_AspInCloseSessions_Type = Counter32
_AspInCloseSessions_Object = MibScalar
aspInCloseSessions = _AspInCloseSessions_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 5),
    _AspInCloseSessions_Type()
)
aspInCloseSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspInCloseSessions.setStatus("mandatory")
_AspOutCloseSessions_Type = Counter32
_AspOutCloseSessions_Object = MibScalar
aspOutCloseSessions = _AspOutCloseSessions_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 6),
    _AspOutCloseSessions_Type()
)
aspOutCloseSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspOutCloseSessions.setStatus("mandatory")
_AspNoMoreSessionsErrors_Type = Counter32
_AspNoMoreSessionsErrors_Object = MibScalar
aspNoMoreSessionsErrors = _AspNoMoreSessionsErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 7),
    _AspNoMoreSessionsErrors_Type()
)
aspNoMoreSessionsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspNoMoreSessionsErrors.setStatus("mandatory")
_AspTickleTimeOutCloses_Type = Counter32
_AspTickleTimeOutCloses_Object = MibScalar
aspTickleTimeOutCloses = _AspTickleTimeOutCloses_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 8),
    _AspTickleTimeOutCloses_Type()
)
aspTickleTimeOutCloses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspTickleTimeOutCloses.setStatus("mandatory")
_AspConnTable_Object = MibTable
aspConnTable = _AspConnTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 9)
)
if mibBuilder.loadTexts:
    aspConnTable.setStatus("mandatory")
_AspConnEntry_Object = MibTableRow
aspConnEntry = _AspConnEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 9, 1)
)
aspConnEntry.setIndexNames(
    (0, "APPLETALK-MIB", "aspConnLocalAddress"),
    (0, "APPLETALK-MIB", "aspConnRemoteAddress"),
    (0, "APPLETALK-MIB", "aspConnID"),
)
if mibBuilder.loadTexts:
    aspConnEntry.setStatus("mandatory")
_AspConnLocalAddress_Type = DdpSocketAddress
_AspConnLocalAddress_Object = MibTableColumn
aspConnLocalAddress = _AspConnLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 9, 1, 1),
    _AspConnLocalAddress_Type()
)
aspConnLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aspConnLocalAddress.setStatus("mandatory")
_AspConnRemoteAddress_Type = DdpSocketAddress
_AspConnRemoteAddress_Object = MibTableColumn
aspConnRemoteAddress = _AspConnRemoteAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 9, 1, 2),
    _AspConnRemoteAddress_Type()
)
aspConnRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aspConnRemoteAddress.setStatus("mandatory")


class _AspConnID_Type(Integer32):
    """Custom type aspConnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AspConnID_Type.__name__ = "Integer32"
_AspConnID_Object = MibTableColumn
aspConnID = _AspConnID_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 9, 1, 3),
    _AspConnID_Type()
)
aspConnID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aspConnID.setStatus("mandatory")


class _AspConnLastReqNum_Type(Integer32):
    """Custom type aspConnLastReqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AspConnLastReqNum_Type.__name__ = "Integer32"
_AspConnLastReqNum_Object = MibTableColumn
aspConnLastReqNum = _AspConnLastReqNum_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 9, 1, 4),
    _AspConnLastReqNum_Type()
)
aspConnLastReqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspConnLastReqNum.setStatus("mandatory")


class _AspConnServerEnd_Type(Integer32):
    """Custom type aspConnServerEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sls", 3),
          ("sss", 1),
          ("wss", 2))
    )


_AspConnServerEnd_Type.__name__ = "Integer32"
_AspConnServerEnd_Object = MibTableColumn
aspConnServerEnd = _AspConnServerEnd_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 9, 1, 5),
    _AspConnServerEnd_Type()
)
aspConnServerEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspConnServerEnd.setStatus("mandatory")


class _AspConnState_Type(Integer32):
    """Custom type aspConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("invalid", 3),
          ("open", 1))
    )


_AspConnState_Type.__name__ = "Integer32"
_AspConnState_Object = MibTableColumn
aspConnState = _AspConnState_Object(
    (1, 3, 6, 1, 2, 1, 13, 12, 9, 1, 6),
    _AspConnState_Type()
)
aspConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aspConnState.setStatus("mandatory")
_Adsp_ObjectIdentity = ObjectIdentity
adsp = _Adsp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 13)
)
_AdspInPkts_Type = Counter32
_AdspInPkts_Object = MibScalar
adspInPkts = _AdspInPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 13, 1),
    _AdspInPkts_Type()
)
adspInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adspInPkts.setStatus("mandatory")
_AdspOutPkts_Type = Counter32
_AdspOutPkts_Object = MibScalar
adspOutPkts = _AdspOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 13, 2),
    _AdspOutPkts_Type()
)
adspOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adspOutPkts.setStatus("mandatory")
_AdspInOctets_Type = Counter32
_AdspInOctets_Object = MibScalar
adspInOctets = _AdspInOctets_Object(
    (1, 3, 6, 1, 2, 1, 13, 13, 3),
    _AdspInOctets_Type()
)
adspInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adspInOctets.setStatus("mandatory")
_AdspOutOctets_Type = Counter32
_AdspOutOctets_Object = MibScalar
adspOutOctets = _AdspOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 13, 13, 4),
    _AdspOutOctets_Type()
)
adspOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adspOutOctets.setStatus("mandatory")
_AdspInDataPkts_Type = Counter32
_AdspInDataPkts_Object = MibScalar
adspInDataPkts = _AdspInDataPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 13, 5),
    _AdspInDataPkts_Type()
)
adspInDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adspInDataPkts.setStatus("mandatory")
_AdspOutDataPkts_Type = Counter32
_AdspOutDataPkts_Object = MibScalar
adspOutDataPkts = _AdspOutDataPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 13, 6),
    _AdspOutDataPkts_Type()
)
adspOutDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adspOutDataPkts.setStatus("mandatory")
_AdspTimeoutErrors_Type = Counter32
_AdspTimeoutErrors_Object = MibScalar
adspTimeoutErrors = _AdspTimeoutErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 13, 7),
    _AdspTimeoutErrors_Type()
)
adspTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adspTimeoutErrors.setStatus("mandatory")
_AdspTimeoutCloseErrors_Type = Counter32
_AdspTimeoutCloseErrors_Object = MibScalar
adspTimeoutCloseErrors = _AdspTimeoutCloseErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 13, 8),
    _AdspTimeoutCloseErrors_Type()
)
adspTimeoutCloseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adspTimeoutCloseErrors.setStatus("mandatory")
_AdspConnTable_Object = MibTable
adspConnTable = _AdspConnTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 13, 9)
)
if mibBuilder.loadTexts:
    adspConnTable.setStatus("mandatory")
_AdspConnEntry_Object = MibTableRow
adspConnEntry = _AdspConnEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 13, 9, 1)
)
adspConnEntry.setIndexNames(
    (0, "APPLETALK-MIB", "adspConnLocalAddress"),
    (0, "APPLETALK-MIB", "adspConnRemoteAddress"),
    (0, "APPLETALK-MIB", "adspConnLocalConnID"),
)
if mibBuilder.loadTexts:
    adspConnEntry.setStatus("mandatory")
_AdspConnLocalAddress_Type = DdpSocketAddress
_AdspConnLocalAddress_Object = MibTableColumn
adspConnLocalAddress = _AdspConnLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 13, 9, 1, 1),
    _AdspConnLocalAddress_Type()
)
adspConnLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adspConnLocalAddress.setStatus("mandatory")


class _AdspConnLocalConnID_Type(Integer32):
    """Custom type adspConnLocalConnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdspConnLocalConnID_Type.__name__ = "Integer32"
_AdspConnLocalConnID_Object = MibTableColumn
adspConnLocalConnID = _AdspConnLocalConnID_Object(
    (1, 3, 6, 1, 2, 1, 13, 13, 9, 1, 2),
    _AdspConnLocalConnID_Type()
)
adspConnLocalConnID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adspConnLocalConnID.setStatus("mandatory")
_AdspConnRemoteAddress_Type = DdpSocketAddress
_AdspConnRemoteAddress_Object = MibTableColumn
adspConnRemoteAddress = _AdspConnRemoteAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 13, 9, 1, 3),
    _AdspConnRemoteAddress_Type()
)
adspConnRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adspConnRemoteAddress.setStatus("mandatory")


class _AdspConnRemoteConnID_Type(Integer32):
    """Custom type adspConnRemoteConnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdspConnRemoteConnID_Type.__name__ = "Integer32"
_AdspConnRemoteConnID_Object = MibTableColumn
adspConnRemoteConnID = _AdspConnRemoteConnID_Object(
    (1, 3, 6, 1, 2, 1, 13, 13, 9, 1, 4),
    _AdspConnRemoteConnID_Type()
)
adspConnRemoteConnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adspConnRemoteConnID.setStatus("mandatory")


class _AdspConnState_Type(Integer32):
    """Custom type adspConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("closed", 5),
          ("invalid", 6),
          ("listening", 4),
          ("localHalfOpen", 2),
          ("open", 1),
          ("remoteHalfOpen", 3))
    )


_AdspConnState_Type.__name__ = "Integer32"
_AdspConnState_Object = MibTableColumn
adspConnState = _AdspConnState_Object(
    (1, 3, 6, 1, 2, 1, 13, 13, 9, 1, 5),
    _AdspConnState_Type()
)
adspConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adspConnState.setStatus("mandatory")
_Atportptop_ObjectIdentity = ObjectIdentity
atportptop = _Atportptop_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 14)
)
_AtportPtoPTable_Object = MibTable
atportPtoPTable = _AtportPtoPTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 14, 1)
)
if mibBuilder.loadTexts:
    atportPtoPTable.setStatus("mandatory")
_AtportPtoPEntry_Object = MibTableRow
atportPtoPEntry = _AtportPtoPEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 14, 1, 1)
)
atportPtoPEntry.setIndexNames(
    (0, "APPLETALK-MIB", "atportPtoPIndex"),
)
if mibBuilder.loadTexts:
    atportPtoPEntry.setStatus("mandatory")
_AtportPtoPIndex_Type = Integer32
_AtportPtoPIndex_Object = MibTableColumn
atportPtoPIndex = _AtportPtoPIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 14, 1, 1, 1),
    _AtportPtoPIndex_Type()
)
atportPtoPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atportPtoPIndex.setStatus("mandatory")
_AtportPtoPProtocol_Type = ObjectIdentifier
_AtportPtoPProtocol_Object = MibTableColumn
atportPtoPProtocol = _AtportPtoPProtocol_Object(
    (1, 3, 6, 1, 2, 1, 13, 14, 1, 1, 2),
    _AtportPtoPProtocol_Type()
)
atportPtoPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportPtoPProtocol.setStatus("mandatory")
_AtportPtoPRemoteName_Type = DisplayString
_AtportPtoPRemoteName_Object = MibTableColumn
atportPtoPRemoteName = _AtportPtoPRemoteName_Object(
    (1, 3, 6, 1, 2, 1, 13, 14, 1, 1, 3),
    _AtportPtoPRemoteName_Type()
)
atportPtoPRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportPtoPRemoteName.setStatus("mandatory")
_AtportPtoPRemoteAddress_Type = OctetString
_AtportPtoPRemoteAddress_Object = MibTableColumn
atportPtoPRemoteAddress = _AtportPtoPRemoteAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 14, 1, 1, 4),
    _AtportPtoPRemoteAddress_Type()
)
atportPtoPRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportPtoPRemoteAddress.setStatus("mandatory")
_AtportPtoPPortIndex_Type = Integer32
_AtportPtoPPortIndex_Object = MibTableColumn
atportPtoPPortIndex = _AtportPtoPPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 14, 1, 1, 5),
    _AtportPtoPPortIndex_Type()
)
atportPtoPPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportPtoPPortIndex.setStatus("mandatory")


class _AtportPtoPStatus_Type(Integer32):
    """Custom type atportPtoPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AtportPtoPStatus_Type.__name__ = "Integer32"
_AtportPtoPStatus_Object = MibTableColumn
atportPtoPStatus = _AtportPtoPStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 14, 1, 1, 6),
    _AtportPtoPStatus_Type()
)
atportPtoPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportPtoPStatus.setStatus("mandatory")
_AtportPtoPProtoOids_ObjectIdentity = ObjectIdentity
atportPtoPProtoOids = _AtportPtoPProtoOids_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 14, 2)
)
_PToPProtoOther_ObjectIdentity = ObjectIdentity
pToPProtoOther = _PToPProtoOther_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 14, 2, 1)
)
_PToPProtoAurp_ObjectIdentity = ObjectIdentity
pToPProtoAurp = _PToPProtoAurp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 14, 2, 2)
)
_PToPProtoCaymanUdp_ObjectIdentity = ObjectIdentity
pToPProtoCaymanUdp = _PToPProtoCaymanUdp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 14, 2, 3)
)
_PToPProtoAtkvmsDecnetIV_ObjectIdentity = ObjectIdentity
pToPProtoAtkvmsDecnetIV = _PToPProtoAtkvmsDecnetIV_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 14, 2, 4)
)
_PToPProtoLiaisonUdp_ObjectIdentity = ObjectIdentity
pToPProtoLiaisonUdp = _PToPProtoLiaisonUdp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 14, 2, 5)
)
_PToPProtoIpx_ObjectIdentity = ObjectIdentity
pToPProtoIpx = _PToPProtoIpx_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 14, 2, 6)
)
_PToPProtoShivaIp_ObjectIdentity = ObjectIdentity
pToPProtoShivaIp = _PToPProtoShivaIp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 14, 2, 7)
)
_RtmpStub_ObjectIdentity = ObjectIdentity
rtmpStub = _RtmpStub_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 16)
)
_RtmpOutRequestPkts_Type = Counter32
_RtmpOutRequestPkts_Object = MibScalar
rtmpOutRequestPkts = _RtmpOutRequestPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 16, 1),
    _RtmpOutRequestPkts_Type()
)
rtmpOutRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpOutRequestPkts.setStatus("mandatory")
_RtmpInVersionMismatches_Type = Counter32
_RtmpInVersionMismatches_Object = MibScalar
rtmpInVersionMismatches = _RtmpInVersionMismatches_Object(
    (1, 3, 6, 1, 2, 1, 13, 16, 2),
    _RtmpInVersionMismatches_Type()
)
rtmpInVersionMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpInVersionMismatches.setStatus("mandatory")
_RtmpInErrors_Type = Counter32
_RtmpInErrors_Object = MibScalar
rtmpInErrors = _RtmpInErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 16, 3),
    _RtmpInErrors_Type()
)
rtmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpInErrors.setStatus("mandatory")
_ZipEndNode_ObjectIdentity = ObjectIdentity
zipEndNode = _ZipEndNode_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 17)
)
_ZipNetInfoTable_Object = MibTable
zipNetInfoTable = _ZipNetInfoTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 17, 1)
)
if mibBuilder.loadTexts:
    zipNetInfoTable.setStatus("mandatory")
_ZipNetInfoEntry_Object = MibTableRow
zipNetInfoEntry = _ZipNetInfoEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 17, 1, 1)
)
zipNetInfoEntry.setIndexNames(
    (0, "APPLETALK-MIB", "atportIndex"),
)
if mibBuilder.loadTexts:
    zipNetInfoEntry.setStatus("mandatory")
_ZipOutGetNetInfos_Type = Counter32
_ZipOutGetNetInfos_Object = MibTableColumn
zipOutGetNetInfos = _ZipOutGetNetInfos_Object(
    (1, 3, 6, 1, 2, 1, 13, 17, 1, 1, 1),
    _ZipOutGetNetInfos_Type()
)
zipOutGetNetInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipOutGetNetInfos.setStatus("mandatory")
_ZipInGetNetInfoReplies_Type = Counter32
_ZipInGetNetInfoReplies_Object = MibTableColumn
zipInGetNetInfoReplies = _ZipInGetNetInfoReplies_Object(
    (1, 3, 6, 1, 2, 1, 13, 17, 1, 1, 2),
    _ZipInGetNetInfoReplies_Type()
)
zipInGetNetInfoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipInGetNetInfoReplies.setStatus("mandatory")
_ZipZoneInInvalids_Type = Counter32
_ZipZoneInInvalids_Object = MibTableColumn
zipZoneInInvalids = _ZipZoneInInvalids_Object(
    (1, 3, 6, 1, 2, 1, 13, 17, 1, 1, 3),
    _ZipZoneInInvalids_Type()
)
zipZoneInInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipZoneInInvalids.setStatus("mandatory")
_ZipInErrors_Type = Counter32
_ZipInErrors_Object = MibScalar
zipInErrors = _ZipInErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 17, 2),
    _ZipInErrors_Type()
)
zipInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipInErrors.setStatus("mandatory")
_PerPort_ObjectIdentity = ObjectIdentity
perPort = _PerPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 18)
)
_PerPortTable_Object = MibTable
perPortTable = _PerPortTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1)
)
if mibBuilder.loadTexts:
    perPortTable.setStatus("mandatory")
_PerPortEntry_Object = MibTableRow
perPortEntry = _PerPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1)
)
perPortEntry.setIndexNames(
    (0, "APPLETALK-MIB", "atportIndex"),
)
if mibBuilder.loadTexts:
    perPortEntry.setStatus("mandatory")
_PerPortAarpInProbes_Type = Counter32
_PerPortAarpInProbes_Object = MibTableColumn
perPortAarpInProbes = _PerPortAarpInProbes_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 1),
    _PerPortAarpInProbes_Type()
)
perPortAarpInProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortAarpInProbes.setStatus("mandatory")
_PerPortAarpOutProbes_Type = Counter32
_PerPortAarpOutProbes_Object = MibTableColumn
perPortAarpOutProbes = _PerPortAarpOutProbes_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 2),
    _PerPortAarpOutProbes_Type()
)
perPortAarpOutProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortAarpOutProbes.setStatus("mandatory")
_PerPortAarpInReqs_Type = Counter32
_PerPortAarpInReqs_Object = MibTableColumn
perPortAarpInReqs = _PerPortAarpInReqs_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 3),
    _PerPortAarpInReqs_Type()
)
perPortAarpInReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortAarpInReqs.setStatus("mandatory")
_PerPortAarpOutReqs_Type = Counter32
_PerPortAarpOutReqs_Object = MibTableColumn
perPortAarpOutReqs = _PerPortAarpOutReqs_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 4),
    _PerPortAarpOutReqs_Type()
)
perPortAarpOutReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortAarpOutReqs.setStatus("mandatory")
_PerPortAarpInRsps_Type = Counter32
_PerPortAarpInRsps_Object = MibTableColumn
perPortAarpInRsps = _PerPortAarpInRsps_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 5),
    _PerPortAarpInRsps_Type()
)
perPortAarpInRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortAarpInRsps.setStatus("mandatory")
_PerPortAarpOutRsps_Type = Counter32
_PerPortAarpOutRsps_Object = MibTableColumn
perPortAarpOutRsps = _PerPortAarpOutRsps_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 6),
    _PerPortAarpOutRsps_Type()
)
perPortAarpOutRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortAarpOutRsps.setStatus("mandatory")
_PerPortDdpInReceives_Type = Counter32
_PerPortDdpInReceives_Object = MibTableColumn
perPortDdpInReceives = _PerPortDdpInReceives_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 7),
    _PerPortDdpInReceives_Type()
)
perPortDdpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortDdpInReceives.setStatus("mandatory")
_PerPortDdpInLocalDatagrams_Type = Counter32
_PerPortDdpInLocalDatagrams_Object = MibTableColumn
perPortDdpInLocalDatagrams = _PerPortDdpInLocalDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 8),
    _PerPortDdpInLocalDatagrams_Type()
)
perPortDdpInLocalDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortDdpInLocalDatagrams.setStatus("mandatory")
_PerPortDdpNoProtocolHandlers_Type = Counter32
_PerPortDdpNoProtocolHandlers_Object = MibTableColumn
perPortDdpNoProtocolHandlers = _PerPortDdpNoProtocolHandlers_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 9),
    _PerPortDdpNoProtocolHandlers_Type()
)
perPortDdpNoProtocolHandlers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortDdpNoProtocolHandlers.setStatus("mandatory")
_PerPortDdpTooShortErrors_Type = Counter32
_PerPortDdpTooShortErrors_Object = MibTableColumn
perPortDdpTooShortErrors = _PerPortDdpTooShortErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 10),
    _PerPortDdpTooShortErrors_Type()
)
perPortDdpTooShortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortDdpTooShortErrors.setStatus("mandatory")
_PerPortDdpTooLongErrors_Type = Counter32
_PerPortDdpTooLongErrors_Object = MibTableColumn
perPortDdpTooLongErrors = _PerPortDdpTooLongErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 11),
    _PerPortDdpTooLongErrors_Type()
)
perPortDdpTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortDdpTooLongErrors.setStatus("mandatory")
_PerPortDdpChecksumErrors_Type = Counter32
_PerPortDdpChecksumErrors_Object = MibTableColumn
perPortDdpChecksumErrors = _PerPortDdpChecksumErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 12),
    _PerPortDdpChecksumErrors_Type()
)
perPortDdpChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortDdpChecksumErrors.setStatus("mandatory")
_PerPortDdpForwRequests_Type = Counter32
_PerPortDdpForwRequests_Object = MibTableColumn
perPortDdpForwRequests = _PerPortDdpForwRequests_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 13),
    _PerPortDdpForwRequests_Type()
)
perPortDdpForwRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortDdpForwRequests.setStatus("mandatory")
_PerPortRtmpInDataPkts_Type = Counter32
_PerPortRtmpInDataPkts_Object = MibTableColumn
perPortRtmpInDataPkts = _PerPortRtmpInDataPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 14),
    _PerPortRtmpInDataPkts_Type()
)
perPortRtmpInDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortRtmpInDataPkts.setStatus("mandatory")
_PerPortRtmpOutDataPkts_Type = Counter32
_PerPortRtmpOutDataPkts_Object = MibTableColumn
perPortRtmpOutDataPkts = _PerPortRtmpOutDataPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 15),
    _PerPortRtmpOutDataPkts_Type()
)
perPortRtmpOutDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortRtmpOutDataPkts.setStatus("mandatory")
_PerPortRtmpInRequestPkts_Type = Counter32
_PerPortRtmpInRequestPkts_Object = MibTableColumn
perPortRtmpInRequestPkts = _PerPortRtmpInRequestPkts_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 16),
    _PerPortRtmpInRequestPkts_Type()
)
perPortRtmpInRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortRtmpInRequestPkts.setStatus("mandatory")
_PerPortRtmpRouteDeletes_Type = Counter32
_PerPortRtmpRouteDeletes_Object = MibTableColumn
perPortRtmpRouteDeletes = _PerPortRtmpRouteDeletes_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 17),
    _PerPortRtmpRouteDeletes_Type()
)
perPortRtmpRouteDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortRtmpRouteDeletes.setStatus("mandatory")
_PerPortZipInZipQueries_Type = Counter32
_PerPortZipInZipQueries_Object = MibTableColumn
perPortZipInZipQueries = _PerPortZipInZipQueries_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 18),
    _PerPortZipInZipQueries_Type()
)
perPortZipInZipQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortZipInZipQueries.setStatus("mandatory")
_PerPortZipInZipReplies_Type = Counter32
_PerPortZipInZipReplies_Object = MibTableColumn
perPortZipInZipReplies = _PerPortZipInZipReplies_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 19),
    _PerPortZipInZipReplies_Type()
)
perPortZipInZipReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortZipInZipReplies.setStatus("mandatory")
_PerPortZipInZipExtendedReplies_Type = Counter32
_PerPortZipInZipExtendedReplies_Object = MibTableColumn
perPortZipInZipExtendedReplies = _PerPortZipInZipExtendedReplies_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 20),
    _PerPortZipInZipExtendedReplies_Type()
)
perPortZipInZipExtendedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortZipInZipExtendedReplies.setStatus("mandatory")
_PerPortZipZoneConflictErrors_Type = Counter32
_PerPortZipZoneConflictErrors_Object = MibTableColumn
perPortZipZoneConflictErrors = _PerPortZipZoneConflictErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 21),
    _PerPortZipZoneConflictErrors_Type()
)
perPortZipZoneConflictErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortZipZoneConflictErrors.setStatus("mandatory")
_PerPortZipInErrors_Type = Counter32
_PerPortZipInErrors_Object = MibTableColumn
perPortZipInErrors = _PerPortZipInErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 22),
    _PerPortZipInErrors_Type()
)
perPortZipInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortZipInErrors.setStatus("mandatory")
_PerPortNbpInLookUpRequests_Type = Counter32
_PerPortNbpInLookUpRequests_Object = MibTableColumn
perPortNbpInLookUpRequests = _PerPortNbpInLookUpRequests_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 23),
    _PerPortNbpInLookUpRequests_Type()
)
perPortNbpInLookUpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortNbpInLookUpRequests.setStatus("mandatory")
_PerPortNbpInLookUpReplies_Type = Counter32
_PerPortNbpInLookUpReplies_Object = MibTableColumn
perPortNbpInLookUpReplies = _PerPortNbpInLookUpReplies_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 24),
    _PerPortNbpInLookUpReplies_Type()
)
perPortNbpInLookUpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortNbpInLookUpReplies.setStatus("mandatory")
_PerPortNbpInBroadcastRequests_Type = Counter32
_PerPortNbpInBroadcastRequests_Object = MibTableColumn
perPortNbpInBroadcastRequests = _PerPortNbpInBroadcastRequests_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 25),
    _PerPortNbpInBroadcastRequests_Type()
)
perPortNbpInBroadcastRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortNbpInBroadcastRequests.setStatus("mandatory")
_PerPortNbpInForwardRequests_Type = Counter32
_PerPortNbpInForwardRequests_Object = MibTableColumn
perPortNbpInForwardRequests = _PerPortNbpInForwardRequests_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 26),
    _PerPortNbpInForwardRequests_Type()
)
perPortNbpInForwardRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortNbpInForwardRequests.setStatus("mandatory")
_PerPortNbpOutLookUpReplies_Type = Counter32
_PerPortNbpOutLookUpReplies_Object = MibTableColumn
perPortNbpOutLookUpReplies = _PerPortNbpOutLookUpReplies_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 27),
    _PerPortNbpOutLookUpReplies_Type()
)
perPortNbpOutLookUpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortNbpOutLookUpReplies.setStatus("mandatory")
_PerPortNbpRegistrationFailures_Type = Counter32
_PerPortNbpRegistrationFailures_Object = MibTableColumn
perPortNbpRegistrationFailures = _PerPortNbpRegistrationFailures_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 28),
    _PerPortNbpRegistrationFailures_Type()
)
perPortNbpRegistrationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortNbpRegistrationFailures.setStatus("mandatory")
_PerPortNbpInErrors_Type = Counter32
_PerPortNbpInErrors_Object = MibTableColumn
perPortNbpInErrors = _PerPortNbpInErrors_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 29),
    _PerPortNbpInErrors_Type()
)
perPortNbpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortNbpInErrors.setStatus("mandatory")
_PerPortEchoRequests_Type = Counter32
_PerPortEchoRequests_Object = MibTableColumn
perPortEchoRequests = _PerPortEchoRequests_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 30),
    _PerPortEchoRequests_Type()
)
perPortEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortEchoRequests.setStatus("mandatory")
_PerPortEchoReplies_Type = Counter32
_PerPortEchoReplies_Object = MibTableColumn
perPortEchoReplies = _PerPortEchoReplies_Object(
    (1, 3, 6, 1, 2, 1, 13, 18, 1, 1, 31),
    _PerPortEchoReplies_Type()
)
perPortEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perPortEchoReplies.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPLETALK-MIB",
    **{"ATNetworkNumber": ATNetworkNumber,
       "DdpNodeAddress": DdpNodeAddress,
       "DdpSocketAddress": DdpSocketAddress,
       "ATName": ATName,
       "appletalk": appletalk,
       "llap": llap,
       "llapTable": llapTable,
       "llapEntry": llapEntry,
       "llapIfIndex": llapIfIndex,
       "llapInPkts": llapInPkts,
       "llapOutPkts": llapOutPkts,
       "llapInNoHandlers": llapInNoHandlers,
       "llapInLengthErrors": llapInLengthErrors,
       "llapInErrors": llapInErrors,
       "llapCollisions": llapCollisions,
       "llapDefers": llapDefers,
       "llapNoDataErrors": llapNoDataErrors,
       "llapRandomCTSErrors": llapRandomCTSErrors,
       "llapFCSErrors": llapFCSErrors,
       "aarp": aarp,
       "aarpTable": aarpTable,
       "aarpEntry": aarpEntry,
       "aarpIfIndex": aarpIfIndex,
       "aarpPhysAddress": aarpPhysAddress,
       "aarpNetAddress": aarpNetAddress,
       "aarpStatus": aarpStatus,
       "aarpLookups": aarpLookups,
       "aarpHits": aarpHits,
       "atport": atport,
       "atportTable": atportTable,
       "atportEntry": atportEntry,
       "atportIndex": atportIndex,
       "atportDescr": atportDescr,
       "atportType": atportType,
       "atportNetStart": atportNetStart,
       "atportNetEnd": atportNetEnd,
       "atportNetAddress": atportNetAddress,
       "atportStatus": atportStatus,
       "atportNetConfig": atportNetConfig,
       "atportZoneConfig": atportZoneConfig,
       "atportZoneDefault": atportZoneDefault,
       "atportIfIndex": atportIfIndex,
       "atportNetFrom": atportNetFrom,
       "atportZoneFrom": atportZoneFrom,
       "atportInPkts": atportInPkts,
       "atportOutPkts": atportOutPkts,
       "atportHome": atportHome,
       "atportCurrentZone": atportCurrentZone,
       "atportConflictPhysAddr": atportConflictPhysAddr,
       "atportZoneTable": atportZoneTable,
       "atportZoneEntry": atportZoneEntry,
       "atportZonePort": atportZonePort,
       "atportZoneName": atportZoneName,
       "atportZoneStatus": atportZoneStatus,
       "ddp": ddp,
       "ddpOutRequests": ddpOutRequests,
       "ddpOutShorts": ddpOutShorts,
       "ddpOutLongs": ddpOutLongs,
       "ddpInReceives": ddpInReceives,
       "ddpForwRequests": ddpForwRequests,
       "ddpInLocalDatagrams": ddpInLocalDatagrams,
       "ddpNoProtocolHandlers": ddpNoProtocolHandlers,
       "ddpOutNoRoutes": ddpOutNoRoutes,
       "ddpTooShortErrors": ddpTooShortErrors,
       "ddpTooLongErrors": ddpTooLongErrors,
       "ddpBroadcastErrors": ddpBroadcastErrors,
       "ddpShortDDPErrors": ddpShortDDPErrors,
       "ddpHopCountErrors": ddpHopCountErrors,
       "ddpChecksumErrors": ddpChecksumErrors,
       "ddpListenerTable": ddpListenerTable,
       "ddpListenerEntry": ddpListenerEntry,
       "ddpListenerAddress": ddpListenerAddress,
       "ddpListenerInPkts": ddpListenerInPkts,
       "ddpListenerStatus": ddpListenerStatus,
       "ddpForwardingTable": ddpForwardingTable,
       "ddpForwardingEntry": ddpForwardingEntry,
       "ddpForwardingNetEnd": ddpForwardingNetEnd,
       "ddpForwardingNetStart": ddpForwardingNetStart,
       "ddpForwardingNextHop": ddpForwardingNextHop,
       "ddpForwardingProto": ddpForwardingProto,
       "ddpForwardingModifiedTime": ddpForwardingModifiedTime,
       "ddpForwardingUseCounts": ddpForwardingUseCounts,
       "ddpForwardingPort": ddpForwardingPort,
       "ddpForwProtoOids": ddpForwProtoOids,
       "rtmpRoutingProto": rtmpRoutingProto,
       "kipRoutingProto": kipRoutingProto,
       "ddpForwardingTableOverflows": ddpForwardingTableOverflows,
       "rtmp": rtmp,
       "rtmpTable": rtmpTable,
       "rtmpEntry": rtmpEntry,
       "rtmpRangeStart": rtmpRangeStart,
       "rtmpRangeEnd": rtmpRangeEnd,
       "rtmpNextHop": rtmpNextHop,
       "rtmpType": rtmpType,
       "rtmpPort": rtmpPort,
       "rtmpHops": rtmpHops,
       "rtmpState": rtmpState,
       "rtmpInDataPkts": rtmpInDataPkts,
       "rtmpOutDataPkts": rtmpOutDataPkts,
       "rtmpInRequestPkts": rtmpInRequestPkts,
       "rtmpNextIREqualChanges": rtmpNextIREqualChanges,
       "rtmpNextIRLessChanges": rtmpNextIRLessChanges,
       "rtmpRouteDeletes": rtmpRouteDeletes,
       "rtmpRoutingTableOverflows": rtmpRoutingTableOverflows,
       "kip": kip,
       "kipTable": kipTable,
       "kipEntry": kipEntry,
       "kipNetStart": kipNetStart,
       "kipNetEnd": kipNetEnd,
       "kipNextHop": kipNextHop,
       "kipHopCount": kipHopCount,
       "kipBCastAddr": kipBCastAddr,
       "kipCore": kipCore,
       "kipType": kipType,
       "kipState": kipState,
       "kipShare": kipShare,
       "kipFrom": kipFrom,
       "zipRouter": zipRouter,
       "zipTable": zipTable,
       "zipEntry": zipEntry,
       "zipZoneName": zipZoneName,
       "zipZoneIndex": zipZoneIndex,
       "zipZoneNetStart": zipZoneNetStart,
       "zipZoneNetEnd": zipZoneNetEnd,
       "zipZoneState": zipZoneState,
       "zipZoneFrom": zipZoneFrom,
       "zipZonePort": zipZonePort,
       "zipInZipQueries": zipInZipQueries,
       "zipInZipReplies": zipInZipReplies,
       "zipInZipExtendedReplies": zipInZipExtendedReplies,
       "zipZoneConflictErrors": zipZoneConflictErrors,
       "zipInObsoletes": zipInObsoletes,
       "zipRouterNetInfoTable": zipRouterNetInfoTable,
       "zipRouterNetInfoEntry": zipRouterNetInfoEntry,
       "zipInGetNetInfos": zipInGetNetInfos,
       "zipOutGetNetInfoReplies": zipOutGetNetInfoReplies,
       "zipZoneOutInvalids": zipZoneOutInvalids,
       "zipAddressInvalids": zipAddressInvalids,
       "nbp": nbp,
       "nbpTable": nbpTable,
       "nbpEntry": nbpEntry,
       "nbpIndex": nbpIndex,
       "nbpObject": nbpObject,
       "nbpType": nbpType,
       "nbpZone": nbpZone,
       "nbpState": nbpState,
       "nbpAddress": nbpAddress,
       "nbpEnumerator": nbpEnumerator,
       "nbpInLookUpRequests": nbpInLookUpRequests,
       "nbpInLookUpReplies": nbpInLookUpReplies,
       "nbpInBroadcastRequests": nbpInBroadcastRequests,
       "nbpInForwardRequests": nbpInForwardRequests,
       "nbpOutLookUpReplies": nbpOutLookUpReplies,
       "nbpRegistrationFailures": nbpRegistrationFailures,
       "nbpInErrors": nbpInErrors,
       "atecho": atecho,
       "atechoRequests": atechoRequests,
       "atechoReplies": atechoReplies,
       "atechoOutRequests": atechoOutRequests,
       "atechoInReplies": atechoInReplies,
       "atp": atp,
       "atpInPkts": atpInPkts,
       "atpOutPkts": atpOutPkts,
       "atpTRequestRetransmissions": atpTRequestRetransmissions,
       "atpTResponseRetransmissions": atpTResponseRetransmissions,
       "atpReleaseTimerExpiredCounts": atpReleaseTimerExpiredCounts,
       "atpRetryCountExceededs": atpRetryCountExceededs,
       "atpListenerTable": atpListenerTable,
       "atpListenerEntry": atpListenerEntry,
       "atpListenerAddress": atpListenerAddress,
       "atpListenerStatus": atpListenerStatus,
       "pap": pap,
       "papInOpenConns": papInOpenConns,
       "papOutOpenConns": papOutOpenConns,
       "papInDatas": papInDatas,
       "papOutDatas": papOutDatas,
       "papInCloseConns": papInCloseConns,
       "papOutCloseConns": papOutCloseConns,
       "papTickleTimeoutCloses": papTickleTimeoutCloses,
       "papServerTable": papServerTable,
       "papServerEntry": papServerEntry,
       "papServerIndex": papServerIndex,
       "papServerListeningSocket": papServerListeningSocket,
       "papServerStatus": papServerStatus,
       "papServerCompletedJobs": papServerCompletedJobs,
       "papServerBusyJobs": papServerBusyJobs,
       "papServerFreeJobs": papServerFreeJobs,
       "papServerAuthenticationFailures": papServerAuthenticationFailures,
       "papServerAccountingFailures": papServerAccountingFailures,
       "papServerGeneralFailures": papServerGeneralFailures,
       "papServerState": papServerState,
       "papServerLastStatusMsg": papServerLastStatusMsg,
       "asp": asp,
       "aspInputTransactions": aspInputTransactions,
       "aspOutputTransactions": aspOutputTransactions,
       "aspInOpenSessions": aspInOpenSessions,
       "aspOutOpenSessions": aspOutOpenSessions,
       "aspInCloseSessions": aspInCloseSessions,
       "aspOutCloseSessions": aspOutCloseSessions,
       "aspNoMoreSessionsErrors": aspNoMoreSessionsErrors,
       "aspTickleTimeOutCloses": aspTickleTimeOutCloses,
       "aspConnTable": aspConnTable,
       "aspConnEntry": aspConnEntry,
       "aspConnLocalAddress": aspConnLocalAddress,
       "aspConnRemoteAddress": aspConnRemoteAddress,
       "aspConnID": aspConnID,
       "aspConnLastReqNum": aspConnLastReqNum,
       "aspConnServerEnd": aspConnServerEnd,
       "aspConnState": aspConnState,
       "adsp": adsp,
       "adspInPkts": adspInPkts,
       "adspOutPkts": adspOutPkts,
       "adspInOctets": adspInOctets,
       "adspOutOctets": adspOutOctets,
       "adspInDataPkts": adspInDataPkts,
       "adspOutDataPkts": adspOutDataPkts,
       "adspTimeoutErrors": adspTimeoutErrors,
       "adspTimeoutCloseErrors": adspTimeoutCloseErrors,
       "adspConnTable": adspConnTable,
       "adspConnEntry": adspConnEntry,
       "adspConnLocalAddress": adspConnLocalAddress,
       "adspConnLocalConnID": adspConnLocalConnID,
       "adspConnRemoteAddress": adspConnRemoteAddress,
       "adspConnRemoteConnID": adspConnRemoteConnID,
       "adspConnState": adspConnState,
       "atportptop": atportptop,
       "atportPtoPTable": atportPtoPTable,
       "atportPtoPEntry": atportPtoPEntry,
       "atportPtoPIndex": atportPtoPIndex,
       "atportPtoPProtocol": atportPtoPProtocol,
       "atportPtoPRemoteName": atportPtoPRemoteName,
       "atportPtoPRemoteAddress": atportPtoPRemoteAddress,
       "atportPtoPPortIndex": atportPtoPPortIndex,
       "atportPtoPStatus": atportPtoPStatus,
       "atportPtoPProtoOids": atportPtoPProtoOids,
       "pToPProtoOther": pToPProtoOther,
       "pToPProtoAurp": pToPProtoAurp,
       "pToPProtoCaymanUdp": pToPProtoCaymanUdp,
       "pToPProtoAtkvmsDecnetIV": pToPProtoAtkvmsDecnetIV,
       "pToPProtoLiaisonUdp": pToPProtoLiaisonUdp,
       "pToPProtoIpx": pToPProtoIpx,
       "pToPProtoShivaIp": pToPProtoShivaIp,
       "rtmpStub": rtmpStub,
       "rtmpOutRequestPkts": rtmpOutRequestPkts,
       "rtmpInVersionMismatches": rtmpInVersionMismatches,
       "rtmpInErrors": rtmpInErrors,
       "zipEndNode": zipEndNode,
       "zipNetInfoTable": zipNetInfoTable,
       "zipNetInfoEntry": zipNetInfoEntry,
       "zipOutGetNetInfos": zipOutGetNetInfos,
       "zipInGetNetInfoReplies": zipInGetNetInfoReplies,
       "zipZoneInInvalids": zipZoneInInvalids,
       "zipInErrors": zipInErrors,
       "perPort": perPort,
       "perPortTable": perPortTable,
       "perPortEntry": perPortEntry,
       "perPortAarpInProbes": perPortAarpInProbes,
       "perPortAarpOutProbes": perPortAarpOutProbes,
       "perPortAarpInReqs": perPortAarpInReqs,
       "perPortAarpOutReqs": perPortAarpOutReqs,
       "perPortAarpInRsps": perPortAarpInRsps,
       "perPortAarpOutRsps": perPortAarpOutRsps,
       "perPortDdpInReceives": perPortDdpInReceives,
       "perPortDdpInLocalDatagrams": perPortDdpInLocalDatagrams,
       "perPortDdpNoProtocolHandlers": perPortDdpNoProtocolHandlers,
       "perPortDdpTooShortErrors": perPortDdpTooShortErrors,
       "perPortDdpTooLongErrors": perPortDdpTooLongErrors,
       "perPortDdpChecksumErrors": perPortDdpChecksumErrors,
       "perPortDdpForwRequests": perPortDdpForwRequests,
       "perPortRtmpInDataPkts": perPortRtmpInDataPkts,
       "perPortRtmpOutDataPkts": perPortRtmpOutDataPkts,
       "perPortRtmpInRequestPkts": perPortRtmpInRequestPkts,
       "perPortRtmpRouteDeletes": perPortRtmpRouteDeletes,
       "perPortZipInZipQueries": perPortZipInZipQueries,
       "perPortZipInZipReplies": perPortZipInZipReplies,
       "perPortZipInZipExtendedReplies": perPortZipInZipExtendedReplies,
       "perPortZipZoneConflictErrors": perPortZipZoneConflictErrors,
       "perPortZipInErrors": perPortZipInErrors,
       "perPortNbpInLookUpRequests": perPortNbpInLookUpRequests,
       "perPortNbpInLookUpReplies": perPortNbpInLookUpReplies,
       "perPortNbpInBroadcastRequests": perPortNbpInBroadcastRequests,
       "perPortNbpInForwardRequests": perPortNbpInForwardRequests,
       "perPortNbpOutLookUpReplies": perPortNbpOutLookUpReplies,
       "perPortNbpRegistrationFailures": perPortNbpRegistrationFailures,
       "perPortNbpInErrors": perPortNbpInErrors,
       "perPortEchoRequests": perPortEchoRequests,
       "perPortEchoReplies": perPortEchoReplies}
)
