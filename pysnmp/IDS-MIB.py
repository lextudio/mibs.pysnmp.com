# SNMP MIB module (IDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:08 2024
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

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

(rsIDS,) = mibBuilder.importSymbols(
    "RADWARE-MIB",
    "rsIDS")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
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





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsIDSTrackingTable_Object = MibTable
rsIDSTrackingTable = _RsIDSTrackingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 1)
)
if mibBuilder.loadTexts:
    rsIDSTrackingTable.setStatus("mandatory")
_RsIDStrackingEntry_Object = MibTableRow
rsIDStrackingEntry = _RsIDStrackingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 1, 1)
)
rsIDStrackingEntry.setIndexNames(
    (0, "IDS-MIB", "rsIDSFilterGroupName"),
)
if mibBuilder.loadTexts:
    rsIDStrackingEntry.setStatus("mandatory")


class _RsIDSFilterGroupName_Type(DisplayString):
    """Custom type rsIDSFilterGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsIDSFilterGroupName_Type.__name__ = "DisplayString"
_RsIDSFilterGroupName_Object = MibTableColumn
rsIDSFilterGroupName = _RsIDSFilterGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 1, 1, 1),
    _RsIDSFilterGroupName_Type()
)
rsIDSFilterGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIDSFilterGroupName.setStatus("mandatory")


class _RsIDSTrackingTime_Type(Integer32):
    """Custom type rsIDSTrackingTime based on Integer32"""
    defaultValue = 1000


_RsIDSTrackingTime_Object = MibTableColumn
rsIDSTrackingTime = _RsIDSTrackingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 1, 1, 2),
    _RsIDSTrackingTime_Type()
)
rsIDSTrackingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSTrackingTime.setStatus("mandatory")


class _RsIDSThreshold_Type(Integer32):
    """Custom type rsIDSThreshold based on Integer32"""
    defaultValue = 50


_RsIDSThreshold_Object = MibTableColumn
rsIDSThreshold = _RsIDSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 1, 1, 3),
    _RsIDSThreshold_Type()
)
rsIDSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSThreshold.setStatus("mandatory")


class _RsIDSFilterGroupType_Type(Integer32):
    """Custom type rsIDSFilterGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("group", 2))
    )


_RsIDSFilterGroupType_Type.__name__ = "Integer32"
_RsIDSFilterGroupType_Object = MibTableColumn
rsIDSFilterGroupType = _RsIDSFilterGroupType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 1, 1, 4),
    _RsIDSFilterGroupType_Type()
)
rsIDSFilterGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSFilterGroupType.setStatus("mandatory")


class _RsIDSTrackingType_Type(Integer32):
    """Custom type rsIDSTrackingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("landattack", 7),
          ("ncpd", 3),
          ("ncpf", 5),
          ("ncps", 2),
          ("ncpsd", 4),
          ("reset", 1),
          ("synattackack", 8),
          ("tcpack", 10),
          ("tcpelse", 14),
          ("tcpfin", 13),
          ("tcprst", 12),
          ("tcpsyn", 9),
          ("tcpsynack", 11),
          ("winnuke", 6))
    )


_RsIDSTrackingType_Type.__name__ = "Integer32"
_RsIDSTrackingType_Object = MibTableColumn
rsIDSTrackingType = _RsIDSTrackingType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 1, 1, 5),
    _RsIDSTrackingType_Type()
)
rsIDSTrackingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSTrackingType.setStatus("mandatory")
_RsIDSStatus_Type = RowStatus
_RsIDSStatus_Object = MibTableColumn
rsIDSStatus = _RsIDSStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 1, 1, 6),
    _RsIDSStatus_Type()
)
rsIDSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSStatus.setStatus("mandatory")
_RsIDSDummy1_Type = Integer32
_RsIDSDummy1_Object = MibScalar
rsIDSDummy1 = _RsIDSDummy1_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 1, 2),
    _RsIDSDummy1_Type()
)
rsIDSDummy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIDSDummy1.setStatus("mandatory")


class _RsIDSMechanismStatus_Type(Integer32):
    """Custom type rsIDSMechanismStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSMechanismStatus_Type.__name__ = "Integer32"
