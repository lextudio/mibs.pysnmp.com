# SNMP MIB module (LLDP-EXT-HM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LLDP-EXT-HM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:08 2024
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

(lldpExtensions,
 lldpLocPortNum,
 lldpPortConfigEntry,
 lldpRemIndex,
 lldpRemLocalPortNum,
 lldpRemTimeMark) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "lldpExtensions",
    "lldpLocPortNum",
    "lldpPortConfigEntry",
    "lldpRemIndex",
    "lldpRemLocalPortNum",
    "lldpRemTimeMark")

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

lldpXHmMIB = ModuleIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867)
)
lldpXHmMIB.setRevisions(
        ("2008-09-12 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LldpXHmLocGMRPServiceReqSyntax(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forwardAll", 1),
          ("forwardUnregistered", 2),
          ("notApplicable", 3))
    )



class LldpXHmLocIGMPVersionSyntax(Bits, TextualConvention):
    status = "current"


class LldpXHmLocPortSecModeSyntax(Integer32, TextualConvention):
    status = "current"
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
        *(("automatic", 4),
          ("forceAuthorized", 2),
          ("forceUnauthorized", 3),
          ("multiClient", 5),
          ("notApplicable", 1))
    )



class LldpXHmLocPTPSupportSyntax(Bits, TextualConvention):
    status = "current"


class LldpXHmLocPTPStatusSyntax(Bits, TextualConvention):
    status = "current"


class LldpXHmLocPTPv2DataTransferSyntax(Integer32, TextualConvention):
    status = "current"
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
        *(("notApplicable", 4),
          ("ptp2Ieee8023", 1),
          ("ptp2UdpIpv4", 2),
          ("ptp2UdpIpv6", 3))
    )



class LldpXHmLocPTPv2DelayMechanismSyntax(Integer32, TextualConvention):
    status = "current"
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
        *(("disabled", 3),
          ("e2e", 2),
          ("notApplicable", 4),
          ("p2p", 1))
    )



class LldpXHmRemGMRPServiceReqSyntax(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forwardAll", 1),
          ("forwardUnregistered", 2),
          ("notApplicable", 3))
    )



class LldpXHmRemPTPv2DataTransferSyntax(Integer32, TextualConvention):
    status = "current"
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
        *(("notApplicable", 4),
          ("ptp2Ieee8023", 1),
          ("ptp2UdpIpv4", 2),
          ("ptp2UdpIpv6", 3))
    )



class LldpXHmRemPTPv2DelayMechanismSyntax(Integer32, TextualConvention):
    status = "current"
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
        *(("disabled", 3),
          ("e2e", 2),
          ("notApplicable", 4),
          ("p2p", 1))
    )



class LldpXHmRemPTPSupportSyntax(Bits, TextualConvention):
    status = "current"


class LldpXHmRemPTPStatusSyntax(Bits, TextualConvention):
    status = "current"


class LldpXHmRemPortSecModeSyntax(Integer32, TextualConvention):
    status = "current"
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
        *(("automatic", 4),
          ("forceAuthorized", 2),
          ("forceUnauthorized", 3),
          ("notApplicable", 1))
    )



class LldpXHmRemIGMPVersionSyntax(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_LldpXHmObjects_ObjectIdentity = ObjectIdentity
lldpXHmObjects = _LldpXHmObjects_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1)
)
_LldpXHmConfig_ObjectIdentity = ObjectIdentity
lldpXHmConfig = _LldpXHmConfig_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1)
)
_LldpXHmConfigGMRPTable_Object = MibTable
lldpXHmConfigGMRPTable = _LldpXHmConfigGMRPTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXHmConfigGMRPTable.setStatus("current")
_LldpXHmConfigGMRPEntry_Object = MibTableRow
lldpXHmConfigGMRPEntry = _LldpXHmConfigGMRPEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXHmConfigGMRPEntry.setStatus("current")


class _LldpXHmConfigGMRPTxEnable_Type(TruthValue):
    """Custom type lldpXHmConfigGMRPTxEnable based on TruthValue"""


_LldpXHmConfigGMRPTxEnable_Object = MibTableColumn
lldpXHmConfigGMRPTxEnable = _LldpXHmConfigGMRPTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 1, 1, 1),
    _LldpXHmConfigGMRPTxEnable_Type()
)
lldpXHmConfigGMRPTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXHmConfigGMRPTxEnable.setStatus("current")
_LldpXHmConfigIGMPTable_Object = MibTable
lldpXHmConfigIGMPTable = _LldpXHmConfigIGMPTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXHmConfigIGMPTable.setStatus("current")
_LldpXHmConfigIGMPEntry_Object = MibTableRow
lldpXHmConfigIGMPEntry = _LldpXHmConfigIGMPEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXHmConfigIGMPEntry.setStatus("current")


