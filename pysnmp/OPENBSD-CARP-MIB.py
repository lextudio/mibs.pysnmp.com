# SNMP MIB module (OPENBSD-CARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPENBSD-CARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:18 2024
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

(openBSD,) = mibBuilder.importSymbols(
    "OPENBSD-BASE-MIB",
    "openBSD")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

carpMIBObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 6)
)
carpMIBObjects.setRevisions(
        ("2012-01-31 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CarpSysctl_ObjectIdentity = ObjectIdentity
carpSysctl = _CarpSysctl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 6, 1)
)
_CarpAllow_Type = TruthValue
_CarpAllow_Object = MibScalar
carpAllow = _CarpAllow_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 1, 1),
    _CarpAllow_Type()
)
carpAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpAllow.setStatus("current")
_CarpPreempt_Type = TruthValue
_CarpPreempt_Object = MibScalar
carpPreempt = _CarpPreempt_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 1, 2),
    _CarpPreempt_Type()
)
carpPreempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpPreempt.setStatus("current")
_CarpLog_Type = TruthValue
_CarpLog_Object = MibScalar
carpLog = _CarpLog_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 1, 3),
    _CarpLog_Type()
)
carpLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpLog.setStatus("current")
_CarpIf_ObjectIdentity = ObjectIdentity
carpIf = _CarpIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 6, 2)
)
_CarpIfNumber_Type = Integer32
_CarpIfNumber_Object = MibScalar
carpIfNumber = _CarpIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 2, 1),
    _CarpIfNumber_Type()
)
carpIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpIfNumber.setStatus("current")
_CarpIfTable_Object = MibTable
carpIfTable = _CarpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 2, 2)
)
if mibBuilder.loadTexts:
    carpIfTable.setStatus("current")
_CarpIfEntry_Object = MibTableRow
carpIfEntry = _CarpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1)
)
carpIfEntry.setIndexNames(
    (0, "OPENBSD-CARP-MIB", "carpIfIndex"),
)
if mibBuilder.loadTexts:
    carpIfEntry.setStatus("current")


class _CarpIfIndex_Type(Integer32):
    """Custom type carpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CarpIfIndex_Type.__name__ = "Integer32"
_CarpIfIndex_Object = MibTableColumn
carpIfIndex = _CarpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 1),
    _CarpIfIndex_Type()
)
carpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpIfIndex.setStatus("current")
_CarpIfDescr_Type = OctetString
_CarpIfDescr_Object = MibTableColumn
carpIfDescr = _CarpIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 2),
    _CarpIfDescr_Type()
)
carpIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpIfDescr.setStatus("current")
_CarpIfVhid_Type = Integer32
_CarpIfVhid_Object = MibTableColumn
carpIfVhid = _CarpIfVhid_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 3),
    _CarpIfVhid_Type()
)
carpIfVhid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpIfVhid.setStatus("current")
_CarpIfDev_Type = OctetString
_CarpIfDev_Object = MibTableColumn
carpIfDev = _CarpIfDev_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 4),
    _CarpIfDev_Type()
)
carpIfDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpIfDev.setStatus("current")
_CarpIfAdvbase_Type = Integer32
_CarpIfAdvbase_Object = MibTableColumn
carpIfAdvbase = _CarpIfAdvbase_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 5),
    _CarpIfAdvbase_Type()
)
carpIfAdvbase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpIfAdvbase.setStatus("current")
_CarpIfAdvskew_Type = Integer32
_CarpIfAdvskew_Object = MibTableColumn
carpIfAdvskew = _CarpIfAdvskew_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 6),
    _CarpIfAdvskew_Type()
)
carpIfAdvskew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpIfAdvskew.setStatus("current")


class _CarpIfState_Type(Integer32):
    """Custom type carpIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("init", 0),
          ("master", 2))
    )


