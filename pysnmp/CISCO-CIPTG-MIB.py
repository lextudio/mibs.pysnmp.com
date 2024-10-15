# SNMP MIB module (CISCO-CIPTG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CIPTG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:26 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SAPType,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "SAPType")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCipTgMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 73)
)
ciscoCipTgMIB.setRevisions(
        ("1999-01-25 00:00",
         "1998-01-06 00:00",
         "1997-02-09 00:00",
         "1997-03-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ChannelTgName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class ChannelTgToken(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )



# MIB Managed Objects in the order of their OIDs

_CipTgObjects_ObjectIdentity = ObjectIdentity
cipTgObjects = _CipTgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1)
)
_CipTgLlc_ObjectIdentity = ObjectIdentity
cipTgLlc = _CipTgLlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1)
)
_CipTgLlcAdminTable_Object = MibTable
cipTgLlcAdminTable = _CipTgLlcAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cipTgLlcAdminTable.setStatus("current")
_CipTgLlcAdminEntry_Object = MibTableRow
cipTgLlcAdminEntry = _CipTgLlcAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1)
)
cipTgLlcAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CIPTG-MIB", "cipTgLlcAdminName"),
)
if mibBuilder.loadTexts:
    cipTgLlcAdminEntry.setStatus("current")
_CipTgLlcAdminName_Type = ChannelTgName
_CipTgLlcAdminName_Object = MibTableColumn
cipTgLlcAdminName = _CipTgLlcAdminName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 1),
    _CipTgLlcAdminName_Type()
)
cipTgLlcAdminName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipTgLlcAdminName.setStatus("current")


class _CipTgLlcAdminLanType_Type(Integer32):
    """Custom type cipTgLlcAdminLanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fddi", 3),
          ("iso88023csmacd", 1),
          ("iso88025tokenRing", 2))
    )


_CipTgLlcAdminLanType_Type.__name__ = "Integer32"
_CipTgLlcAdminLanType_Object = MibTableColumn
cipTgLlcAdminLanType = _CipTgLlcAdminLanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 2),
    _CipTgLlcAdminLanType_Type()
)
cipTgLlcAdminLanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipTgLlcAdminLanType.setStatus("current")


class _CipTgLlcAdminAdaptNo_Type(Integer32):
    """Custom type cipTgLlcAdminAdaptNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CipTgLlcAdminAdaptNo_Type.__name__ = "Integer32"
_CipTgLlcAdminAdaptNo_Object = MibTableColumn
cipTgLlcAdminAdaptNo = _CipTgLlcAdminAdaptNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 3),
    _CipTgLlcAdminAdaptNo_Type()
)
cipTgLlcAdminAdaptNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipTgLlcAdminAdaptNo.setStatus("current")
_CipTgLlcAdminLSAP_Type = SAPType
_CipTgLlcAdminLSAP_Object = MibTableColumn
cipTgLlcAdminLSAP = _CipTgLlcAdminLSAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 4),
    _CipTgLlcAdminLSAP_Type()
)
cipTgLlcAdminLSAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipTgLlcAdminLSAP.setStatus("current")
_CipTgLlcAdminRMAC_Type = MacAddress
_CipTgLlcAdminRMAC_Object = MibTableColumn
cipTgLlcAdminRMAC = _CipTgLlcAdminRMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 5),
    _CipTgLlcAdminRMAC_Type()
)
cipTgLlcAdminRMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipTgLlcAdminRMAC.setStatus("current")


class _CipTgLlcAdminRSAP_Type(SAPType):
    """Custom type cipTgLlcAdminRSAP based on SAPType"""
    defaultValue = 4


_CipTgLlcAdminRSAP_Object = MibTableColumn
cipTgLlcAdminRSAP = _CipTgLlcAdminRSAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 6),
    _CipTgLlcAdminRSAP_Type()
)
cipTgLlcAdminRSAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipTgLlcAdminRSAP.setStatus("current")
_CipTgLlcAdminRowStatus_Type = RowStatus
_CipTgLlcAdminRowStatus_Object = MibTableColumn
cipTgLlcAdminRowStatus = _CipTgLlcAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 7),
    _CipTgLlcAdminRowStatus_Type()
)
cipTgLlcAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipTgLlcAdminRowStatus.setStatus("current")
_CipTgLlcOperTable_Object = MibTable
cipTgLlcOperTable = _CipTgLlcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cipTgLlcOperTable.setStatus("current")
_CipTgLlcOperEntry_Object = MibTableRow
cipTgLlcOperEntry = _CipTgLlcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cipTgLlcOperEntry.setStatus("current")


class _CipTgLlcOperState_Type(Integer32):
    """Custom type cipTgLlcOperState based on Integer32"""
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
        *(("active", 7),
          ("contactPending", 6),
          ("locatePeer", 3),
          ("negotiation", 5),
          ("peerLocated", 4),
          ("reset", 2),
          ("shutdown", 1))
    )


_CipTgLlcOperState_Type.__name__ = "Integer32"
_CipTgLlcOperState_Object = MibTableColumn
cipTgLlcOperState = _CipTgLlcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 1),
    _CipTgLlcOperState_Type()
)
cipTgLlcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperState.setStatus("current")
_CipTgLlcOperTGN_Type = Integer32
_CipTgLlcOperTGN_Object = MibTableColumn
cipTgLlcOperTGN = _CipTgLlcOperTGN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 2),
    _CipTgLlcOperTGN_Type()
)
cipTgLlcOperTGN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperTGN.setStatus("current")


class _CipTgLlcOperLocalCP_Type(DisplayString):
    """Custom type cipTgLlcOperLocalCP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CipTgLlcOperLocalCP_Type.__name__ = "DisplayString"
_CipTgLlcOperLocalCP_Object = MibTableColumn
cipTgLlcOperLocalCP = _CipTgLlcOperLocalCP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 3),
    _CipTgLlcOperLocalCP_Type()
)
cipTgLlcOperLocalCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperLocalCP.setStatus("current")


class _CipTgLlcOperRemoteCP_Type(DisplayString):
    """Custom type cipTgLlcOperRemoteCP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CipTgLlcOperRemoteCP_Type.__name__ = "DisplayString"
