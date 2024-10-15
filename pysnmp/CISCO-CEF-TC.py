# SNMP MIB module (CISCO-CEF-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CEF-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:22 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoCefTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 493)
)
ciscoCefTextualConventions.setRevisions(
        ("2005-09-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CefIpVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )



class CefAdjLinkType(Integer32, TextualConvention):
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("mpls", 3),
          ("raw", 4),
          ("unknown", 5))
    )



class CefAdjacencySource(Bits, TextualConvention):
    status = "current"


class CefPathType(Integer32, TextualConvention):
    status = "current"
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
        *(("adjacencyPrefix", 7),
          ("attachedHost", 4),
          ("attachedNexthop", 5),
          ("attachedPrefix", 3),
          ("connectedPrefix", 2),
          ("receive", 1),
          ("recursiveNexthop", 6),
          ("specialPrefix", 8),
          ("unknown", 9))
    )



class CefPrefixSearchState(Integer32, TextualConvention):
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
        *(("matchFound", 2),
          ("noMatchFound", 3),
          ("running", 1))
    )



class CefForwardingElementSpecialType(Integer32, TextualConvention):
    status = "current"
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
        *(("discard", 4),
          ("drop", 3),
          ("glean", 6),
          ("illegal", 1),
          ("noRoute", 8),
          ("none", 9),
          ("null", 5),
          ("punt", 2),
          ("unresolved", 7))
    )



class CefMplsLabelList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CefAdminStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



class CefOperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class CefFailureReason(Integer32, TextualConvention):
    status = "current"
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
        *(("hwFailure", 3),
          ("internalError", 7),
          ("invalidMsgSize", 6),
          ("keepaliveFailure", 4),
          ("mallocFailure", 2),
          ("noMsgBuffer", 5),
          ("none", 1))
    )



class CefCCType(Integer32, TextualConvention):
    status = "current"
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("fullScanFibHwSw", 12),
          ("fullScanFibLcRp", 11),
          ("fullScanFibRib", 9),
          ("fullScanFibRpLc", 10),
          ("fullScanFibSwHw", 13),
          ("fullScanRibFib", 8),
          ("lcDetect", 1),
          ("scanFibHwSw", 6),
          ("scanFibLcRp", 2),
          ("scanFibRib", 5),
          ("scanFibRpLc", 3),
          ("scanFibSwHw", 7),
          ("scanRibFib", 4))
    )



class CefCCAction(Integer32, TextualConvention):
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
        *(("ccActionAbort", 2),
          ("ccActionNone", 3),
          ("ccActionStart", 1))
    )



class CefCCStatus(Integer32, TextualConvention):
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
        *(("ccStatusDone", 3),
          ("ccStatusIdle", 1),
          ("ccStatusRunning", 2))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CEF-TC",
    **{"CefIpVersion": CefIpVersion,
       "CefAdjLinkType": CefAdjLinkType,
       "CefAdjacencySource": CefAdjacencySource,
       "CefPathType": CefPathType,
       "CefPrefixSearchState": CefPrefixSearchState,
       "CefForwardingElementSpecialType": CefForwardingElementSpecialType,
       "CefMplsLabelList": CefMplsLabelList,
       "CefAdminStatus": CefAdminStatus,
       "CefOperStatus": CefOperStatus,
       "CefFailureReason": CefFailureReason,
       "CefCCType": CefCCType,
       "CefCCAction": CefCCAction,
       "CefCCStatus": CefCCStatus,
       "ciscoCefTextualConventions": ciscoCefTextualConventions}
)