class _LldpXHmConfigIGMPTxEnable_Type(TruthValue):
    """Custom type lldpXHmConfigIGMPTxEnable based on TruthValue"""


_LldpXHmConfigIGMPTxEnable_Object = MibTableColumn
lldpXHmConfigIGMPTxEnable = _LldpXHmConfigIGMPTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 2, 1, 1),
    _LldpXHmConfigIGMPTxEnable_Type()
)
lldpXHmConfigIGMPTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXHmConfigIGMPTxEnable.setStatus("current")
_LldpXHmConfigPortSecTable_Object = MibTable
lldpXHmConfigPortSecTable = _LldpXHmConfigPortSecTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lldpXHmConfigPortSecTable.setStatus("current")
_LldpXHmConfigPortSecEntry_Object = MibTableRow
lldpXHmConfigPortSecEntry = _LldpXHmConfigPortSecEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXHmConfigPortSecEntry.setStatus("current")


class _LldpXHmConfigPortSecTxEnable_Type(TruthValue):
    """Custom type lldpXHmConfigPortSecTxEnable based on TruthValue"""


_LldpXHmConfigPortSecTxEnable_Object = MibTableColumn
lldpXHmConfigPortSecTxEnable = _LldpXHmConfigPortSecTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 3, 1, 1),
    _LldpXHmConfigPortSecTxEnable_Type()
)
lldpXHmConfigPortSecTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXHmConfigPortSecTxEnable.setStatus("current")
_LldpXHmConfigPTPTable_Object = MibTable
lldpXHmConfigPTPTable = _LldpXHmConfigPTPTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 4)
)
if mibBuilder.loadTexts:
    lldpXHmConfigPTPTable.setStatus("current")
_LldpXHmConfigPTPEntry_Object = MibTableRow
lldpXHmConfigPTPEntry = _LldpXHmConfigPTPEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lldpXHmConfigPTPEntry.setStatus("current")


class _LldpXHmConfigPTPTxEnable_Type(TruthValue):
    """Custom type lldpXHmConfigPTPTxEnable based on TruthValue"""


_LldpXHmConfigPTPTxEnable_Object = MibTableColumn
lldpXHmConfigPTPTxEnable = _LldpXHmConfigPTPTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 4, 1, 1),
    _LldpXHmConfigPTPTxEnable_Type()
)
lldpXHmConfigPTPTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXHmConfigPTPTxEnable.setStatus("current")
_LldpXHmLocalData_ObjectIdentity = ObjectIdentity
lldpXHmLocalData = _LldpXHmLocalData_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2)
)
_LldpXHmLocGMRPTable_Object = MibTable
lldpXHmLocGMRPTable = _LldpXHmLocGMRPTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXHmLocGMRPTable.setStatus("current")
_LldpXHmLocGMRPEntry_Object = MibTableRow
lldpXHmLocGMRPEntry = _LldpXHmLocGMRPEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 1, 1)
)
lldpXHmLocGMRPEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    lldpXHmLocGMRPEntry.setStatus("current")
_LldpXHmLocGMRPSupport_Type = TruthValue
_LldpXHmLocGMRPSupport_Object = MibTableColumn
lldpXHmLocGMRPSupport = _LldpXHmLocGMRPSupport_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 1, 1, 1),
    _LldpXHmLocGMRPSupport_Type()
)
lldpXHmLocGMRPSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocGMRPSupport.setStatus("current")
_LldpXHmLocGMRPStatus_Type = TruthValue
_LldpXHmLocGMRPStatus_Object = MibTableColumn
lldpXHmLocGMRPStatus = _LldpXHmLocGMRPStatus_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 1, 1, 2),
    _LldpXHmLocGMRPStatus_Type()
)
lldpXHmLocGMRPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocGMRPStatus.setStatus("current")
_LldpXHmLocGMRPServiceReq_Type = LldpXHmLocGMRPServiceReqSyntax
_LldpXHmLocGMRPServiceReq_Object = MibTableColumn
lldpXHmLocGMRPServiceReq = _LldpXHmLocGMRPServiceReq_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 1, 1, 3),
    _LldpXHmLocGMRPServiceReq_Type()
)
lldpXHmLocGMRPServiceReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocGMRPServiceReq.setStatus("current")
_LldpXHmLocIGMPTable_Object = MibTable
lldpXHmLocIGMPTable = _LldpXHmLocIGMPTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXHmLocIGMPTable.setStatus("current")
_LldpXHmLocIGMPEntry_Object = MibTableRow
lldpXHmLocIGMPEntry = _LldpXHmLocIGMPEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 2, 1)
)
lldpXHmLocIGMPEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    lldpXHmLocIGMPEntry.setStatus("current")
_LldpXHmLocIGMPSupport_Type = TruthValue
_LldpXHmLocIGMPSupport_Object = MibTableColumn
lldpXHmLocIGMPSupport = _LldpXHmLocIGMPSupport_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 2, 1, 1),
    _LldpXHmLocIGMPSupport_Type()
)
lldpXHmLocIGMPSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocIGMPSupport.setStatus("current")
_LldpXHmLocIGMPStatus_Type = TruthValue
_LldpXHmLocIGMPStatus_Object = MibTableColumn
lldpXHmLocIGMPStatus = _LldpXHmLocIGMPStatus_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 2, 1, 2),
    _LldpXHmLocIGMPStatus_Type()
)
lldpXHmLocIGMPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocIGMPStatus.setStatus("current")
_LldpXHmLocIGMPVersion_Type = LldpXHmLocIGMPVersionSyntax
_LldpXHmLocIGMPVersion_Object = MibTableColumn
lldpXHmLocIGMPVersion = _LldpXHmLocIGMPVersion_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 2, 1, 3),
    _LldpXHmLocIGMPVersion_Type()
)
lldpXHmLocIGMPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocIGMPVersion.setStatus("current")
_LldpXHmLocPortSecTable_Object = MibTable
lldpXHmLocPortSecTable = _LldpXHmLocPortSecTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 3)
)
if mibBuilder.loadTexts:
    lldpXHmLocPortSecTable.setStatus("current")