_CipTgLlcOperRemoteCP_Object = MibTableColumn
cipTgLlcOperRemoteCP = _CipTgLlcOperRemoteCP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 4),
    _CipTgLlcOperRemoteCP_Type()
)
cipTgLlcOperRemoteCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperRemoteCP.setStatus("current")
_CipTgLlcOperMaxIn_Type = Integer32
_CipTgLlcOperMaxIn_Object = MibTableColumn
cipTgLlcOperMaxIn = _CipTgLlcOperMaxIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 5),
    _CipTgLlcOperMaxIn_Type()
)
cipTgLlcOperMaxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperMaxIn.setStatus("current")
_CipTgLlcOperMaxOut_Type = Integer32
_CipTgLlcOperMaxOut_Object = MibTableColumn
cipTgLlcOperMaxOut = _CipTgLlcOperMaxOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 6),
    _CipTgLlcOperMaxOut_Type()
)
cipTgLlcOperMaxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperMaxOut.setStatus("current")
_CipTgLlcOperHpr_Type = TruthValue
_CipTgLlcOperHpr_Object = MibTableColumn
cipTgLlcOperHpr = _CipTgLlcOperHpr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 7),
    _CipTgLlcOperHpr_Type()
)
cipTgLlcOperHpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperHpr.setStatus("current")
_CipTgLlcOperHprLSAP_Type = SAPType
_CipTgLlcOperHprLSAP_Object = MibTableColumn
cipTgLlcOperHprLSAP = _CipTgLlcOperHprLSAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 8),
    _CipTgLlcOperHprLSAP_Type()
)
cipTgLlcOperHprLSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperHprLSAP.setStatus("current")
_CipTgLlcOperHprRSAP_Type = SAPType
_CipTgLlcOperHprRSAP_Object = MibTableColumn
cipTgLlcOperHprRSAP = _CipTgLlcOperHprRSAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 9),
    _CipTgLlcOperHprRSAP_Type()
)
cipTgLlcOperHprRSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperHprRSAP.setStatus("current")


class _CipTgLlcOperRIF_Type(OctetString):
    """Custom type cipTgLlcOperRIF based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_CipTgLlcOperRIF_Type.__name__ = "OctetString"
_CipTgLlcOperRIF_Object = MibTableColumn
cipTgLlcOperRIF = _CipTgLlcOperRIF_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 10),
    _CipTgLlcOperRIF_Type()
)
cipTgLlcOperRIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperRIF.setStatus("current")
_CipTgLlcOperLocalVcToken_Type = ChannelTgToken
_CipTgLlcOperLocalVcToken_Object = MibTableColumn
cipTgLlcOperLocalVcToken = _CipTgLlcOperLocalVcToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 11),
    _CipTgLlcOperLocalVcToken_Type()
)
cipTgLlcOperLocalVcToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperLocalVcToken.setStatus("current")
_CipTgLlcOperRemoteVcToken_Type = ChannelTgToken
_CipTgLlcOperRemoteVcToken_Object = MibTableColumn
cipTgLlcOperRemoteVcToken = _CipTgLlcOperRemoteVcToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 12),
    _CipTgLlcOperRemoteVcToken_Type()
)
cipTgLlcOperRemoteVcToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperRemoteVcToken.setStatus("current")
_CipTgLlcOperLocalConnToken_Type = ChannelTgToken
_CipTgLlcOperLocalConnToken_Object = MibTableColumn
cipTgLlcOperLocalConnToken = _CipTgLlcOperLocalConnToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 13),
    _CipTgLlcOperLocalConnToken_Type()
)
cipTgLlcOperLocalConnToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperLocalConnToken.setStatus("current")
_CipTgLlcOperRemoteConnToken_Type = ChannelTgToken
_CipTgLlcOperRemoteConnToken_Object = MibTableColumn
cipTgLlcOperRemoteConnToken = _CipTgLlcOperRemoteConnToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 14),
    _CipTgLlcOperRemoteConnToken_Type()
)
cipTgLlcOperRemoteConnToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperRemoteConnToken.setStatus("current")


class _CipTgLlcOperVcStatus_Type(Integer32):
    """Custom type cipTgLlcOperVcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("reset", 1))
    )


_CipTgLlcOperVcStatus_Type.__name__ = "Integer32"
_CipTgLlcOperVcStatus_Object = MibTableColumn
cipTgLlcOperVcStatus = _CipTgLlcOperVcStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 15),
    _CipTgLlcOperVcStatus_Type()
)
cipTgLlcOperVcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperVcStatus.setStatus("current")


class _CipTgLlcOperConnStatus_Type(Integer32):
    """Custom type cipTgLlcOperConnStatus based on Integer32"""
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
        *(("active", 4),
          ("connRequestSent", 2),
          ("pendingActive", 3),
          ("reset", 1))
    )