_RsIDSMechanismStatus_Object = MibScalar
rsIDSMechanismStatus = _RsIDSMechanismStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 2),
    _RsIDSMechanismStatus_Type()
)
rsIDSMechanismStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSMechanismStatus.setStatus("mandatory")
_RsIDSTCPAgingTimeFreq_Type = Integer32
_RsIDSTCPAgingTimeFreq_Object = MibScalar
rsIDSTCPAgingTimeFreq = _RsIDSTCPAgingTimeFreq_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 3),
    _RsIDSTCPAgingTimeFreq_Type()
)
rsIDSTCPAgingTimeFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSTCPAgingTimeFreq.setStatus("mandatory")
_RsIDSNCPsAgingTimeFreq_Type = Integer32
_RsIDSNCPsAgingTimeFreq_Object = MibScalar
rsIDSNCPsAgingTimeFreq = _RsIDSNCPsAgingTimeFreq_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 4),
    _RsIDSNCPsAgingTimeFreq_Type()
)
rsIDSNCPsAgingTimeFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSNCPsAgingTimeFreq.setStatus("mandatory")
_RsIDSStatsAgingTimeFreq_Type = Integer32
_RsIDSStatsAgingTimeFreq_Object = MibScalar
rsIDSStatsAgingTimeFreq = _RsIDSStatsAgingTimeFreq_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 5),
    _RsIDSStatsAgingTimeFreq_Type()
)
rsIDSStatsAgingTimeFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSStatsAgingTimeFreq.setStatus("mandatory")
_RsIDSNCPSTableSize_Type = Integer32
_RsIDSNCPSTableSize_Object = MibScalar
rsIDSNCPSTableSize = _RsIDSNCPSTableSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 6),
    _RsIDSNCPSTableSize_Type()
)
rsIDSNCPSTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSNCPSTableSize.setStatus("mandatory")
_RsIDSNCPDTableSize_Type = Integer32
_RsIDSNCPDTableSize_Object = MibScalar
rsIDSNCPDTableSize = _RsIDSNCPDTableSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 7),
    _RsIDSNCPDTableSize_Type()
)
rsIDSNCPDTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSNCPDTableSize.setStatus("mandatory")
_RsIDSNCPSDTableSize_Type = Integer32
_RsIDSNCPSDTableSize_Object = MibScalar
rsIDSNCPSDTableSize = _RsIDSNCPSDTableSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 8),
    _RsIDSNCPSDTableSize_Type()
)
rsIDSNCPSDTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSNCPSDTableSize.setStatus("mandatory")
_RsIDSTCPTableSize_Type = Integer32
_RsIDSTCPTableSize_Object = MibScalar
rsIDSTCPTableSize = _RsIDSTCPTableSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 9),
    _RsIDSTCPTableSize_Type()
)
rsIDSTCPTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSTCPTableSize.setStatus("mandatory")
_RsIDSSTATSTableSize_Type = Integer32
_RsIDSSTATSTableSize_Object = MibScalar
rsIDSSTATSTableSize = _RsIDSSTATSTableSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 10),
    _RsIDSSTATSTableSize_Type()
)
rsIDSSTATSTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSSTATSTableSize.setStatus("mandatory")


class _RsIDSBasic_Type(Integer32):
    """Custom type rsIDSBasic based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSBasic_Type.__name__ = "Integer32"
_RsIDSBasic_Object = MibScalar
rsIDSBasic = _RsIDSBasic_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 11),
    _RsIDSBasic_Type()
)
rsIDSBasic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSBasic.setStatus("mandatory")


class _RsIDSAllServers_Type(Integer32):
    """Custom type rsIDSAllServers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSAllServers_Type.__name__ = "Integer32"