_LldpXHmLocPortSecEntry_Object = MibTableRow
lldpXHmLocPortSecEntry = _LldpXHmLocPortSecEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 3, 1)
)
lldpXHmLocPortSecEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    lldpXHmLocPortSecEntry.setStatus("current")
_LldpXHmLocPortSecSupport_Type = TruthValue
_LldpXHmLocPortSecSupport_Object = MibTableColumn
lldpXHmLocPortSecSupport = _LldpXHmLocPortSecSupport_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 3, 1, 1),
    _LldpXHmLocPortSecSupport_Type()
)
lldpXHmLocPortSecSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocPortSecSupport.setStatus("current")
_LldpXHmLocPortSecStatus_Type = TruthValue
_LldpXHmLocPortSecStatus_Object = MibTableColumn
lldpXHmLocPortSecStatus = _LldpXHmLocPortSecStatus_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 3, 1, 2),
    _LldpXHmLocPortSecStatus_Type()
)
lldpXHmLocPortSecStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocPortSecStatus.setStatus("current")
_LldpXHmLocPortSecMode_Type = LldpXHmLocPortSecModeSyntax
_LldpXHmLocPortSecMode_Object = MibTableColumn
lldpXHmLocPortSecMode = _LldpXHmLocPortSecMode_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 3, 1, 3),
    _LldpXHmLocPortSecMode_Type()
)
lldpXHmLocPortSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocPortSecMode.setStatus("current")
_LldpXHmLocPTPTable_Object = MibTable
lldpXHmLocPTPTable = _LldpXHmLocPTPTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4)
)
if mibBuilder.loadTexts:
    lldpXHmLocPTPTable.setStatus("current")
_LldpXHmLocPTPEntry_Object = MibTableRow
lldpXHmLocPTPEntry = _LldpXHmLocPTPEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1)
)
lldpXHmLocPTPEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    lldpXHmLocPTPEntry.setStatus("current")
_LldpXHmLocPTPSupport_Type = LldpXHmLocPTPSupportSyntax
_LldpXHmLocPTPSupport_Object = MibTableColumn
lldpXHmLocPTPSupport = _LldpXHmLocPTPSupport_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 1),
    _LldpXHmLocPTPSupport_Type()
)
lldpXHmLocPTPSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocPTPSupport.setStatus("current")
_LldpXHmLocPTPStatus_Type = LldpXHmLocPTPStatusSyntax
_LldpXHmLocPTPStatus_Object = MibTableColumn
lldpXHmLocPTPStatus = _LldpXHmLocPTPStatus_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 2),
    _LldpXHmLocPTPStatus_Type()
)
lldpXHmLocPTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocPTPStatus.setStatus("current")