_CipTgLlcOperConnStatus_Type.__name__ = "Integer32"
_CipTgLlcOperConnStatus_Object = MibTableColumn
cipTgLlcOperConnStatus = _CipTgLlcOperConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 16),
    _CipTgLlcOperConnStatus_Type()
)
cipTgLlcOperConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcOperConnStatus.setStatus("current")
_CipTgLlcStatsTable_Object = MibTable
cipTgLlcStatsTable = _CipTgLlcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cipTgLlcStatsTable.setStatus("current")
_CipTgLlcStatsEntry_Object = MibTableRow
cipTgLlcStatsEntry = _CipTgLlcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cipTgLlcStatsEntry.setStatus("current")
_CipTgLlcStatsIFramesIn_Type = Counter32
_CipTgLlcStatsIFramesIn_Object = MibTableColumn
cipTgLlcStatsIFramesIn = _CipTgLlcStatsIFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 1),
    _CipTgLlcStatsIFramesIn_Type()
)
cipTgLlcStatsIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsIFramesIn.setStatus("current")
_CipTgLlcStatsIFrameBytesIn_Type = Counter32
_CipTgLlcStatsIFrameBytesIn_Object = MibTableColumn
cipTgLlcStatsIFrameBytesIn = _CipTgLlcStatsIFrameBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 2),
    _CipTgLlcStatsIFrameBytesIn_Type()
)
cipTgLlcStatsIFrameBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsIFrameBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    cipTgLlcStatsIFrameBytesIn.setUnits("octets")
_CipTgLlcStatsHCIFrameBytesIn_Type = Counter64
_CipTgLlcStatsHCIFrameBytesIn_Object = MibTableColumn
cipTgLlcStatsHCIFrameBytesIn = _CipTgLlcStatsHCIFrameBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 3),
    _CipTgLlcStatsHCIFrameBytesIn_Type()
)
cipTgLlcStatsHCIFrameBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsHCIFrameBytesIn.setStatus("current")
_CipTgLlcStatsIFramesOut_Type = Counter32
_CipTgLlcStatsIFramesOut_Object = MibTableColumn
cipTgLlcStatsIFramesOut = _CipTgLlcStatsIFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 4),
    _CipTgLlcStatsIFramesOut_Type()
)
cipTgLlcStatsIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsIFramesOut.setStatus("current")
_CipTgLlcStatsIFrameBytesOut_Type = Counter32
_CipTgLlcStatsIFrameBytesOut_Object = MibTableColumn
cipTgLlcStatsIFrameBytesOut = _CipTgLlcStatsIFrameBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 5),
    _CipTgLlcStatsIFrameBytesOut_Type()
)
cipTgLlcStatsIFrameBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsIFrameBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    cipTgLlcStatsIFrameBytesOut.setUnits("octets")
_CipTgLlcStatsHCIFrameBytesOut_Type = Counter64
_CipTgLlcStatsHCIFrameBytesOut_Object = MibTableColumn
cipTgLlcStatsHCIFrameBytesOut = _CipTgLlcStatsHCIFrameBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 6),
    _CipTgLlcStatsHCIFrameBytesOut_Type()
)
cipTgLlcStatsHCIFrameBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsHCIFrameBytesOut.setStatus("current")
_CipTgLlcStatsUIFramesIn_Type = Counter32
_CipTgLlcStatsUIFramesIn_Object = MibTableColumn
cipTgLlcStatsUIFramesIn = _CipTgLlcStatsUIFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 7),
    _CipTgLlcStatsUIFramesIn_Type()
)
cipTgLlcStatsUIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsUIFramesIn.setStatus("current")
_CipTgLlcStatsUIFrameBytesIn_Type = Counter32
_CipTgLlcStatsUIFrameBytesIn_Object = MibTableColumn
cipTgLlcStatsUIFrameBytesIn = _CipTgLlcStatsUIFrameBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 8),
    _CipTgLlcStatsUIFrameBytesIn_Type()
)
cipTgLlcStatsUIFrameBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsUIFrameBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    cipTgLlcStatsUIFrameBytesIn.setUnits("octets")
_CipTgLlcStatsHCUIFrameBytesIn_Type = Counter64
_CipTgLlcStatsHCUIFrameBytesIn_Object = MibTableColumn
cipTgLlcStatsHCUIFrameBytesIn = _CipTgLlcStatsHCUIFrameBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 9),
    _CipTgLlcStatsHCUIFrameBytesIn_Type()
)
cipTgLlcStatsHCUIFrameBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsHCUIFrameBytesIn.setStatus("current")
_CipTgLlcStatsUIFramesOut_Type = Counter32
_CipTgLlcStatsUIFramesOut_Object = MibTableColumn
cipTgLlcStatsUIFramesOut = _CipTgLlcStatsUIFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 10),
    _CipTgLlcStatsUIFramesOut_Type()
)
cipTgLlcStatsUIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsUIFramesOut.setStatus("current")
_CipTgLlcStatsUIFrameBytesOut_Type = Counter32
_CipTgLlcStatsUIFrameBytesOut_Object = MibTableColumn
cipTgLlcStatsUIFrameBytesOut = _CipTgLlcStatsUIFrameBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 11),
    _CipTgLlcStatsUIFrameBytesOut_Type()
)
cipTgLlcStatsUIFrameBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsUIFrameBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    cipTgLlcStatsUIFrameBytesOut.setUnits("octets")
_CipTgLlcStatsHCUIFrameBytesOut_Type = Counter64
_CipTgLlcStatsHCUIFrameBytesOut_Object = MibTableColumn
cipTgLlcStatsHCUIFrameBytesOut = _CipTgLlcStatsHCUIFrameBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 12),
    _CipTgLlcStatsHCUIFrameBytesOut_Type()
)
cipTgLlcStatsHCUIFrameBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsHCUIFrameBytesOut.setStatus("current")
_CipTgLlcStatsTestCmdsOut_Type = Counter32
_CipTgLlcStatsTestCmdsOut_Object = MibTableColumn
cipTgLlcStatsTestCmdsOut = _CipTgLlcStatsTestCmdsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 13),
    _CipTgLlcStatsTestCmdsOut_Type()
)
cipTgLlcStatsTestCmdsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsTestCmdsOut.setStatus("current")
_CipTgLlcStatsTestRspsIn_Type = Counter32
_CipTgLlcStatsTestRspsIn_Object = MibTableColumn
cipTgLlcStatsTestRspsIn = _CipTgLlcStatsTestRspsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 14),
    _CipTgLlcStatsTestRspsIn_Type()
)
cipTgLlcStatsTestRspsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsTestRspsIn.setStatus("current")
_CipTgLlcStatsXidCmdsIn_Type = Counter32
_CipTgLlcStatsXidCmdsIn_Object = MibTableColumn
cipTgLlcStatsXidCmdsIn = _CipTgLlcStatsXidCmdsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 15),
    _CipTgLlcStatsXidCmdsIn_Type()
)
cipTgLlcStatsXidCmdsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsXidCmdsIn.setStatus("current")
_CipTgLlcStatsXidCmdsOut_Type = Counter32
_CipTgLlcStatsXidCmdsOut_Object = MibTableColumn
cipTgLlcStatsXidCmdsOut = _CipTgLlcStatsXidCmdsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 16),
    _CipTgLlcStatsXidCmdsOut_Type()
)
cipTgLlcStatsXidCmdsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsXidCmdsOut.setStatus("current")
_CipTgLlcStatsXidRspsIn_Type = Counter32
_CipTgLlcStatsXidRspsIn_Object = MibTableColumn
cipTgLlcStatsXidRspsIn = _CipTgLlcStatsXidRspsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 17),
    _CipTgLlcStatsXidRspsIn_Type()
)
cipTgLlcStatsXidRspsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsXidRspsIn.setStatus("current")
_CipTgLlcStatsXidRspsOut_Type = Counter32
_CipTgLlcStatsXidRspsOut_Object = MibTableColumn
cipTgLlcStatsXidRspsOut = _CipTgLlcStatsXidRspsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 18),
    _CipTgLlcStatsXidRspsOut_Type()
)
cipTgLlcStatsXidRspsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsXidRspsOut.setStatus("current")
_CipTgLlcStatsConnNumberRecv_Type = Counter32
_CipTgLlcStatsConnNumberRecv_Object = MibTableColumn
cipTgLlcStatsConnNumberRecv = _CipTgLlcStatsConnNumberRecv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 19),
    _CipTgLlcStatsConnNumberRecv_Type()
)
cipTgLlcStatsConnNumberRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsConnNumberRecv.setStatus("current")
_CipTgLlcStatsConnNumberSent_Type = Counter32
_CipTgLlcStatsConnNumberSent_Object = MibTableColumn
cipTgLlcStatsConnNumberSent = _CipTgLlcStatsConnNumberSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 20),
    _CipTgLlcStatsConnNumberSent_Type()
)
cipTgLlcStatsConnNumberSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgLlcStatsConnNumberSent.setStatus("current")
_CipTgIp_ObjectIdentity = ObjectIdentity
cipTgIp = _CipTgIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2)
)
_CipTgIpAdminTable_Object = MibTable
cipTgIpAdminTable = _CipTgIpAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cipTgIpAdminTable.setStatus("current")
_CipTgIpAdminEntry_Object = MibTableRow
cipTgIpAdminEntry = _CipTgIpAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1)
)
cipTgIpAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CIPTG-MIB", "cipTgIpAdminName"),
)
if mibBuilder.loadTexts:
    cipTgIpAdminEntry.setStatus("current")