_RsIDSAllServers_Object = MibScalar
rsIDSAllServers = _RsIDSAllServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 12),
    _RsIDSAllServers_Type()
)
rsIDSAllServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSAllServers.setStatus("mandatory")


class _RsIDSUNIXServers_Type(Integer32):
    """Custom type rsIDSUNIXServers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSUNIXServers_Type.__name__ = "Integer32"
_RsIDSUNIXServers_Object = MibScalar
rsIDSUNIXServers = _RsIDSUNIXServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 13),
    _RsIDSUNIXServers_Type()
)
rsIDSUNIXServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSUNIXServers.setStatus("mandatory")


class _RsIDSLotusServers_Type(Integer32):
    """Custom type rsIDSLotusServers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSLotusServers_Type.__name__ = "Integer32"
_RsIDSLotusServers_Object = MibScalar
rsIDSLotusServers = _RsIDSLotusServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 14),
    _RsIDSLotusServers_Type()
)
rsIDSLotusServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSLotusServers.setStatus("mandatory")


class _RsIDSMSIISServers_Type(Integer32):
    """Custom type rsIDSMSIISServers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSMSIISServers_Type.__name__ = "Integer32"
_RsIDSMSIISServers_Object = MibScalar
rsIDSMSIISServers = _RsIDSMSIISServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 15),
    _RsIDSMSIISServers_Type()
)
rsIDSMSIISServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSMSIISServers.setStatus("mandatory")


class _RsIDSMSFrontPageServers_Type(Integer32):
    """Custom type rsIDSMSFrontPageServers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSMSFrontPageServers_Type.__name__ = "Integer32"
_RsIDSMSFrontPageServers_Object = MibScalar
rsIDSMSFrontPageServers = _RsIDSMSFrontPageServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 16),
    _RsIDSMSFrontPageServers_Type()
)
rsIDSMSFrontPageServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSMSFrontPageServers.setStatus("mandatory")


class _RsIDSApacheServers_Type(Integer32):
    """Custom type rsIDSApacheServers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSApacheServers_Type.__name__ = "Integer32"
_RsIDSApacheServers_Object = MibScalar
rsIDSApacheServers = _RsIDSApacheServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 17),
    _RsIDSApacheServers_Type()
)
rsIDSApacheServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSApacheServers.setStatus("mandatory")


class _RsIDSNetscapeWebServers_Type(Integer32):
    """Custom type rsIDSNetscapeWebServers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSNetscapeWebServers_Type.__name__ = "Integer32"
_RsIDSNetscapeWebServers_Object = MibScalar
rsIDSNetscapeWebServers = _RsIDSNetscapeWebServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 18),
    _RsIDSNetscapeWebServers_Type()
)
rsIDSNetscapeWebServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSNetscapeWebServers.setStatus("mandatory")


class _RsIDSNovellServers_Type(Integer32):
    """Custom type rsIDSNovellServers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSNovellServers_Type.__name__ = "Integer32"
_RsIDSNovellServers_Object = MibScalar
rsIDSNovellServers = _RsIDSNovellServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 19),
    _RsIDSNovellServers_Type()
)
rsIDSNovellServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSNovellServers.setStatus("mandatory")


class _RsIDSOracleServers_Type(Integer32):
    """Custom type rsIDSOracleServers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSOracleServers_Type.__name__ = "Integer32"
_RsIDSOracleServers_Object = MibScalar
rsIDSOracleServers = _RsIDSOracleServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 20),
    _RsIDSOracleServers_Type()
)
rsIDSOracleServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSOracleServers.setStatus("mandatory")


class _RsIDSOmniHTTPDServers_Type(Integer32):
    """Custom type rsIDSOmniHTTPDServers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSOmniHTTPDServers_Type.__name__ = "Integer32"
_RsIDSOmniHTTPDServers_Object = MibScalar
rsIDSOmniHTTPDServers = _RsIDSOmniHTTPDServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 21),
    _RsIDSOmniHTTPDServers_Type()
)
rsIDSOmniHTTPDServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSOmniHTTPDServers.setStatus("mandatory")


class _RsIDSWebSiteServers_Type(Integer32):
    """Custom type rsIDSWebSiteServers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSWebSiteServers_Type.__name__ = "Integer32"