class _LldpXHmLocPTPSyncInterval_Type(Integer32):
    """Custom type lldpXHmLocPTPSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_LldpXHmLocPTPSyncInterval_Type.__name__ = "Integer32"
_LldpXHmLocPTPSyncInterval_Object = MibTableColumn
lldpXHmLocPTPSyncInterval = _LldpXHmLocPTPSyncInterval_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 3),
    _LldpXHmLocPTPSyncInterval_Type()
)
lldpXHmLocPTPSyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocPTPSyncInterval.setStatus("current")


class _LldpXHmLocPTPv2AnnounceInterval_Type(Integer32):
    """Custom type lldpXHmLocPTPv2AnnounceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_LldpXHmLocPTPv2AnnounceInterval_Type.__name__ = "Integer32"
_LldpXHmLocPTPv2AnnounceInterval_Object = MibTableColumn
lldpXHmLocPTPv2AnnounceInterval = _LldpXHmLocPTPv2AnnounceInterval_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 4),
    _LldpXHmLocPTPv2AnnounceInterval_Type()
)
lldpXHmLocPTPv2AnnounceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocPTPv2AnnounceInterval.setStatus("current")
_LldpXHmLocPTPv2DataTransfer_Type = LldpXHmLocPTPv2DataTransferSyntax
_LldpXHmLocPTPv2DataTransfer_Object = MibTableColumn
lldpXHmLocPTPv2DataTransfer = _LldpXHmLocPTPv2DataTransfer_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 5),
    _LldpXHmLocPTPv2DataTransfer_Type()
)
lldpXHmLocPTPv2DataTransfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocPTPv2DataTransfer.setStatus("current")
_LldpXHmLocPTPv2DelayMechanism_Type = LldpXHmLocPTPv2DelayMechanismSyntax
_LldpXHmLocPTPv2DelayMechanism_Object = MibTableColumn
lldpXHmLocPTPv2DelayMechanism = _LldpXHmLocPTPv2DelayMechanism_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 6),
    _LldpXHmLocPTPv2DelayMechanism_Type()
)
lldpXHmLocPTPv2DelayMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocPTPv2DelayMechanism.setStatus("current")


class _LldpXHmLocPTPClockValues_Type(Bits):
    """Custom type lldpXHmLocPTPClockValues based on Bits"""
    namedValues = NamedValues(
        *(("boundary", 3),
          ("grandmaster", 4),
          ("master", 1),
          ("multidomain", 5),
          ("simplemode", 6),
          ("slave", 0),
          ("transparent", 2))
    )

_LldpXHmLocPTPClockValues_Type.__name__ = "Bits"
_LldpXHmLocPTPClockValues_Object = MibTableColumn
lldpXHmLocPTPClockValues = _LldpXHmLocPTPClockValues_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 7),
    _LldpXHmLocPTPClockValues_Type()
)
lldpXHmLocPTPClockValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocPTPClockValues.setStatus("current")


class _LldpXHmLocPTPv2SubdomainNumber_Type(Integer32):
    """Custom type lldpXHmLocPTPv2SubdomainNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LldpXHmLocPTPv2SubdomainNumber_Type.__name__ = "Integer32"
_LldpXHmLocPTPv2SubdomainNumber_Object = MibTableColumn
lldpXHmLocPTPv2SubdomainNumber = _LldpXHmLocPTPv2SubdomainNumber_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 8),
    _LldpXHmLocPTPv2SubdomainNumber_Type()
)
lldpXHmLocPTPv2SubdomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocPTPv2SubdomainNumber.setStatus("current")


class _LldpXHmLocPTPv1SubdomainName_Type(OctetString):
    """Custom type lldpXHmLocPTPv1SubdomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LldpXHmLocPTPv1SubdomainName_Type.__name__ = "OctetString"