_CipTgIpAdminName_Type = ChannelTgName
_CipTgIpAdminName_Object = MibTableColumn
cipTgIpAdminName = _CipTgIpAdminName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 1),
    _CipTgIpAdminName_Type()
)
cipTgIpAdminName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipTgIpAdminName.setStatus("current")


class _CipTgIpAdminType_Type(Integer32):
    """Custom type cipTgIpAdminType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hsas", 2),
          ("tcpIp", 1))
    )


_CipTgIpAdminType_Type.__name__ = "Integer32"
_CipTgIpAdminType_Object = MibTableColumn
cipTgIpAdminType = _CipTgIpAdminType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 2),
    _CipTgIpAdminType_Type()
)
cipTgIpAdminType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipTgIpAdminType.setStatus("current")
_CipTgIpAdminRemoteIpAddr_Type = IpAddress
_CipTgIpAdminRemoteIpAddr_Object = MibTableColumn
cipTgIpAdminRemoteIpAddr = _CipTgIpAdminRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 3),
    _CipTgIpAdminRemoteIpAddr_Type()
)
cipTgIpAdminRemoteIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipTgIpAdminRemoteIpAddr.setStatus("current")
_CipTgIpAdminLocalIpAddr_Type = IpAddress
_CipTgIpAdminLocalIpAddr_Object = MibTableColumn
cipTgIpAdminLocalIpAddr = _CipTgIpAdminLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 4),
    _CipTgIpAdminLocalIpAddr_Type()
)
cipTgIpAdminLocalIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipTgIpAdminLocalIpAddr.setStatus("current")
_CipTgIpAdminBroadcast_Type = TruthValue
_CipTgIpAdminBroadcast_Object = MibTableColumn
cipTgIpAdminBroadcast = _CipTgIpAdminBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 5),
    _CipTgIpAdminBroadcast_Type()
)
cipTgIpAdminBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipTgIpAdminBroadcast.setStatus("current")
_CipTgIpAdminRowStatus_Type = RowStatus
_CipTgIpAdminRowStatus_Object = MibTableColumn
cipTgIpAdminRowStatus = _CipTgIpAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 6),
    _CipTgIpAdminRowStatus_Type()
)
cipTgIpAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipTgIpAdminRowStatus.setStatus("current")
_CipTgIpOperTable_Object = MibTable
cipTgIpOperTable = _CipTgIpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cipTgIpOperTable.setStatus("current")
_CipTgIpOperEntry_Object = MibTableRow
cipTgIpOperEntry = _CipTgIpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cipTgIpOperEntry.setStatus("current")
_CipTgIpOperLocalVcToken_Type = ChannelTgToken
_CipTgIpOperLocalVcToken_Object = MibTableColumn
cipTgIpOperLocalVcToken = _CipTgIpOperLocalVcToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 1),
    _CipTgIpOperLocalVcToken_Type()
)
cipTgIpOperLocalVcToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgIpOperLocalVcToken.setStatus("current")
_CipTgIpOperRemoteVcToken_Type = ChannelTgToken
_CipTgIpOperRemoteVcToken_Object = MibTableColumn
cipTgIpOperRemoteVcToken = _CipTgIpOperRemoteVcToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 2),
    _CipTgIpOperRemoteVcToken_Type()
)
cipTgIpOperRemoteVcToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgIpOperRemoteVcToken.setStatus("current")
_CipTgIpOperLocalConnToken_Type = ChannelTgToken
_CipTgIpOperLocalConnToken_Object = MibTableColumn
cipTgIpOperLocalConnToken = _CipTgIpOperLocalConnToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 3),
    _CipTgIpOperLocalConnToken_Type()
)
cipTgIpOperLocalConnToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgIpOperLocalConnToken.setStatus("current")
_CipTgIpOperRemoteConnToken_Type = ChannelTgToken
_CipTgIpOperRemoteConnToken_Object = MibTableColumn
cipTgIpOperRemoteConnToken = _CipTgIpOperRemoteConnToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 4),
    _CipTgIpOperRemoteConnToken_Type()
)
cipTgIpOperRemoteConnToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgIpOperRemoteConnToken.setStatus("current")


class _CipTgIpOperVcStatus_Type(Integer32):
    """Custom type cipTgIpOperVcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("reset", 1))
    )