_RsIDSWebSiteServers_Object = MibScalar
rsIDSWebSiteServers = _RsIDSWebSiteServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 22),
    _RsIDSWebSiteServers_Type()
)
rsIDSWebSiteServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSWebSiteServers.setStatus("mandatory")


class _RsIDSColdfusionServers_Type(Integer32):
    """Custom type rsIDSColdfusionServers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSColdfusionServers_Type.__name__ = "Integer32"
_RsIDSColdfusionServers_Object = MibScalar
rsIDSColdfusionServers = _RsIDSColdfusionServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 23),
    _RsIDSColdfusionServers_Type()
)
rsIDSColdfusionServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSColdfusionServers.setStatus("mandatory")


class _RsIDSIRIXServers_Type(Integer32):
    """Custom type rsIDSIRIXServers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSIRIXServers_Type.__name__ = "Integer32"
_RsIDSIRIXServers_Object = MibScalar
rsIDSIRIXServers = _RsIDSIRIXServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 24),
    _RsIDSIRIXServers_Type()
)
rsIDSIRIXServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSIRIXServers.setStatus("mandatory")


class _RsIDSNCSAServers_Type(Integer32):
    """Custom type rsIDSNCSAServers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSNCSAServers_Type.__name__ = "Integer32"
_RsIDSNCSAServers_Object = MibScalar
rsIDSNCSAServers = _RsIDSNCSAServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 25),
    _RsIDSNCSAServers_Type()
)
rsIDSNCSAServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSNCSAServers.setStatus("mandatory")


class _RsIDSCompaqServers_Type(Integer32):
    """Custom type rsIDSCompaqServers based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSCompaqServers_Type.__name__ = "Integer32"
_RsIDSCompaqServers_Object = MibScalar
rsIDSCompaqServers = _RsIDSCompaqServers_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 26),
    _RsIDSCompaqServers_Type()
)
rsIDSCompaqServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSCompaqServers.setStatus("mandatory")


class _RsIDSbackdoors_Type(Integer32):
    """Custom type rsIDSbackdoors based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSbackdoors_Type.__name__ = "Integer32"
_RsIDSbackdoors_Object = MibScalar
rsIDSbackdoors = _RsIDSbackdoors_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 27),
    _RsIDSbackdoors_Type()
)
rsIDSbackdoors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSbackdoors.setStatus("mandatory")


class _RsIDSTraps_Type(Integer32):
    """Custom type rsIDSTraps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIDSTraps_Type.__name__ = "Integer32"
_RsIDSTraps_Object = MibScalar
rsIDSTraps = _RsIDSTraps_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 28),
    _RsIDSTraps_Type()
)
rsIDSTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSTraps.setStatus("mandatory")
_RsIDSStatsTable_Object = MibTable
rsIDSStatsTable = _RsIDSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 29)
)
if mibBuilder.loadTexts:
    rsIDSStatsTable.setStatus("mandatory")
_RsIDSStatsEntry_Object = MibTableRow
rsIDSStatsEntry = _RsIDSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 29, 1)
)
rsIDSStatsEntry.setIndexNames(
    (0, "IDS-MIB", "rsIDSAttackIndex"),
)
if mibBuilder.loadTexts:
    rsIDSStatsEntry.setStatus("mandatory")
_RsIDSAttackIndex_Type = Integer32
_RsIDSAttackIndex_Object = MibTableColumn
rsIDSAttackIndex = _RsIDSAttackIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 29, 1, 1),
    _RsIDSAttackIndex_Type()
)
rsIDSAttackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIDSAttackIndex.setStatus("mandatory")


