# SNMP MIB module (IBMHPRNCL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBMHPRNCL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:53 2024
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
_Hpr_ObjectIdentity = ObjectIdentity
hpr = _Hpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 10)
)
_IbmHprNcl_ObjectIdentity = ObjectIdentity
ibmHprNcl = _IbmHprNcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3)
)
_IbmHprNclGlobe_ObjectIdentity = ObjectIdentity
ibmHprNclGlobe = _IbmHprNclGlobe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 1)
)


class _IbmHprNclGlobeCtrState_Type(Integer32):
    """Custom type ibmHprNclGlobeCtrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_IbmHprNclGlobeCtrState_Type.__name__ = "Integer32"
_IbmHprNclGlobeCtrState_Object = MibScalar
ibmHprNclGlobeCtrState = _IbmHprNclGlobeCtrState_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 1, 1),
    _IbmHprNclGlobeCtrState_Type()
)
ibmHprNclGlobeCtrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmHprNclGlobeCtrState.setStatus("mandatory")
_IbmHprNclGlobeCtrStateTime_Type = TimeTicks
_IbmHprNclGlobeCtrStateTime_Object = MibScalar
ibmHprNclGlobeCtrStateTime = _IbmHprNclGlobeCtrStateTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 1, 2),
    _IbmHprNclGlobeCtrStateTime_Type()
)
ibmHprNclGlobeCtrStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclGlobeCtrStateTime.setStatus("mandatory")
_IbmHprNclGlobeAssignAnrs_Type = Counter32
_IbmHprNclGlobeAssignAnrs_Object = MibScalar
ibmHprNclGlobeAssignAnrs = _IbmHprNclGlobeAssignAnrs_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 1, 3),
    _IbmHprNclGlobeAssignAnrs_Type()
)
ibmHprNclGlobeAssignAnrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclGlobeAssignAnrs.setStatus("mandatory")
_IbmHprNclTable_Object = MibTable
ibmHprNclTable = _IbmHprNclTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2)
)
if mibBuilder.loadTexts:
    ibmHprNclTable.setStatus("mandatory")
_IbmHprNclEntry_Object = MibTableRow
ibmHprNclEntry = _IbmHprNclEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1)
)
ibmHprNclEntry.setIndexNames(
    (0, "IBMHPRNCL-MIB", "ibmHprNclEnvId"),
)
if mibBuilder.loadTexts:
    ibmHprNclEntry.setStatus("mandatory")
_IbmHprNclEnvId_Type = Gauge32
_IbmHprNclEnvId_Object = MibTableColumn
ibmHprNclEnvId = _IbmHprNclEnvId_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 1),
    _IbmHprNclEnvId_Type()
)
ibmHprNclEnvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclEnvId.setStatus("mandatory")
_IbmHprNclDlcRecvNetFrames_Type = Counter32
_IbmHprNclDlcRecvNetFrames_Object = MibTableColumn
ibmHprNclDlcRecvNetFrames = _IbmHprNclDlcRecvNetFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 2),
    _IbmHprNclDlcRecvNetFrames_Type()
)
ibmHprNclDlcRecvNetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcRecvNetFrames.setStatus("mandatory")
_IbmHprNclDlcRecvHiFrames_Type = Counter32
_IbmHprNclDlcRecvHiFrames_Object = MibTableColumn
ibmHprNclDlcRecvHiFrames = _IbmHprNclDlcRecvHiFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 3),
    _IbmHprNclDlcRecvHiFrames_Type()
)
ibmHprNclDlcRecvHiFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcRecvHiFrames.setStatus("mandatory")
_IbmHprNclDlcRecvMedFrames_Type = Counter32
_IbmHprNclDlcRecvMedFrames_Object = MibTableColumn
ibmHprNclDlcRecvMedFrames = _IbmHprNclDlcRecvMedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 4),
    _IbmHprNclDlcRecvMedFrames_Type()
)
ibmHprNclDlcRecvMedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcRecvMedFrames.setStatus("mandatory")
_IbmHprNclDlcRecvLoFrames_Type = Counter32
_IbmHprNclDlcRecvLoFrames_Object = MibTableColumn
ibmHprNclDlcRecvLoFrames = _IbmHprNclDlcRecvLoFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 5),
    _IbmHprNclDlcRecvLoFrames_Type()
)
ibmHprNclDlcRecvLoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcRecvLoFrames.setStatus("mandatory")
_IbmHprNclDlcRecvNetBytes_Type = Counter32
_IbmHprNclDlcRecvNetBytes_Object = MibTableColumn
ibmHprNclDlcRecvNetBytes = _IbmHprNclDlcRecvNetBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 6),
    _IbmHprNclDlcRecvNetBytes_Type()
)
ibmHprNclDlcRecvNetBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcRecvNetBytes.setStatus("mandatory")
_IbmHprNclDlcRecvHiBytes_Type = Counter32
_IbmHprNclDlcRecvHiBytes_Object = MibTableColumn
ibmHprNclDlcRecvHiBytes = _IbmHprNclDlcRecvHiBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 7),
    _IbmHprNclDlcRecvHiBytes_Type()
)
ibmHprNclDlcRecvHiBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcRecvHiBytes.setStatus("mandatory")
_IbmHprNclDlcRecvMedBytes_Type = Counter32
_IbmHprNclDlcRecvMedBytes_Object = MibTableColumn
ibmHprNclDlcRecvMedBytes = _IbmHprNclDlcRecvMedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 8),
    _IbmHprNclDlcRecvMedBytes_Type()
)
ibmHprNclDlcRecvMedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcRecvMedBytes.setStatus("mandatory")
_IbmHprNclDlcRecvLoBytes_Type = Counter32
_IbmHprNclDlcRecvLoBytes_Object = MibTableColumn
ibmHprNclDlcRecvLoBytes = _IbmHprNclDlcRecvLoBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 9),
    _IbmHprNclDlcRecvLoBytes_Type()
)
ibmHprNclDlcRecvLoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcRecvLoBytes.setStatus("mandatory")
_IbmHprNclDlcRecvAnrErrors_Type = Counter32
_IbmHprNclDlcRecvAnrErrors_Object = MibTableColumn
ibmHprNclDlcRecvAnrErrors = _IbmHprNclDlcRecvAnrErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 10),
    _IbmHprNclDlcRecvAnrErrors_Type()
)
ibmHprNclDlcRecvAnrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcRecvAnrErrors.setStatus("mandatory")
_IbmHprNclDlcSendNetFrames_Type = Counter32
_IbmHprNclDlcSendNetFrames_Object = MibTableColumn
ibmHprNclDlcSendNetFrames = _IbmHprNclDlcSendNetFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 11),
    _IbmHprNclDlcSendNetFrames_Type()
)
ibmHprNclDlcSendNetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcSendNetFrames.setStatus("mandatory")
_IbmHprNclDlcSendHiFrames_Type = Counter32
_IbmHprNclDlcSendHiFrames_Object = MibTableColumn
ibmHprNclDlcSendHiFrames = _IbmHprNclDlcSendHiFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 12),
    _IbmHprNclDlcSendHiFrames_Type()
)
ibmHprNclDlcSendHiFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcSendHiFrames.setStatus("mandatory")
_IbmHprNclDlcSendMedFrames_Type = Counter32
_IbmHprNclDlcSendMedFrames_Object = MibTableColumn
ibmHprNclDlcSendMedFrames = _IbmHprNclDlcSendMedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 13),
    _IbmHprNclDlcSendMedFrames_Type()
)
ibmHprNclDlcSendMedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcSendMedFrames.setStatus("mandatory")
_IbmHprNclDlcSendLoFrames_Type = Counter32
_IbmHprNclDlcSendLoFrames_Object = MibTableColumn
ibmHprNclDlcSendLoFrames = _IbmHprNclDlcSendLoFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 14),
    _IbmHprNclDlcSendLoFrames_Type()
)
ibmHprNclDlcSendLoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcSendLoFrames.setStatus("mandatory")
_IbmHprNclDlcSendNetBytes_Type = Counter32
_IbmHprNclDlcSendNetBytes_Object = MibTableColumn
ibmHprNclDlcSendNetBytes = _IbmHprNclDlcSendNetBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 15),
    _IbmHprNclDlcSendNetBytes_Type()
)
ibmHprNclDlcSendNetBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcSendNetBytes.setStatus("mandatory")
_IbmHprNclDlcSendHiBytes_Type = Counter32
_IbmHprNclDlcSendHiBytes_Object = MibTableColumn
ibmHprNclDlcSendHiBytes = _IbmHprNclDlcSendHiBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 16),
    _IbmHprNclDlcSendHiBytes_Type()
)
ibmHprNclDlcSendHiBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcSendHiBytes.setStatus("mandatory")
_IbmHprNclDlcSendMedBytes_Type = Counter32
_IbmHprNclDlcSendMedBytes_Object = MibTableColumn
ibmHprNclDlcSendMedBytes = _IbmHprNclDlcSendMedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 17),
    _IbmHprNclDlcSendMedBytes_Type()
)
ibmHprNclDlcSendMedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcSendMedBytes.setStatus("mandatory")
_IbmHprNclDlcSendLoBytes_Type = Counter32
_IbmHprNclDlcSendLoBytes_Object = MibTableColumn
ibmHprNclDlcSendLoBytes = _IbmHprNclDlcSendLoBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 18),
    _IbmHprNclDlcSendLoBytes_Type()
)
ibmHprNclDlcSendLoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclDlcSendLoBytes.setStatus("mandatory")
_IbmHprNclRtpRecvNetFrames_Type = Counter32
_IbmHprNclRtpRecvNetFrames_Object = MibTableColumn
ibmHprNclRtpRecvNetFrames = _IbmHprNclRtpRecvNetFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 19),
    _IbmHprNclRtpRecvNetFrames_Type()
)
ibmHprNclRtpRecvNetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpRecvNetFrames.setStatus("mandatory")
_IbmHprNclRtpRecvHiFrames_Type = Counter32
_IbmHprNclRtpRecvHiFrames_Object = MibTableColumn
ibmHprNclRtpRecvHiFrames = _IbmHprNclRtpRecvHiFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 20),
    _IbmHprNclRtpRecvHiFrames_Type()
)
ibmHprNclRtpRecvHiFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpRecvHiFrames.setStatus("mandatory")
_IbmHprNclRtpRecvMedFrames_Type = Counter32
_IbmHprNclRtpRecvMedFrames_Object = MibTableColumn
ibmHprNclRtpRecvMedFrames = _IbmHprNclRtpRecvMedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 21),
    _IbmHprNclRtpRecvMedFrames_Type()
)
ibmHprNclRtpRecvMedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpRecvMedFrames.setStatus("mandatory")
_IbmHprNclRtpRecvLoFrames_Type = Counter32
_IbmHprNclRtpRecvLoFrames_Object = MibTableColumn
ibmHprNclRtpRecvLoFrames = _IbmHprNclRtpRecvLoFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 22),
    _IbmHprNclRtpRecvLoFrames_Type()
)
ibmHprNclRtpRecvLoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpRecvLoFrames.setStatus("mandatory")
_IbmHprNclRtpRecvNetBytes_Type = Counter32
_IbmHprNclRtpRecvNetBytes_Object = MibTableColumn
ibmHprNclRtpRecvNetBytes = _IbmHprNclRtpRecvNetBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 23),
    _IbmHprNclRtpRecvNetBytes_Type()
)
ibmHprNclRtpRecvNetBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpRecvNetBytes.setStatus("mandatory")
_IbmHprNclRtpRecvHiBytes_Type = Counter32
_IbmHprNclRtpRecvHiBytes_Object = MibTableColumn
ibmHprNclRtpRecvHiBytes = _IbmHprNclRtpRecvHiBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 24),
    _IbmHprNclRtpRecvHiBytes_Type()
)
ibmHprNclRtpRecvHiBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpRecvHiBytes.setStatus("mandatory")
_IbmHprNclRtpRecvMedBytes_Type = Counter32
_IbmHprNclRtpRecvMedBytes_Object = MibTableColumn
ibmHprNclRtpRecvMedBytes = _IbmHprNclRtpRecvMedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 25),
    _IbmHprNclRtpRecvMedBytes_Type()
)
ibmHprNclRtpRecvMedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpRecvMedBytes.setStatus("mandatory")
_IbmHprNclRtpRecvLoBytes_Type = Counter32
_IbmHprNclRtpRecvLoBytes_Object = MibTableColumn
ibmHprNclRtpRecvLoBytes = _IbmHprNclRtpRecvLoBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 26),
    _IbmHprNclRtpRecvLoBytes_Type()
)
ibmHprNclRtpRecvLoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpRecvLoBytes.setStatus("mandatory")
_IbmHprNclRtpRecvAnrErrors_Type = Counter32
_IbmHprNclRtpRecvAnrErrors_Object = MibTableColumn
ibmHprNclRtpRecvAnrErrors = _IbmHprNclRtpRecvAnrErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 27),
    _IbmHprNclRtpRecvAnrErrors_Type()
)
ibmHprNclRtpRecvAnrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpRecvAnrErrors.setStatus("mandatory")
_IbmHprNclRtpSendNetFrames_Type = Counter32
_IbmHprNclRtpSendNetFrames_Object = MibTableColumn
ibmHprNclRtpSendNetFrames = _IbmHprNclRtpSendNetFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 28),
    _IbmHprNclRtpSendNetFrames_Type()
)
ibmHprNclRtpSendNetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpSendNetFrames.setStatus("mandatory")
_IbmHprNclRtpSendHiFrames_Type = Counter32
_IbmHprNclRtpSendHiFrames_Object = MibTableColumn
ibmHprNclRtpSendHiFrames = _IbmHprNclRtpSendHiFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 29),
    _IbmHprNclRtpSendHiFrames_Type()
)
ibmHprNclRtpSendHiFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpSendHiFrames.setStatus("mandatory")
_IbmHprNclRtpSendMedFrames_Type = Counter32
_IbmHprNclRtpSendMedFrames_Object = MibTableColumn
ibmHprNclRtpSendMedFrames = _IbmHprNclRtpSendMedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 30),
    _IbmHprNclRtpSendMedFrames_Type()
)
ibmHprNclRtpSendMedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpSendMedFrames.setStatus("mandatory")
_IbmHprNclRtpSendLoFrames_Type = Counter32
_IbmHprNclRtpSendLoFrames_Object = MibTableColumn
ibmHprNclRtpSendLoFrames = _IbmHprNclRtpSendLoFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 31),
    _IbmHprNclRtpSendLoFrames_Type()
)
ibmHprNclRtpSendLoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpSendLoFrames.setStatus("mandatory")
_IbmHprNclRtpSendNetBytes_Type = Counter32
_IbmHprNclRtpSendNetBytes_Object = MibTableColumn
ibmHprNclRtpSendNetBytes = _IbmHprNclRtpSendNetBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 32),
    _IbmHprNclRtpSendNetBytes_Type()
)
ibmHprNclRtpSendNetBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpSendNetBytes.setStatus("mandatory")
_IbmHprNclRtpSendHiBytes_Type = Counter32
_IbmHprNclRtpSendHiBytes_Object = MibTableColumn
ibmHprNclRtpSendHiBytes = _IbmHprNclRtpSendHiBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 33),
    _IbmHprNclRtpSendHiBytes_Type()
)
ibmHprNclRtpSendHiBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpSendHiBytes.setStatus("mandatory")
_IbmHprNclRtpSendMedBytes_Type = Counter32
_IbmHprNclRtpSendMedBytes_Object = MibTableColumn
ibmHprNclRtpSendMedBytes = _IbmHprNclRtpSendMedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 34),
    _IbmHprNclRtpSendMedBytes_Type()
)
ibmHprNclRtpSendMedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpSendMedBytes.setStatus("mandatory")
_IbmHprNclRtpSendLoBytes_Type = Counter32
_IbmHprNclRtpSendLoBytes_Object = MibTableColumn
ibmHprNclRtpSendLoBytes = _IbmHprNclRtpSendLoBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 35),
    _IbmHprNclRtpSendLoBytes_Type()
)
ibmHprNclRtpSendLoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclRtpSendLoBytes.setStatus("mandatory")
_IbmHprNclInterSendNetFrames_Type = Counter32
_IbmHprNclInterSendNetFrames_Object = MibTableColumn
ibmHprNclInterSendNetFrames = _IbmHprNclInterSendNetFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 36),
    _IbmHprNclInterSendNetFrames_Type()
)
ibmHprNclInterSendNetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclInterSendNetFrames.setStatus("mandatory")
_IbmHprNclInterSendHiFrames_Type = Counter32
_IbmHprNclInterSendHiFrames_Object = MibTableColumn
ibmHprNclInterSendHiFrames = _IbmHprNclInterSendHiFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 37),
    _IbmHprNclInterSendHiFrames_Type()
)
ibmHprNclInterSendHiFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclInterSendHiFrames.setStatus("mandatory")
_IbmHprNclInterSendMedFrames_Type = Counter32
_IbmHprNclInterSendMedFrames_Object = MibTableColumn
ibmHprNclInterSendMedFrames = _IbmHprNclInterSendMedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 38),
    _IbmHprNclInterSendMedFrames_Type()
)
ibmHprNclInterSendMedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclInterSendMedFrames.setStatus("mandatory")
_IbmHprNclInterSendLoFrames_Type = Counter32
_IbmHprNclInterSendLoFrames_Object = MibTableColumn
ibmHprNclInterSendLoFrames = _IbmHprNclInterSendLoFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 39),
    _IbmHprNclInterSendLoFrames_Type()
)
ibmHprNclInterSendLoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclInterSendLoFrames.setStatus("mandatory")
_IbmHprNclInterSendNetBytes_Type = Counter32
_IbmHprNclInterSendNetBytes_Object = MibTableColumn
ibmHprNclInterSendNetBytes = _IbmHprNclInterSendNetBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 40),
    _IbmHprNclInterSendNetBytes_Type()
)
ibmHprNclInterSendNetBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclInterSendNetBytes.setStatus("mandatory")
_IbmHprNclInterSendHiBytes_Type = Counter32
_IbmHprNclInterSendHiBytes_Object = MibTableColumn
ibmHprNclInterSendHiBytes = _IbmHprNclInterSendHiBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 41),
    _IbmHprNclInterSendHiBytes_Type()
)
ibmHprNclInterSendHiBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclInterSendHiBytes.setStatus("mandatory")
_IbmHprNclInterSendMedBytes_Type = Counter32
_IbmHprNclInterSendMedBytes_Object = MibTableColumn
ibmHprNclInterSendMedBytes = _IbmHprNclInterSendMedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 42),
    _IbmHprNclInterSendMedBytes_Type()
)
ibmHprNclInterSendMedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclInterSendMedBytes.setStatus("mandatory")
_IbmHprNclInterSendLoBytes_Type = Counter32
_IbmHprNclInterSendLoBytes_Object = MibTableColumn
ibmHprNclInterSendLoBytes = _IbmHprNclInterSendLoBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 2, 1, 43),
    _IbmHprNclInterSendLoBytes_Type()
)
ibmHprNclInterSendLoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmHprNclInterSendLoBytes.setStatus("mandatory")
_IbmHprNclCompliances_ObjectIdentity = ObjectIdentity
ibmHprNclCompliances = _IbmHprNclCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 3)
)
_IbmHprNclConfGroups_ObjectIdentity = ObjectIdentity
ibmHprNclConfGroups = _IbmHprNclConfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 10, 3, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBMHPRNCL-MIB",
    **{"ibm": ibm,
       "ibmArchitecture": ibmArchitecture,
       "hpr": hpr,
       "ibmHprNcl": ibmHprNcl,
       "ibmHprNclGlobe": ibmHprNclGlobe,
       "ibmHprNclGlobeCtrState": ibmHprNclGlobeCtrState,
       "ibmHprNclGlobeCtrStateTime": ibmHprNclGlobeCtrStateTime,
       "ibmHprNclGlobeAssignAnrs": ibmHprNclGlobeAssignAnrs,
       "ibmHprNclTable": ibmHprNclTable,
       "ibmHprNclEntry": ibmHprNclEntry,
       "ibmHprNclEnvId": ibmHprNclEnvId,
       "ibmHprNclDlcRecvNetFrames": ibmHprNclDlcRecvNetFrames,
       "ibmHprNclDlcRecvHiFrames": ibmHprNclDlcRecvHiFrames,
       "ibmHprNclDlcRecvMedFrames": ibmHprNclDlcRecvMedFrames,
       "ibmHprNclDlcRecvLoFrames": ibmHprNclDlcRecvLoFrames,
       "ibmHprNclDlcRecvNetBytes": ibmHprNclDlcRecvNetBytes,
       "ibmHprNclDlcRecvHiBytes": ibmHprNclDlcRecvHiBytes,
       "ibmHprNclDlcRecvMedBytes": ibmHprNclDlcRecvMedBytes,
       "ibmHprNclDlcRecvLoBytes": ibmHprNclDlcRecvLoBytes,
       "ibmHprNclDlcRecvAnrErrors": ibmHprNclDlcRecvAnrErrors,
       "ibmHprNclDlcSendNetFrames": ibmHprNclDlcSendNetFrames,
       "ibmHprNclDlcSendHiFrames": ibmHprNclDlcSendHiFrames,
       "ibmHprNclDlcSendMedFrames": ibmHprNclDlcSendMedFrames,
       "ibmHprNclDlcSendLoFrames": ibmHprNclDlcSendLoFrames,
       "ibmHprNclDlcSendNetBytes": ibmHprNclDlcSendNetBytes,
       "ibmHprNclDlcSendHiBytes": ibmHprNclDlcSendHiBytes,
       "ibmHprNclDlcSendMedBytes": ibmHprNclDlcSendMedBytes,
       "ibmHprNclDlcSendLoBytes": ibmHprNclDlcSendLoBytes,
       "ibmHprNclRtpRecvNetFrames": ibmHprNclRtpRecvNetFrames,
       "ibmHprNclRtpRecvHiFrames": ibmHprNclRtpRecvHiFrames,
       "ibmHprNclRtpRecvMedFrames": ibmHprNclRtpRecvMedFrames,
       "ibmHprNclRtpRecvLoFrames": ibmHprNclRtpRecvLoFrames,
       "ibmHprNclRtpRecvNetBytes": ibmHprNclRtpRecvNetBytes,
       "ibmHprNclRtpRecvHiBytes": ibmHprNclRtpRecvHiBytes,
       "ibmHprNclRtpRecvMedBytes": ibmHprNclRtpRecvMedBytes,
       "ibmHprNclRtpRecvLoBytes": ibmHprNclRtpRecvLoBytes,
       "ibmHprNclRtpRecvAnrErrors": ibmHprNclRtpRecvAnrErrors,
       "ibmHprNclRtpSendNetFrames": ibmHprNclRtpSendNetFrames,
       "ibmHprNclRtpSendHiFrames": ibmHprNclRtpSendHiFrames,
       "ibmHprNclRtpSendMedFrames": ibmHprNclRtpSendMedFrames,
       "ibmHprNclRtpSendLoFrames": ibmHprNclRtpSendLoFrames,
       "ibmHprNclRtpSendNetBytes": ibmHprNclRtpSendNetBytes,
       "ibmHprNclRtpSendHiBytes": ibmHprNclRtpSendHiBytes,
       "ibmHprNclRtpSendMedBytes": ibmHprNclRtpSendMedBytes,
       "ibmHprNclRtpSendLoBytes": ibmHprNclRtpSendLoBytes,
       "ibmHprNclInterSendNetFrames": ibmHprNclInterSendNetFrames,
       "ibmHprNclInterSendHiFrames": ibmHprNclInterSendHiFrames,
       "ibmHprNclInterSendMedFrames": ibmHprNclInterSendMedFrames,
       "ibmHprNclInterSendLoFrames": ibmHprNclInterSendLoFrames,
       "ibmHprNclInterSendNetBytes": ibmHprNclInterSendNetBytes,
       "ibmHprNclInterSendHiBytes": ibmHprNclInterSendHiBytes,
       "ibmHprNclInterSendMedBytes": ibmHprNclInterSendMedBytes,
       "ibmHprNclInterSendLoBytes": ibmHprNclInterSendLoBytes,
       "ibmHprNclCompliances": ibmHprNclCompliances,
       "ibmHprNclConfGroups": ibmHprNclConfGroups}
)