_LldpXHmLocPTPv1SubdomainName_Object = MibTableColumn
lldpXHmLocPTPv1SubdomainName = _LldpXHmLocPTPv1SubdomainName_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 9),
    _LldpXHmLocPTPv1SubdomainName_Type()
)
lldpXHmLocPTPv1SubdomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmLocPTPv1SubdomainName.setStatus("current")
_LldpXHmRemoteData_ObjectIdentity = ObjectIdentity
lldpXHmRemoteData = _LldpXHmRemoteData_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3)
)
_LldpXHmRemGMRPTable_Object = MibTable
lldpXHmRemGMRPTable = _LldpXHmRemGMRPTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXHmRemGMRPTable.setStatus("current")
_LldpXHmRemGMRPEntry_Object = MibTableRow
lldpXHmRemGMRPEntry = _LldpXHmRemGMRPEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 1, 1)
)
lldpXHmRemGMRPEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXHmRemGMRPEntry.setStatus("current")
_LldpXHmRemGMRPSupport_Type = TruthValue
_LldpXHmRemGMRPSupport_Object = MibTableColumn
lldpXHmRemGMRPSupport = _LldpXHmRemGMRPSupport_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 1, 1, 1),
    _LldpXHmRemGMRPSupport_Type()
)
lldpXHmRemGMRPSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemGMRPSupport.setStatus("current")
_LldpXHmRemGMRPStatus_Type = TruthValue
_LldpXHmRemGMRPStatus_Object = MibTableColumn
lldpXHmRemGMRPStatus = _LldpXHmRemGMRPStatus_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 1, 1, 2),
    _LldpXHmRemGMRPStatus_Type()
)
lldpXHmRemGMRPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemGMRPStatus.setStatus("current")
_LldpXHmRemGMRPServiceReq_Type = LldpXHmRemGMRPServiceReqSyntax
_LldpXHmRemGMRPServiceReq_Object = MibTableColumn
lldpXHmRemGMRPServiceReq = _LldpXHmRemGMRPServiceReq_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 1, 1, 3),
    _LldpXHmRemGMRPServiceReq_Type()
)
lldpXHmRemGMRPServiceReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemGMRPServiceReq.setStatus("current")
_LldpXHmRemIGMPTable_Object = MibTable
lldpXHmRemIGMPTable = _LldpXHmRemIGMPTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXHmRemIGMPTable.setStatus("current")
_LldpXHmRemIGMPEntry_Object = MibTableRow
lldpXHmRemIGMPEntry = _LldpXHmRemIGMPEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 2, 1)
)
lldpXHmRemIGMPEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXHmRemIGMPEntry.setStatus("current")
_LldpXHmRemIGMPSupport_Type = TruthValue
_LldpXHmRemIGMPSupport_Object = MibTableColumn
lldpXHmRemIGMPSupport = _LldpXHmRemIGMPSupport_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 2, 1, 1),
    _LldpXHmRemIGMPSupport_Type()
)
lldpXHmRemIGMPSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemIGMPSupport.setStatus("current")
_LldpXHmRemIGMPStatus_Type = TruthValue
_LldpXHmRemIGMPStatus_Object = MibTableColumn
lldpXHmRemIGMPStatus = _LldpXHmRemIGMPStatus_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 2, 1, 2),
    _LldpXHmRemIGMPStatus_Type()
)
lldpXHmRemIGMPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemIGMPStatus.setStatus("current")
_LldpXHmRemIGMPVersion_Type = LldpXHmRemIGMPVersionSyntax
_LldpXHmRemIGMPVersion_Object = MibTableColumn
lldpXHmRemIGMPVersion = _LldpXHmRemIGMPVersion_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 2, 1, 3),
    _LldpXHmRemIGMPVersion_Type()
)
lldpXHmRemIGMPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemIGMPVersion.setStatus("current")
_LldpXHmRemPortSecTable_Object = MibTable
lldpXHmRemPortSecTable = _LldpXHmRemPortSecTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 3)
)
if mibBuilder.loadTexts:
    lldpXHmRemPortSecTable.setStatus("current")
_LldpXHmRemPortSecEntry_Object = MibTableRow
lldpXHmRemPortSecEntry = _LldpXHmRemPortSecEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 3, 1)
)
lldpXHmRemPortSecEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXHmRemPortSecEntry.setStatus("current")
_LldpXHmRemPortSecSupport_Type = TruthValue
_LldpXHmRemPortSecSupport_Object = MibTableColumn
lldpXHmRemPortSecSupport = _LldpXHmRemPortSecSupport_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 3, 1, 1),
    _LldpXHmRemPortSecSupport_Type()
)
lldpXHmRemPortSecSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemPortSecSupport.setStatus("current")
_LldpXHmRemPortSecStatus_Type = TruthValue
_LldpXHmRemPortSecStatus_Object = MibTableColumn
lldpXHmRemPortSecStatus = _LldpXHmRemPortSecStatus_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 3, 1, 2),
    _LldpXHmRemPortSecStatus_Type()
)
lldpXHmRemPortSecStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemPortSecStatus.setStatus("current")
_LldpXHmRemPortSecMode_Type = LldpXHmRemPortSecModeSyntax
_LldpXHmRemPortSecMode_Object = MibTableColumn
lldpXHmRemPortSecMode = _LldpXHmRemPortSecMode_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 3, 1, 3),
    _LldpXHmRemPortSecMode_Type()
)
lldpXHmRemPortSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemPortSecMode.setStatus("current")
_LldpXHmRemPTPTable_Object = MibTable
lldpXHmRemPTPTable = _LldpXHmRemPTPTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4)
)
if mibBuilder.loadTexts:
    lldpXHmRemPTPTable.setStatus("current")