class _RsIDSAttackName_Type(DisplayString):
    """Custom type rsIDSAttackName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsIDSAttackName_Type.__name__ = "DisplayString"
_RsIDSAttackName_Object = MibTableColumn
rsIDSAttackName = _RsIDSAttackName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 29, 1, 2),
    _RsIDSAttackName_Type()
)
rsIDSAttackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIDSAttackName.setStatus("mandatory")
_RsIDSAttackSrcAddr_Type = IpAddress
_RsIDSAttackSrcAddr_Object = MibTableColumn
rsIDSAttackSrcAddr = _RsIDSAttackSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 29, 1, 3),
    _RsIDSAttackSrcAddr_Type()
)
rsIDSAttackSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIDSAttackSrcAddr.setStatus("mandatory")
_RsIDSAttackDstAddr_Type = IpAddress
_RsIDSAttackDstAddr_Object = MibTableColumn
rsIDSAttackDstAddr = _RsIDSAttackDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 29, 1, 4),
    _RsIDSAttackDstAddr_Type()
)
rsIDSAttackDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIDSAttackDstAddr.setStatus("mandatory")


class _RsIDSAttackStatus_Type(DisplayString):
    """Custom type rsIDSAttackStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RsIDSAttackStatus_Type.__name__ = "DisplayString"
_RsIDSAttackStatus_Object = MibTableColumn
rsIDSAttackStatus = _RsIDSAttackStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 29, 1, 5),
    _RsIDSAttackStatus_Type()
)
rsIDSAttackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIDSAttackStatus.setStatus("mandatory")