_CipTgIpOperVcStatus_Type.__name__ = "Integer32"
_CipTgIpOperVcStatus_Object = MibTableColumn
cipTgIpOperVcStatus = _CipTgIpOperVcStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 5),
    _CipTgIpOperVcStatus_Type()
)
cipTgIpOperVcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgIpOperVcStatus.setStatus("current")


class _CipTgIpOperConnStatus_Type(Integer32):
    """Custom type cipTgIpOperConnStatus based on Integer32"""
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
        *(("active", 4),
          ("connRequestSent", 2),
          ("pendingActive", 3),
          ("reset", 1))
    )


_CipTgIpOperConnStatus_Type.__name__ = "Integer32"
_CipTgIpOperConnStatus_Object = MibTableColumn
cipTgIpOperConnStatus = _CipTgIpOperConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 6),
    _CipTgIpOperConnStatus_Type()
)
cipTgIpOperConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgIpOperConnStatus.setStatus("current")
_CipTgIpStatsTable_Object = MibTable
cipTgIpStatsTable = _CipTgIpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cipTgIpStatsTable.setStatus("current")
_CipTgIpStatsEntry_Object = MibTableRow
cipTgIpStatsEntry = _CipTgIpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cipTgIpStatsEntry.setStatus("current")
_CipTgIpStatsPacketsIn_Type = Counter32
_CipTgIpStatsPacketsIn_Object = MibTableColumn
cipTgIpStatsPacketsIn = _CipTgIpStatsPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 1),
    _CipTgIpStatsPacketsIn_Type()
)
cipTgIpStatsPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgIpStatsPacketsIn.setStatus("current")
_CipTgIpStatsBytesIn_Type = Counter32
_CipTgIpStatsBytesIn_Object = MibTableColumn
cipTgIpStatsBytesIn = _CipTgIpStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 2),
    _CipTgIpStatsBytesIn_Type()
)
cipTgIpStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgIpStatsBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    cipTgIpStatsBytesIn.setUnits("octets")
_CipTgIpStatsHCBytesIn_Type = Counter64
_CipTgIpStatsHCBytesIn_Object = MibTableColumn
cipTgIpStatsHCBytesIn = _CipTgIpStatsHCBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 3),
    _CipTgIpStatsHCBytesIn_Type()
)
cipTgIpStatsHCBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgIpStatsHCBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    cipTgIpStatsHCBytesIn.setUnits("octets")
_CipTgIpStatsPacketsOut_Type = Counter32
_CipTgIpStatsPacketsOut_Object = MibTableColumn
cipTgIpStatsPacketsOut = _CipTgIpStatsPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 4),
    _CipTgIpStatsPacketsOut_Type()
)
cipTgIpStatsPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgIpStatsPacketsOut.setStatus("current")
_CipTgIpStatsBytesOut_Type = Counter32
_CipTgIpStatsBytesOut_Object = MibTableColumn
cipTgIpStatsBytesOut = _CipTgIpStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 5),
    _CipTgIpStatsBytesOut_Type()
)
cipTgIpStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgIpStatsBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    cipTgIpStatsBytesOut.setUnits("octets")
_CipTgIpStatsHCBytesOut_Type = Counter64
_CipTgIpStatsHCBytesOut_Object = MibTableColumn
cipTgIpStatsHCBytesOut = _CipTgIpStatsHCBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 6),
    _CipTgIpStatsHCBytesOut_Type()
)
cipTgIpStatsHCBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgIpStatsHCBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    cipTgIpStatsHCBytesOut.setUnits("octets")
_CipTgCmgr_ObjectIdentity = ObjectIdentity
cipTgCmgr = _CipTgCmgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3)
)
_CipTgCmgrOperTable_Object = MibTable
cipTgCmgrOperTable = _CipTgCmgrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cipTgCmgrOperTable.setStatus("current")
_CipTgCmgrOperEntry_Object = MibTableRow
cipTgCmgrOperEntry = _CipTgCmgrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1)
)
cipTgCmgrOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CIPTG-MIB", "cipTgCmgrOperName"),
)
if mibBuilder.loadTexts:
    cipTgCmgrOperEntry.setStatus("current")
_CipTgCmgrOperName_Type = ChannelTgName
_CipTgCmgrOperName_Object = MibTableColumn
cipTgCmgrOperName = _CipTgCmgrOperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 1),
    _CipTgCmgrOperName_Type()
)
cipTgCmgrOperName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipTgCmgrOperName.setStatus("current")