_LldpXHmRemPTPEntry_Object = MibTableRow
lldpXHmRemPTPEntry = _LldpXHmRemPTPEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1)
)
lldpXHmRemPTPEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpXHmRemPTPEntry.setStatus("current")
_LldpXHmRemPTPSupport_Type = LldpXHmRemPTPSupportSyntax
_LldpXHmRemPTPSupport_Object = MibTableColumn
lldpXHmRemPTPSupport = _LldpXHmRemPTPSupport_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 1),
    _LldpXHmRemPTPSupport_Type()
)
lldpXHmRemPTPSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemPTPSupport.setStatus("current")
_LldpXHmRemPTPStatus_Type = LldpXHmRemPTPStatusSyntax
_LldpXHmRemPTPStatus_Object = MibTableColumn
lldpXHmRemPTPStatus = _LldpXHmRemPTPStatus_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 2),
    _LldpXHmRemPTPStatus_Type()
)
lldpXHmRemPTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemPTPStatus.setStatus("current")


class _LldpXHmRemPTPSyncInterval_Type(Integer32):
    """Custom type lldpXHmRemPTPSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_LldpXHmRemPTPSyncInterval_Type.__name__ = "Integer32"
_LldpXHmRemPTPSyncInterval_Object = MibTableColumn
lldpXHmRemPTPSyncInterval = _LldpXHmRemPTPSyncInterval_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 3),
    _LldpXHmRemPTPSyncInterval_Type()
)
lldpXHmRemPTPSyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemPTPSyncInterval.setStatus("current")


class _LldpXHmRemPTPv2AnnounceInterval_Type(Integer32):
    """Custom type lldpXHmRemPTPv2AnnounceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_LldpXHmRemPTPv2AnnounceInterval_Type.__name__ = "Integer32"
_LldpXHmRemPTPv2AnnounceInterval_Object = MibTableColumn
lldpXHmRemPTPv2AnnounceInterval = _LldpXHmRemPTPv2AnnounceInterval_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 4),
    _LldpXHmRemPTPv2AnnounceInterval_Type()
)
lldpXHmRemPTPv2AnnounceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemPTPv2AnnounceInterval.setStatus("current")
_LldpXHmRemPTPv2DataTransfer_Type = LldpXHmRemPTPv2DataTransferSyntax
_LldpXHmRemPTPv2DataTransfer_Object = MibTableColumn
lldpXHmRemPTPv2DataTransfer = _LldpXHmRemPTPv2DataTransfer_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 5),
    _LldpXHmRemPTPv2DataTransfer_Type()
)
lldpXHmRemPTPv2DataTransfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemPTPv2DataTransfer.setStatus("current")
_LldpXHmRemPTPv2DelayMechanism_Type = LldpXHmRemPTPv2DelayMechanismSyntax
_LldpXHmRemPTPv2DelayMechanism_Object = MibTableColumn
lldpXHmRemPTPv2DelayMechanism = _LldpXHmRemPTPv2DelayMechanism_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 6),
    _LldpXHmRemPTPv2DelayMechanism_Type()
)
lldpXHmRemPTPv2DelayMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemPTPv2DelayMechanism.setStatus("current")


class _LldpXHmRemPTPClockValues_Type(Bits):
    """Custom type lldpXHmRemPTPClockValues based on Bits"""
    namedValues = NamedValues(
        *(("boundary", 3),
          ("grandmaster", 4),
          ("master", 1),
          ("multidomain", 5),
          ("simplemode", 6),
          ("slave", 0),
          ("transparent", 2))
    )

_LldpXHmRemPTPClockValues_Type.__name__ = "Bits"
_LldpXHmRemPTPClockValues_Object = MibTableColumn
lldpXHmRemPTPClockValues = _LldpXHmRemPTPClockValues_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 7),
    _LldpXHmRemPTPClockValues_Type()
)
lldpXHmRemPTPClockValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemPTPClockValues.setStatus("current")


class _LldpXHmRemPTPv2SubdomainNumber_Type(Integer32):
    """Custom type lldpXHmRemPTPv2SubdomainNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LldpXHmRemPTPv2SubdomainNumber_Type.__name__ = "Integer32"
_LldpXHmRemPTPv2SubdomainNumber_Object = MibTableColumn
lldpXHmRemPTPv2SubdomainNumber = _LldpXHmRemPTPv2SubdomainNumber_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 8),
    _LldpXHmRemPTPv2SubdomainNumber_Type()
)
lldpXHmRemPTPv2SubdomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemPTPv2SubdomainNumber.setStatus("current")


class _LldpXHmRemPTPv1SubdomainName_Type(OctetString):
    """Custom type lldpXHmRemPTPv1SubdomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LldpXHmRemPTPv1SubdomainName_Type.__name__ = "OctetString"