class _RsIDSAttacktime_Type(DisplayString):
    """Custom type rsIDSAttacktime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RsIDSAttacktime_Type.__name__ = "DisplayString"
_RsIDSAttacktime_Object = MibTableColumn
rsIDSAttacktime = _RsIDSAttacktime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 29, 1, 6),
    _RsIDSAttacktime_Type()
)
rsIDSAttacktime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIDSAttacktime.setStatus("mandatory")
_RsIDSStatsStatus_Type = RowStatus
_RsIDSStatsStatus_Object = MibTableColumn
rsIDSStatsStatus = _RsIDSStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 29, 1, 7),
    _RsIDSStatsStatus_Type()
)
rsIDSStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSStatsStatus.setStatus("mandatory")
_RsIDSDummy2_Type = Integer32
_RsIDSDummy2_Object = MibScalar
rsIDSDummy2 = _RsIDSDummy2_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 29, 2),
    _RsIDSDummy2_Type()
)
rsIDSDummy2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIDSDummy2.setStatus("mandatory")
_RsIDSNCPDTableSizeAfterReset_Type = Integer32
_RsIDSNCPDTableSizeAfterReset_Object = MibScalar
rsIDSNCPDTableSizeAfterReset = _RsIDSNCPDTableSizeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 30),
    _RsIDSNCPDTableSizeAfterReset_Type()
)
rsIDSNCPDTableSizeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSNCPDTableSizeAfterReset.setStatus("mandatory")
_RsIDSNCPSDTableSizeAfterReset_Type = Integer32
_RsIDSNCPSDTableSizeAfterReset_Object = MibScalar
rsIDSNCPSDTableSizeAfterReset = _RsIDSNCPSDTableSizeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 31),
    _RsIDSNCPSDTableSizeAfterReset_Type()
)
rsIDSNCPSDTableSizeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSNCPSDTableSizeAfterReset.setStatus("mandatory")
_RsIDSTCPTableSizeAfterReset_Type = Integer32
_RsIDSTCPTableSizeAfterReset_Object = MibScalar
rsIDSTCPTableSizeAfterReset = _RsIDSTCPTableSizeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 32),
    _RsIDSTCPTableSizeAfterReset_Type()
)
rsIDSTCPTableSizeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSTCPTableSizeAfterReset.setStatus("mandatory")
_RsIDSSTATSTableSizeAfterReset_Type = Integer32
_RsIDSSTATSTableSizeAfterReset_Object = MibScalar
rsIDSSTATSTableSizeAfterReset = _RsIDSSTATSTableSizeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65, 33),
    _RsIDSSTATSTableSizeAfterReset_Type()
)
rsIDSSTATSTableSizeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIDSSTATSTableSizeAfterReset.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IDS-MIB",
    **{"TruthValue": TruthValue,
       "RowStatus": RowStatus,
       "NetNumber": NetNumber,
       "rsIDSTrackingTable": rsIDSTrackingTable,
       "rsIDStrackingEntry": rsIDStrackingEntry,
       "rsIDSFilterGroupName": rsIDSFilterGroupName,
       "rsIDSTrackingTime": rsIDSTrackingTime,
       "rsIDSThreshold": rsIDSThreshold,
       "rsIDSFilterGroupType": rsIDSFilterGroupType,
       "rsIDSTrackingType": rsIDSTrackingType,
       "rsIDSStatus": rsIDSStatus,
       "rsIDSDummy1": rsIDSDummy1,
       "rsIDSMechanismStatus": rsIDSMechanismStatus,
       "rsIDSTCPAgingTimeFreq": rsIDSTCPAgingTimeFreq,
       "rsIDSNCPsAgingTimeFreq": rsIDSNCPsAgingTimeFreq,
       "rsIDSStatsAgingTimeFreq": rsIDSStatsAgingTimeFreq,
       "rsIDSNCPSTableSize": rsIDSNCPSTableSize,
       "rsIDSNCPDTableSize": rsIDSNCPDTableSize,
       "rsIDSNCPSDTableSize": rsIDSNCPSDTableSize,
       "rsIDSTCPTableSize": rsIDSTCPTableSize,
       "rsIDSSTATSTableSize": rsIDSSTATSTableSize,
       "rsIDSBasic": rsIDSBasic,
       "rsIDSAllServers": rsIDSAllServers,
       "rsIDSUNIXServers": rsIDSUNIXServers,
       "rsIDSLotusServers": rsIDSLotusServers,
       "rsIDSMSIISServers": rsIDSMSIISServers,
       "rsIDSMSFrontPageServers": rsIDSMSFrontPageServers,
       "rsIDSApacheServers": rsIDSApacheServers,
       "rsIDSNetscapeWebServers": rsIDSNetscapeWebServers,
       "rsIDSNovellServers": rsIDSNovellServers,
       "rsIDSOracleServers": rsIDSOracleServers,
       "rsIDSOmniHTTPDServers": rsIDSOmniHTTPDServers,
       "rsIDSWebSiteServers": rsIDSWebSiteServers,
       "rsIDSColdfusionServers": rsIDSColdfusionServers,
       "rsIDSIRIXServers": rsIDSIRIXServers,
       "rsIDSNCSAServers": rsIDSNCSAServers,
       "rsIDSCompaqServers": rsIDSCompaqServers,
       "rsIDSbackdoors": rsIDSbackdoors,
       "rsIDSTraps": rsIDSTraps,
       "rsIDSStatsTable": rsIDSStatsTable,
       "rsIDSStatsEntry": rsIDSStatsEntry,
       "rsIDSAttackIndex": rsIDSAttackIndex,
       "rsIDSAttackName": rsIDSAttackName,
       "rsIDSAttackSrcAddr": rsIDSAttackSrcAddr,
       "rsIDSAttackDstAddr": rsIDSAttackDstAddr,
       "rsIDSAttackStatus": rsIDSAttackStatus,
       "rsIDSAttacktime": rsIDSAttacktime,
       "rsIDSStatsStatus": rsIDSStatsStatus,
       "rsIDSDummy2": rsIDSDummy2,
       "rsIDSNCPDTableSizeAfterReset": rsIDSNCPDTableSizeAfterReset,
       "rsIDSNCPSDTableSizeAfterReset": rsIDSNCPSDTableSizeAfterReset,
       "rsIDSTCPTableSizeAfterReset": rsIDSTCPTableSizeAfterReset,
       "rsIDSSTATSTableSizeAfterReset": rsIDSSTATSTableSizeAfterReset}
)