class _CipTgCmgrOperType_Type(Integer32):
    """Custom type cipTgCmgrOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pointToMultiPoint", 2),
          ("pointToPoint", 1))
    )


_CipTgCmgrOperType_Type.__name__ = "Integer32"
_CipTgCmgrOperType_Object = MibTableColumn
cipTgCmgrOperType = _CipTgCmgrOperType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 2),
    _CipTgCmgrOperType_Type()
)
cipTgCmgrOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgCmgrOperType.setStatus("current")
_CipTgCmgrOperLocalGrToken_Type = ChannelTgToken
_CipTgCmgrOperLocalGrToken_Object = MibTableColumn
cipTgCmgrOperLocalGrToken = _CipTgCmgrOperLocalGrToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 3),
    _CipTgCmgrOperLocalGrToken_Type()
)
cipTgCmgrOperLocalGrToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgCmgrOperLocalGrToken.setStatus("current")
_CipTgCmgrOperRemoteGrToken_Type = ChannelTgToken
_CipTgCmgrOperRemoteGrToken_Object = MibTableColumn
cipTgCmgrOperRemoteGrToken = _CipTgCmgrOperRemoteGrToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 4),
    _CipTgCmgrOperRemoteGrToken_Type()
)
cipTgCmgrOperRemoteGrToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgCmgrOperRemoteGrToken.setStatus("current")
_CipTgCmgrOperLocalVcToken_Type = ChannelTgToken
_CipTgCmgrOperLocalVcToken_Object = MibTableColumn
cipTgCmgrOperLocalVcToken = _CipTgCmgrOperLocalVcToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 5),
    _CipTgCmgrOperLocalVcToken_Type()
)
cipTgCmgrOperLocalVcToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgCmgrOperLocalVcToken.setStatus("current")
_CipTgCmgrOperRemoteVcToken_Type = ChannelTgToken
_CipTgCmgrOperRemoteVcToken_Object = MibTableColumn
cipTgCmgrOperRemoteVcToken = _CipTgCmgrOperRemoteVcToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 6),
    _CipTgCmgrOperRemoteVcToken_Type()
)
cipTgCmgrOperRemoteVcToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgCmgrOperRemoteVcToken.setStatus("current")
_CipTgCmgrOperLocalConnToken_Type = ChannelTgToken
_CipTgCmgrOperLocalConnToken_Object = MibTableColumn
cipTgCmgrOperLocalConnToken = _CipTgCmgrOperLocalConnToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 7),
    _CipTgCmgrOperLocalConnToken_Type()
)
cipTgCmgrOperLocalConnToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgCmgrOperLocalConnToken.setStatus("current")
_CipTgCmgrOperRemoteConnToken_Type = ChannelTgToken
_CipTgCmgrOperRemoteConnToken_Object = MibTableColumn
cipTgCmgrOperRemoteConnToken = _CipTgCmgrOperRemoteConnToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 8),
    _CipTgCmgrOperRemoteConnToken_Type()
)
cipTgCmgrOperRemoteConnToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgCmgrOperRemoteConnToken.setStatus("current")


class _CipTgCmgrOperVcStatus_Type(Integer32):
    """Custom type cipTgCmgrOperVcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("reset", 1))
    )


_CipTgCmgrOperVcStatus_Type.__name__ = "Integer32"
_CipTgCmgrOperVcStatus_Object = MibTableColumn
cipTgCmgrOperVcStatus = _CipTgCmgrOperVcStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 9),
    _CipTgCmgrOperVcStatus_Type()
)
cipTgCmgrOperVcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgCmgrOperVcStatus.setStatus("current")