_LldpXHmRemPTPv1SubdomainName_Object = MibTableColumn
lldpXHmRemPTPv1SubdomainName = _LldpXHmRemPTPv1SubdomainName_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 9),
    _LldpXHmRemPTPv1SubdomainName_Type()
)
lldpXHmRemPTPv1SubdomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXHmRemPTPv1SubdomainName.setStatus("current")
lldpPortConfigEntry.registerAugmentions(
    ("LLDP-EXT-HM-MIB",
     "lldpXHmConfigGMRPEntry")
)
lldpXHmConfigGMRPEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpPortConfigEntry.registerAugmentions(
    ("LLDP-EXT-HM-MIB",
     "lldpXHmConfigIGMPEntry")
)
lldpXHmConfigIGMPEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpPortConfigEntry.registerAugmentions(
    ("LLDP-EXT-HM-MIB",
     "lldpXHmConfigPortSecEntry")
)
lldpXHmConfigPortSecEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpPortConfigEntry.registerAugmentions(
    ("LLDP-EXT-HM-MIB",
     "lldpXHmConfigPTPEntry")
)
lldpXHmConfigPTPEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LLDP-EXT-HM-MIB",
    **{"LldpXHmLocGMRPServiceReqSyntax": LldpXHmLocGMRPServiceReqSyntax,
       "LldpXHmLocIGMPVersionSyntax": LldpXHmLocIGMPVersionSyntax,
       "LldpXHmLocPortSecModeSyntax": LldpXHmLocPortSecModeSyntax,
       "LldpXHmLocPTPSupportSyntax": LldpXHmLocPTPSupportSyntax,
       "LldpXHmLocPTPStatusSyntax": LldpXHmLocPTPStatusSyntax,
       "LldpXHmLocPTPv2DataTransferSyntax": LldpXHmLocPTPv2DataTransferSyntax,
       "LldpXHmLocPTPv2DelayMechanismSyntax": LldpXHmLocPTPv2DelayMechanismSyntax,
       "LldpXHmRemGMRPServiceReqSyntax": LldpXHmRemGMRPServiceReqSyntax,
       "LldpXHmRemPTPv2DataTransferSyntax": LldpXHmRemPTPv2DataTransferSyntax,
       "LldpXHmRemPTPv2DelayMechanismSyntax": LldpXHmRemPTPv2DelayMechanismSyntax,
       "LldpXHmRemPTPSupportSyntax": LldpXHmRemPTPSupportSyntax,
       "LldpXHmRemPTPStatusSyntax": LldpXHmRemPTPStatusSyntax,
       "LldpXHmRemPortSecModeSyntax": LldpXHmRemPortSecModeSyntax,
       "LldpXHmRemIGMPVersionSyntax": LldpXHmRemIGMPVersionSyntax,
       "lldpXHmMIB": lldpXHmMIB,
       "lldpXHmObjects": lldpXHmObjects,
       "lldpXHmConfig": lldpXHmConfig,
       "lldpXHmConfigGMRPTable": lldpXHmConfigGMRPTable,
       "lldpXHmConfigGMRPEntry": lldpXHmConfigGMRPEntry,
       "lldpXHmConfigGMRPTxEnable": lldpXHmConfigGMRPTxEnable,
       "lldpXHmConfigIGMPTable": lldpXHmConfigIGMPTable,
       "lldpXHmConfigIGMPEntry": lldpXHmConfigIGMPEntry,
       "lldpXHmConfigIGMPTxEnable": lldpXHmConfigIGMPTxEnable,
       "lldpXHmConfigPortSecTable": lldpXHmConfigPortSecTable,
       "lldpXHmConfigPortSecEntry": lldpXHmConfigPortSecEntry,
       "lldpXHmConfigPortSecTxEnable": lldpXHmConfigPortSecTxEnable,
       "lldpXHmConfigPTPTable": lldpXHmConfigPTPTable,
       "lldpXHmConfigPTPEntry": lldpXHmConfigPTPEntry,
       "lldpXHmConfigPTPTxEnable": lldpXHmConfigPTPTxEnable,
       "lldpXHmLocalData": lldpXHmLocalData,
       "lldpXHmLocGMRPTable": lldpXHmLocGMRPTable,
       "lldpXHmLocGMRPEntry": lldpXHmLocGMRPEntry,
       "lldpXHmLocGMRPSupport": lldpXHmLocGMRPSupport,
       "lldpXHmLocGMRPStatus": lldpXHmLocGMRPStatus,
       "lldpXHmLocGMRPServiceReq": lldpXHmLocGMRPServiceReq,
       "lldpXHmLocIGMPTable": lldpXHmLocIGMPTable,
       "lldpXHmLocIGMPEntry": lldpXHmLocIGMPEntry,
       "lldpXHmLocIGMPSupport": lldpXHmLocIGMPSupport,
       "lldpXHmLocIGMPStatus": lldpXHmLocIGMPStatus,
       "lldpXHmLocIGMPVersion": lldpXHmLocIGMPVersion,
       "lldpXHmLocPortSecTable": lldpXHmLocPortSecTable,
       "lldpXHmLocPortSecEntry": lldpXHmLocPortSecEntry,
       "lldpXHmLocPortSecSupport": lldpXHmLocPortSecSupport,
       "lldpXHmLocPortSecStatus": lldpXHmLocPortSecStatus,
       "lldpXHmLocPortSecMode": lldpXHmLocPortSecMode,
       "lldpXHmLocPTPTable": lldpXHmLocPTPTable,
       "lldpXHmLocPTPEntry": lldpXHmLocPTPEntry,
       "lldpXHmLocPTPSupport": lldpXHmLocPTPSupport,
       "lldpXHmLocPTPStatus": lldpXHmLocPTPStatus,
       "lldpXHmLocPTPSyncInterval": lldpXHmLocPTPSyncInterval,
       "lldpXHmLocPTPv2AnnounceInterval": lldpXHmLocPTPv2AnnounceInterval,
       "lldpXHmLocPTPv2DataTransfer": lldpXHmLocPTPv2DataTransfer,
       "lldpXHmLocPTPv2DelayMechanism": lldpXHmLocPTPv2DelayMechanism,
       "lldpXHmLocPTPClockValues": lldpXHmLocPTPClockValues,
       "lldpXHmLocPTPv2SubdomainNumber": lldpXHmLocPTPv2SubdomainNumber,
       "lldpXHmLocPTPv1SubdomainName": lldpXHmLocPTPv1SubdomainName,
       "lldpXHmRemoteData": lldpXHmRemoteData,
       "lldpXHmRemGMRPTable": lldpXHmRemGMRPTable,
       "lldpXHmRemGMRPEntry": lldpXHmRemGMRPEntry,
       "lldpXHmRemGMRPSupport": lldpXHmRemGMRPSupport,
       "lldpXHmRemGMRPStatus": lldpXHmRemGMRPStatus,
       "lldpXHmRemGMRPServiceReq": lldpXHmRemGMRPServiceReq,
       "lldpXHmRemIGMPTable": lldpXHmRemIGMPTable,
       "lldpXHmRemIGMPEntry": lldpXHmRemIGMPEntry,
       "lldpXHmRemIGMPSupport": lldpXHmRemIGMPSupport,
       "lldpXHmRemIGMPStatus": lldpXHmRemIGMPStatus,
       "lldpXHmRemIGMPVersion": lldpXHmRemIGMPVersion,
       "lldpXHmRemPortSecTable": lldpXHmRemPortSecTable,
       "lldpXHmRemPortSecEntry": lldpXHmRemPortSecEntry,
       "lldpXHmRemPortSecSupport": lldpXHmRemPortSecSupport,
       "lldpXHmRemPortSecStatus": lldpXHmRemPortSecStatus,
       "lldpXHmRemPortSecMode": lldpXHmRemPortSecMode,
       "lldpXHmRemPTPTable": lldpXHmRemPTPTable,
       "lldpXHmRemPTPEntry": lldpXHmRemPTPEntry,
       "lldpXHmRemPTPSupport": lldpXHmRemPTPSupport,
       "lldpXHmRemPTPStatus": lldpXHmRemPTPStatus,
       "lldpXHmRemPTPSyncInterval": lldpXHmRemPTPSyncInterval,
       "lldpXHmRemPTPv2AnnounceInterval": lldpXHmRemPTPv2AnnounceInterval,
       "lldpXHmRemPTPv2DataTransfer": lldpXHmRemPTPv2DataTransfer,
       "lldpXHmRemPTPv2DelayMechanism": lldpXHmRemPTPv2DelayMechanism,
       "lldpXHmRemPTPClockValues": lldpXHmRemPTPClockValues,
       "lldpXHmRemPTPv2SubdomainNumber": lldpXHmRemPTPv2SubdomainNumber,
       "lldpXHmRemPTPv1SubdomainName": lldpXHmRemPTPv1SubdomainName}
)