_CarpIfState_Type.__name__ = "Integer32"
_CarpIfState_Object = MibTableColumn
carpIfState = _CarpIfState_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 7),
    _CarpIfState_Type()
)
carpIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpIfState.setStatus("current")
_CarpStats_ObjectIdentity = ObjectIdentity
carpStats = _CarpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3)
)
_CarpIpPktsRecv_Type = Counter64
_CarpIpPktsRecv_Object = MibScalar
carpIpPktsRecv = _CarpIpPktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3, 1),
    _CarpIpPktsRecv_Type()
)
carpIpPktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpIpPktsRecv.setStatus("current")
_CarpIp6PktsRecv_Type = Counter64
_CarpIp6PktsRecv_Object = MibScalar
carpIp6PktsRecv = _CarpIp6PktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3, 2),
    _CarpIp6PktsRecv_Type()
)
carpIp6PktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpIp6PktsRecv.setStatus("current")
_CarpPktDiscardsForBadInterface_Type = Counter64
_CarpPktDiscardsForBadInterface_Object = MibScalar
carpPktDiscardsForBadInterface = _CarpPktDiscardsForBadInterface_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3, 3),
    _CarpPktDiscardsForBadInterface_Type()
)
carpPktDiscardsForBadInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpPktDiscardsForBadInterface.setStatus("current")
_CarpPktDiscardsForWrongTtl_Type = Counter64
_CarpPktDiscardsForWrongTtl_Object = MibScalar
carpPktDiscardsForWrongTtl = _CarpPktDiscardsForWrongTtl_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3, 4),
    _CarpPktDiscardsForWrongTtl_Type()
)
carpPktDiscardsForWrongTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpPktDiscardsForWrongTtl.setStatus("current")
_CarpPktShorterThanHeader_Type = Counter64
_CarpPktShorterThanHeader_Object = MibScalar
carpPktShorterThanHeader = _CarpPktShorterThanHeader_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3, 5),
    _CarpPktShorterThanHeader_Type()
)
carpPktShorterThanHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpPktShorterThanHeader.setStatus("current")
_CarpPktDiscardsForBadChecksum_Type = Counter64
_CarpPktDiscardsForBadChecksum_Object = MibScalar
carpPktDiscardsForBadChecksum = _CarpPktDiscardsForBadChecksum_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3, 6),
    _CarpPktDiscardsForBadChecksum_Type()
)
carpPktDiscardsForBadChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpPktDiscardsForBadChecksum.setStatus("current")
_CarpPktDiscardsForBadVersion_Type = Counter64
_CarpPktDiscardsForBadVersion_Object = MibScalar
carpPktDiscardsForBadVersion = _CarpPktDiscardsForBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3, 7),
    _CarpPktDiscardsForBadVersion_Type()
)
carpPktDiscardsForBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpPktDiscardsForBadVersion.setStatus("current")
_CarpPktDiscardsForTooShort_Type = Counter64
_CarpPktDiscardsForTooShort_Object = MibScalar
carpPktDiscardsForTooShort = _CarpPktDiscardsForTooShort_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3, 8),
    _CarpPktDiscardsForTooShort_Type()
)
carpPktDiscardsForTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpPktDiscardsForTooShort.setStatus("current")
_CarpPktDiscardsForBadAuth_Type = Counter64
_CarpPktDiscardsForBadAuth_Object = MibScalar
carpPktDiscardsForBadAuth = _CarpPktDiscardsForBadAuth_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3, 9),
    _CarpPktDiscardsForBadAuth_Type()
)
carpPktDiscardsForBadAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpPktDiscardsForBadAuth.setStatus("current")
_CarpPktDiscardsForBadVhid_Type = Counter64
_CarpPktDiscardsForBadVhid_Object = MibScalar
carpPktDiscardsForBadVhid = _CarpPktDiscardsForBadVhid_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3, 10),
    _CarpPktDiscardsForBadVhid_Type()
)
carpPktDiscardsForBadVhid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpPktDiscardsForBadVhid.setStatus("current")
_CarpPktDiscardsForBadAddressList_Type = Counter64
_CarpPktDiscardsForBadAddressList_Object = MibScalar
carpPktDiscardsForBadAddressList = _CarpPktDiscardsForBadAddressList_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3, 11),
    _CarpPktDiscardsForBadAddressList_Type()
)
carpPktDiscardsForBadAddressList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpPktDiscardsForBadAddressList.setStatus("current")
_CarpIpPktsSent_Type = Counter64
_CarpIpPktsSent_Object = MibScalar
carpIpPktsSent = _CarpIpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3, 12),
    _CarpIpPktsSent_Type()
)
carpIpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpIpPktsSent.setStatus("current")
_CarpIp6PktsSent_Type = Counter64
_CarpIp6PktsSent_Object = MibScalar
carpIp6PktsSent = _CarpIp6PktsSent_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3, 13),
    _CarpIp6PktsSent_Type()
)
carpIp6PktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpIp6PktsSent.setStatus("current")
_CarpNoMemory_Type = Counter64
_CarpNoMemory_Object = MibScalar
carpNoMemory = _CarpNoMemory_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3, 14),
    _CarpNoMemory_Type()
)
carpNoMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpNoMemory.setStatus("current")
_CarpTransitionsToMaster_Type = Counter64
_CarpTransitionsToMaster_Object = MibScalar
carpTransitionsToMaster = _CarpTransitionsToMaster_Object(
    (1, 3, 6, 1, 4, 1, 30155, 6, 3, 15),
    _CarpTransitionsToMaster_Type()
)
carpTransitionsToMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carpTransitionsToMaster.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPENBSD-CARP-MIB",
    **{"carpMIBObjects": carpMIBObjects,
       "carpSysctl": carpSysctl,
       "carpAllow": carpAllow,
       "carpPreempt": carpPreempt,
       "carpLog": carpLog,
       "carpIf": carpIf,
       "carpIfNumber": carpIfNumber,
       "carpIfTable": carpIfTable,
       "carpIfEntry": carpIfEntry,
       "carpIfIndex": carpIfIndex,
       "carpIfDescr": carpIfDescr,
       "carpIfVhid": carpIfVhid,
       "carpIfDev": carpIfDev,
       "carpIfAdvbase": carpIfAdvbase,
       "carpIfAdvskew": carpIfAdvskew,
       "carpIfState": carpIfState,
       "carpStats": carpStats,
       "carpIpPktsRecv": carpIpPktsRecv,
       "carpIp6PktsRecv": carpIp6PktsRecv,
       "carpPktDiscardsForBadInterface": carpPktDiscardsForBadInterface,
       "carpPktDiscardsForWrongTtl": carpPktDiscardsForWrongTtl,
       "carpPktShorterThanHeader": carpPktShorterThanHeader,
       "carpPktDiscardsForBadChecksum": carpPktDiscardsForBadChecksum,
       "carpPktDiscardsForBadVersion": carpPktDiscardsForBadVersion,
       "carpPktDiscardsForTooShort": carpPktDiscardsForTooShort,
       "carpPktDiscardsForBadAuth": carpPktDiscardsForBadAuth,
       "carpPktDiscardsForBadVhid": carpPktDiscardsForBadVhid,
       "carpPktDiscardsForBadAddressList": carpPktDiscardsForBadAddressList,
       "carpIpPktsSent": carpIpPktsSent,
       "carpIp6PktsSent": carpIp6PktsSent,
       "carpNoMemory": carpNoMemory,
       "carpTransitionsToMaster": carpTransitionsToMaster}
)