class _CipTgCmgrOperConnStatus_Type(Integer32):
    """Custom type cipTgCmgrOperConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("reset", 1))
    )


_CipTgCmgrOperConnStatus_Type.__name__ = "Integer32"
_CipTgCmgrOperConnStatus_Object = MibTableColumn
cipTgCmgrOperConnStatus = _CipTgCmgrOperConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 10),
    _CipTgCmgrOperConnStatus_Type()
)
cipTgCmgrOperConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipTgCmgrOperConnStatus.setStatus("current")
_CiscoCipTgMibConformance_ObjectIdentity = ObjectIdentity
ciscoCipTgMibConformance = _CiscoCipTgMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 3)
)
_CiscoCipTgMibCompliances_ObjectIdentity = ObjectIdentity
ciscoCipTgMibCompliances = _CiscoCipTgMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 1)
)
_CiscoCipTgMibGroups_ObjectIdentity = ObjectIdentity
ciscoCipTgMibGroups = _CiscoCipTgMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 2)
)
cipTgLlcAdminEntry.registerAugmentions(
    ("CISCO-CIPTG-MIB",
     "cipTgLlcOperEntry")
)
cipTgLlcOperEntry.setIndexNames(*cipTgLlcAdminEntry.getIndexNames())
cipTgLlcAdminEntry.registerAugmentions(
    ("CISCO-CIPTG-MIB",
     "cipTgLlcStatsEntry")
)
cipTgLlcStatsEntry.setIndexNames(*cipTgLlcAdminEntry.getIndexNames())
cipTgIpAdminEntry.registerAugmentions(
    ("CISCO-CIPTG-MIB",
     "cipTgIpOperEntry")
)
cipTgIpOperEntry.setIndexNames(*cipTgIpAdminEntry.getIndexNames())
cipTgIpAdminEntry.registerAugmentions(
    ("CISCO-CIPTG-MIB",
     "cipTgIpStatsEntry")
)
cipTgIpStatsEntry.setIndexNames(*cipTgIpAdminEntry.getIndexNames())

# Managed Objects groups

ciscoCipTgLlcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 2, 2)
)
ciscoCipTgLlcGroup.setObjects(
      *(("CISCO-CIPTG-MIB", "cipTgLlcAdminLanType"),
        ("CISCO-CIPTG-MIB", "cipTgLlcAdminAdaptNo"),
        ("CISCO-CIPTG-MIB", "cipTgLlcAdminLSAP"),
        ("CISCO-CIPTG-MIB", "cipTgLlcAdminRMAC"),
        ("CISCO-CIPTG-MIB", "cipTgLlcAdminRSAP"),
        ("CISCO-CIPTG-MIB", "cipTgLlcAdminRowStatus"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperState"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperTGN"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperLocalCP"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperRemoteCP"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperMaxIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperMaxOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperHpr"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperHprLSAP"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperHprRSAP"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperRIF"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFramesIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFrameBytesIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCIFrameBytesIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFramesOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFrameBytesOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCIFrameBytesOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFramesIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFrameBytesIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCUIFrameBytesIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFramesOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFrameBytesOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCUIFrameBytesOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsTestCmdsOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsTestRspsIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidCmdsIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidCmdsOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidRspsIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidRspsOut"))
)
if mibBuilder.loadTexts:
    ciscoCipTgLlcGroup.setStatus("obsolete")

ciscoCipTgLlcGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 2, 3)
)
ciscoCipTgLlcGroupRev1.setObjects(
      *(("CISCO-CIPTG-MIB", "cipTgLlcAdminLanType"),
        ("CISCO-CIPTG-MIB", "cipTgLlcAdminAdaptNo"),
        ("CISCO-CIPTG-MIB", "cipTgLlcAdminLSAP"),
        ("CISCO-CIPTG-MIB", "cipTgLlcAdminRMAC"),
        ("CISCO-CIPTG-MIB", "cipTgLlcAdminRSAP"),
        ("CISCO-CIPTG-MIB", "cipTgLlcAdminRowStatus"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperState"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperTGN"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperLocalCP"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperRemoteCP"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperMaxIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperMaxOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperHpr"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperHprLSAP"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperHprRSAP"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperRIF"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperLocalVcToken"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperRemoteVcToken"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperLocalConnToken"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperRemoteConnToken"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperVcStatus"),
        ("CISCO-CIPTG-MIB", "cipTgLlcOperConnStatus"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFramesIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFrameBytesIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCIFrameBytesIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFramesOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFrameBytesOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCIFrameBytesOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFramesIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFrameBytesIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCUIFrameBytesIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFramesOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFrameBytesOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCUIFrameBytesOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsTestCmdsOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsTestRspsIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidCmdsIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidCmdsOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidRspsIn"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidRspsOut"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsConnNumberRecv"),
        ("CISCO-CIPTG-MIB", "cipTgLlcStatsConnNumberSent"))
)
if mibBuilder.loadTexts:
    ciscoCipTgLlcGroupRev1.setStatus("current")

ciscoCipTgIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 2, 4)
)
ciscoCipTgIpGroup.setObjects(
      *(("CISCO-CIPTG-MIB", "cipTgIpAdminType"),
        ("CISCO-CIPTG-MIB", "cipTgIpAdminRemoteIpAddr"),
        ("CISCO-CIPTG-MIB", "cipTgIpAdminLocalIpAddr"),
        ("CISCO-CIPTG-MIB", "cipTgIpAdminBroadcast"),
        ("CISCO-CIPTG-MIB", "cipTgIpAdminRowStatus"),
        ("CISCO-CIPTG-MIB", "cipTgIpOperLocalVcToken"),
        ("CISCO-CIPTG-MIB", "cipTgIpOperRemoteVcToken"),
        ("CISCO-CIPTG-MIB", "cipTgIpOperLocalConnToken"),
        ("CISCO-CIPTG-MIB", "cipTgIpOperRemoteConnToken"),
        ("CISCO-CIPTG-MIB", "cipTgIpOperVcStatus"),
        ("CISCO-CIPTG-MIB", "cipTgIpOperConnStatus"),
        ("CISCO-CIPTG-MIB", "cipTgIpStatsPacketsIn"),
        ("CISCO-CIPTG-MIB", "cipTgIpStatsBytesIn"),
        ("CISCO-CIPTG-MIB", "cipTgIpStatsHCBytesIn"),
        ("CISCO-CIPTG-MIB", "cipTgIpStatsPacketsOut"),
        ("CISCO-CIPTG-MIB", "cipTgIpStatsBytesOut"),
        ("CISCO-CIPTG-MIB", "cipTgIpStatsHCBytesOut"))
)
if mibBuilder.loadTexts:
    ciscoCipTgIpGroup.setStatus("current")

ciscoCipTgCmgrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 2, 5)
)
ciscoCipTgCmgrGroup.setObjects(
      *(("CISCO-CIPTG-MIB", "cipTgCmgrOperType"),
        ("CISCO-CIPTG-MIB", "cipTgCmgrOperLocalGrToken"),
        ("CISCO-CIPTG-MIB", "cipTgCmgrOperRemoteGrToken"),
        ("CISCO-CIPTG-MIB", "cipTgCmgrOperLocalVcToken"),
        ("CISCO-CIPTG-MIB", "cipTgCmgrOperRemoteVcToken"),
        ("CISCO-CIPTG-MIB", "cipTgCmgrOperLocalConnToken"),
        ("CISCO-CIPTG-MIB", "cipTgCmgrOperRemoteConnToken"),
        ("CISCO-CIPTG-MIB", "cipTgCmgrOperVcStatus"),
        ("CISCO-CIPTG-MIB", "cipTgCmgrOperConnStatus"))
)
if mibBuilder.loadTexts:
    ciscoCipTgCmgrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCipTgMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCipTgMibCompliance.setStatus(
        "obsolete"
    )

ciscoCipTgMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCipTgMibComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CIPTG-MIB",
    **{"ChannelTgName": ChannelTgName,
       "ChannelTgToken": ChannelTgToken,
       "ciscoCipTgMIB": ciscoCipTgMIB,
       "cipTgObjects": cipTgObjects,
       "cipTgLlc": cipTgLlc,
       "cipTgLlcAdminTable": cipTgLlcAdminTable,
       "cipTgLlcAdminEntry": cipTgLlcAdminEntry,
       "cipTgLlcAdminName": cipTgLlcAdminName,
       "cipTgLlcAdminLanType": cipTgLlcAdminLanType,
       "cipTgLlcAdminAdaptNo": cipTgLlcAdminAdaptNo,
       "cipTgLlcAdminLSAP": cipTgLlcAdminLSAP,
       "cipTgLlcAdminRMAC": cipTgLlcAdminRMAC,
       "cipTgLlcAdminRSAP": cipTgLlcAdminRSAP,
       "cipTgLlcAdminRowStatus": cipTgLlcAdminRowStatus,
       "cipTgLlcOperTable": cipTgLlcOperTable,
       "cipTgLlcOperEntry": cipTgLlcOperEntry,
       "cipTgLlcOperState": cipTgLlcOperState,
       "cipTgLlcOperTGN": cipTgLlcOperTGN,
       "cipTgLlcOperLocalCP": cipTgLlcOperLocalCP,
       "cipTgLlcOperRemoteCP": cipTgLlcOperRemoteCP,
       "cipTgLlcOperMaxIn": cipTgLlcOperMaxIn,
       "cipTgLlcOperMaxOut": cipTgLlcOperMaxOut,
       "cipTgLlcOperHpr": cipTgLlcOperHpr,
       "cipTgLlcOperHprLSAP": cipTgLlcOperHprLSAP,
       "cipTgLlcOperHprRSAP": cipTgLlcOperHprRSAP,
       "cipTgLlcOperRIF": cipTgLlcOperRIF,
       "cipTgLlcOperLocalVcToken": cipTgLlcOperLocalVcToken,
       "cipTgLlcOperRemoteVcToken": cipTgLlcOperRemoteVcToken,
       "cipTgLlcOperLocalConnToken": cipTgLlcOperLocalConnToken,
       "cipTgLlcOperRemoteConnToken": cipTgLlcOperRemoteConnToken,
       "cipTgLlcOperVcStatus": cipTgLlcOperVcStatus,
       "cipTgLlcOperConnStatus": cipTgLlcOperConnStatus,
       "cipTgLlcStatsTable": cipTgLlcStatsTable,
       "cipTgLlcStatsEntry": cipTgLlcStatsEntry,
       "cipTgLlcStatsIFramesIn": cipTgLlcStatsIFramesIn,
       "cipTgLlcStatsIFrameBytesIn": cipTgLlcStatsIFrameBytesIn,
       "cipTgLlcStatsHCIFrameBytesIn": cipTgLlcStatsHCIFrameBytesIn,
       "cipTgLlcStatsIFramesOut": cipTgLlcStatsIFramesOut,
       "cipTgLlcStatsIFrameBytesOut": cipTgLlcStatsIFrameBytesOut,
       "cipTgLlcStatsHCIFrameBytesOut": cipTgLlcStatsHCIFrameBytesOut,
       "cipTgLlcStatsUIFramesIn": cipTgLlcStatsUIFramesIn,
       "cipTgLlcStatsUIFrameBytesIn": cipTgLlcStatsUIFrameBytesIn,
       "cipTgLlcStatsHCUIFrameBytesIn": cipTgLlcStatsHCUIFrameBytesIn,
       "cipTgLlcStatsUIFramesOut": cipTgLlcStatsUIFramesOut,
       "cipTgLlcStatsUIFrameBytesOut": cipTgLlcStatsUIFrameBytesOut,
       "cipTgLlcStatsHCUIFrameBytesOut": cipTgLlcStatsHCUIFrameBytesOut,
       "cipTgLlcStatsTestCmdsOut": cipTgLlcStatsTestCmdsOut,
       "cipTgLlcStatsTestRspsIn": cipTgLlcStatsTestRspsIn,
       "cipTgLlcStatsXidCmdsIn": cipTgLlcStatsXidCmdsIn,
       "cipTgLlcStatsXidCmdsOut": cipTgLlcStatsXidCmdsOut,
       "cipTgLlcStatsXidRspsIn": cipTgLlcStatsXidRspsIn,
       "cipTgLlcStatsXidRspsOut": cipTgLlcStatsXidRspsOut,
       "cipTgLlcStatsConnNumberRecv": cipTgLlcStatsConnNumberRecv,
       "cipTgLlcStatsConnNumberSent": cipTgLlcStatsConnNumberSent,
       "cipTgIp": cipTgIp,
       "cipTgIpAdminTable": cipTgIpAdminTable,
       "cipTgIpAdminEntry": cipTgIpAdminEntry,
       "cipTgIpAdminName": cipTgIpAdminName,
       "cipTgIpAdminType": cipTgIpAdminType,
       "cipTgIpAdminRemoteIpAddr": cipTgIpAdminRemoteIpAddr,
       "cipTgIpAdminLocalIpAddr": cipTgIpAdminLocalIpAddr,
       "cipTgIpAdminBroadcast": cipTgIpAdminBroadcast,
       "cipTgIpAdminRowStatus": cipTgIpAdminRowStatus,
       "cipTgIpOperTable": cipTgIpOperTable,
       "cipTgIpOperEntry": cipTgIpOperEntry,
       "cipTgIpOperLocalVcToken": cipTgIpOperLocalVcToken,
       "cipTgIpOperRemoteVcToken": cipTgIpOperRemoteVcToken,
       "cipTgIpOperLocalConnToken": cipTgIpOperLocalConnToken,
       "cipTgIpOperRemoteConnToken": cipTgIpOperRemoteConnToken,
       "cipTgIpOperVcStatus": cipTgIpOperVcStatus,
       "cipTgIpOperConnStatus": cipTgIpOperConnStatus,
       "cipTgIpStatsTable": cipTgIpStatsTable,
       "cipTgIpStatsEntry": cipTgIpStatsEntry,
       "cipTgIpStatsPacketsIn": cipTgIpStatsPacketsIn,
       "cipTgIpStatsBytesIn": cipTgIpStatsBytesIn,
       "cipTgIpStatsHCBytesIn": cipTgIpStatsHCBytesIn,
       "cipTgIpStatsPacketsOut": cipTgIpStatsPacketsOut,
       "cipTgIpStatsBytesOut": cipTgIpStatsBytesOut,
       "cipTgIpStatsHCBytesOut": cipTgIpStatsHCBytesOut,
       "cipTgCmgr": cipTgCmgr,
       "cipTgCmgrOperTable": cipTgCmgrOperTable,
       "cipTgCmgrOperEntry": cipTgCmgrOperEntry,
       "cipTgCmgrOperName": cipTgCmgrOperName,
       "cipTgCmgrOperType": cipTgCmgrOperType,
       "cipTgCmgrOperLocalGrToken": cipTgCmgrOperLocalGrToken,
       "cipTgCmgrOperRemoteGrToken": cipTgCmgrOperRemoteGrToken,
       "cipTgCmgrOperLocalVcToken": cipTgCmgrOperLocalVcToken,
       "cipTgCmgrOperRemoteVcToken": cipTgCmgrOperRemoteVcToken,
       "cipTgCmgrOperLocalConnToken": cipTgCmgrOperLocalConnToken,
       "cipTgCmgrOperRemoteConnToken": cipTgCmgrOperRemoteConnToken,
       "cipTgCmgrOperVcStatus": cipTgCmgrOperVcStatus,
       "cipTgCmgrOperConnStatus": cipTgCmgrOperConnStatus,
       "ciscoCipTgMibConformance": ciscoCipTgMibConformance,
       "ciscoCipTgMibCompliances": ciscoCipTgMibCompliances,
       "ciscoCipTgMibCompliance": ciscoCipTgMibCompliance,
       "ciscoCipTgMibComplianceRev1": ciscoCipTgMibComplianceRev1,
       "ciscoCipTgMibGroups": ciscoCipTgMibGroups,
       "ciscoCipTgLlcGroup": ciscoCipTgLlcGroup,
       "ciscoCipTgLlcGroupRev1": ciscoCipTgLlcGroupRev1,
       "ciscoCipTgIpGroup": ciscoCipTgIpGroup,
       "ciscoCipTgCmgrGroup": ciscoCipTgCmgrGroup}
)
